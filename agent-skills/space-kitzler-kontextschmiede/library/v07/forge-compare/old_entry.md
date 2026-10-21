---
name: wirkungsvergleich
description: "Nutzen, wenn die Wirkung einer Context-Forge-Übergabe oder eines neuen Skills anhand echter Zielagenten-Aufgaben mit einer einfachen Baseline und adversariellen Beispielen vergleichend bewertet werden soll; trennt Strukturtest, Quellenprobe und Wirkung."
---

# Wirkung und Ergebnisse vergleichen

Der schönere Handoff gewinnt hier nicht. Ein System mit zehn Spezialskills kann schlechter sein als eine sorgfältige, kurze Übergabe. Ein Skript, das selbst erzeugte JSON-Felder kontrolliert, misst keine eigenständige Einsicht.

## Aussage und Versuchsdesign

Bei „ist Version 0.4 wirklich besser?“, „beweise die Kreativität“, „Red Team“ oder „lasse zwei Folgeagenten antreten“ lade `references/experimentdesign.md`. Für falsche Selbstbewertungen lade `references/angriffe.md`.

Baue zunächst eine faire **Baseline**, keine absichtlich schlechte Stichwortliste: Sie muss dem Nutzerauftrag ehrlich entsprechen. Vergleiche mit Space-Kitzler-Kontextschmiede bei möglichst gleicher Modellklasse, verfügbaren Originalen, Zeit-/Werkzeugbudget und Zielaufgabe.

A: Sorgfältige direkte Übergabe aus demselben Material. B: strukturierte Quellen- und Entscheidungssicht. C: zusätzliche freie Denkbrücken und Wiederleseangebote. Der Vergleich muss ausdrücklich keine dieser drei Varianten zum Sieger erklären.

## Beobachtbare Ergebnisse

- Hat der Folgeagent die empfohlenen Originale *wirklich* erneut gelesen, wenn zugänglich?
- Kann er die spät korrigierten Ziele und vertagten Ideen richtig auseinanderhalten?
- Entsteht mindestens eine neue, materialgebundene Einsicht, die nicht nur die Handoff-Formulierung wiederholt?
- Werden technische oder begriffliche Fehlannahmen sichtbar korrigiert?
- Erledigt der Agent die wirkliche Aufgabe? Was kostet die zusätzliche Komplexität?
- Kann ein kritischer Reviewer die Befunde unabhängig von der selbst erzeugten Bewertung prüfen?

## Transparente Grenze

Fehlt ein unabhängiger Modelllauf oder eine beobachtbare Skillaktivierung, sage **nicht getestet**. Eine unverblindete Modell-Selbstprobe kann nützlich sein, aber sie ist kein A/B-Beweis. Der Unterschied zwischen `bestanden`, `gescheitert`, `technisch fehlgeschlagen` und `unbewertbar` bleibt wichtig.

**Ergebnis:** konkretes Vergleichsprotokoll, Beobachtungen, offene Fragen und begründete Änderungsentscheidung. Ein besseres Messergebnis darf eine bestehende, echte Nutzerpräferenz nicht aushebeln. Wenn der Nutzer nur eine schnellere Übergabe will, keine Forschungsstudie aufdrängen.

## Ein Versuch, der das Gelingen nicht vorschreibt

Für den offenen Denkraum muss die Bewertungsfrage selbst fair bleiben: Nicht „Hat der Agent unsere Lieblingsbrücke genannt?“, sondern „Hat er eine eigene, auf Originale rückführbare neue Einsicht gewonnen, die seine nächste Handlung oder seine Deutung verändert?“ Eine ruhige, kürzere direkte Übergabe kann dabei gewinnen. Prüfe reale Aufgaben und tatsächliche Folgeschritte, nicht die Anzahl der Skill- oder Forschungsnamen. Wenn Modellläufe fehlen, dokumentiere die Lücke ohne einen Wirksamkeitsnachweis zu erfinden.

