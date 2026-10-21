#!/usr/bin/env python3
"""Deliver evidence-linked Forge products through the current case engine.

This runner does not run a model, grant file permissions, or attest that a real
agent understood a source. Deep-case workflow checks are necessary, not sufficient.
"""
from __future__ import annotations
import argparse
import contextlib
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile

DIR=Path(__file__).resolve().parent
KINDS={"anti-masterprompt","handoff","execution"}
SECRET_RE=re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|\b(?:sk-proj-[A-Za-z0-9_-]{12,}|github_pat_[A-Za-z0-9_]{12,}|ghp_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{16})\b")


def module(filename, name):
    spec=importlib.util.spec_from_file_location(name,DIR/filename)
    if spec is None or spec.loader is None:raise ValueError(f"Missing dependency {filename}")
    obj=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


def sha(body:bytes)->str:return hashlib.sha256(body).hexdigest()


def _reject_unapproved_source_reproduction(case_path: Path, draft_path: Path) -> None:
    """Fail closed for recognizable raw original text copied into a default no-source export.

    This is an *exact-text* barrier, not a semantic DLP scanner or grant validator.
    Short citations and paraphrases still require separate human rights review.
    """
    engine=module('case_engine.py','cfu_source_guard_engine')
    case=json.loads(case_path.read_text(encoding='utf8'))
    if case.get('schema')!='context-forge-case/1':raise ValueError('Unexpected case schema')
    draft=draft_path.read_text(encoding='utf8')
    root=Path(case['root_at_capture'])
    for source in case['sources']:
        original, _=engine.read_text(root,source['path'])
        if engine.sha(original.encode('utf8')) != source['sha256']:
            raise ValueError('Source changed before product disclosure check: '+source['id'])
        cleaned=original.strip()
        # The whole original must never cross by default, even if it is short.
        if len(cleaned)>=24 and cleaned in draft:
            raise ValueError('Unapproved original reproduced in draft: '+source['id'])
        # Long uninterrupted passages are full-copy-equivalent excerpts.
        # This deliberately does not imply shorter excerpts are authorized.
        normalized=' '.join(cleaned.split())
        normalized_draft=' '.join(draft.split())
        if len(normalized)>=160:
            for i in range(0,len(normalized)-159,80):
                if normalized[i:i+160] in normalized_draft:
                    raise ValueError('Unapproved long original passage in draft: '+source['id'])


def _safe_product(a, source, draft, dest, gate):
    # The current live 0.9.2 engine packages only A/B. Do not bypass its rights
    # filters or replace it with a stale local code snapshot.
    engine=module('case_engine.py','cfu_case_engine_live')
    cmd=['package','--case',str(source),'--draft',str(draft),'--out',str(dest),'--kind',a.kind]
    if a.recipient:cmd+=['--recipient',a.recipient]
    output=io.StringIO();errors=io.StringIO()
    with contextlib.redirect_stdout(output),contextlib.redirect_stderr(errors):
        result=engine.main(cmd)
    if result:
        raise ValueError('Case engine blocked package: '+(errors.getvalue() or output.getvalue())[:1600])
    filename={'anti-masterprompt':'ANTI_MASTERPROMPT.md','handoff':'HANDOFF.md'}[a.kind]
    actual=dest/filename
    if not actual.is_file() or actual.read_bytes()!=draft.read_bytes():
        raise ValueError('Delivery readback differs from validated source draft')
    report=json.loads((dest/'DELIVERY_CHECK.json').read_text(encoding='utf8'))
    if report.get('kind')!=a.kind or report.get('source_transfer')!='references_only_not_access_grant':
        raise ValueError('Delivery export rights / kind mismatch')
    if (dest/'sources').exists():raise ValueError('Unapproved original sources in package')
    return {'bundle':str(dest),'kind':a.kind,'status':'PACKAGED_WITH_RESEARCH_GATE',
            'research_gate':gate['status'],'source_transfer':report['source_transfer'],
            'semantic_quality':'REQUIRES_INDEPENDENT_REVIEW','host_activation':'NOT_TESTED'}


def _execution_product(a, source, draft, dest, gate):
    # Execution differs from a handoff. The live 0.9.2 case engine intentionally
    # does not promise an execution bundle, so preserve its source-security code.
    # This separate restricted delivery stores NO source bytes, claims, or paths.
    if not a.execution_evidence:raise ValueError('Actual execution needs an external action receipt')
    evidence_path=Path(a.execution_evidence).expanduser().resolve(strict=True)
    proof=json.loads(evidence_path.read_text(encoding='utf8'))
    if not isinstance(proof,dict) or proof.get('schema')!='context-forge-execution-evidence/1':
        raise ValueError('Unsupported external action receipt')
    if proof.get('status')!='success' or not str(proof.get('tool','')).strip() or not str(proof.get('authorized_scope','')).strip():
        raise ValueError('Execution receipt must identify action, authorized scope and success')
    if not str(proof.get('observed_result','')).strip():
        raise ValueError('Execution receipt missing observed readback')
    artifact_input=Path(str(proof.get('result_artifact_path',''))).expanduser()
    if artifact_input.is_symlink():raise ValueError('Symlink evidence artifact refused')
    target=artifact_input.resolve(strict=True)
    if not target.is_file():raise ValueError('No existing result artifact')
    if sha(target.read_bytes())!=proof.get('result_sha256'):
        raise ValueError('Result artifact does not match receipt')
    # The actual authorizing user and the tool execution can be confirmed only
    # in the real host. A self-declared receipt is never independent attestation.
    case=json.loads(source.read_text(encoding='utf8'))
    if case.get('schema')!='context-forge-case/1':raise ValueError('Unknown case source')
    ref_ids=set(re.findall(r'\[\[(S\d{3})\]\]',draft.read_text(encoding='utf8')))
    src_ids={s['id'] for s in case['sources']}
    if ref_ids-src_ids:raise ValueError('Unknown original cited in execution deliverable')
    text=draft.read_text(encoding='utf8')
    if SECRET_RE.search(text):raise ValueError('Possible credential in product')
    if dest.exists() or dest.is_symlink() or dest.parent.is_symlink():raise ValueError('Existing or symlink destination refused')
    dest.parent.mkdir(parents=True,exist_ok=True)
    stage=Path(tempfile.mkdtemp(prefix='.cfu-execution-stage-',dir=dest.parent))
    try:
        (stage/'WORK_RESULT.md').write_text(text,encoding='utf8')
        check={'schema':'context-forge-delivery/2','kind':'execution',
               'source_transfer':'references_only_not_access_grant',
               'source_ids':sorted(src_ids),'cited_source_ids':sorted(ref_ids),
               'external_receipt_sha256':sha(evidence_path.read_bytes()),
               'action_result_sha256':proof['result_sha256'],
               'execution':'external_receipt_and_result_bytes_matched_not_host_attested',
               'authorization':'declared_by_receipt_not_independently_verified',
               'semantic_quality':'REQUIRES_INDEPENDENT_REVIEW'}
        (stage/'DELIVERY_CHECK.json').write_text(json.dumps(check,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
        os.rename(stage,dest)
    except BaseException:
        shutil.rmtree(stage,ignore_errors=True)
        raise
    if (dest/'WORK_RESULT.md').read_bytes()!=draft.read_bytes():raise ValueError('Execution delivery readback changed')
    return {'bundle':str(dest),'kind':'execution','status':'PACKAGED_WITH_RESEARCH_GATE',
            'research_gate':gate['status'],'source_transfer':'references_only_not_access_grant',
            'execution':'EXTERNAL_RECEIPT_NOT_INDEPENDENTLY_ATTESTED',
            'semantic_quality':'REQUIRES_INDEPENDENT_REVIEW','host_activation':'NOT_TESTED'}


def run(a):
    if a.kind not in KINDS:raise ValueError('Unsupported kind')
    flowpath=Path(a.flow).expanduser().resolve(strict=True)
    source=Path(a.case).expanduser().resolve(strict=True)
    dest=Path(a.out).expanduser().absolute()
    draft=Path(a.draft).expanduser().resolve(strict=True)
    saved=json.loads(flowpath.read_text(encoding='utf8'))
    if saved.get('schema')!='context-forge-research-flow/1':raise ValueError('Unknown workflow')
    if Path(saved['case_path'])!=source:raise ValueError('Workflow source and deliverable case differ')
    if saved.get('kind')!=a.kind:raise ValueError('Workflow and output kind differ')
    if dest.exists() or dest.is_symlink():raise ValueError('Existing delivery destination refused')
    flow=module('research_flow.py','cfu_research_flow_delivery')
    check_out=io.StringIO();check_err=io.StringIO()
    with contextlib.redirect_stdout(check_out),contextlib.redirect_stderr(check_err):
        code=flow.main(['check','--flow',str(flowpath),'--draft',str(draft)])
    if code:raise ValueError('Research flow gate blocked delivery: '+(check_out.getvalue() or check_err.getvalue())[:1600])
    gate=json.loads(check_out.getvalue())
    if gate.get('status')!='MECHANICALLY_READY_NOT_SEMANTICALLY_VERIFIED':
        raise ValueError('Research workflow gate is not ready')
    # A/B/C must not smuggle raw unapproved source text in the product body.
    _reject_unapproved_source_reproduction(source,draft)
    report=(_execution_product(a,source,draft,dest,gate) if a.kind=='execution'
            else _safe_product(a,source,draft,dest,gate))
    print(json.dumps(report,ensure_ascii=False))
    return 0


def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--flow',required=True);p.add_argument('--case',required=True)
    p.add_argument('--draft',required=True);p.add_argument('--out',required=True)
    p.add_argument('--kind',required=True,choices=sorted(KINDS))
    p.add_argument('--recipient');p.add_argument('--execution-evidence')
    args=p.parse_args(argv)
    try:return run(args)
    except (OSError,ValueError,KeyError,TypeError,UnicodeError,json.JSONDecodeError) as e:
        print(json.dumps({'status':'BLOCKED','reason':str(e)},ensure_ascii=False),file=sys.stderr)
        return 2

if __name__=='__main__':sys.exit(main())
