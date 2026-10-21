#!/usr/bin/env python3
"""Evidence-linked research execution gate for Context Forge Ultra.

A small local audit of *observable* work. It does not read semantically, call a model,
verify an agent's beliefs, or establish recipient/host permissions.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile

SCHEMA = "context-forge-research-flow/1"
MODULES = {
    "material": "material-und-quellen.md",
    "context": "drei-repositories-im-einsatz.md",
    "reasoning": "denkraum-und-forschung.md",
    "contrast": "sina-kontrastpruefung.md",
    "lens": "lokales-jlens-instrument.md",
    "product": "anti-masterprompt-und-weiterarbeit.md",
    "execution": "abnahme-und-grenzen.md",
}
EFFECTS = {"reread", "new_source", "revised_claim", "competing_hypothesis", "contrast_probe", "changed_output", "observed_action", "external_measurement"}
TYPES = {"anti-masterprompt", "handoff", "execution"}
SHA_RE = re.compile(r"^[a-f0-9]{64}$")
SECRETS = re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|\b(?:sk-proj-[A-Za-z0-9_-]{12,}|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{12,}|AKIA[A-Z0-9]{16})\b")


def digest(data: bytes) -> str: return hashlib.sha256(data).hexdigest()
def read_json(path: Path): return json.loads(path.read_text(encoding="utf-8"))


def write_state(path: Path, obj: dict, create: bool = False):
    if path.is_symlink() or (create and path.exists()): raise ValueError("Existing/symlink workflow state refused")
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf8", dir=path.parent, prefix=".cf-flow-", delete=False) as h:
        tmp = Path(h.name)
        json.dump(obj, h, ensure_ascii=False, indent=2, sort_keys=True)
        h.write("\n")
        h.flush(); os.fsync(h.fileno())
    try: os.replace(tmp, path)
    finally: tmp.unlink(missing_ok=True)


def case_from_flow(obj: dict) -> dict:
    if obj.get("schema") != SCHEMA: raise ValueError("Not a Forge workflow")
    casepath = Path(obj["case_path"])
    if casepath.is_symlink(): raise ValueError("Case symlink refused")
    case = read_json(casepath)
    if case.get("schema") != "context-forge-case/1": raise ValueError("Invalid case source")
    original = {s["id"]: s["sha256"] for s in obj["sources"]}
    current = {s["id"]: s["sha256"] for s in case.get("sources", [])}
    if original != current: raise ValueError("Changed case source inventory; refresh workflow")
    root = Path(case["root_at_capture"])
    for source in case["sources"]:
        rel = Path(source["path"])
        if rel.is_absolute() or ".." in rel.parts or "." in rel.parts: raise ValueError("Unsafe source path")
        f = root / rel
        if not f.is_file() or f.is_symlink() or any(p.is_symlink() for p in f.parents if p != Path("/")):
            raise ValueError(f"Missing/linked source: {source['id']}")
        if digest(f.read_bytes()) != source["sha256"]:
            raise ValueError(f"Stale source: {source['id']}")
    return case


def start(a):
    if a.kind not in TYPES: raise ValueError("Unknown product type")
    cp = Path(a.case).expanduser().resolve(strict=True)
    case = read_json(cp)
    if case.get("schema") != "context-forge-case/1" or not case.get("sources"):
        raise ValueError("A populated case_engine inventory is required")
    obj = {"schema": SCHEMA, "case_path": str(cp), "kind": a.kind,
           "depth": a.depth, "reason_for_depth": a.why,
           "sources": [{"id":s["id"],"sha256":s["sha256"]} for s in case["sources"]],
           "reads": [], "applications": [],
           "disclaimer": "Read events and research effects are self-reported; hashes do not prove semantic understanding."}
    case_from_flow(obj)
    path=Path(a.out).expanduser().absolute();write_state(path,obj,create=True)
    print(json.dumps({"flow":str(path),"status":"started","depth":a.depth}))


def observed(a):
    path=Path(a.flow).expanduser().absolute();flow=read_json(path);case=case_from_flow(flow)
    s=next((x for x in case["sources"] if x["id"]==a.source),None)
    if s is None: raise ValueError("Unknown source")
    if not a.quote.strip(): raise ValueError("Actual quote required")
    content=(Path(case["root_at_capture"])/s["path"]).read_text(encoding="utf8")
    if a.quote not in content: raise ValueError("Quote not in original source")
    n=content.index(a.quote)
    item={"id":f"R{len(flow['reads'])+1:03d}", "source":s["id"],
          "start":n,"end":n+len(a.quote),"quote_sha256":digest(a.quote.encode()),
          "reason":a.why,"proof":"quoted_span_exists_not_semantic_read_attestation"}
    flow["reads"].append(item);write_state(path,flow)
    print(json.dumps({"recorded":item["id"],"proof":item["proof"]}))



def claim_supported_by_reads(claim, read_events):
    """Mechanically bind each claimed source span to the reads of THIS application.

    This does not attest semantic reading or correctness of the interpretation.
    Quote-free hypotheses require an original read of the attributed source but
    cannot be certified as observed facts.
    """
    source = claim.get("source")
    quote = claim.get("quote") or ""
    start = claim.get("start_char")
    for event in read_events:
        if event.get("source") != source:
            continue
        if not quote:
            return True
        if (isinstance(start, int) and isinstance(event.get("start"), int)
                and isinstance(event.get("end"), int)
                and event["start"] < start + len(quote)
                and event["end"] > start):
            return True
    return False


def applied(a):
    path=Path(a.flow).expanduser().absolute();flow=read_json(path);case_from_flow(flow)
    if a.module not in MODULES: raise ValueError("Unknown module")
    if a.effect not in EFFECTS: raise ValueError("Unknown effect")
    if a.before.strip()==a.after.strip() or not a.before.strip() or not a.after.strip():
        raise ValueError("Specific distinct before/after observations required")
    reads=[x.strip() for x in a.reads.split(",") if x.strip()]
    valid={x["id"] for x in flow["reads"]}
    if not reads or set(reads)-valid: raise ValueError("Research application must reference actual recorded source reads")
    claims=[x.strip() for x in a.claims.split(",") if x.strip()]
    case=case_from_flow(flow)
    index={c["id"]:c for c in case.get("claims",[])}
    if set(claims)-set(index):raise ValueError("Unknown case claim referenced by research application")
    if claims:
        linked = {r["id"]: r for r in flow["reads"] if r["id"] in reads}
        for cid in claims:
            if not claim_supported_by_reads(index[cid], linked.values()):
                raise ValueError("Claim " + cid + " has no overlapping original read in this application")
    ref=Path(__file__).resolve().parents[1]/"references"/MODULES[a.module]
    if not ref.is_file(): raise ValueError("Required skill reference missing")
    evidence=None
    if a.artifact:
        p=Path(a.artifact).expanduser().resolve(strict=True)
        if not p.is_file() or p.is_symlink(): raise ValueError("Evidence artifact unavailable")
        evidence={"path":str(p),"sha256":digest(p.read_bytes())}
    if a.effect in {"observed_action", "external_measurement"} and evidence is None:
        raise ValueError("Action/measurement requires existing external artifact")
    flow["applications"].append({"id":f"A{len(flow['applications'])+1:03d}",
           "module":a.module,"module_reference_sha256":digest(ref.read_bytes()),
           "reads":reads,"claims":claims,"effect":a.effect,"before":a.before,"after":a.after,
           "evidence":evidence,"verification":"recorded_not_independently_semantically_verified"})
    write_state(path,flow)
    print(json.dumps({"applied":flow["applications"][-1]["id"],"module":a.module,"effect":a.effect}))


def check(a):
    flow=read_json(Path(a.flow));case=case_from_flow(flow)
    problems=[]
    draft=Path(a.draft).expanduser().resolve(strict=True)
    text=draft.read_text(encoding="utf8")
    if len(text.strip())<260:problems.append("product_too_short")
    if SECRETS.search(text):problems.append("credential_signature_in_product")
    reads=flow["reads"]
    observed_ids={r["id"] for r in reads}
    # Recompute every reported original span at the delivery gate. A saved flow
    # is user-editable data; a prior successful `read` command is not immunity
    # from post-hoc edits to offsets or quote hashes.
    source_index={s["id"]:s for s in case["sources"]}
    original_text={sid:(Path(case["root_at_capture"])/src["path"]).read_text(encoding="utf8")
                   for sid,src in source_index.items()}
    for r in reads:
        raw=original_text.get(r.get("source"))
        start=r.get("start");end=r.get("end")
        if (raw is None or type(start) is not int or type(end) is not int
                or start<0 or end<=start or end>len(raw)
                or digest(raw[start:end].encode("utf8")) != r.get("quote_sha256")):
            problems.append("invalid_recorded_read:"+str(r.get("id", "unknown")))
    if not reads:problems.append("no_original_spans_checked")
    # One substantial original may contain an entire project history. Number of
    # files is not a proxy for difficult reasoning or independent corroboration.
    # An agent and independent reviewer must judge the *semantic* adequacy of
    # the reading; that is not certifiable by counting source identifiers.
    required={"material","product"}
    if flow["depth"]=="deep":required|={"context","reasoning"}
    if flow["kind"]=="execution":required|={"execution"}
    present={x["module"] for x in flow["applications"]}
    for module in sorted(required-present):problems.append("missing_application:"+module)
    if flow["depth"]=="deep" and not any(a["effect"] in {"reread","new_source","revised_claim","competing_hypothesis","contrast_probe"} for a in flow["applications"] if a["module"] in {"context","reasoning","contrast"}):
        problems.append("research_affected_no_question_source_or_hypothesis")
    # The research trace must touch the actual case claims rather than becoming a
    # parallel, unbound narrative. A factual link still does not prove correctness.
    claim_index={c["id"]:c for c in case.get("claims",[])}
    if flow["depth"]=="deep":
        if not claim_index:problems.append("deep_case_has_no_source_anchored_claims")
        for mod in ("material","context","reasoning"):
            if not any(x["module"]==mod and x.get("claims") for x in flow["applications"]):
                problems.append("unbound_research_to_case_claims:"+mod)
        artifact=next((x.get("evidence") for x in flow["applications"] if x["module"]=="product" and x.get("effect")=="changed_output" and x.get("evidence") and x["evidence"]["path"]==str(draft)),None)
        if artifact is None or artifact.get("sha256")!=digest(draft.read_bytes()):
            problems.append("deep_product_not_linked_to_actual_draft_bytes")
    # Validate that all evidence artifacts are still exactly the submitted bytes.
    for a0 in flow["applications"]:
        if set(a0["reads"])-observed_ids:problems.append("unlinked_read:"+a0["id"])
        if set(a0.get("claims",[]))-set(claim_index):problems.append("unknown_claim:"+a0["id"])
        matching=[r for r in reads if r["id"] in a0.get("reads",[])]
        for cid in a0.get("claims",[]):
            if cid in claim_index and not claim_supported_by_reads(claim_index[cid],matching):
                problems.append("unread_claim_span:"+a0["id"]+":"+cid)
        ref=Path(__file__).resolve().parents[1]/"references"/MODULES[a0["module"]]
        if not ref.exists() or digest(ref.read_bytes())!=a0["module_reference_sha256"]:
            problems.append("changed_reference:"+a0["id"])
        e=a0["evidence"]
        if e:
            f=Path(e["path"])
            if not f.exists() or digest(f.read_bytes())!=e["sha256"]:
                problems.append("stale_artifact:"+a0["id"])
    if flow["kind"]=="execution" and not any(a0["module"]=="execution" and a0["effect"]=="observed_action" and a0["evidence"] for a0 in flow["applications"]):
        problems.append("execution_not_observed")
    # Do not validate authorization by a local boolean or an unverifiable JSON declaration.
    product_refs=set(re.findall(r"\[\[(S\d{3})\]\]",text))
    source_ids={s["id"] for s in case["sources"]}
    if product_refs-source_ids:problems.append("unknown_source_referenced")
    if flow["depth"]=="deep" and not product_refs:
        problems.append("deep_product_needs_an_actual_source_anchor")
    result={"schema":"context-forge-research-gate/1","status":"MECHANICALLY_READY_NOT_SEMANTICALLY_VERIFIED" if not problems else "BLOCKED",
        "kind":flow["kind"],"depth":flow["depth"],"sources_observed":len({r['source'] for r in reads}),
        "modules_applied":sorted(present),"application_count":len(flow["applications"]),
        "problems":problems,"host_activation":"NOT_TESTED","semantic_quality":"REQUIRES_REAL_AGENT_REVIEW",
        "recipient_authority":"NOT_VERIFIED","package_export":"NOT_PERFORMED"}
    print(json.dumps(result,ensure_ascii=False,indent=2))
    if problems:return 2
    return 0


def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest="cmd",required=True)
    a=sub.add_parser("start");a.add_argument("--case",required=True);a.add_argument("--out",required=True);a.add_argument("--kind",choices=sorted(TYPES),required=True);a.add_argument("--depth",choices=["standard","deep"],required=True);a.add_argument("--why",required=True);a.set_defaults(func=start)
    a=sub.add_parser("read");a.add_argument("--flow",required=True);a.add_argument("--source",required=True);a.add_argument("--quote",required=True);a.add_argument("--why",required=True);a.set_defaults(func=observed)
    a=sub.add_parser("apply");a.add_argument("--flow",required=True);a.add_argument("--module",choices=sorted(MODULES),required=True);a.add_argument("--reads",required=True);a.add_argument("--effect",choices=sorted(EFFECTS),required=True);a.add_argument("--before",required=True);a.add_argument("--after",required=True);a.add_argument("--artifact");a.add_argument("--claims",default="");a.set_defaults(func=applied)
    a=sub.add_parser("check");a.add_argument("--flow",required=True);a.add_argument("--draft",required=True);a.set_defaults(func=check)
    args=p.parse_args(argv)
    try:return args.func(args) or 0
    except (OSError,ValueError,KeyError,TypeError,UnicodeError,json.JSONDecodeError) as e:
        print(json.dumps({"status":"BLOCKED","reason":str(e)},ensure_ascii=False),file=sys.stderr)
        return 2

if __name__=="__main__":sys.exit(main())
