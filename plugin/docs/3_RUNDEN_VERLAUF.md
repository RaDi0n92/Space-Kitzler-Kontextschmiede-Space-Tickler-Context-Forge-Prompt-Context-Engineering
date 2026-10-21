# Drei ausgeführte Red-Team- und Korrekturschleifen, Version 0.2.0

**Lokal geprüfte Dateien.** Kein Beleg für bessere innere Modellaktivität oder einen realen Folgeagenten-Vergleich.

## Runde 1: Quellentreue und Skills tatsächlich verankern

**Angriff gegen v0.1.0:** Forschungsbegriffe waren teils nur verlinkt; der JSON-Prüfer akzeptierte leere Register und Behauptungen ohne konkrete Lektürefundstellen. **Korrektur:** Skill-Eintrittspunkte, Quellenklassen und Ausgabeartefakte präzisiert; 33 Sokrates-Fragen und Gegenproben dokumentiert; Auditor mit Pflichtquellen-/Statuskontrolle und Wahrheitsvorbehalt versehen. Nach Integration scheiterte die ehemals gültige Fixture wegen fehlendem Lektürenachweis, dann wurde sie berichtigt. **Teststand:** 30 bestanden.

## Runde 2: feindselige Datentypen und tatsächliche Forschungswirkung

**Angriff:** 12 zusätzliche adversarielle Fälle, darunter ungültige Quell-/Entscheidungs-/Claim-IDs und freie Claim-Status. Ergebnis: vier Abstürze und ein akzeptierter Fantasie-Status. **Korrektur:** Auditor defensiv neu strukturiert, Claim-Status und Beziehungen kontrolliert, Fehler/Unbewertbarkeit getrennt und Quellen-/Forschungsreferenzen mit Auslöser, Verhaltensänderung und methodischer Grenze ergänzt. Eine Regression in einer Warnformulierung wurde sichtbar und korrigiert. **Teststand:** 42 bestanden.

## Runde 3: Statusfelder, Querverbindungen und Skill-Aktivierung

**Angriff:** 11 weitere Fälle, unter anderem Statusobjekte als Liste/Diktat, ungültige Graph-ID, falsche Cross-Skill-Referenzen und ein nur loses 33-Ideen-Dokument. Ergebnis: acht Fehler. **Korrektur:** Typensichere Enumeration-Checks, Graphreferenzen und Referenzpfade behoben; 33 Ideen tatsächlich in den Skills als bedarfsweise lesbare Referenz erreichbar gemacht und im Plugin-Audit als Arbeitsauslöser erwähnt. **Teststand:** 53 bestanden.

## Residualrisiken

- `actually_read` und `read_evidence` sind JSON-Felder, keine durch diesen Prüfer bestätigten Zugriffe. Originallektüre braucht externe Gegenprobe.
- Keine unabhängigen semantischen Agenten-A/B/C-Tests; keine gemessene kreative Leistungssteigerung.
- Repositories wurden in früheren Rechercheantworten zusammengefasst, in dieser Pluginrevision aber nicht komplett erneut ausgeführt oder extern auditiert.
- Kein Zugriff auf neuronalen JSpace. Weder das Harness noch automatische Loops sind aktiv.

Die Tests belegen kontrollierte Regeln, nicht die Wahrheit sämtlicher Aussagen oder die Wirksamkeit sämtlicher Forschungsansätze.

## Folgedurchlauf 0.3.0: Zitatbelege und unverblindete Praxissichtung

Die formalen `actually_read`-Felder aus dem alten Ledger blieben bloße Behauptungen. Deshalb ist jetzt eine separate offline lesende Quellenprobe eingebaut. Das Script prüft exakte Zitate, Zeilenbereiche und optional Dateiversions-Hashes innerhalb eines vorgegebenen Ordners; das sagt weiterhin nichts über modellinternes Lesen. 13 neue Angriffstests decken gefälschte Zitate, Versionswechsel, Dateipfad-Traversal, Symlinks, fehlende Quellen und falsch typisierte Zeilen ab. Ein veralteter Test, der genau die alte Manifestversion verlangte, wurde korrigiert.

Die unverblindete qualitative Fallstudie `docs/UNVERBLINDETE_PRAXISPROBE.md` legt einige offene Denkbrücken am vorliegenden Material offen und dokumentiert die Grenzen dieser Eigenprüfung. Eine erneute VPS-Lektüre wurde von einer Sicherheitsprüfung blockiert und nicht umgangen. **Kein unabhängiger Vergleich mit anderem Zielmodell erfolgt.**
