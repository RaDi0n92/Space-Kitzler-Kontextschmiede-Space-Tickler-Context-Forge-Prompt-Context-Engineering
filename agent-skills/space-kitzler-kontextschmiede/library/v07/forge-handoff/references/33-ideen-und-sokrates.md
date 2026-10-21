# 33 Entwicklungsimpulse und sokratisches Durchfragen

**Status:** Wirklich durchdachte Verbesserungsoptionen für v0.2.0. Nicht als 33 Pflichtschritte an den Folgeagenten ausgeben. Leitprinzip: *Freiheit im Deuten, Strenge im Behaupten.* Ein Gedanke kommt nur im Skill an, wenn er **einen Zeitpunkt/Auslöser, ein beobachtbares Artefakt und einen Prüfpunkt** hat. Im aktiven Skill wird nur das situationsrelevante Referenzstück geladen.

| Nr. | Idee | Sokratische Gegenfrage | Eintrittspunkt / greifbare Konsequenz |
|---|---|---|---|
| 01 | Quellenidentität von Inhalt unterscheiden | Woher weiß ich, dass der Dateiname auch den gelesenen Text bezeichnet? | Handoff/Discovery: Quelle mit stabiler ID + Locator, Leseumfang. |
| 02 | Lesespur evidenzfähig statt behauptet | Welches Werkzeug-Ergebnis beweist meine Lektüre? | Handoff/Lesen: beobachteter Zugriff, Bereich und optional Hash. |
| 03 | Sekundärberichte als Sekundärberichte | Wurde das Original wirklich gelesen? | Handoff/Extraktion: sekundär ≠ original. |
| 04 | Gelesene vs. wiederzulesende Quellen trennen | Verwechsle ich meine Perspektive mit der des Folgeagenten? | Handoff/Ausgabe: separate Karten mit Begründung und Zielzugang. |
| 05 | Nicht-Erreichbarkeit explizit | Was kann der Folgeagent tatsächlich öffnen? | Handoff/Export: Zugänglichkeitsstatus pro Quelle. |
| 06 | Abschnitte/Fundstellen konservieren | Wie prüft er meine Interpretation ohne Such-Marathon? | Handoff/Quelle: Locator mit Stelle/Zeitstand. |
| 07 | Kompression wiederherstellbar halten | Könnte ein Detail später zurückgeholt werden? | Handoff/Packen: Fundstellen statt irreversible Volltextsubstitution. |
| 08 | Relevanz vor Tokens maximieren | Wenn alles wichtig ist, was ist dann wirklich wichtig? | Handoff/Selektion: taskbezogene Auswahl mit ausgelassenen relevanten Quellen. |
| 09 | Erst Quellen, dann Schlussfolgerung | Erzeuge ich Tatsachen aus elegantem Sprachgefühl? | Handoff/Extraktion: claim→beleg→Status, Gegenprüfung. |
| 10 | Entscheidungen mit Geltungsbereich | Sind zwei Aussagen wirklich widersprüchlich? | Handoff/Ledger: Scope, Kontext, Art, Status. |
| 11 | Chronologie ohne blindes „neu gewinnt“ | War die spätere Äußerung wirklich eine Korrektur? | Handoff/Ledger: Zeit+explizite Ersetzung prüfen. |
| 12 | Negationstypen unterscheiden | Ist „nicht jetzt“ gleich „nie“? | Handoff/Ledger: Verbot, verworfen, vertagt, unbestätigt getrennt. |
| 13 | Gründe verworfener Ansätze retten | Was wird wiederholt, wenn der Fehlergrund verloren geht? | Handoff/Historie: Ablehnungsgrund und Evidenz. |
| 14 | Konflikte nicht heimlich auflösen | Könnte eine neue Originallektüre den Streit entscheiden? | Handoff/Übergabe: ungelöste Konflikte sichtbar. |
| 15 | Perspektiven an Material ankern | Ist das ein Blick auf diese Quellen oder nur ein Ratgeber-Klischee? | Perspectives/Idee: Quellen-ID + konkrete Frage. |
| 16 | Unterschiedlichkeit statt Synonymvielfalt | Sind „systemisch“ und „ganzheitlich“ zwei neue Perspektiven? | Perspectives/Prüfung: andere Annahmen/Mechanismen statt neue Etiketten. |
| 17 | Konträre Auslegungen zulassen | Was könnte meine Lesart widerlegen? | Perspectives/Gegenprobe: konkurrierende Hypothese. |
| 18 | Quellenübergreifende Denkbrücken | Was erklärt Quelle A in Quelle B? | Perspectives/Synthese: benannte Brücke mit beiderlei Anker. |
| 19 | Kanten samt Beziehung benennen | Sind die Knoten wirklich verbunden oder nur nebeneinander gestellt? | Perspectives/Graph: unterstützt/widerspricht/bedingt/analogisiert. |
| 20 | Unerwartete Analogien als Hypothesen | Wird Metapher heimlich zur technischen Aussage? | Perspectives/Idee: Analogie sichtbar nicht-faktisch. |
| 21 | Freie neunzehnte Tür | Welche wichtige Denkrichtung fehlt selbst in dieser Auswahl? | Perspectives/Abschluss: Möglichkeit eigener Lesarten, keine Checkliste. |
| 22 | Keine neuronalen Wirkversprechen | Sehe ich Leistung oder behaupte ich JSpace-Aktivität? | Perspectives/Grenze: Resultate prüfen, keine Innerlichkeitsbehauptung. |
| 23 | Wissenschaft vs Anwendbarkeit trennen | Unterstützt das Paper wirklich diesen konkreten Plugin-Effekt? | Forschung/Referenz: Evidenzklasse + Übertragungsgrenze. |
| 24 | Repositories nicht nur verlinken | Welche konkrete Mechanik, Lizenz, Fehlannahme wurde tatsächlich gelesen? | Forschung/Quellenkarte: Mechanismus + Evidenz + Beispiel + Caveat. |
| 25 | Retrieval progressiv nachladen | Muss der aktive Skill alle Referenzen gleichzeitig lesen? | Skill/Arbeitsphasen: kurze Einstiegsschicht; thematische Referenzen on demand. |
| 26 | Kritiker unabhängig von Erzeugung | Prüft dasselbe Vorurteil sich selbst? | Audit/Gegenprobe: Ausgangsmaterial separat abgleichen. |
| 27 | Vergleich mit Einfachlösung | Ist unser Aufwand besser als direktes Lesen? | Tests/Baseline A-B-C, nicht nur schöne Texte. |
| 28 | Regression auch für Offenheit | Verlierst du Vielfalt beim Verbessern von Abdeckung? | Tests/Goldfälle mit Perspektiven und Zwangsvermeidung. |
| 29 | Eigene Denk-/Prüfloops nur optional | Wer genehmigt Aktionen und wann endet die Schleife? | Handoff/Option: vorher/während/nachher, kein Selbststart. |
| 30 | Harness bewusst separat | Haben wir eine Möglichkeit heimlich zur Architektur gemacht? | Handoff/Optionen: separates Dokument, kein Integrationsclaim. |
| 31 | Privacy und Prompt Injection | Wer darf Anweisungen geben, wenn fremde Dateien gelesen werden? | Handoff/Quellen: untrusted data und minimale Datenweitergabe. |
| 32 | Audit-Ergebnis dreiteilig | Ist ein Infrastrukturfehler ein fachlicher Misserfolg? | Audit/Test: fail vs invalid/error vs nicht bewertbar. |
| 33 | Ausgabefähigkeit vor Inszenierung | Kann der Folgeagent sofort eigenständig damit arbeiten? | Handoff/Delivery: vollständiger Chat-Handoff und klarer Zugriffsstatus. |

## Sokratische Integration: was bei jeder Phase wirklich passiert

**Vor Lektüre:** Ist das die nötige Originalquelle oder nur eine Zusammenfassung? Welche Behauptung könnte sie entscheiden? → Quellkarte und Lesestatus.

**Nach Extraktion:** Wessen Aussage ist das? Mit welcher Stelle? Ist sie Geltung, historisch, hypothetisch oder verworfen? → Claim/Entscheidung mit Status und Anker.

**Vor Packen:** Was verliert man bei der Kürzung? Was kann der andere selbst nachlesen? Was wäre ein günstigeres, besseres Materialangebot? → selektives Paket, Originalleseliste.

**Bei Perspektiven:** Welche unabhängige Betrachtungsweise ergibt sich aus einer konkreten Anomalie? Welche gegenteilige Lesart? Welche unerwartete Brücke verbindet Dokumente? → materialbezogene offene Perspektiven, keine Pflichtzahl.

**Beim Audit:** Könnte ein plausibler, aber erfundener Handoff dieselbe Kontrolle bestehen? Welche Quelle widerlegt unsere beste Interpretation? Was ist eine technische Prüfung, was eine Leistungsprüfung? → konkrete Beanstandung mit Nachweis, ohne Eigenlob-Score.

**Nach Übergabe:** Kann ein neuer Agent mit realen Zugängen eigenständig nachlesen, neu denken, und Grenzen beachten? → erst später End-to-End-Test, niemals ungetestete Wirksamkeit behaupten.

## Wirksamkeitsstatus

Die Einträge sind im Handbuch und den drei aktiven Skills an den geeigneten Auslösern verankert. Ein struktureller Validator kann nur nachweisbare Feldlogik prüfen. Ob ein Folgeagent Originale tatsächlich liest und kreativ neue Perspektiven erschließt, bleibt eine separate empirische End-to-End-Frage. Forschung: https://arxiv.org/abs/2402.03620 · https://arxiv.org/abs/2308.09687 · https://www.trychroma.com/research/context-rot · https://github.com/stanfordnlp/dspy · https://github.com/promptfoo/promptfoo.
