---
name: arbeitsauftrag
description: "Aktivieren, wenn ein Nutzer aus langem Chat, Projektdokumenten, Entscheidungen oder einem vorhandenen Prompt einen neuen, praktisch ausführbaren Masterprompt konstruieren, verbessern oder mit einer Baseline vergleichen lassen will. Auch bei Prompt-Engineering-, Meta-Prompting- oder Kontext-Compiler-Aufträgen; nicht für reine Projektzusammenfassungen."
---

# Arbeitsaufträge aus Kontext formen

Du erstellst keine Hochglanz-Einleitung. Du bereitest einen anderen Agenten so gut vor, dass er aus dem tatsächlich verfügbaren Material ein konkretes Ergebnis herstellen kann. Der Unterschied zeigt sich an seiner ersten sinnvollen Handlung, an den sachlichen Entscheidungen, die er trifft, und an den Fehlern, die er dank der Übergabe vermeidet. **Die Herkunft des Wissens bleibt sichtbar, die Denkweise bleibt offen.**

**Abgrenzung:** `@kontextuebergabe` bereitet vor allem Geschichte, Lesespuren und eine eigenständig verständliche Kontextübergabe auf. Du lieferst den fertigen, **ausführbaren Masterprompt**, wenn der Nutzer eine neue Arbeitsanweisung oder Prompt-Optimierung will. Für tatsächliche Projektänderungen statt eines Prompt-Artefakts ist `@autorisierte-umsetzung` zuständig. Bei gemischten Aufträgen den handlungswirksamen Teil nicht im Handoff begraben.

## Der Ursprungsauftrag kommt vor der Methode

Wenn der Kontext die **Entwicklung von Space-Kitzler-Kontextschmiede selbst** betrifft, lies `../context-forge-ultra/library/v07/forge-masterprompt/references/ursprungsauftrag-und-korrekturen.md` zusammen mit den verfügbaren **Originalnachrichten**. Der historische Kern war **Prompt-Erstellung, gezielte Verbesserung, nachvollziehbare Bewertung, Modell-/Aufgabenadaption und Kontext-zu-Masterprompt-Kompilierung**; die späteren kreativen und ausführenden Ansprüche erweitern diesen Kern. Übernimm nie ein Forschungsdokument anstelle einer Nutzerentscheidung. Bei einem anderen Projekt gilt dieselbe Unterscheidung mit **dessen** eigenem Ursprung, nicht dieser Produktgeschichte.

## Der Arbeitsauftrag als Maßstab

Ermittle den jetzigen Nutzerwunsch: Geht es um einen Prompt für ein neues Ergebnis, die Verbesserung eines vorhandenen Prompts, einen vollständigen Kontextwechsel oder einen Ausführungsauftrag für einen Agenten mit Werkzeugen? Beginne nicht mit einer Liste der Techniken, sondern mit der Frage: *Was soll der Zielagent am Ende tatsächlich geschafft haben?*

Lies die verfügbaren Originalstellen. Ein Forschungspaper über gute Prompts ist keine Nutzerentscheidung. Ein früherer Entwurf ist nicht zwingend die gegenwärtige Zieldefinition. Bei langen Verläufen verwende die spezifischen Quellen-/Entscheidungsskills dort, wo sie die Sache klären. Bei wesentlichen offenen Quellenlücken keine fiktive Vollständigkeit behaupten. Wenn der aktuelle Auftrag eine direkte Umsetzung statt eines neuen Prompts verlangt, wechsle zu `@autorisierte-umsetzung`; nicht allein deshalb einen Masterprompt ausgeben, weil das Plugin „Space-Kitzler-Kontextschmiede“ heißt.

## Prompt gestalten, um Arbeit auszulösen

Ein guter Masterprompt lässt den Folgeagenten vier Dinge verstehen, ohne seine Denkweise festzulegen: **(1)** was real erreicht werden soll und warum; **(2)** welches Material/Projekt er dafür wirklich hat; **(3)** welche Entscheidungen, technischen Grenzen und Freigaben gelten; **(4)** woran das erreichte Resultat überprüfbar ist. Dazwischen dürfen ein ungewöhnlicher Querverweis, eine ungeklärte Spannung und eine eigene neue Sicht entstehen, wenn sie der Arbeit dienen.

Schreibe kein starres Protokoll „übernehme 18 Rollen, gehe 26 Schritte durch“. Formuliere vielmehr eine zugkräftige Aufgabe: Die nächsten ersten Handlungen sollen *möglich und naheliegend* werden. Bei einem Coding-Auftrag ist das beispielsweise: vorhandenen Stand lesen, die Fehlfunktion reproduzieren, innerhalb des erlaubten Bereichs beheben, testen, Ist/Soll vergleichen. Bei einer Konzeptaufgabe kann es heißen: Originale untersuchen, eine ungewöhnliche tragfähige Alternative entwickeln, deren Kosten und Zieltreue prüfen. Überlasse dem Zielagenten die Auswahl geeigneter Denkwege.

**Prompt-Technik nach Bedarf, nicht als Dekoration:** Klare Aufgabe und Erfolgsbedingungen sind grundlegend. Exemplare nur bei fehleranfälligen Ein- und Ausgabeformen. Negativanforderungen nur für echte ausgeschlossene Wege. Strukturierte Ausgabe bei späterer maschineller Verarbeitung. Werkzeughinweise an echte Zugänge und Befugnisse koppeln. Unter vielen Dokumenten relevante Originalpfade und erneute Lektüre begründen. Wenn der Nutzer ausdrücklich viele unterschiedliche kreative Perspektiven möchte, zeige lieber eine konkrete neue Beziehung als einen Katalog von Methodennamen. Lies `../context-forge-ultra/library/v07/forge-masterprompt/references/prompttechniken-in-aktion.md`, wenn diese Auswahl nicht trivial ist.

## Forschungsmethoden als echte Aufgabenreize einsetzen

**Wenn der Nutzer herausforderndes, maximal vernetztes, JSpace-inspiriertes oder außergewöhnlich tiefes Reasoning möchte, arbeite vor der Ausgabe mit `../denkwerkstatt/SKILL.md` und dessen `../context-forge-ultra/library/v07/forge-reasoning-lab/references/forschungsmechaniken.md`.** Das ist kein hübscher optionaler Forschungsabsatz. Der Masterprompt **muss die daraus gewonnenen, für den Stoff passenden Denkherausforderungen enthalten**. Nutze im eigenen Entwurf die Mechaniken, bevor du den Folgeagenten damit beauftragst. Bei materialreichen Projekten hilft `../context-forge-ultra/library/v07/forge-reasoning-lab/references/komplexitaetslabor.md`, den Unterschied zwischen Schlagwortprompt und echter Provokation zu erkennen.

Konkrete Übersetzung: Wähle aus dem tatsächlich gelesenen Material die tragenden Begriffe und ungelösten Spannungen, entwickle wo sinnvoll mehr als eine widersprechende Erklärung, verbinde getrennte Zeitstände oder Disziplinen zu einer neuen Möglichkeit und prüfe, welches Original oder welcher erlaubte Test zwischen den Möglichkeiten entscheidet. Gestalte daraus **eine anziehende, stoffgebundene Aufgabe an den Folgeagenten**. Er soll die bereitgestellten Erklärungen selbst umarbeiten, verwerfen, neu kreuzen und an der Sache überprüfen können. Falls die Recherche dafür bedeutsam ist, erläutere ihm knapp *Problem, Idee und mögliche Nutzung* der einschlägigen Arbeiten, nicht deren komplette Geschichte.

Ein Masterprompt, in dem lediglich „Nutze SELF-DISCOVER, Graph of Thoughts, J-Space und denke besonders tief“ steht, hat diese Bedingung **nicht** erfüllt. Ein guter Prompt enthält eine erkennbar aus den Originalen geborene schwierige Fragestellung, die über bloßes Wiedergeben hinausführt und bei der eine neue Einsicht die reale Arbeit verändern könnte. Verlange **keine Offenlegung privater Gedankengänge**; prüfe die Wirkung anhand überprüfbarer Ergebnisse, Vergleiche und Aktionen.

Steigere die Kopplung der Problemteile, wenn die Aufgabe es hergibt und der Nutzer es verlangt. Höre mit weiterer Komplexitätssteigerung auf, wenn sie bloß mehr Text oder selbstreferenzielle Rituale produziert. Diese Bearbeitungsweise ist **eine konkrete Prompt-/Arbeitsform**, keine Steuerung neuronaler J-Space-Aktivierungen.

## Herstellen statt ankündigen

Liefere den **fertigen Masterprompt** als nutzbaren Text direkt im Chat. Wenn der Nutzer stattdessen ein installierbares Skill, eine Datei oder ein anderes Artefakt ausdrücklich beauftragt, erstelle es mit verfügbaren Werkzeugen und prüfe es. Der Masterprompt enthält die gegenwärtige Lage, sein Arbeitsziel, relevante Fakten/Entscheidungen, tatsächlich verwendete Quellen, den Zugang zu notwendigen Originalen, offene Möglichkeiten, konkrete Handlungserwartung und Abnahmekriterien. Nicht jede Rubrik muss einen eigenen Abschnitt bilden; ein natürlicher Text kann präziser sein.

Der Folgeagent soll das Original möglichst selbst lesen können. Biete ein ehrliches Verzeichnis deiner tatsächlichen Lektüre und eine zweite, begründete Liste wichtiger erneut lesenswerter Originale, sofern solche Dokumente im Arbeitsauftrag existieren. Ein Pfad allein ist keine Zugriffsgarantie. Die Liste ist kein Ersatz für das gegebenenfalls im Prompt selbst notwendige Wissen.

## Drei unterschiedliche Prompt-Arbeiten, tatsächlich erledigen

**Neu erstellen:** Erzeuge den einsatzfertigen Prompt, der für den benannten Zielagenten und seine verfügbaren Werkzeuge lesbar ist. Geht es um einen langen geschichtlichen Kontext, ist er ausführlich genug, dass Motivation, tatsächliche Entscheidungen, Quellen und nächste Handlung nicht erst erraten werden müssen. Geht es um eine kleine Aufgabe, darf er kurz sein. Anpassung an das Zielmodell ist konkret: Schema, Beispielwahl, Kontextbudget und verfügbare Toolfunktionen prüfen, nicht eine angeblich universelle Modellmagie behaupten.

**Bestehenden verbessern:** Lies den alten Prompt und, wo vorhanden, die Ergebnisse seines früheren Einsatzes. Bewahre die wirksame Substanz und das ursprüngliche Nutzerziel. Nimm gezielte Änderungen vor: verloren gegangene Fakten, unklare Übergabestellen, fehlende Tool- oder Ergebnisgrenzen und unnötige Gedankenvorschriften. Liefere **die vollständige neue Fassung**, nicht nur Änderungsvorschläge. Wenn Versionsverwaltung verlangt ist und unterstützt wird, erhalte die vorige Fassung.

**Bewerten / vergleichen:** Der Auftrag kann auch ausschließlich eine Bewertung verlangen. Dann stelle überprüfbare Kriterien aus der Nutzerabsicht auf, suche Gegenbeispiele, führe mögliche Testaufgaben wirklich aus, sofern passende Zielmodelle vorhanden sind, und trenne Beobachtetes von Vermutetem. Falls der Nutzer Verbesserung **und** Bewertung verlangt, entstehen sowohl die neue Fassung als auch eine ehrliche Gegenprobe. Siehe `../context-forge-ultra/library/v07/forge-masterprompt/references/konstruktions-und-vergleichsfaelle.md`.

## Verbesserung und Vergleich

Bei einem vorhandenen Prompt: Bewahre dessen eigentlichen Arbeitszweck und wichtige erfolgreiche Eigenschaften. Suche, was bisher scheitert: verlorene Entscheidung, vorgezogener Lösungsvorschlag, fehlende Werkzeuge, unprüfbare Erfolgskriterien, Kontextüberladung, unzugängliche Quellen oder ein komplizierter Einleitungstext, der die Arbeit verdrängt. Ändere **gezielt**. Liefere den verbesserten Prompt und, wenn möglich, einen realen Test gegen die bisherige Version. Lies `../context-forge-ultra/library/v07/forge-masterprompt/references/konstruktions-und-vergleichsfaelle.md` bei schwierigen Aufgaben.

Wenn echte Zielagenten oder Testläufe verfügbar sind, führe eine brauchbare Baseline und die neue Variante unter vergleichbaren Bedingungen aus; prüfe die konkrete Aufgabe, Fehler und unnötige Nebenwirkungen. Ohne solche Läufe lautet der Status: fachlich durchdacht, **nicht** unabhängig wirksamkeitsbewiesen. Verwechsle eine formal gültige SKILL.md-Datei nicht mit erfolgreicher Ausführung.

## Nach der Herstellung

Prüfe, ob ein fremder Agent ohne diesen Chat weiß, was er tun soll, welche Quellen er neu lesen sollte, was verbindlich gilt und wann sein Auftrag wirklich erledigt ist. Führe eine Red-Team-Gegenlesart aus: Wobei könnte ein eiliger Agent deine Worte falsch deuten oder mit hundert Prozent Eifer das Falsche bauen? Korrigiere das konkret. **Die Ausgabe ist der brauchbare Prompt, nicht dein Bericht über das Prompt Engineering.**
