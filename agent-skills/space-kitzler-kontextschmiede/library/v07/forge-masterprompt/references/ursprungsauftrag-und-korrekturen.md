# Der Auftrag, der das Produkt geboren hat: Originalwünsche und ihre späteren Erweiterungen

**Leseanlass:** Context Forge selbst wird entwickelt, ein großer heterogener Gesprächsverlauf muss in einen Masterprompt übergehen, ein alter Prompt wird gegen die gewachsene Nutzerabsicht geprüft, oder ein neuer Agent droht das Produkt als Forschungsarchiv / Plugin-Generator zu missverstehen. Für fremde Projekte ist *deren eigene* Nutzerhistorie vorrangig; diese Akte darf niemals unbemerkt deren Wünsche ersetzen.

**Quellenstatus:** Aus dem vom Nutzer ausdrücklich erneut in die Sitzung eingebrachten historischen Handoff-Dossier und seinen anschließenden direkten Korrekturen vom 17. Oktober 2026. Das Dossier berichtet frühere Phasen zum Teil aus zweiter Hand; in dieser Sitzung neu ausgesprochenen Anforderungen kommt unmittelbare Geltung zu. Die ursprünglich nicht übergebenen Chats sind nicht nachträglich als gelesen auszugeben. Das Dokument ist ein Erkenntnispfad, keine künstlich beschlossene Architektur.

## Der erste Wunsch, den wir wieder und wieder verloren

Der Nutzer wollte zunächst das Können eines spezialisierten Prompt-Engineering-GPT als wiederverwendbare Fähigkeit: Prompts **neu erstellen**, **bestehende verbessern**, die Qualität **an nachvollziehbaren Fällen bewerten**, Varianten vergleichen und bei Bedarf für Modelle, Aufgaben, Werkzeuge und gewünschte Ausgaben passend bauen. Rollen, Beispiele, Zero-/Few-Shot, negative Anforderungen, strukturierte Ausgaben, Versionen und Tests waren mögliche Werkzeuge, nicht das Produkt an sich. Die Konfiguration des früher verwendeten GPT wurde nie belegt vollständig ausgelesen. Eine 1:1-Migration ist nicht bestätigt.

Es folgte der Wunsch, große Sammlungen auf GitHub als Muster- und Inspirationsmaterial zu nutzen. Ein Repository voller Beispiele ist jedoch weder eine importierte Datenbank noch ein Wirkungsbeweis. Entscheidend war von Anfang an, dass der Assistent diese Beispiele für eine **bessere konkrete Aufgabe** nutzen können soll.

Der frühe Fehler war, aus „Plugin Autopilot“ eine allgemeine Maschine zum Erzeugen anderer Plugins zu machen. Der Nutzer korrigierte ausdrücklich: Nicht die Fabrik ist das Ziel, sondern das bessere Prompten und Arbeiten **des Agenten selbst**. Ein später zusätzlich gewünschter Pluginbau-Einstieg darf diese historische Negativentscheidung nicht überstimmen.

Mit **Context Forge Ultra** wurde das Problem greifbar: In einem langen Gespräch wachsen Ziele, Unterlagen, Entscheidungen, Fehlversuche, Kurswechsel und Entwürfe. Ein neuer Agent soll aus dem **wirklich verfügbaren Kontext** einen **eigenständig ausführbaren Masterprompt** erhalten, der ihn zur nächsten Aufgabe befähigt. Nicht eine lieblose Zusammenfassung, nicht ein generischer Einleitungstext und auch keine Methode, die schon vor dem Lesen den Lösungsweg vorgibt.

## Der Gegenstand ist breiter als Prompttext

Bei einer solchen Übergabe sind folgende Eigenschaften aus dem frühen Auftrag zu erhalten, soweit für den konkreten Zielauftrag relevant: das tatsächliche Ziel, tragende Projektanforderungen und Hintergrundinformationen, Gesprächerkenntnisse, tatsächlich zugängliche und gelesene Dokumente, gültige und überholte Entscheidungen, technische Anforderungen und Funktionen, Grenzen und Ausschlüsse, nützliche Kompetenzen und Werkzeugzugänge, passende Arbeitsmöglichkeiten, Qualitätsanforderungen, erwartetes Ergebnis, überprüfbare Abnahme, Unsicherheit und ungelöste Datenlücken. Auch der Zweck einer verworfenen Alternative kann wesentlich sein. **Nicht** aus dieser Liste ein Zwanzig-Punkte-Pflichtformular für den Folgeagenten machen.

Der frühe Qualitätsanspruch war extrem hoch, aber inhaltlich bestimmbar: **Kontexttreue, semantische Präzision, zweckmäßige fortgeschrittene Prompttechnik, praktische Wirksamkeit, Informationsdichte, Adaptivität, Überprüfbarkeit**. „1000 % besser“ war keine gemessene Behauptung. Eine gute direkte Baseline muss bei Qualitätstests die Vergleichsgröße bleiben.

Für die praktische Prompt-Erstellung stehen **verschiedene reale Aufträge** nebeneinander: einen Prompt von Grund auf bauen, einen vorhandenen verbessern, ihn beurteilen, Varianten/Modelle vergleichen, einen großen historischen Kontext übergeben oder die im Prompt beschriebene Arbeit **jetzt tatsächlich ausführen**. Letzteres ist keine zwangsläufige Konsequenz des Ersteren. Ein ausdrücklich gewünschter Handoff autorisiert nicht das heimliche Bearbeiten des Zielprojekts; ein ausdrücklich beauftragter Eingriff darf nicht bei einem schönen Handoff enden.

## Die späteren Korrekturen haben die Aufgabe bereichert, nicht ersetzt

Zunächst war die Übergabe zu sehr eine perfekte Befehlsanweisung. Der Nutzer widersprach: Ein neues Modell soll sein eigenes Projektverständnis entwickeln können. Die Übergabe soll **einladen, öffnen, herausfordern**, vorhandene Deutungen als veränderbar zeigen, unerwartete Verbindungen ermöglichen, ohne verbindliche Fakten preiszugeben. Die fantasierte Zahl 18 war ein Bild großer Vielseitigkeit, keine Anzahl von Pflichtrollen. „JSpace“ wurde als Interesse an komplexer interner Verarbeitung diskutiert. Aus Forschungsbeschreibungen folgt nicht, dass unser Text neuronale Aktivierungen ansteuern könnte. Der praktische Gehalt bleibt: breite, verknüpfbare Anregungen statt vorweggenommener Denkfolge.

Der Nutzer verlangte ausdrücklich **zwei unterschiedliche Lesespuren**: Was hat diese Instanz wirklich, im belegbaren Umfang, gelesen? Welche konkreten **Originale** sollte der Nachfolger selbst neu lesen, aus welchem Grund und mit welcher offenen Frage? Ein bloßer Name oder eine frühere Erinnerung ist keine eigene Lektüre. Gerade die neue Originallesung soll den neuen Agenten dazu bringen können, andere Beziehungen zu sehen als der Vorgänger.

Optionale Arbeits- und Nachprüfungsschleifen wurden später eingebracht, ebenso ein **separat vertagter** möglicher Anschluss an `ProgrammHarness+ObservingController-Betriebssystemwesenwahnsinn`. Beide Möglichkeiten sollen als solche auffindbar sein; sie sind nicht automatisch eingerichtete externe Programme oder Bestandteil des verbindlichen Kerns. Eine nachvollziehbare erneute Bearbeitung **im laufenden beauftragten Durchlauf** ist hingegen ganz normale Arbeitsqualität.

Danach zeigte sich ein zweiter großer Umweg: Die Forschung über Kontext, GitHub, Prompt-Optimierung und Denkperspektiven wurde von uns in drei kurze Skills übersetzt. Es entstanden zahlreiche lokale Strukturtests und später zwölf, vierzehn Spezialisierungen. Trotzdem war der Nutzer unzufrieden, weil wir **die Forschung erklärten, anstatt sie in tatsächliches Handeln zu übersetzen**. Ein langer Abschnitt darüber, wie Quellen zu lesen wären, ist noch keine Quellenlektüre. Die Nennung von SELF-DISCOVER ist noch keine situationsgerechte neue Perspektive. Ein Audit mit vielen grünen Tests macht keinen anderen Agenten produktiver, solange ihm wirkliche Ausführungsaufträge und Erfolgskontrolle fehlen.

Der Nutzer hat die Forderung zuletzt noch klarer gemacht: **Nimm das verfügbare Material, finde einen direkt umsetzbaren nächsten Schritt, handle mit wirklichen Werkzeugen innerhalb der Befugnisse, prüfe das Ergebnis und verbessere bei Bedarf erneut.** Forschung und Dokumentation sollen als **benutztes Denk- und Arbeitsmaterial** wirken, nicht als Hauptinhalt der Antwort. Sie dürfen den Agenten fördern, ohne ihm einen Forschungsvortrag aufzudrängen.

## Was daraus bei der nächsten konkreten Arbeit wird

Ein Auftrag „Baue mir aus diesen Sitzungen einen Masterprompt“ verlangt ein fertiges, ausführbares Textprodukt. Der Assistent erschließt die wirklichen Nutzerentscheidungen, liest zugängliche Quellen, wählt aufgabengerechte Prompttechnik, schreibt den vollständigen Prompt, hinterlässt nachvollziehbare Quellen-/Wiederlesepfade und prüft wenigstens anhand der bekannten Anforderungen, dass er keine entscheidenden Ziele verdreht hat. **Kein** eigenmächtiger Eingriff in andere Projekte.

Ein Auftrag „Repariere jetzt das Plugin“ verlangt dagegen die tatsächliche Änderung am **bestehenden** Plugin, Quelllektüre, Tests, Fehlersuche, Korrektur und Rückleseprobe nach dem Installieren. Ein bloßes ZIP, ein Bericht über Forschungsmethoden oder ein Plan sind nicht die fertige Leistung. Wer an einen Hostblock stößt, benennt den blockierten Eingriff und den angegebenen Grund, ohne Umgehungsakrobatik.

Ein Auftrag „Mach meine Übergabe kreativer“ darf nicht automatisch drei neue Checklisten oder ein Forschungsseminar erzeugen. Interessanter wäre eine **wirklich materialgebundene dritte Idee**: Aus einer frühen Fehlinterpretation und einer späteren technischen Fehlentwicklung ein mögliches gemeinsames Muster entdecken, Originalstellen neu befragen und den Folgeagenten einladen, die Deutung zu korrigieren. Wenn die neue Idee die aktuellen Arbeitsergebnisse nicht verändert, ist sie im sichtbaren Handoff vielleicht Ballast.

Ein Auftrag „Prüfe die Qualität“ verlangt Vergleich gegen das Originalziel und eine ehrliche Grenze dessen, was getestet wurde. Syntax- und Dateitests können Belege oder Fehler liefern; nur reale Folgeagenten-Proben unter vergleichbaren Bedingungen können eine verbesserte Wirkung belegen.

## Was für alle Fälle als kritische Frage bleibt

**Hat der Agent das Material benutzt, um eine richtige und für den Nutzer hilfreiche Sache zu schaffen? Oder hat er nur ausführlich beschrieben, wie beeindruckend seine Methode angeblich ist?** Die Antwort bestimmt, ob noch gearbeitet werden muss. Diese Frage hat Vorrang vor Skillanzahl, Textlänge und akademischem Ton.
