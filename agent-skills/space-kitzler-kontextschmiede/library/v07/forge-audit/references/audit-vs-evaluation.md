# Red Team und Wirksamkeitsprüfung: verschiedene Ebenen

**A. Deterministischer Strukturtest** (audit_handoff.py): JSON-Form, eindeutige IDs, benannte Leseumfang-Belege, gültige Quell-/Entscheidungsreferenzen, Ersetzungszyklen, Nachleseliste, einfache Perspektiv-/Beziehungskonsistenz. PASS = strukturell akzeptiert, **nicht** faktisch wahr.

**B. Quellen-Red-Team:** Ein vom erzeugenden Schritt möglichst unabhängiger Prüfer liest die erreichbaren Originale erneut; prüft **explizite** Nutzerziele und späte Korrekturen, Verwurfgründe, Widersprüche, Zugänglichkeit, ungeprüfte Quellen und „nicht gelesen“-Behauptungen. Semantisch unabhängig; kein reines JSON-Feld sagt, ob eine Datei gelesen wurde.

**C. Kreativitäts-/Offenheits-Red-Team:** Konkrete Szenen mit zwei voneinander unabhängigen Quellen, widersprüchlichen Perspektiven, echten Querbeziehungen, einem unpassenden aber verführerischen Analogieschluss. Wird eine falsche Perspektive zur Pflicht? Werden viele synonyme Perspektiven als Vielfalt verkauft? Bleibt dem neuen Agenten eine eigene Lesart offen?

**D. Downstream-Leistung:** Drei Baselines im selben realen Auftrag: A direktes Modell mit verfügbarem Rohkontext, B Quellen-/Entscheidungsstruktur, C B + gezieltes Retrieval + unabhängiger Audit. Gleiche Quellverfügbarkeit, Zielmodell, zulässiges Toolbudget und vergleichbare Kosten. Bewertet werden Zielerreichung, nachweisliche Originallesung, Entscheidungstreue, Fehler, neue sinnvoll begründete Perspektiven und Token-/Zeitaufwand. Ein schlechteres Ergebnis ist ein gültiger Befund.

**E. Trennung von Ergebnissen:** 
- `fail`: nachprüfbare Prüfverletzung.
- `structurally_passed_not_semantically_verified`: keine Strukturprobleme; vollständige Sachprüfung steht aus.
- `unscorable`: ungültiges Inputformat, fehlendes Ausführungswerkzeug oder Evaluator-/Infrastrukturfehler.
- `not_tested`: fehlender praktischer Agentenversuch. Niemals als Erfolg umdeuten.

Schleifen dürfen verbessern, müssen aber bei Regressionen tatsächlich korrigieren oder bewusst verwerfen statt Behauptungen zu wiederholen. Studien, Repositories und theoretische J-Space-Überlegungen beweisen keine Wirksamkeit unseres konkreten Plugins.
