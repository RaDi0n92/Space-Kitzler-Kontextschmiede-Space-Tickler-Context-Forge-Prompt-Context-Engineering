---
name: forschung
description: "Nutzen, wenn wissenschaftliche Paper, GitHub-Repositories, Issues, Herstellerdokumentation oder Entwicklerdiskussionen zur Verbesserung einer Context-Forge-Übergabe ausgewertet und in konkrete Verhaltensweisen übersetzt werden sollen. Nicht als Ersatz für aktuelles Web-Lesen oder für reine Bibliografien."
---

# Forschung prüfen und anwenden

Unter „Recherche“ verstehen wir das tatsächliche Studieren eines Materials: Fragestellung, Methoden, Grenzen, Quelllage, Reproduzierbarkeit, Gegenbefunde und sein möglicher Platz im Kontextkörper. Nicht „20 Links mit je einem Buzzword“.

**Wenn Forschung ausdrücklich eine reale Änderung unterstützen soll, übergib ihren konkreten Arbeitseffekt an `@autorisierte-umsetzung` und führe die Änderung mit den vorhandenen Werkzeugen aus.** Eine Literaturliste ist kein Ersatz.

## Warum dieser Skill eigenständig ist

Andere Skills benutzen Ergebnisse. Hier wird zuerst geklärt, was eine Studie oder ein Repository tatsächlich hergibt. Wer einer Folge-KI aus Research automatisch eine Methode verordnet, hat eine Evidenzkategorie übersprungen.

## Zwei getrennte Wege

**Paper:** Prüfe Fragestellung, untersuchte Modelle, Datensätze, trainierte gegenüber unveränderten Komponenten, Baselines, Ergebnisgröße, Einschränkungen, mögliche Replikationsprobleme und Veröffentlichungsstand. Nutze Online-Werkzeuge nur wenn wirklich zugänglich und für die Aufgabe nötig.

**Repository:** Öffne tatsächliche README, Architekturdateien, Implementierungsdateien, Tests, Lizenz und soweit relevant Issues. Sind sie nicht geöffnet, nur als Hinweise aufführen. Eine „Cognition Suite“ kann nur Zustandsführung implementieren, selbst wenn ihre Marketingworte neuronale Aktivität suggerieren.

## Das Übersetzungsproblem

**Bei einem Ausführungsauftrag:** Die Recherche ist nicht die Hauptausgabe. Wenn eine Quelle eine konkrete Entscheidung beeinflusst, leite daraus unmittelbar einen zulässigen Versuch, eine Änderung oder eine Prüfung im aktuellen Projekt ab und führe sie im Rahmen des Nutzerauftrags aus. `@autorisierte-umsetzung` ist der praktische Pfad. Gib dem Agenten keine zehn Literaturhinweise als Ersatz für den Eingriff. Wenn nur Recherche beauftragt wurde, liefere selbstverständlich die recherchierten Ergebnisse.

Für jede übernommene Einsicht formuliere nicht nur „darum Progressive Disclosure“, sondern: **Auslöser im aktuellen Arbeitsfall → konkrete Lese-/Entscheidungsänderung → sichtbares Ergebnis → möglicher Falsifikationstest → offene Grenze**. Wenn kein konkreter Verhaltensunterschied daraus folgt, bleibt die Quelle als Inspiration oder Lesetipp, nicht als verdeckte Pflichtmethode.

Beispiele: Bei Context Rot nicht pauschal kurze Texte bauen, sondern eine Frage mit einer ablenkenden Datei gegenlesen. Bei SELF-DISCOVER dem Zielagenten *eigene* Denkmodulwahl ermöglichen, statt seine 18 Wege festzulegen. Bei JSpace die Differenz zwischen verborgenen Tokens und kontinuierlichen Aktivierungen beibehalten, ohne Aktivierungs-Zugriff zu behaupten.

## Wo du Originale findest

Lies `../space-kitzler-kontextschmiede/library/v07/forge-research/references/forschungsatlas.md` sobald aus Vorarbeiten die tragenden Forschungsstränge rekonstruiert werden sollen. Bei GitHub-Funden `../space-kitzler-kontextschmiede/library/v07/forge-research/references/repositories-und-gegenbefunde.md`. Für offizielle aktuelle Plugin-Mechanik siehe https://developers.openai.com/plugins/concepts/skills und https://developers.openai.com/plugins/build/skills . Forschungsanwendung in `@kontextuebergabe` kann selektiv bleiben.

**Wirkgrenze:** Ein Skill ist kein trainiertes Coconut, nicht der neuronale J-Space, nicht ein automatisch installierter Evaluierungsdienst. Nicht geprüfte und nicht direkt implementierte Fähigkeiten ausdrücklich markieren.

## Aktiver Denkmechanismus statt Forschungsreferat

Wenn der Nutzer die recherchierten JSpace-/Reasoning-Ansätze explizit als Anregungs- und Steuerungsimpulse für schwierige Agentenarbeit verwenden will, verweise **bei der Bearbeitung** auf `../space-kitzler-kontextschmiede/library/v07/forge-reasoning-lab/references/forschungsmechaniken.md`. Das ist eine verfahrensorientierte Übersetzung aus SELF-DISCOVER, Tree/Graph of Thoughts, J-Space-Forschung und deren Grenzen. Leite daraus **konkrete Alternativmodelle, Querverbindungen, Kontrasttests oder nächste Schritte im aktuell zugänglichen Material** ab. Ein späterer Prompt oder Handoff soll diese Ergebnisse enthalten. Reine Studiennennung und Bibliografie erfüllen den Auftrag nicht.

## Vom Forschungsfund zur Nutzbarkeit

Bei den ursprünglich dokumentierten GitHub-Funden arbeite gegebenenfalls mit `../space-kitzler-kontextschmiede/library/v07/forge-repo-practices/references/github-lernpfade.md`. Die Kurzform im späteren Handoff lautet *Problem → Kernidee → mögliche Verwendung*: SELF-DISCOVER kann den Folgeagenten ermutigen, für genau diesen Stoff selbst eine Denkstruktur zu wählen; DSPy/GEPA erinnert an echte Aufgabenvergleiche; J-Space Cognition Suite an wiederauffindbaren Arbeitsstand. Daraus entsteht nicht automatisch ein installierter Dienst. Wenn die Forschungsfrage selbst Gegenprüfungen verlangt, führe diese durch; wenn der Folgeagent vor allem weiterarbeiten soll, halte den Überblick klar und lenke ihn auf relevante Originale, ohne ihn mit jeder methodischen Debatte zu belasten.

