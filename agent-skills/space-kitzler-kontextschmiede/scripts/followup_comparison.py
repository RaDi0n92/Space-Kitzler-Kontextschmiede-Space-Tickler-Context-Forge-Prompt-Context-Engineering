#!/usr/bin/env python3
"""Compare independently supplied downstream-agent trials; NEVER launch an agent.

A frozen battery and paired run artifacts are input, not proof of independent
sampling, host permissions, an unbiased reviewer, or causal improvement.
Standard library only; no network, mutation of source projects, or model access.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import statistics
import sys

SCHEMA='context-forge-receiver-battery/1'
RUN_SCHEMA='context-forge-receiver-runs/1'
RESULT_SCHEMA='context-forge-receiver-comparison/1'
ARMS={'direct','forge'}
CRITERIA=('goal','sources','permissions','originality','execution')


def digest(data:bytes)->str:
    return hashlib.sha256(data).hexdigest()


def canonical(o)->bytes:
    return json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf8')


def read_object(p):
    obj=json.loads(Path(p).read_text(encoding='utf8'))
    if not isinstance(obj,dict):raise ValueError('Expected JSON object')
    return obj


def write_once(path,obj):
    p=Path(path)
    if p.exists() or p.is_symlink():raise ValueError('Refusing to overwrite existing output')
    if not p.parent.exists():raise ValueError('Output parent must already exist')
    with p.open('x',encoding='utf8') as f:
        json.dump(obj,f,ensure_ascii=False,indent=2,sort_keys=True)
        f.write('\n')


def hex_hash(s):
    return isinstance(s,str) and len(s)==64 and all(c in '0123456789abcdef' for c in s)


def validate_cases(cases):
    if not isinstance(cases,list) or len(cases)<6:raise ValueError('At least six real case declarations required')
    ids=set();types=set()
    for c in cases:
        if not isinstance(c,dict):raise ValueError('Case must be object')
        cid=c.get('id');kind=c.get('kind');fingerprints=c.get('source_hashes')
        if not isinstance(cid,str) or not cid.strip() or cid in ids:raise ValueError('Empty/duplicate case id')
        if not isinstance(kind,str) or not kind.strip():raise ValueError('Case kind required')
        if not isinstance(fingerprints,dict) or not fingerprints or not all(isinstance(k,str) and k and hex_hash(v) for k,v in fingerprints.items()):
            raise ValueError(f'Invalid source hashes: {cid}')
        if not isinstance(c.get('task'),str) or not c['task'].strip():raise ValueError('Case task required')
        ids.add(cid);types.add(kind)
    if len(types)<3:raise ValueError('At least three different case types required')
    return ids


def freeze(args):
    obj=read_object(args.cases)
    if obj.get('schema')!=SCHEMA:raise ValueError('Bad battery schema')
    validate_cases(obj.get('cases'))
    required=('model','tool_profile','max_tokens','temperature')
    if not all(k in obj and obj[k] not in ('',None) for k in required):raise ValueError('Model/tool/budget/temperature must be frozen')
    if type(obj['max_tokens']) is not int or obj['max_tokens']<1:raise ValueError('Bad token budget')
    if type(obj['temperature']) not in (int,float) or not 0<=obj['temperature']<=2:raise ValueError('Bad temperature')
    frozen={'schema':SCHEMA,'battery':obj,'battery_sha256':digest(canonical(obj)),
            'limitations':['Freezing cannot attest that agents were actually run independently.',
                           'Freezing does not authorize access or transmission of sources.']}
    write_once(args.out,frozen)
    print(json.dumps({'frozen':args.out,'cases':len(obj['cases']),'status':'frozen_not_evaluated'}))


def evaluate(args):
    frozen=read_object(args.frozen)
    battery=frozen.get('battery')
    if frozen.get('schema')!=SCHEMA or not isinstance(battery,dict):raise ValueError('Invalid frozen battery')
    if digest(canonical(battery))!=frozen.get('battery_sha256'):raise ValueError('Battery hash mismatch')
    ids=validate_cases(battery.get('cases'))
    cidx={c['id']:c for c in battery['cases']}
    runs=read_object(args.runs)
    if runs.get('schema')!=RUN_SCHEMA or runs.get('battery_sha256')!=frozen['battery_sha256']:
        raise ValueError('Run set not bound to exact frozen battery')
    rows=runs.get('runs')
    if not isinstance(rows,list):raise ValueError('Missing run observations')
    seen=set();scores={cid:{arm:[] for arm in ARMS} for cid in ids}
    errors=[];guardrail_errors=[];file_count=0
    for row in rows:
        if not isinstance(row,dict):errors.append('Run entry not object');continue
        cid=row.get('case_id');arm=row.get('arm');rid=row.get('run_id')
        if cid not in ids or arm not in ARMS or not isinstance(rid,str) or not rid or rid in seen:
            errors.append('Unknown case/arm or invalid/duplicate run id');continue
        seen.add(rid)
        for key,value in (('model',battery['model']),('tool_profile',battery['tool_profile']),('max_tokens',battery['max_tokens']),('temperature',battery['temperature'])):
            if row.get(key)!=value:errors.append(f'{rid}: unfair {key}');break
        if row.get('source_hashes')!=cidx[cid]['source_hashes']:
            errors.append(f'{rid}: unequal source fingerprints');continue
        artifact=row.get('artifact')
        if not isinstance(artifact,str) or not artifact:
            errors.append(f'{rid}: missing output artifact');continue
        p=Path(artifact)
        if not p.is_file() or p.is_symlink():errors.append(f'{rid}: unavailable or symlinked artifact');continue
        try:
            if p.stat().st_size>2_000_000:raise ValueError('oversized')
            raw=p.read_bytes()
        except Exception:errors.append(f'{rid}: output unreadable or oversized');continue
        if digest(raw)!=row.get('artifact_sha256'):
            errors.append(f'{rid}: output artifact hash mismatch');continue
        file_count+=1
        rubric=row.get('review')
        if not isinstance(rubric,dict) or not all(type(rubric.get(k)) is int and 0<=rubric[k]<=4 for k in CRITERIA):
            errors.append(f'{rid}: invalid external rubric');continue
        if not isinstance(row.get('reviewer_id'),str) or not row['reviewer_id'].strip():
            errors.append(f'{rid}: reviewer identity missing');continue
        if row.get('source_leak') is True or row.get('unauthorized_action') is True:
            guardrail_errors.append(rid)
        scores[cid][arm].append(sum(rubric[k] for k in CRITERIA)/len(CRITERIA))
    insufficient=[cid for cid in sorted(ids) if min(len(scores[cid][a]) for a in ARMS)<2]
    summaries=[];better=[];worse=[]
    if not errors and not insufficient:
        for cid in sorted(ids):
            baseline=statistics.mean(scores[cid]['direct']);forge=statistics.mean(scores[cid]['forge'])
            delta=round(forge-baseline,4)
            summaries.append({'case_id':cid,'kind':cidx[cid]['kind'],'direct_mean':round(baseline,4),'forge_mean':round(forge,4),'difference':delta})
            if delta>0:better.append(cid)
            elif delta<0:worse.append(cid)
    # Never label performance 'proven': reviewer independence and host permissions
    # are declarations, not technically attestable by this standalone CLI.
    status=('safety_violations_reported' if guardrail_errors else
            'incomplete_or_incomparable' if errors or insufficient else
            'comparison_ready_for_independent_review')
    kind_wins=len({cidx[cid]['kind'] for cid in better})
    result={'schema':RESULT_SCHEMA,'status':status,'frozen_battery_sha256':frozen['battery_sha256'],
            'declared_cases':len(ids),'artifact_hashes_verified':file_count,
            'errors':errors,'insufficient_case_ids':insufficient,'reported_safety_violations':guardrail_errors,
            'comparison':summaries,'forge_better_cases':better,'forge_worse_cases':worse,
            'two_distinct_types_better':kind_wins>=2,
            'performance_proven':False,
            'limits':['Rubric values and reviewer independence are externally asserted, not authenticated.',
                      'Artifact hashes prove bytes, not independence, originality or factual correctness.',
                      'Equal tool-profile strings cannot establish equal real host privileges.',
                      'No agent was launched, no source was transmitted and no tool action was performed.']}
    write_once(args.out,result)
    print(json.dumps({'status':status,'cases':len(ids),'verified_artifacts':file_count,'two_types_better':kind_wins>=2}))


def main(argv=None):
    ap=argparse.ArgumentParser(description=__doc__)
    sub=ap.add_subparsers(dest='command',required=True)
    a=sub.add_parser('freeze');a.add_argument('--cases',required=True);a.add_argument('--out',required=True);a.set_defaults(func=freeze)
    a=sub.add_parser('evaluate');a.add_argument('--frozen',required=True);a.add_argument('--runs',required=True);a.add_argument('--out',required=True);a.set_defaults(func=evaluate)
    ns=ap.parse_args(argv)
    try:ns.func(ns);return 0
    except (ValueError,OSError,UnicodeError,json.JSONDecodeError) as exc:
        print(json.dumps({'status':'rejected','reason':str(exc)},ensure_ascii=False),file=sys.stderr);return 2

if __name__=='__main__':sys.exit(main())
