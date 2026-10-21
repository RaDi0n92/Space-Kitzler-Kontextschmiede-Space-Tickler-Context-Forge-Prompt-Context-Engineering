#!/usr/bin/env python3
"""Context Forge: evidence-bound case work, from the three researched repository mechanisms.

Stdlib only. No network access, model inference, background tasks, or implicit mutations.
The model/agent must itself read and interpret the source texts; file inventory != reading.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import shutil
import tempfile
from pathlib import Path
import re
import sys

VERSION = "0.9.0"
KINDS = {"observation", "decision", "user_intent", "requirement", "correction", "hypothesis", "open_question", "work_result"}
ACTORS = {"user", "assistant", "document_author", "agent_interpretation", "tool"}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def encoded(obj) -> bytes:
    return (json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf8")


def load(path: Path):
    return json.loads(path.read_text(encoding="utf8"))


def save(path: Path, obj):
    if path.exists() and path.is_symlink():
        raise ValueError("Symlink output forbidden")
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    if temp.is_symlink():
        raise ValueError("Symlink staging forbidden")
    temp.write_bytes(encoded(obj))
    os.replace(temp, path)


def within(root: Path, path_str: str) -> tuple[Path, str]:
    rel = Path(path_str)
    if rel.is_absolute() or not rel.parts or any(part in ("..", ".") for part in rel.parts):
        raise ValueError(f"Not a clean relative source path: {path_str}")
    path = root.joinpath(rel)
    if root.is_symlink() or any(p.is_symlink() for p in (root, *path.parents, path)):
        raise ValueError(f"Symlink path refused: {path_str}")
    resolved = path.resolve(strict=True)
    if resolved == root or root not in resolved.parents or not resolved.is_file():
        raise ValueError(f"Source outside scope or not a file: {path_str}")
    return resolved, rel.as_posix()


def read_text(root: Path, relative: str) -> tuple[str, str]:
    path, rel = within(root, relative)
    if path.stat().st_size > 8_000_000:
        raise ValueError(f"Oversized single text source: {rel}")
    return path.read_text(encoding="utf8"), rel


def check_case(obj):
    if obj.get("schema") != "context-forge-case/1":
        raise ValueError("Unsupported case schema")
    if not isinstance(obj.get("sources"), list) or not isinstance(obj.get("claims"), list):
        raise ValueError("Invalid source/claim arrays")


def command_inventory(a):
    root = Path(a.root).expanduser().resolve(strict=True)
    if not root.is_dir(): raise ValueError("Root must be a directory")
    if not a.sources: raise ValueError("Explicit source files required")
    sources = []
    seen = set()
    for n, item in enumerate(a.sources, 1):
        data, rel = read_text(root, item)
        if rel in seen: raise ValueError("Duplicate source")
        seen.add(rel)
        sources.append({"id":f"S{n:03d}", "path":rel, "sha256":sha(data.encode("utf8")),
                        "characters":len(data),"capture":"mechanical_read_not_semantic_read",
                        "recipient_access":"not_assessed", "transfer_modes":[], "read_ranges": []})
    case = {"schema":"context-forge-case/1", "version":VERSION,"root_at_capture":str(root),
            "sources":sources,"claims":[],"relations":[],"lens_observations":[],"read_events":[],"work_events":[],
            "limits":["File bytes were mechanically inspected; no LLM semantic reading is implied.",
                      "Recipient access must be checked independently."]}
    dest = Path(a.out).expanduser().absolute()
    if dest.exists() and not a.force: raise ValueError("Refusing to overwrite case without --force")
    save(dest,case)
    print(json.dumps({"case":str(dest),"sources":len(sources),"status":"inventoried_not_understood"}))


def command_record(a):
    case_path=Path(a.case).expanduser().absolute()
    obj=load(case_path); check_case(obj)
    if a.kind not in KINDS or a.actor not in ACTORS: raise ValueError("Invalid classification")
    source=next((s for s in obj["sources"] if s["id"]==a.source),None)
    if not source: raise ValueError("Unknown source ID")
    if a.kind != "hypothesis" and not a.quote: raise ValueError("Evidence quote required for asserted observations")
    root=Path(obj["root_at_capture"])
    data,_=read_text(root,source["path"])
    if sha(data.encode("utf8"))!=source["sha256"]: raise ValueError("Source changed since inventory; refresh via new snapshot")
    quote=a.quote or ""
    if quote and quote not in data: raise ValueError("Quote not present in this source")
    if a.supersedes and not any(c["id"]==a.supersedes for c in obj["claims"]):
        raise ValueError("Superseded claim not found")
    if a.supersedes and a.kind != "correction": raise ValueError("Only corrections may supersede claims")
    if a.supersedes:
        previous=next(c for c in obj["claims"] if c["id"]==a.supersedes)
        if a.actor!="user" or previous.get("actor")!="user":
            raise ValueError("Only explicit user corrections can supersede user decisions")
        if not a.scope or a.scope in {"unknown","global"} or a.scope!=previous.get("scope"):
            raise ValueError("A correction may replace only the exact nonempty prior scope")

    if a.kind=="hypothesis" and a.actor not in {"agent_interpretation","assistant"}:
        raise ValueError("Hypotheses require analyst/assistant attribution")
    if a.kind in {"decision", "correction", "user_intent"} and a.actor=="tool":
        raise ValueError("Tool output cannot itself authorize a user decision")
    ident=f"C{len(obj['claims'])+1:03d}"
    start=data.find(quote) if quote else None
    obj["claims"].append({"id":ident,"kind":a.kind,"actor":a.actor,"source":a.source,
           "source_sha256":source["sha256"],"quote":quote,"start_char":start,
           "scope":a.scope,"meaning":a.meaning,"status":"hypothesis" if a.kind=="hypothesis" else "source_anchored_not_independently_validated",
           "supersedes":a.supersedes})
    # Record only evidence of specific source inspection; never claim full semantic read.
    if quote:
        source["read_ranges"].append({"start_char":start,"end_char":start+len(quote),"proof":"exact_source_substring"})
    save(case_path,obj)
    print(json.dumps({"claim":ident,"status":obj["claims"][-1]["status"]}))


def command_relation(a):
    obj=load(Path(a.case));check_case(obj)
    valid={x["id"] for x in obj["claims"]}
    if a.left not in valid or a.right not in valid or a.left==a.right:
        raise ValueError("Missing or identical relation endpoints")
    if a.type not in {"supports","contradicts","replaces","requires","analogy","opens_question"}:
        raise ValueError("Unknown relation type")
    obj["relations"].append({"from":a.left,"to":a.right,"type":a.type,
                             "reason":a.reason,"epistemic_status":"agent_proposal_not_proven"})
    save(Path(a.case),obj)
    print(json.dumps({"relations":len(obj["relations"])}))


def command_verify(a):
    obj=load(Path(a.case));check_case(obj)
    root=Path(obj["root_at_capture"])
    issues=[]
    index={s["id"]:s for s in obj["sources"]}
    for s in obj["sources"]:
        try:
            data,_=read_text(root,s["path"])
            if sha(data.encode("utf8"))!=s["sha256"]: issues.append({"source":s["id"],"error":"stale_snapshot"})
        except (OSError,ValueError,UnicodeError) as e: issues.append({"source":s["id"],"error":str(e)})
    for c in obj["claims"]:
        s=index.get(c["source"])
        if not s: issues.append({"claim":c["id"],"error":"dangling_source"});continue
        if c.get("quote"):
            try:
                data,_=read_text(root,s["path"])
                if c["quote"] not in data: issues.append({"claim":c["id"],"error":"quote_mismatch"})
            except (OSError,ValueError,UnicodeError): pass
    print(json.dumps({"status":"source_integrity_ok_semantics_not_verified" if not issues else "source_integrity_failed",
         "sources":len(obj["sources"]),"claims":len(obj["claims"]),"issues":issues},ensure_ascii=False,indent=2))
    return 0 if not issues else 2


def validate_battery(rows):
    if not isinstance(rows,list) or not rows: raise ValueError("Nonempty battery list required")
    ids=[]
    for r in rows:
        if not isinstance(r,dict): raise ValueError("Probe must be an object")
        if set(["id","base","relevant_intervention","irrelevant_paraphrase","expected_base","expected_changed"]) - r.keys():
            raise ValueError("Probe misses triplet or expected labels")
        if not all(isinstance(r[k],str) and r[k].strip() for k in ["id","base","relevant_intervention","irrelevant_paraphrase","expected_base","expected_changed"]):
            raise ValueError("Empty probe field")
        if r["expected_base"]==r["expected_changed"]: raise ValueError("Relevant intervention lacks distinct predicted result")
        if len({r["base"],r["relevant_intervention"],r["irrelevant_paraphrase"]})!=3:
            raise ValueError("Textually duplicate probe variants")
        ids.append(r["id"])
    if len(set(ids))!=len(ids): raise ValueError("Repeated probe IDs")


def command_freeze(a):
    content=Path(a.battery).read_bytes()
    rows=json.loads(content)
    validate_battery(rows)
    obj={"schema":"context-forge-probes/1","frozen_source_sha256":sha(content),
         "count":len(rows),"cases":rows,"limitations":"Textual contrast tests, not activation measurements"}
    out=Path(a.out)
    if out.exists(): raise ValueError("Frozen manifest exists; do not silently rewrite after results")
    save(out,obj)
    print(json.dumps({"sha256":obj["frozen_source_sha256"],"count":obj["count"],"status":"frozen_before_results"}))


def command_score(a):
    frozen=load(Path(a.frozen))
    if frozen.get("schema")!="context-forge-probes/1": raise ValueError("Wrong frozen manifest")
    results=load(Path(a.results))
    if not isinstance(results,dict): raise ValueError("Results must be keyed object")
    rows=[]
    for c in frozen["cases"]:
        got=results.get(c["id"],{})
        if not isinstance(got,dict) or any(k not in got for k in ("base","relevant","irrelevant")):
            rows.append({"id":c["id"],"status":"unscorable_missing_observation"});continue
        base=got["base"]==c["expected_base"]
        relevant=got["relevant"]==c["expected_changed"]
        irrelevant=got["irrelevant"]==c["expected_base"]
        rows.append({"id":c["id"],"base_correct":base,"relevant_change_correct":relevant,
                     "irrelevant_paraphrase_invariant":irrelevant,"status":"observed_triplet_pass" if all([base,relevant,irrelevant]) else "observed_triplet_fail"})
    scores={"schema":"context-forge-contrast-results/1","frozen_source_sha256":frozen["frozen_source_sha256"],
       "items":rows,"passing":sum(x["status"]=="observed_triplet_pass" for x in rows),
       "status":"offline_reported_results_no_neural_claim"}
    if a.out: save(Path(a.out),scores)
    print(json.dumps(scores,ensure_ascii=False,indent=2))


def command_import_lens(a):
    obj=load(Path(a.case));check_case(obj)
    data=load(Path(a.report))
    required={"model","experiment_id","mode","baseline","intervention","matched_control"}
    if not isinstance(data,dict) or required-data.keys():raise ValueError("Lens report contract incomplete")
    if data["mode"] not in {"readout","steer","swap","ablate"}:
        raise ValueError("Invalid local lens mode")
    if any(not isinstance(data[x],(str,dict)) or not data[x] for x in required):
        raise ValueError("Empty lens report input")
    digest=sha(Path(a.report).read_bytes())
    obj["lens_observations"].append({"id":f"J{len(obj['lens_observations'])+1:03d}",
        "report_sha256":digest,"instrument":"jlens-gguf_local_report",
        "provenance":"user_supplied_external_not_replicated_here","model":data["model"],
        "experiment_id":data["experiment_id"],"mode":data["mode"],
        "baseline":data["baseline"],"intervention":data["intervention"],
        "matched_control":data["matched_control"],
        "limitation":"Does not measure ChatGPT internals; interventions not reproduced by this importer."})
    save(Path(a.case),obj)
    print(json.dumps({"lens_imported":len(obj["lens_observations"]),"status":"externally_reported_not_independently_confirmed"}))


TRANSFER_SCHEMA = "context-forge-transfer-grants/1"
SENSITIVE_RE = re.compile(
    r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"
    r"|\b(?:sk-proj-[A-Za-z0-9_-]{12,}|github_pat_[A-Za-z0-9_]{12,}|ghp_[A-Za-z0-9]{20,}|xox[baprs]-[A-Za-z0-9-]{16,}|AKIA[A-Z0-9]{16})\b"
)


def check_sensitive(text: str, label: str) -> None:
    if SENSITIVE_RE.search(text):
        raise ValueError(f"Potential credential in {label}; remove or redact before transfer")


def select_transfers(obj: dict, a) -> tuple[list, list]:
    if not a.include_sources:
        if a.grants: raise ValueError("--grants requires --include-sources")
        return [], []
    if not a.grants or not a.recipient:
        raise ValueError("Full source transfer requires --grants AND --recipient")
    manifest=load(Path(a.grants))
    if not isinstance(manifest,dict) or manifest.get("schema")!=TRANSFER_SCHEMA:
        raise ValueError("Invalid explicit transfer manifest schema")
    grants=manifest.get("grants")
    if not isinstance(grants,list): raise ValueError("Missing grants array")
    recipient=str(a.recipient).strip()
    if not recipient or recipient.lower() in {"*", "any", "unknown"}:
        raise ValueError("Concrete recipient required")
    index={s["id"]:s for s in obj["sources"]}
    accepted={}
    for g in grants:
        if not isinstance(g,dict): raise ValueError("Malformed transfer grant")
        sid=g.get("source_id")
        if sid not in index or sid in accepted: raise ValueError("Unknown/duplicate source grant")
        s=index[sid]
        if (g.get("recipient")!=recipient or g.get("mode")!="full"
           or g.get("source_sha256")!=s["sha256"] or g.get("path")!=s["path"]
           or g.get("approved") is not True or not str(g.get("authority", "")).strip()):
            raise ValueError("Transfer grant lacks matching recipient, identity, scope or approval")
        accepted[sid]=g
    chosen=[]; omitted=[]
    root=Path(obj["root_at_capture"])
    for s in obj["sources"]:
        if s["id"] not in accepted:
            omitted.append({"source_id":s["id"],"reason":"not_authorized_for_recipient"})
            continue
        content,rel=read_text(root,s["path"])
        if sha(content.encode("utf8"))!=s["sha256"]:
            raise ValueError("Source changed during transfer preflight")
        check_sensitive(content,f"source {s['id']}")
        chosen.append((s,rel,content))
    if a.require_all and omitted:
        raise ValueError("Require-all requested, but not every source has a matching grant")
    return chosen,omitted


def decision_summary(obj: dict) -> tuple[list, list]:
    claims=list(obj["claims"])
    index={c["id"]:c for c in claims}
    overridden=set(); conflicts=[]
    for c in claims:
        prior=index.get(c.get("supersedes")) if c.get("supersedes") else None
        if c.get("kind")=="correction" and prior is not None:
            if (c.get("actor")=="user" and prior.get("actor")=="user"
                and c.get("scope") not in {"unknown", "global", ""}
                and c.get("scope")==prior.get("scope")):
                overridden.add(prior["id"])
            else:
                conflicts.append({"claim":c["id"],"prior":prior["id"],"reason":"unverified_supersession_scope_or_actor"})
    return [c for c in claims if c["id"] not in overridden],conflicts


def command_record_read(a):
    case_path=Path(a.case);obj=load(case_path);check_case(obj)
    source=next((s for s in obj["sources"] if s["id"]==a.source),None)
    if source is None: raise ValueError("Source missing")
    original,_=read_text(Path(obj["root_at_capture"]),source["path"])
    if sha(original.encode("utf8"))!=source["sha256"]:
        raise ValueError("Source changed since inventory")
    if not a.quote or a.quote not in original:
        raise ValueError("Observed source excerpt not found")
    start=original.find(a.quote)
    event={"id":f"R{len(obj.get('read_events',[]))+1:03d}","source_id":source["id"],
           "source_sha256":source["sha256"],"start_char":start,"end_char":start+len(a.quote),
           "actor":a.actor,"proof":"quote_present_and_user_declared_read_not_host_attested",
           "semantic_understanding":"not_independently_verified"}
    obj.setdefault("read_events",[]).append(event)
    save(case_path,obj)
    print(json.dumps({"recorded":event["id"],"read_status":event["proof"]}))


def command_compose(a):
    obj=load(Path(a.case));check_case(obj)
    if a.kind not in {"anti-masterprompt","handoff"}:
        raise ValueError("Unknown compose kind")
    active,conflicts=decision_summary(obj)
    claims=[c for c in active if c.get("meaning") and c.get("source")]
    if not claims: raise ValueError("No source anchored claims for composing")
    lines=["# "+("Anti-Masterprompt" if a.kind=="anti-masterprompt" else "Kontextübergabe"),
           "", "**Status:** Strukturentwurf aus angelegten Aussagen; die Semantik wurde nicht automatisch geprüft.",
           "", "## Auftrag, historische Entscheidungen und Beobachtungen"]
    for c in claims:
        label={"user_intent":"Nutzerziel","correction":"Nutzerkorrektur","decision":"Entscheidung",
            "hypothesis":"Offene Hypothese","open_question":"Ungeklärte Frage"}.get(c["kind"],c["kind"])
        lines.append(f"- **{label}** [{c['id']}], Scope `{c.get('scope','unknown')}`: "
                     +c["meaning"].replace("\n"," ")+f" [[{c['source']}]]")
    if conflicts:
        lines += ["", "## Nicht aufgelöste Geltungskonflikte"]
        for c in conflicts: lines.append(f"- {c['claim']} zu {c['prior']}: {c['reason']}")
    lines += ["", "## Originale und Zugriffslage"]
    for s in obj["sources"]:
        lines.append(f"- [[{s['id']}]] {s['path']} (SHA256 {s['sha256'][:16]}…; "
                     "Empfängerzugang **NICHT verifiziert**, keine Datei automatisch übertragen)")
    lines += ["", "## Eigenständige Weiterarbeit", "Prüfe zuerst die wirklich erreichbaren Originale "
              "und den Geltungsbereich der Entscheidungen. Entwickle abweichende, überprüfbare Deutungen, "
              "ohne Quellen oder Nutzeraufträge zu erfinden. Führe Aktionen nur bei konkreter Autorisation "
              "und mit realen verfügbaren Werkzeugen aus."]
    if a.kind=="anti-masterprompt":
        lines += ["", "Erzeuge das konkret beauftragte Ergebnis vollständig; ersetze keine Ausführung "
                  "durch einen bloßen Plan. Markiere unzugängliche Quellen und fehlende Voraussetzungen."]
    else:
        lines += ["", "## Zwei Lesewege", "**Ersteller:** Nur ausdrücklich protokollierte "
                  "Quellenausschnitte, keine behauptete semantische Vollleseabdeckung.",
                  "**Nachfolger:** Öffne die oben genannten Originale nur, wenn dein Host sie tatsächlich "
                  "bereitstellt; ansonsten echte Zugriffslücke melden."]
    out=Path(a.out)
    if out.exists(): raise ValueError("Compose output already exists")
    out.parent.mkdir(parents=True,exist_ok=True)
    with out.open("x",encoding="utf8") as handle:handle.write("\n".join(lines)+"\n")
    print(json.dumps({"status":"structured_draft_requires_semantic_review","path":str(out),"claims":len(claims)}))


def command_package(a):
    obj=load(Path(a.case));check_case(obj)
    draft=Path(a.draft).read_text(encoding="utf8")
    if len(draft.strip())<200: raise ValueError("Independent prose draft too short")
    check_sensitive(draft,"draft")
    ids={s["id"] for s in obj["sources"]}
    refs=set(re.findall(r"\[\[(S\d{3})\]\]",draft))
    if refs-ids: raise ValueError("Draft cites unknown source IDs")
    selected,omitted=select_transfers(obj,a)
    out=Path(a.out).expanduser().absolute()
    if out.exists() or out.is_symlink(): raise ValueError("Existing output, refusing overwrite")
    if out.parent.is_symlink(): raise ValueError("Symlink output parent refused")
    out.parent.mkdir(parents=True,exist_ok=True)
    stage=Path(tempfile.mkdtemp(prefix=".cfu-stage-",dir=str(out.parent)))
    try:
        (stage/("ANTI_MASTERPROMPT.md" if a.kind=="anti-masterprompt" else "HANDOFF.md")).write_text(draft,encoding="utf8")
        allowed_ids={s["id"] for s,_,_ in selected}
        # Publish an explicit whitelist; arbitrary or older case fields may carry
        # private commentary and must not leak merely because they were stored.
        public_case={
            "schema":obj["schema"],"version":obj.get("version","unknown"),
            "sources":[{
                "id":s["id"], "path":s["path"] if s["id"] in allowed_ids else "not_exported",
                "sha256":s["sha256"],"transfer_status":"full_approved_manifest_unverified_authority"
                     if s["id"] in allowed_ids else "no_source_transfer"
            } for s in obj["sources"]],
            "claims":[
                {key:c.get(key) for key in ("id","source","kind","actor","scope","status","quote","meaning")}
                    if c.get("source") in allowed_ids else
                {"id":c.get("id"),"source":c.get("source"),"kind":c.get("kind"),
                 "scope":c.get("scope"),"status":"redacted_unapproved_source"}
                for c in obj["claims"]
            ],
            "relations":[{key:r.get(key) for key in ("from","to","type","reason","epistemic_status")}
                for r in obj.get("relations",[]) if
                all(any(c.get("id")==cid and c.get("source") in allowed_ids
                        for c in obj["claims"]) for cid in (r.get("from"),r.get("to")))],
            "read_events":[{key:e.get(key) for key in ("id","source_id","start_char","end_char","proof","semantic_understanding")}
                for e in obj.get("read_events",[]) if e.get("source_id") in allowed_ids],
            "lens_observations":[],
            "transfer_warning":"Grant authority cannot be authenticated by JSON alone. Confirm user authorization in host."
        }
        save(stage/"CASE.json",public_case)
        if selected:
            for s,rel,content in selected:
                target=stage/"sources"/rel
                target.parent.mkdir(parents=True,exist_ok=True)
                target.write_text(content,encoding="utf8")
        report={"schema":"context-forge-delivery/2","kind":a.kind,"recipient":a.recipient or "not_identified",
                "source_count":len(ids),"cited_source_ids":sorted(refs),"uncited_source_ids":sorted(ids-refs),
                "included_source_ids":[s["id"] for s,_,_ in selected],"excluded_sources":omitted,
                "source_transfer":"explicit_source_grants" if selected else "references_only_not_access_grant",
                "recipient_access":"not_verified_by_package", "llm_understanding":"not_verified_by_package"}
        save(stage/"DELIVERY_CHECK.json",report)
        # Verify source snapshots again at the commit boundary; never declare a stale bundle current.
        if selected:
            for s,_,_ in selected:
                body,_=read_text(Path(obj["root_at_capture"]),s["path"])
                if sha(body.encode("utf8"))!=s["sha256"]:raise ValueError("Changed source before delivery commit")
        os.rename(stage,out)
    except Exception:
        shutil.rmtree(stage,ignore_errors=True)
        raise
    print(json.dumps({"bundle":str(out),"sources_included":len(selected),
                      "excluded":len(omitted),"status":"packaged_semantic_validation_still_needed"}))


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest="command",required=True)
    s=sub.add_parser("inventory");s.add_argument("--root",required=True);s.add_argument("--out",required=True);s.add_argument("--force",action="store_true");s.add_argument("sources",nargs="+");s.set_defaults(func=command_inventory)
    s=sub.add_parser("record");s.add_argument("--case",required=True);s.add_argument("--source",required=True);s.add_argument("--kind",required=True);s.add_argument("--actor",required=True);s.add_argument("--meaning",required=True);s.add_argument("--quote",default="");s.add_argument("--scope",default="unknown");s.add_argument("--supersedes",default=None);s.set_defaults(func=command_record)
    s=sub.add_parser("relate");s.add_argument("--case",required=True);s.add_argument("--left",required=True);s.add_argument("--right",required=True);s.add_argument("--type",required=True);s.add_argument("--reason",required=True);s.set_defaults(func=command_relation)
    s=sub.add_parser("verify");s.add_argument("--case",required=True);s.set_defaults(func=command_verify)
    s=sub.add_parser("freeze-probes");s.add_argument("--battery",required=True);s.add_argument("--out",required=True);s.set_defaults(func=command_freeze)
    s=sub.add_parser("score-probes");s.add_argument("--frozen",required=True);s.add_argument("--results",required=True);s.add_argument("--out");s.set_defaults(func=command_score)
    s=sub.add_parser("import-jlens");s.add_argument("--case",required=True);s.add_argument("--report",required=True);s.set_defaults(func=command_import_lens)
    s=sub.add_parser("record-read");s.add_argument("--case",required=True);s.add_argument("--source",required=True);s.add_argument("--quote",required=True);s.add_argument("--actor",choices=["assistant","user","tool"],default="assistant");s.set_defaults(func=command_record_read)
    s=sub.add_parser("compose");s.add_argument("--case",required=True);s.add_argument("--out",required=True);s.add_argument("--kind",choices=["anti-masterprompt","handoff"],default="anti-masterprompt");s.set_defaults(func=command_compose)
    s=sub.add_parser("package");s.add_argument("--case",required=True);s.add_argument("--draft",required=True);s.add_argument("--out",required=True);s.add_argument("--include-sources",action="store_true");s.add_argument("--grants");s.add_argument("--recipient");s.add_argument("--require-all",action="store_true");s.add_argument("--kind",choices=["anti-masterprompt","handoff"],default="anti-masterprompt");s.set_defaults(func=command_package)
    args=parser.parse_args(argv)
    try: return args.func(args) or 0
    except (ValueError,OSError,UnicodeError,json.JSONDecodeError) as exc:
        print(json.dumps({"status":"blocked","reason":str(exc)},ensure_ascii=False),file=sys.stderr);return 2

if __name__=="__main__":sys.exit(main())
