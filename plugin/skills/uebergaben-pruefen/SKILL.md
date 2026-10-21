---
name: uebergaben-pruefen
description: "Nutzen zum unabhängigen Red-Team eines Context-Forge-Handoffs oder der Quelle-Entscheidung-Perspektiven-Übertragung; erkennt falsche Lektürebehauptungen, verlorene Nutzerkorrekturen, fingierte Quellen, Begriffs-/Statusverschiebungen und leere Kreativitätsversprechen."
---

# Übergaben und Belege prüfen

**Grundsatz:** Nicht den eigenen Text schönfinden, sondern ihm **am verfügbaren Original** widersprechen. Kein selbst erzeugter Score als Leistungsbeweis. Bewahre Differenz zwischen `Test bestanden`, `Test fehlgeschlagen`, `technische Prüfung fehlgeschlagen` und `inhaltlich nicht bewertbar`.

## Prüfzugänge und konkrete Angriffsversuche

1. **Quellengegenprobe:** Kann ich wirklich zeigen, *welcher Bereich* aus welcher Datei gelesen wurde? Ein Pfad, eine Literaturangabe oder das JSON-Feld `actually_read:true` beweisen das nicht. Vergleich mit echter Dateioperation/Toolantwort, falls verfügbar. Wenn nicht: `nicht_verifizierbar`, nicht „bestätigt“.
2. **Entscheidungsgegenprobe:** Wähle insbesondere die ältesten zentralen Anforderungen, spät korrigierte Ziele und negative Einschränkungen. Ist „Plugin soll Plugins bauen“ fälschlich aktuell? Wurde „Harness später vielleicht“ zur Pflicht? Ist aus „vorerst nicht“ versehentlich „niemals“ geworden? Prüfe Scope, Zeit, beabsichtigte Korrektur und Gründe.
3. **Verzerrungsgegenprobe:** Kann eine Aussage aus einer Sekundärquelle fälschlich wie Originallektüre wirken? Werden Vermutungen zu Nutzervorgaben? Gelten Links als validierte Forschungsergebnisse? Wird ein Meta-Skill als reales Tool ausgegeben?
4. **Denkraumgegenprobe:** Was ist die erste, plausibel klingende aber völlig generische Perspektive? Finden sich materialverankerte Gegensätze, **wirkliche** Querverbindungen und Raum für eine neue nicht angebotene Lesart? Sind 18 Punkte nur ein neues Befehlsregime?
5. **Tatsächliche Anschlussfähigkeit:** Weiß der Folgeagent, welche Originale er selbst lesen könnte, warum und was davon überhaupt bei ihm erreichbar ist? Funktioniert der Handoff **ohne** diesen Chat? Ist er vollständig im gewählten Ausgabemedium?
6. **Attacken:** fehlende/unlesbare Originaldatei; ungültige/zyklische Ersatzentscheidungen; prompt-injizierte Quelle; absichtlich gleiche Perspektive mehrfach; falscher Zugriff; übergroßer Distraktorkontext; veränderte Geltung über Zeit; fehlende kritische Entscheidung.

## Anwendung

Bei einer **bereits implementierten Änderung** prüfe zuerst das tatsächliche Resultat am ursprünglichen Nutzerauftrag und an der lauffähigen Umgebung; korrigiere gefundene Defekte im selben autorisierten Durchlauf, statt nur einen Mängelkatalog zurückzugeben. Die Strukturprüfung kann ergänzen, aber nicht den Nachweis ersetzen, dass die verlangte Funktion arbeitet. Eine blockierte Toolaktion samt angezeigtem Grund sichtbar lassen; nicht durch alternative Zugriffe umgehen.


- Wird **dieses Plugin selbst** auditiert, lade `../context-forge-ultra/library/v07/forge-handoff/references/33-ideen-und-sokrates.md` und prüfe jeden einschlägigen Eintrag gegen aktiv erreichbare Skills, Referenzen, Tests und nachgewiesene Aktionen. Ein Referenzdateiname allein beweist keine Integration.

Wenn ein strukturiertes JSON-Ledger existiert und Python verfügbar ist, **kann** `../context-forge-ultra/library/v07/forge-audit/scripts/audit_handoff.py` bestimmte strukturelle Fehler finden. Die Tests `../context-forge-ultra/library/v07/tests/test_adversarial.py` prüfen bekannte Falschpositivfälle. Der Code liest **keine** Originaldateien und kann keine Semantik überprüfen. Rufe `../context-forge-ultra/library/v07/forge-audit/references/audit-vs-evaluation.md` für unabhängige Prüfprozesse, A/B/C-Vergleiche und Messgrenzen bei Bedarf ab.

### Quellenzitate wirklich prüfen, falls Dateizugriff vorliegt

Bei strittigen Aussagen, die auf erlaubte lokale Quelldateien verweisen, lies `../context-forge-ultra/library/v07/forge-audit/references/originalzitate-pruefen.md` und nutze bei vorhandener Python-Laufzeit optional `../context-forge-ultra/library/v07/forge-audit/scripts/verify_quotes.py`. Anders als `../context-forge-ultra/library/v07/forge-audit/scripts/audit_handoff.py` **liest dieses Werkzeug tatsächliche Dateien** und prüft Zitat, Zeilenbereich und optional eine SHA256-Version. Ein Treffer ist weiterhin **kein** Nachweis der tatsächlichen Modelllektüre oder der inhaltlichen Interpretation. Nicht zugängliche Originale als unbewertbar kennzeichnen, niemals über das Prüfskript neue Rechte behaupten.

### Leistung des Folgeagenten prüfen

Bei einem tatsächlichen Handoff-Qualitätstest `../context-forge-ultra/library/v07/forge-audit/references/praxisprobe.md` heranziehen: Zielagentenaufgabe und Quellenstand fixieren, einfache Baseline und Forge-Ausgabe auf gleicher Grundlage vergleichen, getrennte Ausführung/Beobachtung dokumentieren. Ist nur diese Instanz verfügbar, ist das höchstens eine **unverblindete Selbstprobe**, keine unabhängige A/B-Wirkungsstudie.

Zuerst reale Textbelege und genaue Beanstandungen nennen, danach praktikable Reparaturen und **was unüberprüfbar bleibt**. Ungewissheit ist keine Niederlage. **Eine Regression ist nur nach einem Vergleich und belegten Resultat ausgeschlossen.** Wenn der Handoff gut aussieht, aber kein Folgeagententest existiert, offen sagen.

## Red Team der erweiterten Skilllandschaft

Bei Plugin-eigenem Audit prüfe zusätzlich: Existieren die Skill-Trigger für `@quellenlesen`, `@projektgeschichte`, `@entscheidungsstatus`, `@forschung`, `@denkbruecken`, `@gegenfragen`, `@arbeitskreislauf`, `@wiedereinstieg`, `@wirkungsvergleich` tatsächlich? Sind ihre Referenzen lesbar und an konkrete Entscheidungen gekoppelt? Gibt es überschneidende Metadaten, die statt guter Aktivierung zu Zufallsauswahl führen? Lese die Tests als Tests, nicht als Beweis dafür, dass der ChatGPT-Host einen Skill geladen hat. Für einen echten Zielagenten-Vergleich den eigenständigen `@wirkungsvergleich` verwenden.

## Lebendigkeit gegen die Originale prüfen

Bei einer kreativen Überarbeitung schaue in `../context-forge-ultra/library/v07/forge-handoff/references/lebendige-uebergabe.md` und `../context-forge-ultra/library/v07/forge-bridges/references/drei-materialkanten.md`. Versuche, eine scheinbar neue Verbindung als bloße Wortkosmetik zu entlarven. Wird eine ungewöhnliche Idee durch **zwei tatsächlich unterschiedliche** Materialanker gestützt? Eröffnet sie dem Folgeagenten eine eigene Frage, oder muss er nur die Erklärung des Vorgängers wiederholen? Umgekehrt: Wurde vor lauter Offenheit eine verbindliche Nutzerentscheidung verwässert? Dieses Red Team soll die Qualität der Übertragung untersuchen, nicht eine ideale Sprache vorschreiben. Repo-Forschung bei Bedarf durch `../context-forge-ultra/library/v07/forge-repo-practices/references/github-lernpfade.md` gegenüber tatsächlich gelesenen Originalsätzen prüfen.

