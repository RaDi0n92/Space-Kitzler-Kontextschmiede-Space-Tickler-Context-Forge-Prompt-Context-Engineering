# Verification record and current limits

## English

### Directly verified on 21 October 2026

| Item | Evidence | Result |
|---|---|---|
| Live plugin identity | Plugin Creator metadata | Private USER plugin, ID plugins_6ad3075c7ab08191871a0b9f73d19a57, backend context-forge-ultra, version 0.10.0. |
| Current release | Plugin Creator metadata and archive result | pluginrel_6ad3b7d2bd2c819188e30f5409a556dd, version 0.10.0. |
| Display identity | Both live manifests | Space-Kitzler-Kontextschmiede. |
| Main invocation | Main skill metadata and contents | space-kitzler-kontextschmiede; the skill describes @space-kitzler-kontextschmiede. |
| Active skill files | Full paginated live file inventory and archive | 18 active SKILL.md files: one main skill and 17 specialists. No skill file was missing from the inventory. |
| Package file count | Downloaded current archive, extracted and counted | 173 files; compressed archive size 270,686 bytes. |
| Archive integrity | SHA-256 of downloaded archive | 3058ede2aa8037a58c1a2767004ef89c16e692536b77c71ad7b8366ede44dd23. |
| Copyable skill index | Repository files | Direct links are provided for all 18 full skill files in both the portable export and original plugin tree. |
| Agent Skills export | Local structural check against the published format | 18 skill folders; folder names match `name`; required metadata limits pass; all checked relative references resolve. |
| ZIP downloads | Extracted ZIP contents and integrity checks | Original plugin ZIP: 173 files, byte-for-byte matches the unpacked package. MIT redistribution ZIP: those same 173 files plus root LICENSE, integrity PASS. Agent Skills ZIP: 18 skills, shared references, README, and LICENSE; integrity PASS. |
| Default prompts | Both live manifests | Three prompts: context handoff, think-space, and handoff review. |
| Supplied repository | GitHub repository metadata and main-branch contents | Public repository `RaDi0n92/Space-Kitzler-Kontextschmiede-Space-Tickler-Context-Forge-Prompt-Context-Engineering`, writable through the connected GitHub account. |

The exact live release archive is preserved under **downloads/**. The unpacked package under **plugin/** comes from that same downloaded archive.

### Evidence inherited from earlier project records

A surviving handoff reports that a local test run on 20 October produced **93 passing tests and one skipped Playwright preview test** because Playwright was unavailable. That run was performed against a local 0.10.0 package copy and was not repeated against this archive during the present repository task. It is historical evidence, not a fresh test result for this repository.

The same handoff says that all 18 live skills had been returned by Plugin Creator and the skill catalog in a previous session. The inventory was independently paginated again on 21 October in this work.

### Not verified here

- The original conversation in the ChatGPT project **Plugins herstellen** was not accessible here.
- The VPS handoff and development plan were not directly read during this repository task.
- The ChatGPT plugin page and its rendered list of skills were not checked in the host UI.
- Actual main and specialist @ invocations were not run in ChatGPT.
- No independent next-agent comparison measured whether the skills improve work quality.
- The current archive's test suite was not executed as part of repository preparation.
- The user-provided public GitHub repository was accessible. Its initial main branch contained a placeholder README and a malformed MIT license file; this repository work replaces those and publishes the prepared project files. The final remote inventory and selected files are checked after publication.

### Version and product status

The current verified release remains **0.10.0**. This repository operation does not update the plugin or change its version. The prior handoff's reasoning for not declaring 1.0.0 was that end-to-end host invocation and practical use were not demonstrated. That acceptance gap remains; this document does not claim a 1.0.0-ready state.

### License and visibility

The downloaded plugin package contained no license file. The public GitHub repository now includes an MIT License with the copyright name RaDi0n92. The separate ChatGPT plugin remains a private USER plugin; making the repository public does not publish that plugin in ChatGPT. The original package archive retains its release metadata unchanged.

---

## Deutsch

### Am 21. Oktober 2026 direkt geprüft

| Gegenstand | Beleg | Ergebnis |
|---|---|---|
| Live-Pluginidentität | Plugin-Creator-Metadaten | Privates USER-Plugin, ID plugins_6ad3075c7ab08191871a0b9f73d19a57, Backendname context-forge-ultra, Version 0.10.0. |
| Aktueller Release | Plugin-Creator-Metadaten und Archivergebnis | pluginrel_6ad3b7d2bd2c819188e30f5409a556dd, Version 0.10.0. |
| Anzeigename | Beide Live-Manifeste | Space-Kitzler-Kontextschmiede. |
| Hauptaufruf | Metadaten und Inhalt des Hauptskills | space-kitzler-kontextschmiede; der Skill nennt @space-kitzler-kontextschmiede. |
| Aktive Skill-Dateien | Vollständig paginierte Live-Dateiliste und Archiv | 18 aktive SKILL.md-Dateien: ein Hauptskill und 17 Fachskills. Keine Skill-Datei fehlte in der Liste. |
| Paketdateien | Abgerufenes aktuelles Archiv, entpackt und gezählt | 173 Dateien; komprimierte Archivgröße 270.686 Bytes. |
| Archivintegrität | SHA-256 des abgerufenen Archivs | 3058ede2aa8037a58c1a2767004ef89c16e692536b77c71ad7b8366ede44dd23. |
| Kopierbarer Skillindex | Repository-Dateien | Direkte Links führen zu allen 18 vollständigen Skill-Dateien im portablen Export und im Original-Pluginbaum. |
| Agent-Skills-Export | Lokale Strukturprüfung anhand des veröffentlichten Formats | 18 Skill-Ordner; Ordnernamen stimmen mit `name` überein; Pflichtmetadaten halten die Grenzen ein; alle geprüften relativen Verweise lösen sich auf. |
| ZIP-Downloads | Entpackte ZIP-Inhalte und Integritätsprüfung | Originales Plugin-ZIP: 173 Dateien, bytegenau wie das entpackte Paket. MIT-Weitergabe-ZIP: dieselben 173 Dateien plus LICENSE im Stammverzeichnis, Integrität PASS. Agent-Skills-ZIP: 18 Skills, gemeinsame Referenzen, README und LICENSE; Integrität PASS. |
| Standardprompts | Beide Live-Manifeste | Drei Prompts: Kontextübergabe, Denkraum und Prüfung einer Übergabe. |
| Bereitgestelltes Repository | GitHub-Repositorymetadaten und Inhalte des main-Branches | Öffentliches Repository `RaDi0n92/Space-Kitzler-Kontextschmiede-Space-Tickler-Context-Forge-Prompt-Context-Engineering`, über das verbundene GitHub-Konto beschreibbar. |

Das exakte Archiv des Live-Releases liegt unter **downloads/**. Das entpackte Paket unter **plugin/** stammt aus demselben heruntergeladenen Archiv.

### Aus früheren Projektaufzeichnungen übernommen

Eine erhaltene Übergabe berichtet, dass ein lokaler Testlauf am 20. Oktober **93 bestandene Tests und einen übersprungenen Playwright-Vorschautest** ergab, weil Playwright nicht verfügbar war. Der Lauf wurde mit einer lokalen Kopie des Pakets 0.10.0 ausgeführt und für diese Repository-Arbeit nicht mit dem aktuellen Archiv wiederholt. Das ist historische Evidenz und kein frischer Test dieses Repositorys.

Dieselbe Übergabe berichtet, dass Plugin Creator in einer früheren Sitzung alle 18 Live-Skills zurückgegeben hatte und der Skill-Katalog vollständig vorlag. Die Dateiliste wurde am 21. Oktober für diese Arbeit erneut vollständig paginiert.

### Hier nicht verifiziert

- Die Originalunterhaltung im ChatGPT-Projekt **Plugins herstellen** war hier nicht erreichbar.
- VPS-Übergabe und Entwicklungsplan wurden für diese Repository-Arbeit nicht direkt gelesen.
- Die ChatGPT-Plugin-Seite und ihre dargestellte Skillliste wurden nicht in der Hostoberfläche geprüft.
- Hauptaufruf und Fachaufrufe mit @ wurden nicht tatsächlich in ChatGPT ausgeführt.
- Ein unabhängiger Vergleich mit Folgeagenten hat nicht gemessen, ob die Skills die Arbeitsqualität verbessern.
- Die Testsuite des aktuellen Archivs wurde während der Vorbereitung dieses Repositorys nicht ausgeführt.
- Das vom Nutzer bereitgestellte öffentliche GitHub-Repository war erreichbar. Sein ursprünglicher main-Branch enthielt einen Platzhalter-README und eine fehlerhafte MIT-Lizenzdatei; diese Repository-Arbeit ersetzt beide und veröffentlicht die vorbereiteten Projektdateien. Die abschließende Remote-Dateiliste und ausgewählte Dateien werden nach der Veröffentlichung geprüft.

### Version und Produktstand

Der aktuelle bestätigte Release bleibt **0.10.0**. Durch die Repository-Arbeit wurde das Plugin nicht aktualisiert und die Versionsnummer nicht verändert. Die frühere Übergabe begründete den Verzicht auf 1.0.0 mit dem fehlenden Nachweis tatsächlicher Hostaufrufe und praktischer Nutzung. Diese Abnahmelücke bleibt bestehen; dieses Dokument behauptet keine Bereitschaft für 1.0.0.

### Lizenz und Sichtbarkeit

Das abgerufene Pluginpaket enthielt keine Lizenzdatei. Das öffentliche GitHub-Repository enthält nun eine MIT-Lizenz mit dem Copyright-Namen RaDi0n92. Das separate ChatGPT-Plugin bleibt ein privates USER-Plugin; das öffentliche Repository veröffentlicht dieses Plugin nicht in ChatGPT. Das Originalarchiv bewahrt seine Release-Metadaten unverändert.

