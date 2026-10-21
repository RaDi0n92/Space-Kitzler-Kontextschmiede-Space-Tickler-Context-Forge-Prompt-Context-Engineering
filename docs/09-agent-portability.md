# Agent portability and copyable skills

## English

### What is included

- `agent-skills/` contains all 18 complete, separately readable skill files in a folder-based Agent Skills layout, with the shared reference library required by their relative links.
- `downloads/Space-Kitzler-Kontextschmiede-Agent-Skills-0.10.0.zip` contains that complete portable skills tree and a copy of the MIT license.
- `plugin/skills/` keeps the exact skill files from the live plugin archive.
- `downloads/Space-Kitzler-Kontextschmiede-0.10.0.tar.gz` is the untouched archive returned for the live plugin release. `downloads/Space-Kitzler-Kontextschmiede-ChatGPT-Plugin-0.10.0.zip` contains the same 173 package files in ZIP form. The [MIT redistribution ZIP](../downloads/Space-Kitzler-Kontextschmiede-ChatGPT-Plugin-MIT-0.10.0.zip) adds the license notice without altering those package files. Importing this extra-file variant into ChatGPT was not tested.

### Portability boundary

The Agent Skills specification defines a folder with a `SKILL.md`, YAML frontmatter, and Markdown instructions; optional references and resources can be included beside it. The export uses that structure, with each `name` matching its folder and the required `name` and `description` fields checked against the published limits. Its relative file references were checked in the exported tree. See the [Agent Skills specification](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx).

This is a portable file format, not a guarantee that every agent has a skill loader. A compatible agent may load the folders as skills. Another agent can still use an individual skill by receiving the full `SKILL.md` text and any referenced files. The `@skill` invocation convention, automatic skill selection, tools, permissions, and host-specific actions must be adapted to what the target agent actually supports. Instructions do not provide missing tools or access.

For an individual copy, use the links in [`skills/README.md`](../skills/README.md). For best fidelity, use the complete Agent Skills ZIP so shared references remain available. Use the ChatGPT plugin archive only with an importer or host that accepts its package format; the repository alone does not publish the private ChatGPT plugin to other users.

### Language and license

The skill bodies remain in German to preserve the live plugin wording. Repository-authored documentation is English first, then German. The public repository is licensed under MIT; retain the root **LICENSE** notice when copying or redistributing its contents. The original live package itself remains unchanged and had no license file when retrieved.

## Deutsch

### Was enthalten ist

- `agent-skills/` enthält alle 18 vollständigen, einzeln lesbaren Skill-Dateien in einer ordnerbasierten Agent-Skills-Struktur samt gemeinsamer Referenzbibliothek für ihre relativen Verweise.
- `downloads/Space-Kitzler-Kontextschmiede-Agent-Skills-0.10.0.zip` enthält diesen vollständigen portablen Skill-Baum und eine Kopie der MIT-Lizenz.
- `plugin/skills/` bewahrt die exakten Skill-Dateien aus dem Live-Pluginarchiv.
- `downloads/Space-Kitzler-Kontextschmiede-0.10.0.tar.gz` ist das unveränderte Archiv des Live-Plugin-Releases. `downloads/Space-Kitzler-Kontextschmiede-ChatGPT-Plugin-0.10.0.zip` enthält dieselben 173 Paketdateien im ZIP-Format. Das [MIT-ZIP zur Weitergabe](../downloads/Space-Kitzler-Kontextschmiede-ChatGPT-Plugin-MIT-0.10.0.zip) ergänzt die Lizenz, ohne die Paketdateien zu verändern. Der Import dieser Variante in ChatGPT wurde nicht getestet.

### Grenze der Übertragbarkeit

Die Agent-Skills-Spezifikation definiert einen Ordner mit `SKILL.md`, YAML-Metadaten und Markdown-Anweisungen; optionale Referenzen und Ressourcen können daneben liegen. Der Export nutzt diese Struktur. Bei jeder Datei stimmen `name` und Ordnername überein; die Pflichtfelder `name` und `description` wurden gegen die veröffentlichten Grenzen geprüft. Die relativen Dateiverweise wurden im Export geprüft. Siehe die [Agent-Skills-Spezifikation](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx).

Das ist ein portables Dateiformat, aber keine Garantie, dass jeder Agent einen Skill-Lader besitzt. Ein kompatibler Agent kann die Ordner als Skills laden. Ein anderer Agent kann einen einzelnen Skill trotzdem nutzen, wenn er den vollständigen `SKILL.md`-Text und referenzierte Dateien erhält. Die `@skill`-Aufrufkonvention, automatische Auswahl, Werkzeuge, Berechtigungen und hostabhängige Aktionen müssen an das angepasst werden, was der Zielagent tatsächlich unterstützt. Anweisungen verschaffen keine fehlenden Werkzeuge oder Zugriffe.

Für einzelne Skills nutze die Links in [`skills/README.md`](../skills/README.md). Für die beste Vollständigkeit verwende das gesamte Agent-Skills-ZIP, damit gemeinsame Referenzen erhalten bleiben. Das ChatGPT-Pluginarchiv kann nur mit einem Importer oder Host verwendet werden, der dieses Paketformat akzeptiert; das Repository allein veröffentlicht das private ChatGPT-Plugin nicht für andere Nutzer.

### Sprache und Lizenz

Die Skill-Texte bleiben auf Deutsch, damit der Wortlaut des Live-Plugins erhalten bleibt. Neu verfasste Repository-Dokumente stehen zuerst auf Englisch und darunter auf Deutsch. Das öffentliche Repository steht unter MIT; beim Kopieren oder Weitergeben seiner Inhalte ist der Hinweis aus **LICENSE** im Stammverzeichnis beizubehalten. Das ursprüngliche Live-Paket selbst bleibt unverändert und enthielt beim Abruf keine Lizenzdatei.
