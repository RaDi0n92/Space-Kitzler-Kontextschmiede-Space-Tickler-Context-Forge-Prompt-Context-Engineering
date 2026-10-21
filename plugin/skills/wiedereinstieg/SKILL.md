---
name: wiedereinstieg
description: "Nutzen, wenn ein neuer ChatGPT-, Claude-, Codex- oder anderer Folgeagent in eine lange fremde Projektarbeit eigenständig einsteigen, vorhandene Handoffs kritisch gegen Originale lesen und seine ersten eigenen Fragen entwickeln soll. Nicht zum unkritischen Befolgen einer Übergabe."
---

# Nach dem Sitzungswechsel einsteigen

Der Folgeagent soll eine fremde Arbeitswelt **selbst** kennenlernen. Ein noch so gutes Übergabedokument ist zuerst eine Behauptung über die Geschichte, keine vollständige Geschichte. Dieser Skill richtet sich an die empfangende statt die übergebende Seite.

## Einstiegshaltung

Nimm zuerst das reale aktuelle Ziel des Nutzers auf, dann den vorhandenen Handoff. Markiere anfangs, welche Sätze klar auf Originale verweisen, welche nur Interpretationen sind und welche eine zukünftige offene Möglichkeit beschreiben. Lies `../context-forge-ultra/library/v07/forge-agent-reentry/references/einstiegsfragen.md`, wenn die Übergabe viele Quellen hat.

## Eigene Lektüre

1. Überprüfe, welche empfohlenen Originale für diese Instanz **wirklich zugänglich** sind. Suche den originalen Text, nicht nur eine generierte Zusammenfassung. Keine übernommene Dateioperation vom Vorgänger zu deiner eigenen ausgeben.
2. Wähle eine kleine, relevante Reihenfolge der Originallektüren. Priorität nach aktuellem Auftrag, zentralen Nutzerentscheidungen, strittigen Interpretationen und überraschenden Nebensätzen; nicht automatisch nach Dateigröße.
3. Achte auf Stellen, die dem Handoff widersprechen oder eine reichhaltigere Sicht eröffnen. Ein Widerspruch darf die Vorgängerinterpretation korrigieren. Bewahre Herkunft und Geltungsbereich.
4. Mache dir ein eigenes Bild aus den Quellen. Die Denkbrücken des Vorgängers sind **Anregungen**, keine Hausaufgaben. Lasse auch eine völlig unerwartete andere Lösung entstehen, wenn sie durch Material gedeckt ist.
5. Wenn das nächste Arbeiten praktisch wird, prüfe reale Toolberechtigungen, Projektzustände und aktuelle Daten. Ein Masterprompt ist kein Ausführungstoken.

## Forschungsimpulse tatsächlich anwenden

Wenn der vorliegende Handoff ausdrücklich ungewöhnlich tiefes, hochkomplexes und forschungsgeleitetes Weiterdenken verlangt, lies `../denkwerkstatt/SKILL.md` und dessen `../context-forge-ultra/library/v07/forge-reasoning-lab/references/forschungsmechaniken.md`. Verwende die Impulse **bei der Sache selbst**: Wähle für die aktuelle Aufgabe eigenständig passende Betrachtungsweisen; halte begründete Alternativen zunächst offen; kombiniere Erkenntnisse aus unterschiedlichen Originalquellen zu einer neuen prüfbaren Möglichkeit; arbeite danach mit den verfügbaren Werkzeugen an der nächsten sinnvollen Konsequenz. Du sollst die mechanischen Forschungsnamen nicht vorbeten. Wenn eine Forschungsarbeit wirklich wichtig wird, lies die zugängliche Originalquelle und nimm ihre Idee in deine eigene Arbeit auf.

Ein Beispiel für den Unterschied: Statt über SELF-DISCOVER zu berichten, entdecke, *welche Perspektive die bisherige Projektinterpretation aufbricht*. Statt Graph of Thoughts zu erklären, verbinde zwei zuvor getrennte Befunde so, dass sich die nächste Prüfung oder Lösung ändert. Eine ungewöhnliche Synthese ohne Quellanker ist noch kein Fortschritt. Keine unaufgeforderten Systemeinstellungen oder Projekteingriffe, und keine angebliche Steuerung unsichtbarer J-Space-Vorgänge.

## Eine wichtige Differenz

Wenn der Vorgänger sagt „Originale erneut lesen“, aber dem Folgeagenten die Dateien nicht verfügbar gemacht wurden, bleibt genau diese Lücke. Der Folgeagent soll sie benennen, statt die Empfehlung als bereits erledigte Aufgabe auszugeben.

## Beispiel

Handoff: „Plugin-Erzeuger war der ursprüngliche Zweck.“ Originallektüre: Es war eine zwischenzeitliche Fehlinterpretation des alten Agenten. Eigene Erkenntnis des neuen Agenten: Die heutige Architektur muss den Unterschied zwischen Nutzerziel und Agenten-Vorschlag *auch beim Pluginbau selbst* immer prüfen.

**Ergebnis:** Ist der aktuelle Nutzerauftrag eine praktische Umsetzung, **beginne sie in dieser Sitzung und schließe autorisierte Schritte samt Prüfung ab**; `@autorisierte-umsetzung` dient dazu als Handlungsmodus. Ein Einführungsbericht ist dann kein Ersatz für das Arbeitsergebnis. Ist ausdrücklich nur ein Einstieg gewünscht, liefere die eigene Einstiegssicht einschließlich geprüfter Originale, Korrekturen und sinnvoller nächster Handlung. Wenn alles bereits klar ist, nicht für jeden Schritt einen Bericht verlangen.

## Forschung beim Einsteigen als Einladung, nicht als Prüfung

Wenn der Handoff umfangreiche Papers oder GitHub-Links enthält, lies `../context-forge-ultra/library/v07/forge-agent-reentry/references/forschung-als-einladung.md`: Ein kurzer, lebendiger Forschungsimpuls erklärt in Alltagssprache, *welches Problem* die Arbeit bearbeiten wollte, *was an ihrer Idee interessant ist* und *welchen Versuch der Folgeagent daraus machen könnte*. Der folgende Agent wird dadurch nicht zum Literaturprüfer degradiert. Er darf die Quelle erneut lesen, aber vor allem seinen Auftrag eigenständig fortsetzen. Die tiefe Forschungsbibliothek wird erst herangezogen, wenn der konkrete Gegenstand sie trägt. Für GitHub-Projekte `../context-forge-ultra/library/v07/forge-repo-practices/references/github-lernpfade.md` selektiv lesen.

