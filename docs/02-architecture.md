# Architecture and package boundaries

## English

### Package layout

The current plugin archive has 173 files. Its main parts are:

- Two manifests: **plugin.json** and **.codex-plugin/plugin.json**.
- One central skill and 17 optional specialist skills under **skills/**.
- A central library of references and helper scripts under **skills/context-forge-ultra/**.
- An archived **library/v07/** with earlier skills, references, documentation, and tests retained as historical material.
- Root package documentation and a test suite.

The archive in **downloads/** is the complete live package. **plugin/** is the same archive unpacked. The archive checksum is recorded in the repository README and verification document.

### Active entry and specialist skills

The central skill is **space-kitzler-kontextschmiede**. It can route a request to the relevant specialist when useful. The 17 specialist skills have their own German names and distinct task descriptions. They are optional entry points, not 17 required routines.

The central skill owns broad source, purpose, and output guidance. The specialist skills add depth for specific needs such as research, source reading, decisions, handoffs, and comparisons. The historical v0.7 archive remains distinct from the 18 active skill files.

### Local helper scripts

The package README describes five helpers:

| Script | Documented role |
|---|---|
| case_engine.py | Inventory local source material, bind claims to source passages, identify contradictions, and assemble traceable handoff packages. |
| research_flow.py | Track research reading, source anchors, changes, and available action outcomes. Its checks establish mechanical consistency, not truth. |
| forge_pipeline.py | Carry a checked case into an authorized package; original sources are excluded by default. |
| followup_comparison.py | Evaluate frozen and fair follow-up comparisons; it does not claim impact without independent run data. |
| jlens_local.py | Read existing local J-Lens reports over loopback only when explicitly requested. |

These are optional package helpers. They do not create new ChatGPT host permissions, browse hidden conversations, control a model's internal state, or prove that a source was understood.

### Manifest prompts

Both manifests contain three default prompts: a context handoff, an open think-space request, and a handoff review. No prompt text or skill list was changed while preparing this repository. The three prompts are part of the live 0.10.0 package, not newly authored repository content.

### Preserved material

The v0.7 library contains earlier entries, references, scripts, tests, and design material. It is kept as a historical archive, not treated as the current active skill architecture. The current active catalog lives in **skills/<skill-name>/SKILL.md**.

### Integrity and licensing

This repository keeps the live archive intact and offers a readable unpacked copy. The repository is licensed under MIT; see the root **LICENSE** file. The downloaded live archive itself had no license file and remains unchanged. Its manifests retain the author metadata from the private plugin release, which is now visible in this public repository.

---

## Deutsch

### Paketaufbau

Das aktuelle Pluginarchiv enthält 173 Dateien. Die wichtigsten Bestandteile sind:

- Zwei Manifeste: **plugin.json** und **.codex-plugin/plugin.json**.
- Ein zentraler Skill und 17 optionale Fachskills unter **skills/**.
- Eine zentrale Bibliothek mit Referenzen und Hilfsskripten unter **skills/context-forge-ultra/**.
- Ein archiviertes **library/v07/** mit früheren Skills, Referenzen, Dokumentation und Tests als erhaltenem historischem Material.
- Paketdokumentation im Stammverzeichnis und eine Testsuite.

Das Archiv unter **downloads/** ist das vollständige Live-Paket. **plugin/** enthält dasselbe Archiv entpackt. Der Archivprüfwert steht in README und Prüfbericht.

### Aktiver Einstieg und Fachskills

Der zentrale Skill heißt **space-kitzler-kontextschmiede**. Wenn es sinnvoll ist, kann er eine Anfrage an den passenden Fachskill weiterleiten. Die 17 Fachskills haben eigene deutsche Namen und unterschiedliche Aufgabenbeschreibungen. Sie sind optionale Zugänge, keine 17 Pflichtstationen.

Der Hauptskill enthält die allgemeine Orientierung zu Quellen, Ziel und Ergebnissen. Die Fachskills vertiefen bestimmte Bedürfnisse wie Forschung, Quellenlektüre, Entscheidungen, Übergaben und Vergleiche. Das historische v0.7-Archiv bleibt von den 18 aktiven Skill-Dateien getrennt.

### Lokale Hilfsskripte

Das Paket-README beschreibt fünf Helfer:

| Skript | Dokumentierte Aufgabe |
|---|---|
| case_engine.py | Lokales Quellenmaterial inventarisieren, Aussagen an Fundstellen binden, Widersprüche erkennen und nachvollziehbare Übergabepakete erstellen. |
| research_flow.py | Forschungslektüre, Quellenanker, Änderungen und vorliegende Handlungsergebnisse verfolgen. Die Prüfungen belegen technische Konsistenz, nicht Wahrheit. |
| forge_pipeline.py | Einen geprüften Fall in ein berechtigtes Paket überführen; Originalquellen bleiben standardmäßig ausgeschlossen. |
| followup_comparison.py | Vorab eingefrorene und faire Anschlussvergleiche bewerten; ohne unabhängige Laufdaten wird keine Wirkung behauptet. |
| jlens_local.py | Nur auf ausdrücklichen Wunsch bestehende lokale J-Lens-Berichte über Loopback lesen. |

Diese Helfer sind optionale Paketwerkzeuge. Sie erteilen keine zusätzlichen ChatGPT-Berechtigungen, öffnen keine verborgenen Gespräche, kontrollieren keinen inneren Modellzustand und beweisen kein Quellenverständnis.

### Startvorschläge im Manifest

Beide Manifeste enthalten drei Standardprompts: eine Kontextübergabe, einen offenen Denkraum und eine Prüfung einer Übergabe. Beim Erstellen dieses Repositorys wurden weder Prompttexte noch Skillliste geändert. Die drei Prompts gehören zum Livepaket 0.10.0 und wurden nicht für das Repository neu geschrieben.

### Bewahrtes Material

Die v0.7-Bibliothek enthält frühere Einträge, Referenzen, Skripte, Tests und Designmaterial. Sie bleibt als historisches Archiv erhalten und gilt nicht als aktuelle aktive Skillarchitektur. Der aktive Katalog liegt unter **skills/<skill-name>/SKILL.md**.

### Integrität und Lizenz

Dieses Repository bewahrt das Livearchiv unverändert und stellt zusätzlich eine lesbare entpackte Kopie bereit. Das Repository steht unter MIT; siehe **LICENSE** im Stammverzeichnis. Das abgerufene Livearchiv selbst enthielt keine Lizenzdatei und bleibt unverändert. Seine Manifeste bewahren die Autorenmetadaten des privaten Plugin-Releases, die in diesem öffentlichen Repository nun sichtbar sind.

