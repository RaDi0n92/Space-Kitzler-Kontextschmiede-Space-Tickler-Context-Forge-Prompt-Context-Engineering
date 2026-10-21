#!/usr/bin/env python3
"""Read-only inspection of an explicitly provided LOCAL jlens-gguf HTTP bridge.

No installation, model launch, weights, activation capture, steering or arbitrary network.
The caller runs this locally alongside an already configured, authorized jlens bridge.
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from urllib.parse import urlsplit
from urllib.request import Request, build_opener, HTTPRedirectHandler, ProxyHandler
from urllib.error import URLError, HTTPError

class BlockRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, msg, headers, newurl):
        raise ValueError('Redirects are forbidden')


def validated_root(value):
    url=urlsplit(value)
    if url.scheme!='http' or url.username or url.password or url.query or url.fragment or url.path not in ('','/'):
        raise ValueError('Only plain http://127.0.0.1:PORT or http://localhost:PORT')
    if url.hostname not in ('127.0.0.1','localhost','::1'):
        raise ValueError('Remote destinations are forbidden')
    try: port=url.port
    except ValueError: raise ValueError('Port invalid') from None
    if not port or not (1<=port<=65535):raise ValueError('Explicit TCP port is required')
    return f'http://{url.netloc}'


def request_json(root,endpoint,payload=None):
    uri=root+endpoint
    data=None if payload is None else json.dumps(payload).encode('utf-8')
    req=Request(uri,data=data,headers={'Content-Type':'application/json','Accept':'application/json'},method='GET' if payload is None else 'POST')
    opener=build_opener(ProxyHandler({}), BlockRedirect())
    with opener.open(req,timeout=6) as resp:
        if resp.status != 200:raise ValueError(f'Unexpected HTTP status {resp.status}')
        length=resp.headers.get('Content-Length')
        if length and int(length)>1_000_000:raise ValueError('Response too large')
        raw=resp.read(1_000_001)
        if len(raw)>1_000_000:raise ValueError('Response too large')
    answer=json.loads(raw)
    if not isinstance(answer,dict):raise ValueError('Expected JSON object from local bridge')
    return answer


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--url',required=True,help='Explicit loopback jlens bridge, e.g. http://127.0.0.1:8090')
    ap.add_argument('--out',help='Optional report destination; must not already exist')
    sub=ap.add_subparsers(dest='command',required=True)
    sub.add_parser('props',help='Read /api/props without computing or changing activations')
    readout=sub.add_parser('readout',help='Read existing context layer/position from bridge')
    readout.add_argument('--ctx-id',required=True)
    readout.add_argument('--pos',type=int,required=True)
    readout.add_argument('--layer',type=int,required=True)
    readout.add_argument('--top-n',type=int,default=10)
    a=ap.parse_args()
    try:
        root=validated_root(a.url)
        if a.command=='props':
            answer=request_json(root,'/api/props')
        else:
            if len(a.ctx_id)>128 or not a.ctx_id or a.pos<0 or a.layer<0 or not (1<=a.top_n<=100):raise ValueError('Invalid readout selector')
            answer=request_json(root,'/api/readout',{'ctx_id':a.ctx_id,'pos':a.pos,'layer':a.layer,'top_n':a.top_n})
        result={'schema':'context-forge-jlens-observation/1','source':'live_local_jlens_gguf_bridge',
                'command':a.command,'endpoint':root,'response':answer,
                'limits':['Requires user-provided local jlens bridge and its own model runtime',
                          'No live ChatGPT activation access','Output is a model-specific readout, not full hidden reasoning',
                          'No baseline/intervention/control comparison was performed by this command']}
        if a.out:
            path=Path(a.out).expanduser().absolute()
            if path.exists() or path.is_symlink():raise ValueError('Refusing to overwrite report')
            path.parent.mkdir(parents=True,exist_ok=True)
            with path.open('x',encoding='utf8') as h:json.dump(result,h,ensure_ascii=False,indent=2)
        print(json.dumps(result,ensure_ascii=False,indent=2))
        return 0
    except (ValueError,OSError,HTTPError,URLError,UnicodeError,json.JSONDecodeError) as exc:
        print(json.dumps({'status':'blocked','reason':str(exc)},ensure_ascii=False),file=sys.stderr)
        return 2

if __name__=='__main__':sys.exit(main())
