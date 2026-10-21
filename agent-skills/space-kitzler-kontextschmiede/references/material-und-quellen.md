# Eine lesbare Projektwelt aufbauen: Materialfluss und wirkliche Lektüre

## Was die Arbeitswelt ist

Gespräch, Dokument, Repository, Fehlerprotokoll, Code, Bild und Forschungsnotiz können im selben Projekt die Bedeutung eines Satzes verändern. Eine Datei kann selbst Quelle oder nur Zusammenfassung sein. Deshalb nicht mit dem gewünschten Ergebnis beginnen und nach Belegen suchen, sondern zunächst den **tatsächlich zugänglichen Stoff** betreten. Offene Suche und wiederholte Lektüre sind nötig; ein Verzeichnisbaum enthält keinen semantischen Befund.

**Ein Quellenereignis ist nicht das Lesen des Agenten.** `case_engine.py inventory` liest und hasht Dateibytes, um Existenz, Version und Pfad festzuhalten. Das Werkzeug besitzt keine künstliche semantische Einsicht und meldet `mechanical_read_not_semantic_read`. Der Agent liest die relevanten Originaltexte wirklich über seine tatsächlichen Host-Lesefunktionen; danach darf er einzelne geprüfte Behauptungen über `record` mit konkretem Originalzitat ablegen. Ein exaktes Zitat ist immer noch kein Beweis, dass die Behauptung **korrekt interpretiert** wurde.

## Gemeinsame semantische Karte

Quelle → wortgenauer Anker → **Aussage mit Urheber und Typ** → Beziehungen zwischen Aussagen → aktuelle und historische Geltung → offene Fragen und Hypothesen. Die gemeinsame Karte darf sich mit neuem Lesen ändern, aber nie ohne Herkunftsstatus alte Behauptungen überschreiben. Entscheidend sind gerade die Punkte, an denen der Nutzer eine Assistentendeutung zurückweist. Eine explizite Korrektur hat ein *Objekt und einen Bereich*; bloße spätere Erwähnung erzeugt keine gültige Ersetzung.

Wie diese Karte im konkreten Host lebt, hängt von tatsächlichen Fähigkeiten ab. Mit Python und lokalen Textdateien gibt es eine mechanische Ausgangsform:

```bash
python scripts/case_engine.py inventory --root /autorisiertes/projekt --out /arbeitsmappe/case.json gespruech.md entwurf.md
python scripts/case_engine.py record --case /arbeitsmappe/case.json --source S001 --kind user_intent --actor user --quote 'Ein Originalsatz aus dem wirklich gelesenen Text' --meaning 'Das tatsächlich ausgesprochene Ziel'
python scripts/case_engine.py record --case /arbeitsmappe/case.json --source S002 --kind correction --actor user --quote 'Eine ausdrückliche neue Korrektur' --meaning 'Welcher alte Punkt dadurch ersetzt wird' --supersedes C001
python scripts/case_engine.py relate --case /arbeitsmappe/case.json --left C001 --right C002 --type contradicts --reason 'Aus dem gelesenen Material erkennbarer Konflikt'
python scripts/case_engine.py verify --case /arbeitsmappe/case.json
```

`--supersedes` und Beziehungen prüfen IDs und Quellversionen, **nicht die semantische Wahrheit einer Ersetzung**. Die Quelle gilt nur in der Lesepassung als unverändert, solange der Hash übereinstimmt. Bei neuem Inhalt ist ein neuer Snapshot erforderlich. Geparkte ältere Varianten bleiben für Historie und neue Deutungen erhalten.

## Zwei Lesewege

**Weg des Compilers:** Welche Dateien im aktuell zugänglichen Zustand tatsächlich (teilweise/vollständig) gelesen wurden, welche wichtigen Passagen, welche Korrekturen, warum eine Aussage heute zählt. Textsuche zählt als Treffer; Drittbericht zählt als sekundär; maschineller Hash als Dateibeleg.

**Weg des Nachfolgers:** Welche Originale *er selbst* noch einmal lesen sollte, was diese Quelle neu erschließen könnte, welchen Abschnitt und welche alternative Frage er dabei beachten könnte und ob er sie in seiner Umgebung tatsächlich öffnen kann. Ein geschickter Handoff darf Originalauszüge zur eigenständigen Interpretation bereitstellen, sofern autorisiert; ein bloßer VPS-Pfad in einem neuen Chat ist kein Zugang.

## Lesen ohne Scheuklappen

Eine Quellenabfrage nach fünf Schlagwörtern darf einen unbekannten, überraschenden Fall nicht systematisch ausschließen. Beginne gegebenenfalls mit einer breiteren historischen Sichtung, verwende dann aufgabenbezogene Originallektüre und revidiere die Auswahl, sobald die Hypothese kippt. Nicht automatisch jede Datei komplett in das aktive Kontextfenster kippen, aber **nie unsichtbare Auslassungen als Vollständigkeit ausgeben**. Lange, eigentümliche Rohstellen und Fehlversuche können für den späteren Nachfolger wichtiger sein als eine glatte Zusammenfassung.

## Grenzen

`inventory` akzeptiert ausschließlich explizit benannte lokale UTF-8-Dateien innerhalb eines angegebenen Wurzelordners, verweigert `..`, absolute Quellpfade, Symlinks und Dubletten. Es durchsucht nicht heimlich den VPS oder das ChatGPT-Konto. Kein Tool erhält durch diese Anweisungen mehr Zugriffsrecht. Ein direkter normaler Chat ist ebenfalls Material: wenn er bereits sichtbar ist, braucht er keine künstliche Zwischendatei.

## CLI-Vertrag seit v0.9.0 (operative Kurzreferenz)

Der auf dem Host mit eigenem Python und echten freigegebenen Dateien ausgeführte Helfer `scripts/case_engine.py` kann Material in einem lokalen `case.json` erfassen. Die Case-Datei selbst ist der gemeinsame Arbeitskörper, keine Dokumentation für die Veröffentlichung.

- `inventory --root ORDN --out case.json datei1.md datei2.md`: mechanisch inventarisiert, **nicht** semantisch gelesen.
- `record --case case.json --source S001 --kind user_intent --actor user --scope produkt --quote "..." --meaning "..."`: Anker und Interpretation getrennt.
- `record-read --case case.json --source S001 --quote "..." --actor assistant`: Quelle/Teilbereich protokollieren, **nicht** über die echte Host-Leseabdeckung lügen.
- `compose --case case.json --out entwurf.md --kind anti-masterprompt|handoff`: strukturierter Entwurf; anschließende eigenständige Quellen- und Bedeutungsprüfung ist Voraussetzung für ein fertiges Ergebnis.
- `package --case case.json --draft fertiger-text.md --out ausgabe --kind anti-masterprompt|handoff`: verpackt ohne Originalvollkopien und mit redigiertem Fallregister.
- `package ... --include-sources --recipient folgeagent-a --grants grants.json`: kopiert nur vollständig quellgenau und empfängerbezogen freigegebene Texte; `--require-all` lehnt unvollständige Transfers ab.

Das Freigabemanifest ist **kein von der KI selbst zu erfindendes Formular**. Eine externe tatsächliche Freigabe muss bereits vorliegen und gegen Quelle/Empfänger geprüft werden. Beispiel für die maschinenlesbare, vom Verantwortlichen erhaltene Darstellung:

```json
{
  "schema": "context-forge-transfer-grants/1",
  "grants": [
    {
      "source_id": "S001",
      "path": "datei1.md",
      "source_sha256": "<tatsaechlicher SHA256 aus case.json>",
      "recipient": "folgeagent-a",
      "mode": "full",
      "authority": "explizit bestatigte Nutzerfreigabe",
      "approved": true
    }
  ]
}
```

Ein solcher JSON-Eintrag allein beweist keine legitime Zustimmung. Keine automatische Erzeugung von `approved: true`. Das Quellpaket prüft Dateiversionen vor und unmittelbar vor dem finalen Veröffentlichen. Vertrauliche Inhalte oder faktische Zugangsrechte kann es nicht umfassend allein aus Strings beurteilen. Ein vollständiger semantischer Leak-Check bleibt echte Arbeit des Agenten.
