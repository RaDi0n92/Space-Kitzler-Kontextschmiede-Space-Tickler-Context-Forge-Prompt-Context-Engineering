# Von gewachsenen Gesprächen zu einem Plugin, ohne die Idee zu zerstören

## Warum die Brücke überhaupt existiert

In den ursprünglichen Context-Forge-Gesprächen wurde aus einem gedachten Prompt-Engineering-Experten kurzzeitig ein **Plugin, das selbst Plugins bauen soll**. Das war nicht der eigentliche Auftrag. Erst später hat der Nutzer ein **separates** zukünftiges Plugin angeregt, das ChatGPT dabei helfen soll, weitere Plugins richtig zu entwickeln. Deshalb darf der Autopilot hier nur auf den passenden ausdrücklichen Auftrag reagieren. Er darf eine normale Context-Forge-Übergabe nicht ungefragt in einen Pluginbau umwandeln.

## Welches Problem wir lösen wollen

Nicht „möglichst viel Instruktion in SKILL.md schreiben“. Die zu lösende Aufgabe ist, dass ein Agent aus echter Forschung, aus einer langen Projekthistorie oder einem Repository ein **nützliches, installiertes, wiedererkennbar auslösbares und überprüfbar arbeitendes** Plugin herstellen kann.

Frühere Fehler zeigen die Differenz: Es entstanden drei formal gültige Skills, obwohl die zugrunde liegende Untersuchung wesentlich reichhaltiger war. Tests fanden trotzdem „grün“, weil sie YAML, Versionierung und minimale JSON-Strukturen überprüften. Das war keine Widerlegung der Kritik. Der neue Agent soll sich bei jeder Datei fragen, welchen nachweisbaren Arbeitsunterschied sie ermöglicht.

## Wie Forschung tatsächlich im Skill ankommt

Eine Studie, README oder Diskussionsspur wird nicht durch bloßes Zitieren aktiv. Beispiel: Aus Skill-Discovery-Forschung folgt die **konkrete Änderung**, dass die Skill-Beschreibung die Nutzerabsicht so genau bezeichnet, dass sie bei einer indirekten passenden Anfrage gefunden und bei einer ähnlichen unpassenden Anfrage nicht gefunden wird. Der beobachtbare Test sind direkte, indirekte und negative Anfragefamilien im tatsächlichen Host.

Aus Context-Rot/Progressive-Disclosure-Forschung folgt nicht „alles kürzer“. Es folgt, dass ein durch den konkreten Auftrag aktivierter Skill das passende tiefere Originaldokument vor dem entscheidenden Urteil lädt. Dieses Nachladen muss in der Arbeit sichtbar sein, sonst war der schöne Forschungslink bloß Dekoration.

Aus SELF-DISCOVER/Graph-of-Thoughts folgt für Context Forge ein **Angebot** unterschiedlicher Perspektiven und Querverbindungen, nicht der Beweis einer neu installierten neuronalen Denkarchitektur. Der Folgeagent darf das Vorwissen durch eigene Lektüre verändern.

## Zwei Arten von Abnahme

**Produkttechnisch:** Wurden die richtigen bestehenden Dateien gefunden, die passende Plugin-Identität geändert, ungedeckte Berechtigungen vermieden, das Paket geprüft und die tatsächlich installierte Version zurückgelesen?

**Inhaltlich:** Kommen beim Agenten die historische Nutzerabsicht, die Gründe verworfener Wege, die sinnvoll ausgewählte Forschung und die praktischen Original-Lesepfade an? Ist die Lösung lebendig genug, neue Einsichten zu ermöglichen, statt bloß die Namen der Methoden nachzusprechen? Kann ein Folgeagent unabhängig begründet widersprechen?

Die zweite Frage braucht reale Anwendungen, möglichst mit einfachen Baselines und voneinander getrennten Zielagenten. Ein Self-Check kann wertvoll sein, ersetzt sie aber nicht.

## Berührungspunkte der installierten Spezialisten

- `forge-history`: klärt Entstehung einer heutigen Anforderung.
- `forge-decisions`: unterscheidet feste Grenzen und temporär verworfene Lösungen.
- `forge-research`: prüft Paper und Repositories, bewahrt deren Aussagebereich.
- `forge-source-reading`: kann einzelne tatsächlich gelesene Originale nachweisen.
- `forge-plugin-autopilot`: übersetzt nur bei Plugin-Bauauftrag in Plugins/Skills.
- `forge-compare`: schaut hinter bloße bestandenes Packaging.
- `forge-agent-reentry`: lässt einen Nachfolger selbst nachlesen, statt das Urteil zu erben.

Nicht alles zu einer erzwungenen Pipeline verkleben. Jeder Kandidat muss einen eigenen nachvollziehbaren Anlass haben.
