# Prüfe Originalzitate gegen echte Dateien, falls vorhanden

Wenn die Aufgabe **Quellentreue** oder ein adversarielles Audit verlangt und reale lokale Quelldateien zur Verfügung stehen, ist eine Gegenprüfung sinnvoll. `scripts/verify_quotes.py` kann in einem **ausdrücklich festgelegten Quellordner** genannte Zitate mit echten UTF-8-Dateien und Zeilenbereichen vergleichen; optional auch SHA256 gegen eine konkrete Dateiversion. Es liest nur die angegebenen Dateien, führt keinen externen Zugriff aus und verändert nichts.

1. Originaldateien mit dem verfügbaren Host-Werkzeug zunächst wirklich öffnen und im benötigten Umfang lesen, bevor Interpretation behauptet wird.
2. Nur für eine ausführbare Gegenprobe ein JSON mit `evidence` anlegen, pro Beleg `{id, path, start_line, end_line, quote, sha256?}`. `path` ist relativ zum genehmigten Quellordner. Nichts über den aktuellen Zugriffsstatus des Folgeagenten daraus ableiten.
3. Bei vorhandener Python-Ausführung: `python verify_quotes.py belege.json --root /tatsaechlich/freigegebener/quellordner`. Bei nicht vorhandenen Werkzeugen nicht so tun, als sei der Check erfolgt.
4. `excerpt_verified_not_reading` bedeutet **nur**, dass ein exakter Zitatabschnitt in einer lokal verfügbaren Datei existiert und ggf. die Hash-Version stimmt. Es bestätigt weder, dass ein Modell den gesamten Text gelesen hat, noch dass die spätere Interpretation stimmt.
5. Ein Zitatfehler bedeutet `contradiction`, fehlende/ungültige oder nicht erreichbare Quellen `unscorable`. Nicht beides zu einer inhaltlichen Nullbewertung vermischen.

Das Verfahren ist optional. Viele Chat- oder Cloud-Dateien lassen sich besser mit hosteigenen Quellenzitaten prüfen. Niemals einen echten Quellenbeleg künstlich durch ein leeres JSON ersetzen.
