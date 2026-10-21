#!/usr/bin/env python3
"""Offline check of excerpts against permitted local source files.

This verifies only matching text and bytes, *not* model reading, meaning,
chronology or creativity. No network and no mutation of source files.

Usage: python verify_quotes.py EVIDENCE.json --root AUTHORIZED_DIRECTORY
Exit codes: 0 every listed quote verified; 1 contradiction; 2 unscorable.
"""
import argparse
import hashlib
import json
from pathlib import Path

MAX_BYTES = 5_000_000
MAX_ITEMS = 250


def text(x):
    return isinstance(x, str) and bool(x.strip())


def check_record(record, root):
    ident = record.get('id')
    rel = record.get('path')
    quote = record.get('quote')
    start = record.get('start_line')
    end = record.get('end_line')
    if not text(ident) or not text(rel) or not text(quote):
        return ('unscorable', 'id, path und quote brauchen Text')
    if not isinstance(start, int) or isinstance(start, bool) or start < 1:
        return ('unscorable', 'start_line muss positive ganze Zahl sein')
    if not isinstance(end, int) or isinstance(end, bool) or end < start:
        return ('unscorable', 'end_line muss ganzzahlig >= start_line sein')
    raw = Path(rel)
    if raw.is_absolute() or not raw.parts or any(part in {'..', '.'} for part in raw.parts):
        return ('unscorable', 'Unsicherer relativer Pfad')
    target = root / raw
    try:
        # Refuse symlinked paths before resolve (also protects the user from
        # confusing one source identity with a referenced target).
        cur = root
        for part in raw.parts:
            cur = cur / part
            if cur.is_symlink():
                return ('unscorable', 'Symbolische Verknüpfung ist keine Quelle')
        resolved = target.resolve(strict=True)
        resolved.relative_to(root)
        if not resolved.is_file():
            return ('unscorable', 'Quelle ist keine reguläre Datei')
        if resolved.stat().st_size > MAX_BYTES:
            return ('unscorable', 'Quelle überschreitet Dateigrößenbegrenzung')
        data = resolved.read_bytes()
        actual_sha = hashlib.sha256(data).hexdigest()
        expected = record.get('sha256')
        if expected is not None and (not isinstance(expected, str) or len(expected) != 64 or any(c not in '0123456789abcdefABCDEF' for c in expected)):
            return ('unscorable', 'SHA256-Format ungültig')
        if expected and expected.lower() != actual_sha:
            return ('mismatch', 'Datei-Hash stimmt nicht mit dokumentierter Version überein')
        try:
            lines = data.decode('utf-8').splitlines()
        except UnicodeDecodeError:
            return ('unscorable', 'Quelle ist nicht UTF-8')
        if end > len(lines):
            return ('mismatch', 'Angegebener Zeilenbereich existiert nicht')
        selection = '\n'.join(lines[start-1:end])
        if quote not in selection:
            return ('mismatch', 'Originalzitat in angegebenem Bereich nicht gefunden')
        return ('verified_excerpt', f'Zitatexistenz und Dateiversion geprüft; sha256={actual_sha}')
    except (OSError, ValueError) as ex:
        return ('unscorable', f'Quelle nicht lesbar/zulässig: {type(ex).__name__}')


def audit(obj, root):
    if not isinstance(obj, dict) or not isinstance(obj.get('evidence'), list):
        return [{'id': None, 'status': 'unscorable', 'detail': 'evidence-Liste fehlt'}]
    ev = obj['evidence']
    if not ev or len(ev) > MAX_ITEMS:
        return [{'id': None, 'status': 'unscorable', 'detail': 'Belege fehlen oder Anzahl unzulässig'}]
    seen = set()
    output = []
    for item in ev:
        if not isinstance(item, dict):
            output.append({'id': None, 'status': 'unscorable', 'detail':'Beleg ist kein Objekt'})
            continue
        eid = item.get('id')
        if not text(eid) or eid in seen:
            output.append({'id': eid if text(eid) else None,'status':'unscorable','detail':'Ungültige/doppelte ID'})
            continue
        seen.add(eid)
        status, detail = check_record(item, root)
        output.append({'id':eid,'status':status,'detail':detail})
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('evidence')
    parser.add_argument('--root', required=True)
    args = parser.parse_args()
    try:
        root = Path(args.root).resolve(strict=True)
        if not root.is_dir():
            raise ValueError('root ist kein Verzeichnis')
        obj = json.loads(Path(args.evidence).read_text(encoding='utf-8'))
        records = audit(obj,root)
    except (OSError, ValueError, UnicodeError) as ex:
        records = [{'id':None,'status':'unscorable','detail':f'{type(ex).__name__}: {str(ex)}'}]
    states = [x['status'] for x in records]
    verdict = 'contradiction' if 'mismatch' in states else 'unscorable' if 'unscorable' in states else 'excerpt_verified_not_reading'
    print(json.dumps({'verdict':verdict,'results':records,'limit':'Zitat/Datei prüfbar; weder Leseakt noch Interpretation noch Modellleistung nachgewiesen'},ensure_ascii=False,indent=2))
    return 1 if verdict=='contradiction' else 2 if verdict=='unscorable' else 0

if __name__ == '__main__':
    raise SystemExit(main())
