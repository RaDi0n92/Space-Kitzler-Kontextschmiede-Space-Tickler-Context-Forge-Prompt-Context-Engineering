# Forschungswissen ist erst dann im Skill, wenn ein Verarbeitungsanlass es benutzt

**Stand 0.4.0.** Diese Karte ist eine Architektur- und Testhilfe, keine Behauptung, dass das Modell Referenzen tatsächlich nachgeladen hat.

| Ursprüngliche Einsicht / Material | Auslöser in realer Arbeit | Zuständiger Skill + vertiefende Referenz | Sichtbare Konsequenz oder falsifizierende Probe |
|---|---|---|---|
| Originale können durch Zusammenfassung verloren gehen | „Lies wirklich“, „belege“ | forge-source-reading / lesespuren.md | reale Lesespur statt Dateiname; Teil-Lektüre korrekt |
| Context Rot und große Distraktoren | sehr lange Materialbestände | forge-research / forschungsatlas.md; forge-source-reading | selektive relevante Passagen + wiederauffindbare Fundstellen, frühe Korrektur erhalten |
| LongMemEval und zeitlich veränderliche Aussage | mehrere Versionen einer Entscheidung | forge-history / zeitpfade.md; forge-decisions / entscheidungslandschaft.md | keine automatische Neu-gewinnt-alt-Regel |
| Negative Constraints und vertagte Ideen | „nicht jetzt“ / „nie“ / „vielleicht“ | forge-decisions / negative-grenzen.md | aktuelle Verbote nicht mit gescheiterten Varianten vermischt |
| Progressive Disclosure / SkillJuror | zu viel Forschung im Eingabefenster | forge-handoff + forge-research; Skillmetadaten | Referenz bei Trigger geladen, nicht nur verlinkt; reale Host-Überprüfung fehlt noch |
| Empirischer Zweifel an aufgeblähten Anweisungen | neuer Handoff hat enorme Länge | forge-compare / experimentdesign.md | faire direkte Baseline darf gewinnen |
| SELF-DISCOVER | Agent soll eigene Denkstruktur wählen | forge-perspectives; forge-socratic | neue alternative Deutung, nicht 18 Pflichtfelder |
| Graph of Thoughts | getrennte Quellen ergeben neue Frage | forge-bridges / brueckenwerkstatt.md | konkrete, widerlegbare Querbeziehung statt generischer Metapher |
| J-Space / Coconut / Latent Recurrent Thoughts | Benutzer fragt nach internem Denken | forge-research / forschungsatlas.md | saubere Grenzen, keine J-Space-Steuerbehauptung |
| GitHub-Systemprompt-Sammlungen | Nutzer will daraus Muster ableiten | forge-research / repositories-und-gegenbefunde.md | Code, Lizenz, README, Tests lesen, Links nicht als Benchmark ausgeben |
| Fehlversuche nach Kompression | Agentenübergabe nach langer Session | forge-history + forge-agent-reentry | zentrale frühere Korrektur aus Original selbst prüfen |
| Sokrates / kreative Offenheit | schöpferische Tiefe gefordert | forge-socratic / gegenstimmen.md + forge-bridges | Lieblingsdeutung darf fallen, neues Problemverständnis möglich |
| Vorher/Mittendrin/Nachher-Loops | Nutzer erkundet spätere wiederholte Arbeit | forge-workloops / schleifenarten.md | Option statt fingierter Hintergrundautomation |
| ProgrammHarness+ObservingController | spätere Integrationsphantasie | forge-workloops und forge-decisions | ausdrücklich separater Möglichkeitsraum, kein integrierter Controller |
| Promptfoo/GEPA/Regression | behauptete Plugin-Leistungssteigerung | forge-compare / experimentdesign.md | getrennte Qualitäts-/Toolfehler, unabhängiger Agentenvergleich erforderlich |
| Eigene Ursprungsdiskussion inkl. Friktion | Handoff aus langjähriger Arbeit | forge-handoff / grundidee-langanalyse.md | keine glattgebügelte Aufzählung; Leser kann Ursprungsmissverständnis nachvollziehen |

**Ein zentraler ungelöster Test:** Die Einträge sind **statisch verknüpft** und wurden auf ihre Existenz geprüft. Das beweist noch nicht, dass ein ChatGPT-Modell bei passender Anfrage den Skill aktiviert, die Referenz liest oder bessere originelle Gedanken entwickelt. Das muss mit tatsächlichen, beobachtbaren ChatGPT-Hostdurchläufen anhand `SKILL_TRIGGER_PROBEN.md` und separaten Folgeagenten-Aufgaben untersucht werden.
