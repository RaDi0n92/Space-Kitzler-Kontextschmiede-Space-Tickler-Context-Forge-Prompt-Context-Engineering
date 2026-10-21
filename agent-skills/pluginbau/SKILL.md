---
name: pluginbau
description: "Verwenden, wenn der Nutzer ausdrücklich aus einem GitHub-Repository, gewachsenen Agentenabläufen oder einem Context-Forge-Handoff ein echtes ChatGPT/Codex-Plugin bauen, prüfen oder aktualisieren möchte, insbesondere mit @Plugin Autopilot. Nicht für normale Kontextübergaben ohne Plugin-Bauauftrag."
---

# Pluginabläufe in Skills übersetzen

Hier begegnen sich zwei verschiedene Tätigkeiten: Space-Kitzler-Kontextschmiede sorgt dafür, dass aus Gesprächs- und Quellenmaterial die **richtige Absicht und ihre Geschichte** erhalten bleiben. **Plugin Autopilot** prüft, welche wiederverwendbaren Arbeitsabläufe daraus ein funktionsfähiges Plugin ergeben und welche Dateien, Prüfungen und Freigaben dafür real notwendig sind. Ersetze die eine Tätigkeit nicht durch die andere.

## Was dem nachfolgenden Agenten vermittelt werden soll

Ein Repository ist noch kein Plugin, und ein lang diskutierter Gedanke ist noch kein ausführbarer Skill. Beginne mit dem konkreten Problem, das der Nutzer lösen möchte. Ein Beispiel aus diesem Projekt: Aus gewachsener Forschungs- und Projektarbeit soll ein neuer Agent eigenständig und schöpferisch weiterarbeiten können. Das ist **nicht** automatisch eine Aufforderung, einen universellen Plugin-Generator zu bauen. Wenn der Nutzer aber **ausdrücklich** einen solchen Pluginbau verlangt, darf das bestehende Wissen dafür eingesetzt werden.

Nutze die unter `../space-kitzler-kontextschmiede/library/v07/forge-plugin-autopilot/references/plugin-autopilot-und-kontext-forge.md` dokumentierte Unterscheidung zwischen Entdeckung, Übersetzung, technischer Implementierung und überprüfter Anwendung. Wenn die Herkunft der Nutzerabsicht komplex ist, hilft `@projektgeschichte` und bei gültigen/verworfenen Entscheidungen `@entscheidungsstatus`. Verwende diese nur, sofern sie eine echte Unsicherheit auflösen. Der Arbeitsweg darf nicht die spätere Lösung schon vorzeichnen.

## Aus tatsächlicher Quelle zu wirklicher Funktion

Bei einem Repository **lies** nach Möglichkeit die relevanten README-, Workflow-, Skill-, Test- und Lizenzdateien. Kein einzelner Suchtreffer ersetzt die Originallesung. In der GitHub-Arbeit unterscheiden sich `AGENTS.md`, ein lauffähiges Python-Skript, eine Beispielsammlung und eine fremde Systemanweisung beträchtlich: Sie sind nicht austauschbare Bausteine. Zeige, welche Erkenntnis aus welcher tatsächlich betrachteten Quelle hervorgeht, und was du noch nicht gelesen hast.

Frage beim Übersetzen: Welcher Nutzerjob wird wiederholt gebraucht? Was würde diesen Skill aufrufen? Welche Eingaben sind vorhanden, welche fehlen? Was soll nachher *wirklich vorliegen* und wie können wir es erkennen? Was braucht echte Toolrechte? Welche interessante Eigenschaft der ursprünglichen Arbeit würde durch die Verkürzung verloren gehen? Welches Beispiel würde die neue Formulierung widerlegen?

Eine geglättete Kompetenzbeschreibung ist kein Ersatz für den Ablauf. Erhalte relevante Fälle, Quellen, Entscheidungspunkte, Fehlversuche und den Grund dafür, *warum* der Ablauf auf diese Weise hilft. Die Tiefe gehört gegebenenfalls in `../space-kitzler-kontextschmiede/library/v07/forge-plugin-autopilot/references/`; im `SKILL.md` müssen **Auslöser, konkret zu ladendes Wissen, Nutzungsweise und Ergebnis** klar sein. Das ist keine Anweisung an den Folgeagenten, seine Gedankengänge offenzulegen.

## Den vorhandenen Plugin Autopilot wirklich nutzen

Das öffentliche, unter MIT veröffentlichte Projekt `imMamdouhaboammar/chatgpt-codex-plugin-autopilot` enthält die spezialisierten Skills `agentic-repo-discovery`, `workflow-to-skill-compiler`, `plugin-experience-architect` und das Hauptverfahren `chatgpt-codex-plugin-autopilot`. Die Quelle und konkrete Anwendungspunkte sind in `../space-kitzler-kontextschmiede/library/v07/forge-plugin-autopilot/references/autopilot-quellen-und-technik.md` dokumentiert.

**Wenn diese installierten Skills zur aktuellen Umgebung gehören**, ziehe sie für den jeweiligen Teilauftrag hinzu, anstatt dieselbe Schnittstelle schlecht nachzuerfinden. Die bloße Nennung von `@Plugin Autopilot` oder einer Skill-URI ist aber noch **kein ausgeführter Aufruf**. Wo keine entsprechende Hostfunktion angeboten wird, halte dich an die hier beschriebenen überprüfbaren Teilaufgaben; behaupte nicht, Autopilot habe etwas ausgeführt.

Behalte seine wesentlichen Qualitätsgrenzen: Quellrepository ansehen; öffentlich/private Komponenten trennen; Typ `skills-only`/`MCP-backed`/`hybrid` nach tatsächlichem Bedarf wählen; nutzbare Skill-Metadaten formulieren; Format und Pfade prüfen; technische Prüfungen **ausführen**, sofern verfügbar; gegen die bereits funktionsfähige Version testen; vorhandene private Plugin-ID **aktualisieren**, nicht einen Doppelgänger erstellen. Kein veröffentlichter Release und keine Freigabe ohne Benutzerauftrag.

## Wie dieses Skillset den anderen Agenten fördert

Die Ergänzung soll das Selbstverständnis des nächsten Agenten erweitern: Er erfährt, was wir zu Context Engineering, Quellenwahrheit, kreativen Querverbindungen und Pluginbau erforscht haben, **welche Probleme wir damit lösen wollten** und **wie er die passenden Erkenntnisse praktisch einsetzen kann**. Empfiehl einschlägige Originale konkret, wenn sie ihm wirklich helfen. Weder literarische Schönfärberei noch eine riesige Pflichtlektüreliste.

Bei einem tatsächlichen Pluginbau muss der Agent seine eigene Lösung wählen dürfen: Einige Vorhaben brauchen einen einzigen tiefen Skill, andere zwölf unterscheidbare; manches braucht einen MCP-Server, vieles nicht. Das ist nicht mit der Anzahl der Dateien zu entscheiden. Die Quellen dürfen zu neuen, begründeten Alternativen führen.

## Ergebnis und klare Trennung

Liefere bei einem Bauauftrag die tatsächlich mögliche Änderung am Plugin und nachgewiesene Tests; wenn nicht ausführbar, einen ehrlichen, direkt brauchbaren Entwurf mit dokumentierter Lücke. Beim Update in ChatGPT die vorhandene Identität, Versionsgeschichte, Standard-Startanfragen und Nutzerfreigaben bewahren. Für den Prüfmaßstab `@wirkungsvergleich`/`@uebergaben-pruefen` heranziehen, **nicht** grüne Verpackungstests mit besserem Denken gleichsetzen.

**Absichtliche Grenze:** Dieser Skill ist eine **optionale Pluginbau-Brücke**. Die Kernfähigkeit von Space-Kitzler-Kontextschmiede bleibt der offene, quellentreue, kreative Handoff. Die künftige Verbindung zum ProgrammHarness+ObservingController und Automationen werden dadurch nicht aktiviert.
