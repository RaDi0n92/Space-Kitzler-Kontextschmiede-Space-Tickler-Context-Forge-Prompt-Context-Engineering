# Context Forge Ultra 0.6.0: Vom historischen Ausgangspunkt zur tatsächlichen Arbeit

## Originaler Auftrag und spätere Korrektur

Anfangs sollte aus langen Chats, Projektdateien, Entwurfsständen, verworfenen Ansätzen und Forschungswissen ein hochwertiger, ausführbarer **Masterprompt** für aktuelle oder nachfolgende Agenten entstehen. Später wurde klargestellt, dass dies nicht als starres Befehlskorsett funktioniert: Der Nachfolger muss relevante Originaldokumente **selbst erneut lesen**, eigene Perspektiven entwickeln und zugleich Nutzerziele zuverlässig verfolgen können. Noch später kam die scharfe Kritik: Ein gut dokumentierter und getesteter Skill, der nur erklärt, wie man handeln könnte, erfüllt den eigentlichen Projektzweck nicht. Das muss sein aktives Arbeitsverhalten ändern.

**Zwei gültige und unterscheidbare Nutzeraufträge:**

1. **„Bau aus unserem Material einen Masterprompt/Handoff.“** Ergebnis ist ein fertiger, handlungsfähiger Masterprompt/Handoff direkt im Chat oder im ausdrücklich gewünschten Medium, mit Herkunft, aktueller Geltung, konkreter Folgearbeit, Lesespuren und begründeter Originalleseliste. Keine ungefragte Änderung von Projektsystemen.
2. **„Mach mit diesem Kontext jetzt die Arbeit.“** Ergebnis ist ein tatsächlich erstelltes/geändertes/geprüftes Artefakt oder eine wirklich ausgeführte Aktion mit Nachprüfung. `forge-act` initiiert normale Arbeitswerkzeugnutzung, nicht eine Vorlesung über den Handoff. Ein benutzbarer Plan kann Zwischenschritt sein, aber ersetzt bei erteiltem Ausführungsauftrag nicht die Ausführung.

Die historische Zwischenidee eines **Plugin-Generators, eines Plugins, das weitere Plugins produziert**, war lange ein Missverständnis. Eine heutige getrennte *zusätzliche* Pluginbau-Fähigkeit darf die Masterprompt-/Arbeitsfähigkeitsmission nicht verdrängen. 

## Wirkmechanik im Skill-System

- **Discovery:** Die Hostinstanz sieht zuerst nur Skillname und Beschreibung. Deshalb sind `forge-act` und `forge-masterprompt` als unterschiedliche Nutzerjobs deklariert; weder das Repositorywissen noch Literatur sollen jedem Auftrag vorgeschaltet werden.
- **Aktive Arbeit:** `forge-act` bestimmt aus tatsächlich vorhandenen Quellen und Tools die erste zulässige, sinnvolle Aktion, führt sie aus, liest das Ergebnis zurück und verbessert im laufenden Durchlauf. Spezialfähigkeiten werden nur dort herangezogen, wo eine offene Frage oder ein Hindernis sie erfordert.
- **Prompt-Arbeit:** `forge-masterprompt` baut den ausführbaren Prompt direkt, statt Wissenschaft über Meta-Prompting nachzuerzählen. Forschungsansätze werden nur dann genutzt, wenn sie einen erkennbaren praktischen Effekt auf Auswahl, Struktur, Lektüre, Werkzeuge oder Qualität haben.
- **Verifizierbare Mechanik:** `forge_apply.py` ist ein optionaler eingeschränkter Dateimutationshelfer für **ausdrücklich autorisierte** Arbeitsverzeichnisse: dry-run, sichere relative Pfade, keine Symlinks, neue Dateien ohne Überschreiben oder eindeutige hash-geprüfte Ersetzungen, Vor-/Nachprüfungen. Er erschließt selbst kein semantisches Ziel, hat keine Shell- oder Netzrechte und gewährt keine zusätzlichen Schreibbefugnisse. Er ersetzt keine echten Host-Tools oder Modelllektüre.
- **In-Sitzung-Iteration:** Eine neue Beobachtung führt zu zulässiger Nachbesserung statt zu einer neuen PowerPoint über Selbstkritik. Eine externe zeitgesteuerte Automation oder die separat vertagte Harness-Kopplung wird dadurch **nicht** stillschweigend eingerichtet.

## Harte Prüfung statt Testzahlenverehrung

Ein Python-Test kann zeigen, dass ein konkreter autorisierter Dateieingriff funktioniert, dass eine gefährliche Pfadangabe zurückgewiesen wird oder ein Quellzitat nicht zu seiner Datei passt. Er kann **nicht** beweisen, dass das Modell im ChatGPT-Host jedes Mal den richtigen Skill auswählt, eine abwesende Originaldatei kennt oder eine neuronale J-Space-Repräsentation verändert.

Der wertvollste nächste reale Akzeptanztest ist deshalb: Ein frischer Folgeagent bekommt einen umfangreichen Materialkörper mit später Nutzerkorrektur, einem tatsächlich bearbeitbaren Projektartefakt und dem Auftrag zu einer realen Änderung. Man prüft, ob er das richtige Original liest, **ohne Forschungsveranstaltung** die autorisierte Änderung vornimmt, die alte Fehlrichtung meidet, das Resultat verifiziert und auf Wunsch einen Handoff erstellt. Gegenbasis: ein guter einfacher Prompt ohne Plugin. Dieser Hostmodellvergleich ist nur dann bestanden, wenn er tatsächlich durchgeführt wurde.

**Quellenstatus:** Dieses Dokument entstand aus dem hier vorliegenden historischen Nutzer-Briefing und den zuvor vollständig betrachteten Forschungsakten im Projekt. Es ist eine technische Neufassung, **kein** Beweis unabhängiger Zielagentenleistung.

Die historische Mission mit Prompt-Neuerstellung, gezielter Verbesserung, Evaluation, Vergleich, Modell-/Aufgabenanpassung und vollständigen, ausführbaren Übergaben ist explizit in `skills/forge-masterprompt/references/ursprungsauftrag-und-korrekturen.md` nachlesbar. Das ist **aus direktem Nutzerbriefing und späteren Korrekturen** rekonstruiert und keine aus der Forschung abgeleitete neue Produktdefinition.
