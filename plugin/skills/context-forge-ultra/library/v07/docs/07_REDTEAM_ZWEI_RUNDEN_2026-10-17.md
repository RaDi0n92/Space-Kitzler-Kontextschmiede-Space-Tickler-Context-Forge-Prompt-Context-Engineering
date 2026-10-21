# Red Team der Umsetzungsversion 0.6.0, zwei Angriffs- und Korrekturrunden

**Ausgangspunkt:** aktuell installierte Fassung 0.5.0 sowie lokaler noch unveröffentlichter 0.6.0-Entwurf. Benutzerziel stammt aus dem ausdrücklich erneut eingebrachten historischen Context-Forge-Briefing und den anschließenden Korrekturen: Prompt-Neuerstellung, -Verbesserung, -Evaluation, Masterprompt-Compilation, echte Ausführung beauftragter Arbeit, offene Folgeagenten-Interpretation, Quellenlektüre und Ergebnisprüfung. Forschungsnamen sind Mittel, nicht Ersatz für Handlung.

## Runde 1: Kann die neue Ausführung konkrete Fehler erzeugen?

**Vorher geprüft:** Der optionale Mutationshelfer akzeptierte bis zu 30 Schreib-/Ersetzoperationen und konnte sie nacheinander anwenden. Unter eingeschränkten Dateirechten zeigte ein konkreter nichtprivilegierter Dateiversuch: Erste Datei erfolgreich geschrieben, zweite scheitert mit `Permission denied`, Rückgabecode 1 und **erste Datei bleibt liegen**. Das widerspricht einer naheliegenden Erwartung atomarer Gruppen. Dies ist ein echter reproduzierter Fehler, nicht nur eine behauptete Gefährdung.

**Korrektur:** Der Helfer verlangt nun exakt eine Dateioperation pro Plan; für mehrere Dateien sind die eigentlichen Hosttools und nachweisbare Zwischenschritte vorgesehen. Eine Quellhash-Prüfung und Symlink-Prüfung werden unmittelbar vor Anwendung wiederholt; nach Anwendung wird der Dateitext zurückgelesen. README und Arbeitsreferenz erklären die Begrenzung. Der Helper behauptet weder automatische Semantic-Ausführung noch Mehrdatei-Transaktion oder Schutz gegen jede feindliche parallele Dateisystemänderung.

**Zusätzlicher Fehler:** `forge-handoff` und `forge-masterprompt` waren im Ergebnis zu ähnlich. Beide konnten die direkte Arbeit durch Meta-Prosa verzögern. Die Skills sind jetzt nach Art des tatsächlichen Nutzerergebnisses abgegrenzt: historisch lesbarer Handoff, einsatzfertiger Masterprompt, beauftragte tatsächliche Umsetzung. Wichtig: Bei kombinierten Aufträgen wird nicht erzwungen, alle Skills zu aktivieren.

**Tests:** Eigene Angriffsdatei `tests/test_redteam_operational.py`. Realer permission-basierter Gegenversuch bestätigte Teilcommit im Ausgangsskript. Nach Fix sind die Fälle bestanden. Die vorherigen drei in `cfu060_all_tests_v1.log` festgehaltenen Tests waren zum Teil brittle Text-/Versions-Erwartungen, keine drei Beweise fehlerhafter Arbeitsleistung; diese Unterscheidung bleibt dokumentiert.

## Runde 2: Unterlaufen unklare Pfade und falsche Skill-Routen die neuen Regeln?

**Vorher geprüft:** Ein absichtlich nichtkanonisches Workspace-Root mit `/child/..` wurde akzeptiert. Die Beschreibung von `forge-act` schloss reine Forschung und Handoffs aus, aber nicht explizit die normale Masterprompt-Erstellung. Ein direkter Angriffsfall mit Quelländerung **nach Planung vor dem Schreiben** wurde hingegen erfolgreich erkannt; ebenso ein nach der Planung angelegter Symlink zum anderen Verzeichnis.

**Korrektur:** Nichtkanonische Root-Pfade werden abgelehnt. In den Frontmatter-Beschreibungen stehen konkrete negative Grenzen für Masterprompt-Bau und Handoff. `forge-masterprompt` und `forge-handoff` benennen das jeweils andere Ergebnis und die zuständige Arbeitsform. Das ist eine Verbesserung für Discovery, aber **kein** bereits gemessener ChatGPT-Host-Discovery-Erfolg.

**Tests:** `tests/test_redteam_round_two_operational.py`: vier adversarielle Proben, erst zwei neue Failures, nach Korrektur alle bestanden.

## Durchlauf und Grenzen

Die Tests aus zwölf Testdateien wurden mit echten Python-Prozessen ausgeführt (nicht nur als Beispiele gelesen). **99 Testfälle bestanden**, über die Einzeltestsuiten verteilt (Ausgabe je Testdatei im Baukontext). Das prüft Python-Operationen, YAML-/Manifest-Annahmen, relevante Querverweise und adversarielle Eingaben. Die Tests enthalten weiterhin etliche statische Zeichenfolgenprüfungen; sie sind **kein** Beweis, dass ChatGPT die richtigen Skills tatsächlich zur richtigen Zeit auswählt, Forschung semantisch optimal anwendet oder ein fremder Folgeagent besser arbeitet.

### Was bewusst nicht behauptet wird

- Der Helper ist kein vollwertiger autonomer Agent, sondern ein optionales deterministisches Teilwerkzeug. Die eigentliche Kontextlektüre und Entscheidung bleiben Modell-/Werkzeugarbeit.
- Mehrere Dateien werden **nicht** atomar geändert; bei mehreren autorisierten Schritten sind Hostwerkzeuge und eigene Prüfungen notwendig.
- Die Plugin-Installation allein garantiert keine autonome Hintergrundarbeit, neuen Server, Promptfoo- oder DSPy-Betrieb oder Messbarkeit interner Modellaktivierungen.
- Ein echten unabhängigen Zielagenten-A/B-Vergleich haben diese lokalen Tests nicht ersetzt.

**Abnahmeprinzip:** Der vom Nutzer beauftragte Gegenstand, nicht die Menge an Skills oder Forschungsverweisen, entscheidet über die erste Handlung und über das Ende der Arbeit. Ein ausdrücklich beauftragter Umbau soll in der nächsten Ausführung zu einem überprüften Umbau führen; ein ausdrücklich beauftragter Handoff oder Masterprompt soll das fertige Arbeitsprodukt liefern, ohne ungefragte Mutationen.
