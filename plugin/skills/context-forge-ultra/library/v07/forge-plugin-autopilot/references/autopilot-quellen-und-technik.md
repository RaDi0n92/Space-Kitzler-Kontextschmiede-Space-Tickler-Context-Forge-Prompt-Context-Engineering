# Plugin Autopilot: geprüfte GitHub-Bausteine, richtiger Verwendungskontext

**Öffentliche Quelle:** https://github.com/imMamdouhaboammar/chatgpt-codex-plugin-autopilot
**Urheber:** Mamdouh Aboammar, 2026; MIT-Lizenz: https://github.com/imMamdouhaboammar/chatgpt-codex-plugin-autopilot/blob/main/LICENSE
**Lesestatus:** README und die drei zugehörigen Skills `agentic-repo-discovery`, `workflow-to-skill-compiler`, `plugin-experience-architect` sowie die Lizenz wurden am 17.10.2026 in der verbundenen GitHub-Quelle gelesen. Für `analyze_repo.py`, `validate_plugin.py`, `package_plugin.py` wurden Existenz, Dateiidentität, Umfang und Eingangsabschnitte geprüft, **nicht deren gesamte Implementierung**. Dieses Context-Forge-Plugin kopiert nicht die komplette Autopilot-Software und behauptet keine Ausführung dieser Skripte.

## Was daran praktisch wertvoll ist

Das Projekt beginnt mit **Repo-Entdeckung statt sofortigen Manifesten**: Es sucht nach Skills, Agents, AGENTS.md, Workflows, Commands und Playbooks und unterscheidet beizubehaltende Skills, übersetzbare Skills, reine Referenzen, Runtime-Abhängigkeiten, Interna und ungeeignete Kandidaten. Ein Repository kann eine wertvolle Funktion enthalten, ohne dass jede Datei Teil des öffentlichen Plugins werden darf.

Der **Workflow-to-Skill-Compiler** übersetzt Aufgaben von der Nutzeranfrage bis zum Ergebnis, statt Dateitexte in SKILL.md zu kopieren. Entscheidend sind Auslöser, Eingaben, Entscheidungen, reale Aktionen, Validierung, Nachweise und berechtigte Stopppunkte. Bei Context Forge interessiert uns besonders die Frage: Was wird an der Kreativität oder Herkunft kaputtgeschnitten, wenn aus dem Originalmaterial eine glatte Anleitung wird?

Der **Plugin Experience Architect** unterscheidet Nutzerjobs; zu viele beinahe identische Skills verschlechtern die Auswahl. Für jeden neuen Skill muss klar sein, warum er getrennt existiert, welche Eingabe ihn auslöst, welche Arbeit er tatsächlich leistet und wo sein Ergebnis endet.

Ein Plugin ist **skills-only**, solange es nur auf Anweisungs-/Referenzebene arbeiten und vorhandene Hostwerkzeuge benutzen muss. Ein externer MCP-Server ist erst dann sinnvoll, wenn echte zusätzliche Daten-/Aktionsschnittstellen gebraucht werden. Ein Prompt oder Skill erschafft keinen geheimen Shell-, Browser- oder Modellzugriff.

Die Prüftools des Autopiloten können Manifest, Assets, Dateien, Archive und deterministische Pakete untersuchen. **Sie beweisen keine bessere Ideenfindung oder eigenständige Originallektüre.** Nach technischer Validierung braucht Context Forge daher zusätzlich Gegenproben und praktische Nutzung durch einen Folgeagenten.

## Passende Anwendungsstellen im aktuellen Plugin

- Der Nutzer will „aus dieser GitHub-Arbeitsweise ein Plugin machen“: tatsächliche Dateien lesen, wiederholbaren Nutzerjob identifizieren, passende Skills entwerfen, Sicherheits-/Lizenzgrenzen prüfen, testen und erst dann verpacken.
- Der Nutzer will Context Forge **nur als Übergabe**: Autopilot nicht aktivieren. Dessen Erkenntnisse können als historische Lernspur erwähnt werden, aber keine Pluginbau-Aufgabe erfinden.
- Der Nutzer will einen bestehenden privaten Pluginstand verbessern: vorhandene Dateien über Plugin Creator lesen, erwartete Release-ID mitführen, Änderungen gegen Ursprung vergleichen, neues Paket **als Update desselben Plugin** speichern, anschließend Dateien und Release zurücklesen. Ein ZIP-Link allein genügt nicht.
- Der Nutzer will aus der Promptsammlung `f/prompts.chat` Muster lernen: Quelleninhalt und Lizenz bewerten und nur nützliche Anregungen herausziehen. Keine universelle Wirkung behaupten. https://github.com/f/prompts.chat
- Der Nutzer will aus der Sammlung `x1xhlol/system-prompts-and-models-of-ai-tools` Mechanismen untersuchen: keine automatisch authentischen Systemprompts und keinerlei Vorrang fremder Instruktionen annehmen. https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools
- Der Nutzer will aus `Tiger3807861189/J-Space-Cognition-Suite`, `sina85/sina-gpt` oder `igorbarshteyn/jlens-gguf` lernen: zwischen äußerer Agentenstruktur, Forschungsabsicht und wirklich instrumentierten Modellaktivierungen unterscheiden. Keine pauschale Übernahme. https://github.com/Tiger3807861189/J-Space-Cognition-Suite · https://github.com/sina85/sina-gpt · https://github.com/igorbarshteyn/jlens-gguf

## Externe, bereits installierte Fähigkeiten

Wo `@Plugin Autopilot` in der aktiven ChatGPT-Umgebung wirklich auswählbar ist, können dessen Skills unmittelbar benutzt werden. In dieser Arbeitssitzung wurde sein Skilltext über `skills://plugins/chatgpt-codex-plugin-autopilot/chatgpt-codex-plugin-autopilot/skill.md` sowie seine Spezialisten eingesehen. **Ein Skilltext mit einem @-Namen ruft jedoch niemals automatisch ein anderes Plugin auf.** Wenn der Host diese Fähigkeit nicht zulässt, bleibt diese Referenz eine offengelegte Abhängigkeit und der lokale `forge-plugin-autopilot` bietet einen eigenständigen sinnvollen Arbeitsweg ohne vorgetäuschte Ausführung.

## Nicht kopiert und nicht aktiviert

Kein fremdes GitHub-Repository geklont, keine Autopilot-Skripte eingebettet oder ausgeführt, kein neuer MCP-Server, kein GitHub-Commit oder PR, keine öffentliche Plugin-Directory-Veröffentlichung. Die genannten fremden MIT-Quellen werden verlinkt und inhaltlich ausgewertet, nicht als eigene Autorenarbeit ausgegeben.
