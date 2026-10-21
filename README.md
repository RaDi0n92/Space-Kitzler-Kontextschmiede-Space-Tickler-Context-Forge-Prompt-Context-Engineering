# Space-Kitzler-Kontextschmiede

## English

This repository documents and preserves the existing private ChatGPT plugin **Space-Kitzler-Kontextschmiede**. It is not a new plugin. The downloadable package below was retrieved from the live private plugin release on **21 October 2026**.

### Download the plugin

[Download the complete plugin package, version 0.10.0](downloads/Space-Kitzler-Kontextschmiede-0.10.0.tar.gz)

The archive is the unmodified current-release archive returned by Plugin Creator. Its SHA-256 is **3058ede2aa8037a58c1a2767004ef89c16e692536b77c71ad7b8366ede44dd23**. It contains 173 files, including the manifests, 18 active skills, support scripts, references, historical material, and the package's existing tests and documentation. The exact ZIP with those same 173 package files is also available: [download the original ChatGPT plugin ZIP](downloads/Space-Kitzler-Kontextschmiede-ChatGPT-Plugin-0.10.0.zip). For redistribution with the MIT notice inside the ZIP, use the [ChatGPT plugin ZIP with MIT License](downloads/Space-Kitzler-Kontextschmiede-ChatGPT-Plugin-MIT-0.10.0.zip); it adds only a top-level `LICENSE` file. ChatGPT import of that extra-file variant was not tested. For other skills-compatible agents, [download all 18 portable Agent Skills](downloads/Space-Kitzler-Kontextschmiede-Agent-Skills-0.10.0.zip); that bundle also includes the MIT notice.

### Verified identity

| Field | Verified value |
|---|---|
| Display name | Space-Kitzler-Kontextschmiede |
| Main skill name | space-kitzler-kontextschmiede |
| Main invocation written in the skill | @space-kitzler-kontextschmiede |
| Technical plugin name | context-forge-ultra |
| Plugin ID | plugins_6ad3075c7ab08191871a0b9f73d19a57 |
| Current release | pluginrel_6ad3b7d2bd2c819188e30f5409a556dd |
| Version | 0.10.0 |
| Scope and discoverability | Private, USER |

The visible German name and main skill invocation are distinct from the unchanged technical backend name. This repository records that distinction accurately.

### What the plugin is for

The plugin reads accessible conversations, project files, decisions, and research, then produces one of three practical outcomes:

1. A ready-to-use work order or master prompt.
2. A self-contained context handoff that lets a later agent check the original sources and form its own view.
3. Work actually carried out when the user explicitly authorizes the change and the available tools permit it.

Its core discipline is source fidelity: a search result, a file listing, a summary, an original source read, and a verified action are different evidence states. The plugin encourages new connections and competing interpretations while keeping facts, user decisions, uncertainty, permissions, and completed work distinct. It does not claim access to hidden ChatGPT sessions or control over internal model processes.

### Contents

- **downloads/** — exact current plugin archive for download.
- **plugin/** — the same 0.10.0 package unpacked for browsing and review.
- **agent-skills/** — all 18 skills in a portable Agent Skills directory layout, with shared references.
- **skills/README.md** — direct links to every full skill for reading and copying.
- **docs/01-identity-and-scope.md** — product identity and purpose.
- **docs/02-architecture.md** — architecture, runtime helpers, and package boundaries.
- **docs/03-skills-catalog.md** — the main skill and all 17 specialist skills.
- **docs/04-origin-and-history.md** — development history and user corrections.
- **docs/05-collaboration-method.md** — the working agreements learned in this collaboration.
- **docs/06-research-foundations.md** — how research was translated into task behavior.
- **docs/07-verification-and-limits.md** — live evidence, what it proves, and what remains untested.
- **docs/08-source-map.md** — source provenance and reading guide.
- **docs/09-agent-portability.md** — individual skill access, complete downloads, and portability limits.
- **LICENSE** — the repository's MIT License.

### Language and fidelity

The repository's newly written documentation is bilingual in every file: English comes first and German follows. The original plugin package is preserved in its original form so that it remains a faithful, usable download. Existing plugin files are not rewritten to translate them.

This repository is licensed under the MIT License; see **LICENSE**. The original live plugin package is preserved unchanged and did not contain a license file when retrieved. Its manifests retain the author metadata from the private release. The GitHub repository is public, but the ChatGPT plugin itself remains a private USER plugin.

### Evidence boundary

Live plugin metadata, both manifests, the README, the full paginated file inventory, and the current archive were inspected directly on 21 October 2026. The prior project handoff and live-abnahme note were also read. The original ChatGPT conversation in the project **Plugins herstellen** and the VPS plan files were not available in this session; therefore, the history documentation is an evidence-labeled reconstruction, not a claim that those originals were reread. Host UI invocation of the plugin was not tested during this repository work.

See **docs/07-verification-and-limits.md** for the evidence register and open verification items.

---

## Deutsch

Dieses Repository dokumentiert und bewahrt das bestehende private ChatGPT-Plugin **Space-Kitzler-Kontextschmiede**. Es ist kein neues Plugin. Das herunterladbare Paket stammt aus dem Live-Release des bestehenden privaten Plugins und wurde am **21. Oktober 2026** abgerufen.

### Plugin herunterladen

[Das vollständige Plugin-Paket, Version 0.10.0, herunterladen](downloads/Space-Kitzler-Kontextschmiede-0.10.0.tar.gz)

Das Archiv ist unverändert das vom Plugin Creator gelieferte Archiv des aktuellen Releases. Der SHA-256-Wert lautet **3058ede2aa8037a58c1a2767004ef89c16e692536b77c71ad7b8366ede44dd23**. Es enthält 173 Dateien: Manifeste, 18 aktive Skills, Hilfsskripte, Referenzen, historisches Material sowie die bereits vorhandenen Tests und Dokumente des Pluginpakets. Das exakte ZIP mit denselben 173 Paketdateien gibt es ebenfalls: [Originales ChatGPT-Plugin-ZIP herunterladen](downloads/Space-Kitzler-Kontextschmiede-ChatGPT-Plugin-0.10.0.zip). Für die Weitergabe mit MIT-Lizenz im ZIP gibt es zusätzlich das [ChatGPT-Plugin-ZIP mit MIT-Lizenz](downloads/Space-Kitzler-Kontextschmiede-ChatGPT-Plugin-MIT-0.10.0.zip); es ergänzt nur eine `LICENSE`-Datei im Stammverzeichnis. Der Import dieser Variante in ChatGPT wurde nicht getestet. Für andere Agenten mit Skills-Unterstützung: [alle 18 portablen Agent Skills herunterladen](downloads/Space-Kitzler-Kontextschmiede-Agent-Skills-0.10.0.zip); dieses Paket enthält ebenfalls die MIT-Lizenz.

### Verifizierte Identität

| Feld | Verifizierter Wert |
|---|---|
| Anzeigename | Space-Kitzler-Kontextschmiede |
| Name des Hauptskills | space-kitzler-kontextschmiede |
| Im Skill dokumentierter Hauptaufruf | @space-kitzler-kontextschmiede |
| Technischer Pluginname | context-forge-ultra |
| Plugin-ID | plugins_6ad3075c7ab08191871a0b9f73d19a57 |
| Aktueller Release | pluginrel_6ad3b7d2bd2c819188e30f5409a556dd |
| Version | 0.10.0 |
| Scope und Sichtbarkeit | USER, privat |

Der sichtbare deutsche Name und der Hauptaufruf unterscheiden sich vom unveränderten technischen Backendnamen. Das Repository hält diese Unterscheidung korrekt fest.

### Wofür das Plugin da ist

Das Plugin erschließt zugängliche Gespräche, Projektdateien, Entscheidungen und Forschung und stellt daraus eines von drei praktischen Ergebnissen her:

1. Einen sofort verwendbaren Arbeitsauftrag oder Masterprompt.
2. Eine eigenständig verständliche Kontextübergabe, mit der ein späterer Agent die Originalquellen selbst prüfen und sich eine eigene Sicht bilden kann.
3. Tatsächlich ausgeführte Arbeit, wenn der Nutzer die Änderung ausdrücklich beauftragt und die verfügbaren Werkzeuge sie erlauben.

Im Kern steht Quellentreue: Suchtreffer, Dateiliste, Zusammenfassung, Lektüre der Originalquelle und verifizierte Handlung sind unterschiedliche Belegzustände. Das Plugin fördert neue Verbindungen und konkurrierende Deutungen, hält aber Fakten, Nutzerentscheidungen, Unsicherheit, Berechtigungen und erledigte Arbeit auseinander. Es behauptet weder Zugriff auf verborgene ChatGPT-Sitzungen noch Kontrolle über interne Modellprozesse.

### Inhalt

- **downloads/** — exaktes aktuelles Pluginarchiv zum Herunterladen.
- **plugin/** — dasselbe 0.10.0-Paket entpackt zum Lesen und Prüfen.
- **agent-skills/** — alle 18 Skills als portable Agent-Skills-Ordner mit gemeinsamen Referenzen.
- **skills/README.md** — direkte Links zu jedem vollständigen Skill zum Lesen und Kopieren.
- **docs/01-identity-and-scope.md** — Produktidentität und Zweck.
- **docs/02-architecture.md** — Architektur, Laufzeithelfer und Paketgrenzen.
- **docs/03-skills-catalog.md** — Hauptskill und alle 17 Fachskills.
- **docs/04-origin-and-history.md** — Entwicklungsgeschichte und Nutzerkorrekturen.
- **docs/05-collaboration-method.md** — gelernte Arbeitsvereinbarungen unserer Zusammenarbeit.
- **docs/06-research-foundations.md** — Übersetzung von Forschung in konkretes Aufgabenverhalten.
- **docs/07-verification-and-limits.md** — Live-Belege, Aussagekraft und noch offene Prüfungen.
- **docs/08-source-map.md** — Quellenherkunft und Lesehinweise.
- **docs/09-agent-portability.md** — einzelne Skills, Gesamtdownloads und Grenzen der Übertragbarkeit.
- **LICENSE** — die MIT-Lizenz des Repositorys.

### Sprache und Originaltreue

Jede neu geschriebene Dokumentationsdatei in diesem Repository ist zweisprachig: zuerst Englisch, darunter Deutsch. Das Original-Pluginpaket bleibt unverändert, damit der Download dem tatsächlichen Plugin entspricht und nutzbar bleibt. Bestehende Plugin-Dateien werden nicht nachträglich übersetzt.

Dieses Repository steht unter der MIT-Lizenz; siehe **LICENSE**. Das ursprüngliche Live-Pluginpaket bleibt unverändert und enthielt beim Abruf keine Lizenzdatei. Seine Manifeste bewahren die Autorenmetadaten des privaten Releases. Das GitHub-Repository ist öffentlich, das ChatGPT-Plugin selbst bleibt jedoch ein privates USER-Plugin.

### Beleggrenze

Live-Metadaten, beide Manifeste, README, vollständige paginierte Dateiliste und aktuelles Archiv wurden am 21. Oktober 2026 direkt geprüft. Auch die vorhandene Projektübergabe und die Live-Abnahme-Notiz wurden gelesen. Die Originalunterhaltung im ChatGPT-Projekt **Plugins herstellen** und die VPS-Planungsdateien waren in dieser Sitzung nicht verfügbar. Die historische Darstellung ist deshalb eine gekennzeichnete Rekonstruktion und keine Behauptung, diese Originale erneut gelesen zu haben. Der Pluginaufruf in der ChatGPT-Oberfläche wurde bei dieser Repository-Arbeit nicht getestet.

Das Belegverzeichnis und die offenen Prüfungen stehen in **docs/07-verification-and-limits.md**.

