#!/usr/bin/env python3
"""Optional, restricted, deterministic local text operations.

This is NOT a general purpose agent executor. It enforces a caller-written, authorized
plan for new text files or exact guarded replacements under one workspace root.
Dry run by default. No network, shell, deletes, or overwrite-new.
"""
import argparse
import hashlib
import json
import os
import pathlib
import stat
import sys
import tempfile


def sha(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def safe_rel(root, rel):
    if not isinstance(rel, str) or not rel or '\\' in rel or '\x00' in rel:
        raise ValueError('Unsafe path')
    p = pathlib.PurePosixPath(rel)
    if p.is_absolute() or any(k in ('..', '.') for k in rel.split('/')) or str(p) != rel:
        raise ValueError('Path traversal or non-canonical path: ' + rel)
    target = root / rel
    for x in [root, *reversed(list(target.parents)[:-1]), target]:
        if x.is_symlink():
            raise ValueError('Symlink in target path: ' + rel)
    return target


def compile_plan(plan):
    if not isinstance(plan, dict):
        raise ValueError('Plan must be an object')
    rawroot = plan.get('root')
    if not isinstance(rawroot, str) or not pathlib.Path(rawroot).is_absolute():
        raise ValueError('Root must be an absolute existing workspace directory')
    if any(bit in ('.', '..') for bit in rawroot.split('/')) or os.path.normpath(rawroot) != rawroot:
        raise ValueError('Workspace root must be an explicit canonical absolute path')
    root = pathlib.Path(rawroot)
    if not root.is_dir() or root.is_symlink():
        raise ValueError('Root unavailable or symlink')
    actions = plan.get('operations')
    if not isinstance(actions, list) or len(actions) != 1:
        raise ValueError('Exactly one operation per plan: multiple file changes cannot be committed atomically')
    staging = {}
    for act in actions:
        if not isinstance(act, dict):
            raise ValueError('Operation must be object')
        rel = act.get('path')
        path = safe_rel(root, rel)
        if path in staging:
            raise ValueError('Only one action per path: '+rel)
        kind = act.get('kind')
        if kind not in ('write', 'replace'):
            raise ValueError('Only write-new or exact replace supported')
        if kind == 'write':
            if path.exists() or not path.parent.is_dir():
                raise ValueError('Write requires absent file and existing parent: '+rel)
            value = act.get('content')
            if not isinstance(value, str):
                raise ValueError('Write content must be text')
        else:
            if not path.is_file() or not stat.S_ISREG(path.stat().st_mode):
                raise ValueError('Replace requires existing regular file: '+rel)
            previous = path.read_text(encoding='utf-8')
            expect = act.get('sha256_before')
            if not isinstance(expect, str) or len(expect) != 64 or sha(previous) != expect:
                raise ValueError('SHA256 precondition failed: '+rel)
            old = act.get('old')
            new = act.get('new')
            if not isinstance(old, str) or not old or not isinstance(new, str):
                raise ValueError('old/new must be strings, old nonempty')
            if previous.count(old) != 1:
                raise ValueError('Replace target not unique: '+rel)
            value = previous.replace(old,new,1)
        staging[path] = {'kind':kind, 'content':value, 'root':root, 'rel':rel, 'before_sha':sha(previous) if kind == 'replace' else None}
    checks = plan.get('checks', [])
    if not isinstance(checks, list):
        raise ValueError('checks must be a list')
    for chk in checks:
        if not isinstance(chk, dict):
            raise ValueError('check must be object')
        path = safe_rel(root,chk.get('path'))
        content = staging.get(path, {}).get('content')
        if content is None:
            if not path.is_file():
                raise ValueError('Check target missing')
            content = path.read_text(encoding='utf-8')
        tests = chk.get('contains',[])
        if not isinstance(tests,list) or not all(isinstance(q,str) for q in tests):
            raise ValueError('contains must be text list')
        if any(q not in content for q in tests):
            raise ValueError('Content check failed: '+str(path))
        want = chk.get('sha256_after')
        if want is not None and (not isinstance(want,str) or sha(content)!=want):
            raise ValueError('Expected output SHA256 mismatch: '+str(path))
    return staging


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('plan')
    ap.add_argument('--apply',action='store_true')
    args=ap.parse_args()
    try:
        plan=json.loads(pathlib.Path(args.plan).read_text(encoding='utf-8'))
        staging=compile_plan(plan)
        if args.apply:
            for target,entry in staging.items():
                if safe_rel(entry['root'], entry['rel']) != target:
                    raise ValueError('Target changed after validation')
                if entry['kind']=='replace':
                    if not target.is_file() or target.is_symlink() or sha(target.read_text(encoding='utf-8')) != entry['before_sha']:
                        raise ValueError('Source changed between planning and applying')
                elif target.exists() or target.is_symlink():
                    raise ValueError('New target appeared after planning')
                data=entry['content']
                if entry['kind']=='write':
                    with target.open('x',encoding='utf-8') as f:
                        f.write(data)
                        f.flush(); os.fsync(f.fileno())
                else:
                    fd,tmp=tempfile.mkstemp(dir=target.parent, prefix='.forge-stage-')
                    try:
                        with os.fdopen(fd,'w',encoding='utf-8') as f:
                            f.write(data); f.flush(); os.fsync(f.fileno())
                        os.chmod(tmp,stat.S_IMODE(target.stat().st_mode))
                        os.replace(tmp,target)
                    finally:
                        if os.path.exists(tmp): os.unlink(tmp)
                if target.read_text(encoding='utf-8') != data:
                    raise ValueError('Post-apply readback differs from expected bytes')
        print(json.dumps({'ok':True,'applied':args.apply,'files':[{'path':str(p),'sha256_after':sha(e['content'])} for p,e in staging.items()]},ensure_ascii=False))
        return 0
    except (ValueError,OSError,UnicodeError,TypeError,KeyError,json.JSONDecodeError) as exc:
        print(json.dumps({'ok':False,'error':str(exc)},ensure_ascii=False), file=sys.stderr)
        return 1

if __name__=='__main__':
    raise SystemExit(main())
