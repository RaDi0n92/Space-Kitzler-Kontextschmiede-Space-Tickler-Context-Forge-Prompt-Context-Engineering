#!/usr/bin/env python3
"""Conservative STRUCTURAL validator for Context Forge Ultra Handoff ledger.

Exit 0: structurally pass (semantic/source and agent behavior unverified)
Exit 1: blocking structural inconsistency
Exit 2: input unavailable, malformed or unscorable

This script never searches files, reads source documents, verifies read evidence,
or measures creative performance / neuron activations. It reads only the supplied
ledger JSON and checks declarative structural relationships.
"""
import json
import sys
from pathlib import Path

VALID_READ = {"gelesen_voll", "gelesen_teilweise", "zitiert_aus_zweitquelle", "nur_erwähnt", "nicht_zugänglich", "ungeprüfte_behauptung"}
VALID_DECISION = {"aktuell", "ersetzt", "offen", "verworfen", "vertagt", "widerspruechlich"}
VALID_ACCESS = {"ja", "nein", "unbekannt"}
VALID_CLAIM = {"belegt", "beobachtet", "sekundaer", "hypothese", "offen", "widerspruechlich"}


def nonempty(x):
    return isinstance(x, str) and bool(x.strip())


def valid_enum(value, allowed):
    return isinstance(value, str) and value in allowed


def ids(value):
    return isinstance(value, list) and all(nonempty(x) for x in value)


def label(x):
    return " ".join(x.casefold().split()) if isinstance(x, str) else ""


def audit(obj):
    """Return (issues, warnings); must never raise due to malformed JSON values."""
    issues, warnings = [], []
    if not isinstance(obj, dict):
        return ["JSON-Wurzel muss Objekt sein"], warnings
    for k in ("sources", "decisions", "read_again"):
        if k not in obj or not isinstance(obj[k], list):
            issues.append(f"{k}: erforderliche Liste fehlt/ungültig")
    if issues:
        return issues, warnings
    sources, decisions, reread = (obj[k] for k in ("sources", "decisions", "read_again"))
    if not sources:
        issues.append("Quellenregister ist leer: mindestens eine tatsächliche Kontextquelle nötig")
    if not decisions:
        warnings.append("Keine Entscheidungen: Originalmaterial auf Nutzerentscheidungen prüfen")

    by_id = {}
    for i, source in enumerate(sources):
        if not isinstance(source, dict):
            issues.append(f"sources[{i}]: kein Objekt")
            continue
        sid, locator = source.get("id"), source.get("locator")
        if not nonempty(sid) or not nonempty(locator):
            issues.append(f"sources[{i}]: ID/Locator ungültig")
            continue
        if sid in by_id:
            issues.append(f"Quelle {sid}: doppelte ID")
        by_id[sid] = source
        status = source.get("read_status")
        if not valid_enum(status, VALID_READ):
            issues.append(f"Quelle {sid}: Lesestatus fehlt/ungültig")
        seen = source.get("actually_read")
        if not isinstance(seen, bool):
            issues.append(f"Quelle {sid}: actually_read muss Boolean sein")
        if valid_enum(status, {"gelesen_voll", "gelesen_teilweise"}):
            if seen is not True:
                issues.append(f"Quelle {sid}: als gelesen markiert, aber actually_read nicht true")
            if not nonempty(source.get("read_evidence")):
                issues.append(f"Quelle {sid}: Leseangabe ohne Fundstelle/Zugriffsbeleg")
            if status == "gelesen_teilweise" and not nonempty(source.get("read_extent")):
                issues.append(f"Quelle {sid}: Teillektüre ohne Leseumfang")
            warnings.append(f"Quelle {sid}: Lektürebeleg ist nur Behauptung im Ledger und muss separat überprüft werden")
        elif seen is True:
            issues.append(f"Quelle {sid}: ungelesen/sekundär und gleichzeitig tatsächlich gelesen")
        if "accessible_to_next" in source and not valid_enum(source["accessible_to_next"], VALID_ACCESS):
            issues.append(f"Quelle {sid}: ungültiger Ziel-Zugriffsstatus")

    by_did, successor = {}, {}
    for i, decision in enumerate(decisions):
        if not isinstance(decision, dict):
            issues.append(f"decisions[{i}]: kein Objekt")
            continue
        did = decision.get("id")
        if not nonempty(did) or not nonempty(decision.get("statement")):
            issues.append(f"decisions[{i}]: ID/Aussage ungültig")
            continue
        if did in by_did:
            issues.append(f"Entscheidung {did}: doppelte ID")
        by_did[did] = decision
        status = decision.get("status")
        if not valid_enum(status, VALID_DECISION):
            issues.append(f"Entscheidung {did}: Status fehlt/ungültig")
        nxt = decision.get("superseded_by")
        if status == "ersetzt":
            if not nonempty(nxt):
                issues.append(f"Entscheidung {did}: ersetzt ohne gültigen Nachfolger")
            else:
                successor[did] = nxt
        elif nxt is not None:
            issues.append(f"Entscheidung {did}: Nachfolger vorhanden obwohl nicht ersetzt")
        refs = decision.get("source_ids")
        if not ids(refs) or not refs:
            issues.append(f"Entscheidung {did}: Quellennachweise fehlen/ungültig")
        else:
            for ref in refs:
                if ref not in by_id:
                    issues.append(f"Entscheidung {did}: Quelle {ref} nicht registriert")
            if status == "aktuell":
                read_types = [by_id[ref].get("read_status") for ref in refs if ref in by_id]
                if read_types and all(valid_enum(x, {"nur_erwähnt", "nicht_zugänglich", "ungeprüfte_behauptung"}) for x in read_types):
                    issues.append(f"Entscheidung {did}: aktuell ausschließlich aus ungelesenen/unzugänglichen Quellen")
                elif read_types and all(x == "zitiert_aus_zweitquelle" for x in read_types):
                    warnings.append(f"Entscheidung {did}: aktuelle Geltung nur durch Sekundärquellen gestützt")
        if valid_enum(status, {"verworfen", "vertagt"}) and not nonempty(decision.get("reason")):
            warnings.append(f"Entscheidung {did}: Warum für Verwurf/Vertagung fehlt")
    for did, nxt in successor.items():
        if nxt not in by_did:
            issues.append(f"Entscheidung {did}: Nachfolger {nxt} nicht registriert")
        elif nxt == did:
            issues.append(f"Entscheidung {did}: Selbstersetzung")
    completed = set()
    for start in successor:
        if start in completed:
            continue
        chain, cur = set(), start
        while cur in successor:
            if cur in chain:
                issues.append(f"Ersetzungszyklus bei Entscheidung {cur}")
                break
            chain.add(cur)
            cur = successor[cur]
        completed.update(chain)

    for i, entry in enumerate(reread):
        if not isinstance(entry, dict):
            issues.append(f"read_again[{i}]: kein Objekt")
            continue
        ref = entry.get("source_id")
        if not nonempty(ref) or ref not in by_id:
            issues.append(f"read_again[{i}]: unbekannte/ungültige Quell-ID")
            continue
        if not nonempty(entry.get("why")):
            issues.append(f"read_again[{i}]: keine Lektürebegründung")
        status = entry.get("accessible_to_next")
        if status is not None and not valid_enum(status, VALID_ACCESS):
            issues.append(f"read_again[{i}]: Zielzugänglichkeit ungültig")
        if status == "ja" and by_id[ref].get("accessible_to_next") == "nein":
            issues.append(f"read_again[{i}]: Zielzugang widerspricht Quelle {ref}")
    if sources and not reread:
        issues.append("Original-Nachleseliste fehlt")

    if "claims" in obj:
        claims = obj["claims"]
        if not isinstance(claims, list):
            issues.append("claims muss Liste sein")
        else:
            for i, cl in enumerate(claims):
                if not isinstance(cl, dict) or not nonempty(cl.get("statement")):
                    issues.append(f"claims[{i}]: kein valider Claim")
                    continue
                status = cl.get("status")
                if not valid_enum(status, VALID_CLAIM):
                    issues.append(f"claims[{i}]: ungültiger oder fehlender Claim-Status")
                refs = cl.get("source_ids")
                if refs is not None and not ids(refs):
                    issues.append(f"claims[{i}]: Quell-IDs müssen Strings sein")
                    refs = []
                refs = refs or []
                for ref in refs:
                    if ref not in by_id:
                        issues.append(f"claims[{i}]: Quelle {ref} nicht registriert")
                if status == "belegt":
                    if cl.get("supported") is not True or not refs:
                        issues.append(f"claims[{i}]: 'belegt' erfordert Belege und supported=true")
                    elif all(valid_enum(by_id.get(ref, {}).get("read_status"), {"nur_erwähnt", "nicht_zugänglich", "ungeprüfte_behauptung"}) for ref in refs):
                        issues.append(f"claims[{i}]: 'belegt' nur mit ungelesenen Quellen")
                    elif all(by_id.get(ref, {}).get("read_status") == "zitiert_aus_zweitquelle" for ref in refs):
                        warnings.append(f"claims[{i}]: 'belegt' nur über Sekundärquellen; Lesestatus richtig kennzeichnen")
                if valid_enum(status, {"hypothese", "offen"}) and cl.get("supported") is True:
                    warnings.append(f"claims[{i}]: Hypothese/offen als supported markiert; Claimtext prüfen")

    perspective_ids = set()
    if "perspectives" in obj:
        perspectives = obj["perspectives"]
        if not isinstance(perspectives, list):
            issues.append("perspectives muss Liste sein")
        else:
            seen_labels = set()
            for i, perspective in enumerate(perspectives):
                if not isinstance(perspective, dict) or not nonempty(perspective.get("label")):
                    issues.append(f"perspectives[{i}]: Label fehlt")
                    continue
                pid = perspective.get("id")
                if pid is not None:
                    if not nonempty(pid):
                        issues.append(f"perspectives[{i}]: ID ungültig")
                    elif pid in perspective_ids:
                        issues.append(f"perspectives[{i}]: Perspektiven-ID {pid} doppelt")
                    else:
                        perspective_ids.add(pid)
                lbl = label(perspective["label"])
                if lbl in seen_labels:
                    issues.append(f"perspectives[{i}]: Label/Sicht wiederholt")
                seen_labels.add(lbl)
                refs = perspective.get("source_ids", [])
                if not ids(refs) or any(ref not in by_id for ref in refs):
                    issues.append(f"perspectives[{i}]: Quellenanker ungültig")
                if not refs and perspective.get("hypothetical") is not True:
                    issues.append(f"perspectives[{i}]: weder Materialanker noch Hypothesenkennzeichnung")
            warnings.append("Perspektiven-Vielfalt, Neuheit und Denkoffenheit bleiben semantisch ungetestet")

    if "relations" in obj:
        relations = obj["relations"]
        if not isinstance(relations, list):
            issues.append("relations muss Liste sein")
        else:
            for i, edge in enumerate(relations):
                if not isinstance(edge, dict):
                    issues.append(f"relations[{i}]: kein Objekt")
                    continue
                for endpoint in ("from", "to"):
                    ref = edge.get(endpoint)
                    if not nonempty(ref) or ref not in perspective_ids:
                        issues.append(f"relations[{i}]: {endpoint}-Perspektiven-ID fehlt/ungültig")
                if not nonempty(edge.get("relation")):
                    issues.append(f"relations[{i}]: Beziehung nicht beschrieben")
    return issues, warnings


def main():
    if len(sys.argv) != 2:
        print('Usage: audit_handoff.py LEDGER.json', file=sys.stderr)
        return 2
    try:
        data = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    except (OSError, ValueError, UnicodeError) as ex:
        print(json.dumps({'verdict':'unscorable','passed':False,'error':str(ex)}, ensure_ascii=False))
        return 2
    issues, warnings = audit(data)
    print(json.dumps({
        'verdict':'fail' if issues else 'structurally_passed_not_semantically_verified',
        'passed':not issues,
        'issues':issues,
        'warnings':warnings,
        'counts':{k:len(data[k]) for k in ('sources','decisions','read_again','claims','perspectives') if isinstance(data,dict) and isinstance(data.get(k),list)},
        'important_limit':'Keine Verifikation echter Lektüre, semantischer Wahrheit oder neuronaler Verarbeitung'
    },ensure_ascii=False,indent=2))
    return 1 if issues else 0

if __name__=='__main__':
    sys.exit(main())
