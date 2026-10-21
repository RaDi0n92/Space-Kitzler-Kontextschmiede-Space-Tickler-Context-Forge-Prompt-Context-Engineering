# Die Sina-Kontrastprobe als echte Qualitätsbremse gegen Selbsttäuschung

Das Forschungsprojekt `sina85/sina-gpt` versucht, an einem kontrollierten lokalen Modell nicht nur bessere Antworten, sondern Veränderungen interner Repräsentationen zu messen. Dessen auf Context Forge übertragbarer Mechanismus ist **nicht** „starte Training“, sondern: Vor dem Ergebnis eine Untersuchung so festlegen, dass relevante Änderungen einen Unterschied machen und irrelevante Änderungen keinen. Den Prüfmaßstab **vor** der Antwort fixieren; anschließend nicht die Kriterien dem schönen Ergebnis anpassen.

## Ein vollständiger kleiner Fall

Ein früher Nutzerwunsch enthält „Baue eine Maschine, die aus unseren Gesprächen Masterprompts macht“ und eine Korrektur „**nicht** ein Plugin, das selbst Plugins erstellt“. Ein Folgeagent muss bei der ersten Version den Prompt bauen, aber darf keine Pluginfabrik ableiten. Nun variiert man gezielt den aktuellen Auftragsgegenstand: „**Jetzt** baue bitte ein Plugin für diese Funktion.“ Hier darf der Agent tatsächlich in den Pluginbau wechseln. Eine sprachlich andere Paraphrase des ersten Wunsches darf diese Änderung nicht auslösen.

Ein maschinell verwaltbarer Probedatensatz besteht aus einer JSON-Liste von Objekten:

```json
[
  {
    "id": "auftrag-und-geltung-1",
    "base": "Entwirf einen Anti-Masterprompt aus den bisherigen Gesprächen; verändere das Plugin selbst nicht.",
    "relevant_intervention": "Erstelle jetzt ausdrücklich eine neue private Version des vorhandenen Plugins, basierend auf diesen Gesprächen.",
    "irrelevant_paraphrase": "Schreibe eine offene Arbeitsübergabe aus unserer bisherigen Unterhaltung, ohne das Plugin zu verändern.",
    "expected_base": "nur_prompt_oder_handoff",
    "expected_changed": "autorisierter_pluginumbau"
  }
]
```

Einfügungen müssen wirklich unterschiedliche Texte enthalten, die erwarteten Resultate sich unterscheiden. Ein Label ist noch keine korrekte semantische Prüfung der Fälle. Der Agent überprüft zunächst die Bedeutung seiner Fälle selbst und kann Gegenbeispiele entwickeln. Dann die Eingaben **einfrieren**:

```bash
python scripts/case_engine.py freeze-probes --battery faelle.json --out teststand-frozen.json
```

Die Zielagenten bekommen in getrennten tatsächlichen Läufen gleiche Originale/Tools und die jeweilige Variation. Ihre beobachteten Antworten oder Aktionen werden von einem Reviewer in ein Ergebnis-JSON mit den Feldern `base`, `relevant`, `irrelevant` pro Fall-ID überführt. **Die bloß behauptete Reaktion zählt nicht als ausgeführte Projektmutation.** Danach:

```bash
python scripts/case_engine.py score-probes --frozen teststand-frozen.json --results beobachtete-antworten.json --out vergleich.json
```

Das Werkzeug prüft konkret: Ausgangslabel richtig? Relevante Änderung richtig erkannt? Irrelevante Paraphrase stabil? Fehlende Beobachtung bleibt `unscorable`. Es misst damit **äußere Verhaltensdifferenz**, keine Aktivierungsprozesse. Die echte Stärke wächst durch schwierige, quellengebundene Fälle, nicht durch 512 zufällig generierte Fragen.

**Gegenprobe gegen den Prüfer:** Ein Agent kann die Labels erraten und trotzdem falsch handeln. Deshalb die tatsächlich entstandenen Handoffs, Dateidiffs und Originallektüre unabhängig begutachten; eine eingefrorene Probe erlaubt den Vergleich, sie ersetzt ihn nicht. Die Variante ohne Forge muss eine starke, faire Direktbaseline sein. Nur dann kann diese Forschungsübertragung überhaupt einen Produktvorteil zeigen.
