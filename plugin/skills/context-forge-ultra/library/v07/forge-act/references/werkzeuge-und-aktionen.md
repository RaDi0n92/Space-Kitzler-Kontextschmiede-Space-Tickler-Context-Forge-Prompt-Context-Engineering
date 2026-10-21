# Praktisch arbeiten, ohne mehr Rechte zu behaupten

**Leseanlass:** Ein Auftrag erfordert konkrete, überprüfbare Dateiänderungen oder eine wiederholbare Bearbeitungsfolge.

1. Lies die Zielstellen tatsächlich. Arbeite mit Host-Tools, die in dieser Ausführung vorhanden sind; dieses Plugin gewährt keine zusätzlichen Berechtigungen.
2. Notiere deine erwartete Veränderung und eine passende Gegenprüfung. Bei Konflikten mit bestehenden Vorgaben nicht eigenmächtig umdeuten.
3. Führe die autorisierten Handlungen unmittelbar aus. Bei einzelnen Patches ist ein vorhandenes Host-Patchwerkzeug meist einfacher als das optionale Python-Programm. Für präzise wiederholbare Textmutationen kann `scripts/forge_apply.py` die operative Arbeit maschinell absichern.
4. `forge_apply.py` erhält eine JSON-Datei mit `root`, `operations` und `checks`. Ein Plan enthält bewusst **genau eine** Dateimutationsoperation, damit ein späterer Fehler keine halbfertige Gruppe zurücklässt. Für mehrere Dateien führe mehrere verifizierte Host-Operationen aus; dieser Helfer ist keine Mehrdatei-Transaktion. Es erlaubt `write` (nur neue Dateien, nie überschreiben) und `replace` (ein vorhandener, eindeutiger alter Text plus SHA256-Vorbedingung). **Standard: Dry Run.** Nur `--apply` verändert Dateien. Vor jeder Mutation: sichere relative Pfade, vor und unmittelbar vor der Änderung geprüfte Symlink-/Quellbedingungen (keine Garantie gegen einen gleichzeitig bösartig veränderten Dateibaum), keine Symlinks, eindeutige Zielstellen, überprüfter vorheriger Hash. Führe nur solche Pläne aus, deren Wirkung vom Nutzer beauftragt ist.
5. Nach Ausführung verifiziere die tatsächlichen Datei-Inhalte und prüfe fachliche Richtigkeit selbst. Der Script-Erfolg bedeutet nicht, dass die Lösung semantisch richtig war. Berechtigungsfehler nicht mit Umwegen umgehen.

**Beispiel einer Plan-Datei:**

```json
{
  "root": "/ein/ausdruecklich/autorisiertes/arbeitsverzeichnis",
  "operations": [
    {"kind": "write", "path": "resultat.md", "content": "Tatsaechlich erarbeitetes Ergebnis\n"}
  ],
  "checks": [{"path": "resultat.md", "contains": ["erarbeitetes Ergebnis"]}]
}
```

Ausführen: `python3 forge_apply.py plan.json` zur Simulation, danach `python3 forge_apply.py plan.json --apply`. Kein Skript ersetzt die menschliche oder modellseitige Entscheidung, *was* das richtige Ergebnis ist.

Für nicht-dateibasierte Aufträge benutze die dort real vorhandenen passenden Tools, nicht dieses Programm als Universalhammer. Autonomie heißt: die geeignete nächste Handlung wählen, ausführen und prüfen, statt zu behaupten, ein Tool sei irgendwo dokumentiert.
