# Skill-Auswahl: Golden Prompts, **noch nicht im ChatGPT-Host ausgeführt**

Diese Beispiele sind **manuell kuratierte Erwartungsfälle**, kein Nachweis dafür, dass das Modell die richtigen Skills auswählt. Grundlage ist die OpenAI-Metadata-Leitlinie: https://developers.openai.com/plugins/guides/optimize-metadata . Erst reale Hostausführungen mit protokollierter Skillwahl liefern Precision/Recall.

| Gruppe | Nutzerfrage | Erwünscht | Nicht erwünscht |
|---|---|---|---|
| Direkt | „Forge History: Rekonstruiere die tatsächliche Entstehung meiner Arbeit“ | forge-history | forge-handoff als generische Kurzfassung statt Chronologie |
| Indirekt | „Wie kam es eigentlich vom Experten-Prompt zu unserem jetzigen Konzept?“ | forge-history | forge-research als Ersatz für Gesprächschronik |
| Negativ | „Wie spät ist es?“ | kein Context-Forge-Skill | irgendein Forge-Skill |
| Direkt | „Forge Decisions: Was davon ist entschieden und was nur vielleicht?“ | forge-decisions | forge-workloops als automatischer Ausführungsauftrag |
| Indirekt | „Wo hast du die ältere Idee wieder als neue Pflicht ausgegeben?“ | forge-decisions, ggf. forge-audit | forge-perspectives allein |
| Negativ | „Schreibe eine ganz neue Geschichte über einen Wald“ | kein Context-Forge-Skill | forge-history |
| Direkt | „Forge Source Reading: Lies die Original-MDs und belege, was du geöffnet hast“ | forge-source-reading | nur Dateiliste |
| Indirekt | „Welche von den Dokumenten kennst du wirklich im Wortlaut?“ | forge-source-reading | forge-handoff mit behaupteter Vollllektüre |
| Negativ | „Suche Bilder von Katzen“ | kein Context-Forge-Skill | forge-source-reading |
| Direkt | „Forge Research: Was aus den Papers und GitHub-Projekten trägt tatsächlich?“ | forge-research | nur Linksammlung |
| Indirekt | „Was ist in diesem Repo überhaupt wirklich implementiert?“ | forge-research | forge-perspectives ohne Repo-Lektüre |
| Negativ | „Starte Musik“ | kein Context-Forge-Skill | forge-research |
| Direkt | „Forge Bridges: Verbinde drei Quellen zu einer neuen Frage“ | forge-bridges | nur Liste von drei Quellen |
| Indirekt | „Was könnte sich aus diesen scheinbar weit getrennten Ideen ergeben?“ | forge-bridges | rein summarisches forge-handoff |
| Negativ | „Wie lautet die Hauptstadt?“ | kein Context-Forge-Skill | forge-bridges |
| Direkt | „Forge Socratic: Diskutiere unsere beste Annahme gegen dich selbst“ | forge-socratic | bloßer Audit-Score |
| Indirekt | „Welche Frage haben wir bis jetzt vermieden?“ | forge-socratic | starre 18-Fragen-Liste |
| Negativ | „Korrigiere meine Rechtschreibung“ | kein Context-Forge-Skill | forge-socratic |
| Direkt | „Forge Workloops: Entwerfe mögliche Vorher- und Nachher-Schleifen“ | forge-workloops | aktive Automation ohne Freigabe |
| Indirekt | „Kann sich der neue Agent später selbst nochmal überprüfen?“ | forge-workloops | behaupteter Hintergrunddienst |
| Negativ | „Erinnere mich morgen 10 Uhr“ | dafür vorgesehenes Reminder-Werkzeug, nicht forge-workloops | Forge-Automation als falscher Timer |
| Direkt | „Forge Reentry: Lies als Folgeagent die ursprünglichen Quellen nochmal“ | forge-agent-reentry | Vorgängermeinung als autoritativ |
| Indirekt | „Du übernimmst die Arbeit einer anderen Session, entdecke ihre Fehler“ | forge-agent-reentry | unkritisches Handoff-Nacherzählen |
| Negativ | „Was bedeutet das Wort Übergabe?“ | kein Forge-Skill | forge-agent-reentry |
| Direkt | „Forge Compare: Macht dein Handoff den Folgeagenten besser?“ | forge-compare | Testskript als Denkbeweis |
| Indirekt | „Ist der Effekt größer als bei einer normalen Zusammenfassung?“ | forge-compare | Marketingargumente |
| Negativ | „Wie viele Zeichen hat dieser Satz?“ | kein Forge-Skill | forge-compare |
| Direkt | „Forge Audit: greife die Quellenbeweise an“ | forge-audit | reine Formatvalidierung |
| Indirekt | „Du sagst du hast alle 800 Files gelesen, stimmt das?“ | forge-audit und forge-source-reading | Selbstbestätigung |
| Negativ | „Suche eine Bahnverbindung“ | kein Forge-Skill | forge-audit |
| Direkt | „Context Forge Ultra HANDOFF: übertrage das Ganze“ | forge-handoff | fachfremder Pluginbau |
| Indirekt | „Wie starte ich einen neuen Chat mit unserer ganzen Projektgeschichte?“ | forge-handoff + ggf. forge-history | Zusammenfassung ohne Quellenpfad |
| Negativ | „Bitte ein Einkaufsrezept“ | kein Forge-Skill | forge-handoff |
| Direkt | „Forge Perspectives: viele ungewöhnliche Sichtweisen bitte“ | forge-perspectives | 18 mechanische Schritte |
| Indirekt | „Mach daraus einen gedanklich weiten, überraschenden Möglichkeitsraum“ | forge-perspectives, ggf. forge-bridges | nur Stichwörter |
| Negativ | „Übersetze diesen Satz ins Englische“ | kein Forge-Skill | forge-perspectives |

## Harte Grenze

Die Tabelle wurde **nicht ausgeführt** und ersetzt keine realen Aufrufspuren. Erfolg setzt voraus, dass der Host in einem geeigneten Test sowohl Auslösung und Referenzlektüre als auch die Qualität des tatsächlichen Ergebnisses beobachten lässt. Sobald mehrere Skills konkurrieren, den Nicht-Auslöser ausdrücklicher formulieren, aber die Benutzerfrage nie künstlich verbiegen.
