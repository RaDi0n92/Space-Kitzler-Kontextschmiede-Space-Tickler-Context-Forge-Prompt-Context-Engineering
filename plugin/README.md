# Space-Kitzler-Kontextschmiede 0.10.0 — Hauptzugang mit 17 Fachskills

**Hauptzugang:** `skills/context-forge-ultra/SKILL.md`.
**Skill-Aufruf in ChatGPT:** `@space-kitzler-kontextschmiede`.

Die Space-Kitzler-Kontextschmiede erschließt zugängliche Gespräche, Dateien, Projekte und Forschung, prüft Originale und entwickelt daraus einen unmittelbar verwendbaren Arbeitsauftrag, eine gründliche Kontextübergabe oder ausdrücklich beauftragte Arbeit. Tiefe und Forschungsmechaniken richten sich nach Material und Auftrag.

## Aktive Laufzeit

Alle aktiven Helfer liegen unter `skills/context-forge-ultra/scripts/`:

- `case_engine.py` inventarisiert lokale Quellen, bindet Aussagen an geprüfte Originalstellen, prüft Widersprüche und erstellt nachvollziehbare Übergabepakete.
- `research_flow.py` prüft Forschungslektüren, Quellenanker, Änderungen und vorliegende Handlungsergebnisse. Ein erfolgreicher Lauf belegt nur mechanische Bereitschaft, keine inhaltliche Wahrheit.
- `forge_pipeline.py` führt den geprüften Forschungsfall in ein berechtigtes Paket über. Originalquellen werden standardmäßig nicht übertragen.
- `followup_comparison.py` bewertet eingefrorene, faire Anschlussvergleiche; das Werkzeug behauptet keine Wirkung ohne unabhängige Versuchsdaten.
- `jlens_local.py` liest nur bei ausdrücklichem Auftrag bereits vorhandene lokale J-Lens-Berichte über Loopback.

## 17 aktive Fachskills

Die 17 optionalen Fachskills sind als eigene `SKILL.md`-Einträge registriert. Der zentrale Skill bleibt `@space-kitzler-kontextschmiede`.

| Aufruf | Schwerpunkt |
|---|---|
| `@autorisierte-umsetzung` | Autorisierte Arbeit umsetzen |
| `@wiedereinstieg` | Nach dem Sitzungswechsel einsteigen |
| `@uebergaben-pruefen` | Übergaben und Belege prüfen |
| `@denkbruecken` | Denkbrücken zwischen Quellen bauen |
| `@wirkungsvergleich` | Wirkung und Ergebnisse vergleichen |
| `@entscheidungsstatus` | Entscheidungen und offene Punkte ordnen |
| `@kontextuebergabe` | Kontext für die Weiterarbeit übergeben |
| `@projektgeschichte` | Projektverlauf und Absicht rekonstruieren |
| `@arbeitsauftrag` | Arbeitsaufträge aus Kontext formen |
| `@perspektiven` | Andere Lesarten entwickeln |
| `@pluginbau` | Pluginabläufe in Skills übersetzen |
| `@denkwerkstatt` | Denkwege am Material schärfen |
| `@repo-erkenntnisse` | Erkenntnisse aus Repositories übertragen |
| `@forschung` | Forschung prüfen und anwenden |
| `@gegenfragen` | Gegenfragen und Gegenpositionen entwickeln |
| `@quellenlesen` | Originalquellen lesen und belegen |
| `@arbeitskreislauf` | Arbeit prüfen und verbessern |

## Historisches Material

`skills/context-forge-ultra/library/v07/` bewahrt die ursprünglichen 17 Einträge, Referenzen, Dokumentation und Tests als historische Quelle. Die aktiven Skill-Einträge liegen zusätzlich direkt unter `skills/<name>/SKILL.md`; ihre Verweise führen zu den erhaltenen Referenzdateien. Die früheren 0.7-Testdateien liegen unter `library/v07/tests/` und werden nicht als Tests der aktuellen Architektur ausgeführt.

## Prüfung

Der aktuelle Paket-Testsatz läuft mit:

```sh
python -m unittest discover -s tests -v
```

Der Vorschau-Test mit Playwright wird übersprungen, wenn Playwright in der Umgebung nicht verfügbar ist. Frische Release-Prüfungen stehen in `docs/FINAL_TEST_RUN.log`. Lokale Tests belegen weder die Aktivierung im ChatGPT-Host noch eine unabhängige Wirkung bei Folgeagenten.
