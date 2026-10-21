# Plugin Autopilot: was Context Forge davon übernehmen kann

Diese Notiz bezieht sich auf den bereits verfügbaren Spezial-Skill **ChatGPT/Codex Plugin Autopilot**, dessen Installationsanleitungen in der vorhandenen Skills-Umgebung gelesen wurden. Er ist ein Werkzeug für Pluginarbeit und nicht der neue Produktkern von Context Forge. Er wird hier nicht still in ein weiteres selbsternanntes „Pluginbau-Plugin“ verwandelt.

## Das eigentliche Problem

Wir hatten eine beeindruckende Geschichte, umfangreiche Forschungs-MDs, einen konkreten Nutzergedanken und anschließend drei dünne Skills. Selbst 67 bestandene Testfälle bewiesen nicht, dass die kreative Übertragung gelungen war. Die **Methode** hinter Autopilot hilft an einer wichtigen Stelle: Zwischen Material und nutzbarem Plugin gibt es eine eigenständige Übersetzungsarbeit.

## Drei brauchbare Teile

**Agentic Repo Discovery:** Der Anfang ist kein Import. In README, Skill, Modulen, Tests und Nutzungsbeispielen wird nach wirklich wiederholbaren Tätigkeiten gesucht. Im Context-Forge-Projekt sind das unter anderem Originallesung, Entscheidungsgeltung, ungewöhnliche Denkbrücken und Folgeagenten-Einstieg. Ein Kapitel ist noch keine Tätigkeit.

**Workflow to Skill Compiler:** Ein Skill braucht einen verständlichen Anlass, seine eigene Erkenntnisleistung und ein erkennbares Ergebnis. Die komplexe Quellen- und Entscheidungsgeschichte darf dabei nicht auf ein paar schmückende Stichwörter reduziert werden. Hintergrundwissen gehört unter lesbare Referenzen, deren **Aufrufbedingung** im Skill steht.

**Plugin Experience Architect:** Ein Agent muss erkennen, wann eine Fähigkeit passt und wann sie gerade stört. Dafür unterscheidet man Auslöser, fertiges Resultat und mögliche Fehlaktivierung. Mehr Skills sind nicht besser, wenn jeder auf die gleiche Frage anspringt. Ein spezieller Quellenskill hat einen anderen Anlass als ein sokratischer Denkdialog.

## Wie der nachfolgende Agent damit arbeiten kann

Wenn er eine neue Context-Forge-Version selbst bauen soll, kann er die vorhandenen Fähigkeiten an echten Aufträgen prüfen: In welcher Situation wird die Skillbeschreibung gefunden? Hat der Agent die passenden Referenzen dann auch gelesen? Welche neue Beobachtung kann er vorweisen? Hat die zusätzliche Struktur die Freiheit des Denkens verbessert oder eingeschränkt?

Wenn er nur einen Handoff erstellen soll, **muss er keine Pluginbau-Tests ausführen**. Die Autopilot-Gedanken dürfen still in der Qualität seiner Werkzeugwahl wirken, ohne den Handoff in eine technische Wartungsanleitung zu verwandeln.

## Konkrete Grenzen

Ein installierter Spezial-Skill ist keine API, die Context Forge durch einen Textlink automatisch aufruft. Er kann nur in Hosts genutzt werden, die ihn tatsächlich anbieten. Autopilot verlangt beim echten Bauen unter anderem Quellinspektion, korrekte Paketformate, lokale Tests, deterministisches Packaging und Prüfung nach Installation. Diese Schritte sind im Pluginbau-Auftrag konkret und nützlich, aber keine allgemeine Pflicht für eine kreative Projektdeutung.

**Weitere Originale:**
- `skills://plugins/chatgpt-codex-plugin-autopilot/chatgpt-codex-plugin-autopilot/skill.md`
- `skills://plugins/chatgpt-codex-plugin-autopilot/agentic-repo-discovery/skill.md`
- `skills://plugins/chatgpt-codex-plugin-autopilot/workflow-to-skill-compiler/skill.md`
- `skills://plugins/chatgpt-codex-plugin-autopilot/plugin-experience-architect/skill.md`
- Offizielle Pluginpaketform: https://developers.openai.com/plugins/build/skills

Keine Behauptung, diese extern installierten Skills seien als fremder Quellcode in Context Forge eingepackt oder automatisch ausführbar. Die Übertragung umfasst ihre **brauchbaren Arbeitsprinzipien**, hier dokumentiert, plus die tatsächliche Nutzung des vorhandenen Plugin Autopilot während unserer Pluginentwicklung.
