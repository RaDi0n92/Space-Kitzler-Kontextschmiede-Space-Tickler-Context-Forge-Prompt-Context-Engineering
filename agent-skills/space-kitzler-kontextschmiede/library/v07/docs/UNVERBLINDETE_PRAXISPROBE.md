# Praktische Qualitätsprobe vor einer unabhängig ausgeführten Folgeagenten-Evaluation

**Stand:** 17.10.2026. **Testart:** eine manuell aus Quellenmaterial entwickelte Handoff-Probe und anschließende kritische Gegenlektüre durch dieselbe ChatGPT-Instanz. **Keine** A/B-Studie, kein unabhängiger Folgeagenten-Test. Externe Modell-API/CLI war nicht verfügbar bzw. nicht für eine isolierte Aufgabe verbunden. Es gibt keinen gemessenen Effekt auf den neuronalen J-Space.

## Tatsächliche Ausgangsbasis

Zuvor direkt im Chat vorliegende VPS-Dokumente zum Context-Forge-Projekt: `03_Projektverstaendnis.md` (vorangehend in dieser Sitzung vollständig ausgelesen), `04_Option_Harness_Kopplung.md` und `05_Option_Automationen_Loops.md`; ferner recherchierte Punkte aus `01_Recherche_Context_Forge.md` und `02_Recherche_JSpace.md`. Das sind teilweise **bereits erstellte Gesprächsarchive** und keine Originalprotokolle aller älteren Chats. Eine erneute Tool-Lektüre ausgewählter Passagen wurde am 17.10.2026 von einer Sicherheitsprüfung blockiert; sie wurde nicht auf anderem Weg erzwungen. Der Text der früheren Toolantworten und die installierten Skills waren weiterhin vorhanden.

## Beispiel eines Context-Forge-Handoffs

**Aufgabe:** Context Forge Ultra soll aus einem langen und sich wandelnden Projektkontext einen offenen Übergabekörper für einen anderen Agenten entwickeln. Der nächste Agent soll eigenständig verstehen und weiterdenken, statt die Antwort eines Vorgängers mechanisch fortzusetzen.

**Entwicklung:** Aus einer ursprünglich allgemeinen Prompt-Engineering-Idee entstand zwischenzeitlich die Fehlinterpretation eines Plugins, das Plugins produziert. Der Nutzer korrigierte das Ziel zum Context-to-Masterprompt- beziehungsweise Handoff-Werkzeug. Später präzisierte er die entscheidende Haltung: Nicht einen mächtigen Anweisungskatalog überreichen, sondern reichhaltiges, präzises und gedanklich offenes Material, das eigene Lesarten provoziert. Die Zahl „18“ beschreibt in diesem Zusammenhang keine Regel, sondern die erwünschte Vielfalt möglicher Interpretationsräume.

**Gelernte Grenzen:** Ein Referenzlink ist keine gelesene Quelle. Eine zweiteilige Lesespur ist wichtig: Was der erste Agent wirklich gelesen hat und was ein Folgeagent bewusst selbst lesen könnte. Die Quellen-MDs sind Gesprächsarchive. Falls die ursprünglichen älteren Chats oder Originalpapers für den Zielagenten nicht zugänglich sind, darf die Übergabe diese Lücke nicht mit erfundenem Zugriff auffüllen. JSpace-/latent-reasoning-Publikationen können Ideen inspirieren, beweisen jedoch keine direkte Steuerung interner Denkzustände durch einen Plugin-Skill.

**Sinnvolle Originallektüre:** Ein Folgeagent könnte zuerst das echte Projektverständnis (`03_Projektverstaendnis.md`) selbst lesen, weil darin ausdrücklich die Nutzerkorrekturen und die Grenze zwischen Entscheidung und Anregung erläutert sind. Die Forschungstexte (`01_Recherche_Context_Forge.md` und `02_Recherche_JSpace.md`) sind danach zur Prüfung konkreter Methoden relevant, aber die referenzierten Papers/Repositories sind als eigenständige Originalquellen bei Bedarf nochmals zu prüfen. Für die ausdrücklich **separate** spätere Option wären `04_Option_Harness_Kopplung.md` und `05_Option_Automationen_Loops.md` interessant. **Zugänglichkeit in einer neuen Umgebung: unbekannt, bis dort geprüft.**

**Offene Denkbrücken:**

1. Quellenbindung und radikale Freiheit klingen zunächst gegensätzlich. Sie könnten einander gerade erst ermöglichen: Wenn Tatsachen sauber belegt sind, kann die nächste Instanz mit Hypothesen wesentlich freier umgehen, weil neue Einfälle nicht unbemerkt zu Fakten werden.
2. Die frühere Fehlinterpretation „Plugin baut Plugins“ ist nicht bloß eine historische Peinlichkeit. Sie ist ein Testfall dafür, wie leicht Systeme innerhalb derselben Wortfamilie das Ziel wechseln. Ein gutes Handoff muss neben Schlagworten die *Absicht* weitergeben.
3. Kontextreichtum steht in Spannung zur Forschung über Context Rot: Möglichst viel Material ist nicht identisch mit maximal viel Text im aktiven Prompt. Vielleicht ist deshalb die Kombination aus *ausführlicher Materialkarte*, *gezielter Originalleseliste* und *kompakten Denkbrücken* fruchtbarer als ein enzyklopädischer Masterprompt.
4. Automationen und Graph-/Harness-Rückkopplung könnten eines Tages miteinander kommunizieren, müssen aber vorerst gedanklich getrennt bleiben. Die Unterscheidung zwischen optionalem zukünftigen Kanal und sofort aktivierter Funktion ist hier selbst eine wichtige Nutzerentscheidung.
5. Ein offener Perspektivenraum könnte völlig neu gesehen werden: nicht als Methode zur Vermehrung von Denkideen, sondern als Probe, ob eine Übergabe **andere Deutungen zulässt, ohne Nutzerabsichten zu verändern**. Ob das im Zielagenten besser funktioniert als eine normale Zusammenfassung, ist unbeantwortet.

**Weiterführung:** Eigenständige Originallesung wäre ein sinnvoller Anfang, aber keine zwingende vollständige Aufgabenfolge. Ein Folgeagent darf Grenzen, Alternativen und weitere Fragen neu fassen. Er muss die vom Nutzer gesetzten Ziele und reale Berechtigungen respektieren. Ein echter Qualitätstest würde das Arbeitsresultat des Nachfolgeagenten mit einem vergleichbar ausgestatteten Baseline-Agenten kontrastieren.

## Unverblindete Gegenlektüre

**Quellen-/Zieltreue im obigen Beispiel:** Die Zielkorrektur, selbständige neue Lektüre, offene Kreativität, „18“ als Metapher, JSpace als Hypothese und Harness als Option sind ausdrücklich enthalten. Automationen werden nicht ungefragt aktiviert. Das *Warum* der frühen Fehlinterpretation erscheint. Quellenzugang beim Folgeagenten wird nicht erfunden.

**Schwächen im Beispiel:** Keine echte Überprüfung, dass ein anderer Agent die Originale öffnen kann. Keine überprüfte unabhängige Originallektüre sämtlicher älterer Chatnachrichten. Die Denkbrücken stammen aus der Interpretation eines einzelnen Modells; ob sie den Zielagenten kreativ über sich hinaus führen, ist nicht beobachtet. Es gibt keinen getrennt generierten Baseline-Handoff und keine verblindete Auswertung. Die Belege sind für narrative Abschnitte überwiegend Dokument-/Abschnittsverweise, nicht durchgehend zeilenpräzise.

**Nächste sinnvolle unabhängige Messung:** Gleicher Quellensatz, zwei Handoff-Arten, zwei getrennte Zielagentenläufe mit Vergleich der tatsächlichen Originallektüre, Entscheidungstreue, neuen belegbaren Verknüpfungen, Toolschritten und Aufgabenerfolg. Erfolg/Fehler/Unbewertbarkeit getrennt dokumentieren.
