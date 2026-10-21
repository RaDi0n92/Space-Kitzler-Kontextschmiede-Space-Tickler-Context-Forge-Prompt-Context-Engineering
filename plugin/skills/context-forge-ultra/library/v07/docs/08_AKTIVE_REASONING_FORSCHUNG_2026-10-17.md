# Context Forge Ultra 0.7.0 – Forschung in aktive Reasoning-Herausforderungen übersetzt

**Datum:** 17.10.2026. **Status:** Plugin-Skill-Design plus überprüfbare Beispiele, *keine* gemessene J-Space-Intervention und kein unabhängig ausgeführter Folgeagententest.

## Korrektur des Projektverlaufs

Der Nutzer hat wiederholt gesagt: Es genügt nicht, einen Folgeagenten auf wissenschaftliche Arbeiten hinzuweisen oder einen Forschungsvortrag in einen Handoff einzubauen. Der Masterprompt soll die **Mechanismen der erforschten Denkverfahren im aufgabenbezogenen Kontext einsetzen**, damit der nächste Agent sich an echten Gegenständen weiterdenken, abweichende Erklärungen ausprobieren, weit auseinanderliegende Beobachtungen verknüpfen, neue Möglichkeiten entdecken und daraus reale weitere Arbeit machen kann. **Explizit hohe Komplexität ist erwünscht, wenn sie die Tiefe der Bearbeitung steigert.** Ein bloßes Erhöhen der Wortanzahl, Persona-Zahl oder vorgeschriebenen Denkschritte erfüllt das nicht.

## Unterschied der Forschungsansätze

- **SELF-DISCOVER:** Aufgabe erhält keine starre Allzweckroutine. Der Agent wählt/erzeugt zu diesem Material passende Denkzugänge. Quelle https://arxiv.org/abs/2402.03620.
- **Tree of Thoughts:** Sinnvolle konkurrierende Alternativen vor voreiliger Festlegung auf eine Interpretation untersuchen. Quelle https://arxiv.org/abs/2305.10601.
- **Graph of Thoughts:** Alternative Einsichten nicht isolieren, sondern zusammenführen, gegenseitig verändern und zurück in das Material wirken lassen. Quelle https://arxiv.org/abs/2308.09687.
- **J-Space / Jacobian Lens:** Erforschung interner Repräsentationen und selektiver flexibler Verarbeitung. Für ein herkömmliches Skill nur *Inspirationsquelle*, keine direkte Kontrolle der Gewichte oder Aktivierungen. Primärquelle https://transformer-circuits.pub/2026/workspace/index.html.
- **Coconut:** Speziell trainierte latente Verarbeitung, nicht aus einer Promptanweisung installierbar. Quelle https://arxiv.org/abs/2412.06769.

## Was sich im Paket konkret ändert

Es gibt neu `forge-reasoning-lab` mit genauem Aktivierungsgrund, einer umfassenden Anleitung zur **aufgabengebundenen Denkhervorrufung**, einem Forschungsmechanismen-Text und einer exemplarischen Materialkreuzung. Der neue Skill ist explizit in `forge-masterprompt`, `forge-handoff`, `forge-agent-reentry`, `forge-act`, `forge-perspectives`, `forge-research` eingebettet, immer bei entsprechenden komplexen Aufträgen. Er soll die Forschungsabsicht *im tatsächlichen Masterprompt* wiederfinden lassen, nicht in einer separaten Rechercheliste. Das Plugin bleibt ein Skills-only-Plugin; seine Ausführung benötigt die von ChatGPT bereitgestellten Werkzeuge, es erhält keine neuen API-Rechte.

## Gedankliche Probe 1: schwacher Baseline-Prompt

> Lies unsere Dateien. Denke besonders kreativ und nutze SELF-DISCOVER, Graph of Thoughts und J-Space. Entwickle 18 Perspektiven und schreibe einen guten Masterprompt.

**Problem:** Austauschbare Anweisung; keine tatsächlichen Quellenkanten, keine konkurrierenden Hypothesen, keine Art der praktischen Unterscheidung. Viele Worte, wenig neue Entscheidungsmöglichkeit.

## Gedankliche Probe 2: gezielter aufgabengebundener Masterprompt-Ausschnitt

> Dieses Projekt begann mit einer Bitte, eine Prompt-Engineering-Kompetenz wiederverwendbar zu machen. An einer Stelle wurde daraus irrtümlich eine Pluginfabrik. Später entstand erneut eine Abweichung: Die dokumentierte Forschung über leistungsfähige Übergaben wurde selbst zum Produkt, während das eigentliche Arbeiten mit dem Material zu kurz kam. Lies die beiden Entwicklungsmomente in den verfügbaren Originalquellen selbst. Tragen sie dieselbe Ursache, etwa eine schleichende Ersetzung des Nutzerzwecks durch ein gewohntes Produktionsschema? Oder sind es zwei verschiedene Fehler, einer im Zielverständnis und einer in der Auslösung von Skills? Entwickle aus deiner Lektüre eine eigene Erklärung; die beiden Vorschläge hier dürfen falsch sein. Suche nach einer dritten Verbindung mit einem anderen Teil des Projekts. Was würde die bevorzugte Erklärung widerlegen? Wenn du einen überprüfbaren Unterschied gefunden hast, baue eine kleine nutzbare Masterprompt-Variante, die genau diesen Fehler bei einem anderen realistischen Projekt vermeidet, und stelle sie einer direkten Version gegenüber. Gib an, welche originalen Stellen du wirklich gelesen hast und welche der Folgeagent selbst lesen sollte.

**Warum anders:** Der Text stellt die Forschung nicht als Prüfpflicht oder Buzzword voran. Er nutzt: *aufgabenbezogene Denkwegwahl, alternative Ursachentheorien, Kreuzung von Quellen, Rückführung auf überprüfbares Material und handlungsfähige nächste Probe*. Ob der Folgeagent daraus tatsächlich etwas Besseres macht, ist eine eigene experimentelle Frage.

## Empirische Akzeptanzprobe, noch ausstehend

Für einen belastbaren Produktnachweis sind mindestens drei reale schwierigere Dokument-Sets sinnvoll. Pro Set vergleichen: (A) guter direkter Prompt, (B) v0.6.0-Handlungs-Handoff, (C) v0.7.0 mit aktiviertem Reasoning Lab. Alle Varianten mit identischem verfügbarem Material, identischem Zielagenten und vergleichbaren Werkzeugrechten. Relevante Ergebnisse getrennt festhalten:

1. Rückgewinnung zentraler Nutzerentscheidungen und korrekte Originalzugriffe.
2. Unterschiedlichkeit und materialbezogene Begründung eigener neuer Hypothesen.
3. Tatsächlich neue Verknüpfungen statt umbenannter Zusammenfassungen.
4. Die Fähigkeit, sich von einer angebotenen falschen Vorgängerinterpretation zu lösen.
5. Qualität der tatsächlich hergestellten Arbeit, etwa eine getestete Änderung oder ein nutzbarer Masterprompt.
6. Nebenwirkungen: Kosten, falsche Claims, aufgezwungene Denkrituale, unnötige Komplexität.

Ein bestandenes lokales YAML-/Referenztestpaket ist keine Messung der Modellwirkung. Ohne unabhängige Agentenläufe ist nur das **vorbereitete und installierte Verhalten** nachgewiesen.

## Red Team vor Veröffentlichung

- **Naming-Bug:** Ein Skills-only-Paket darf keine tatsächlich manipulierten neuronalen J-Space-Aktivierungen versprechen. Deshalb wird ausdrücklich nur die *von der Forschung inspirierte Gestaltung äußerer Aufgabenreize* umgesetzt.
- **Aktivierungs-Bug:** Ein langer Forschungsanhang ohne Zugriffspunkt wird nicht wirksam. Die Auslöser stehen in den produktiven Hauptskills und im eigenen beschreibenden Skill-Metadatum.
- **Übersteuerungs-Bug:** 18 Pflichtschritte und viele Persona-Module können freie Interpretation zerstören. Deshalb sind Varianten und Komplexität dynamisch nach Material und Nutzerwunsch zu wählen.
- **Deko-Bug:** Forschungsnamen im Prompt ohne konkrete Spannung oder neue Prüffrage sind keine Anwendung. Deshalb enthalten aktive Instruktionen ein explizites Antibeispiel und eine materialgebundene Musterlösung.
- **Herkunfts-Bug:** Forschungshypothesen können die gültige Nutzerabsicht überdecken. Die neue Routine bindet sich an Originale und an nachweisbare Aufgabenresultate.
- **Eigenbestätigungs-Bug:** Ein eigener exemplarischer Text beweist noch keine Zielagentenleistung; unabhängige Vergleichsläufe bleiben Pflicht für Wirkungsbehauptungen.

Diese Prüfungen sind Designprüfungen; der tatsächliche Host-Activation-Test muss noch erfolgen.
