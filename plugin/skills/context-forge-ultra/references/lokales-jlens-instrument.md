# Wirkliche lokale J-Lens-Forschung an GGUF-Modellen: optionaler instrumentierter Pfad

Das ist **keine** geheime ChatGPT-API. `igorbarshteyn/jlens-gguf` ist ein eigenständiges Forschungswerkzeug für **lokale GGUF-/llama.cpp-Modelllaufzeit**: Native-Server, Python-Numpy-Brücke und Webvisualisierung. Sein `jlens_gguf/server.py` dokumentiert unter anderem `GET /api/props`, `POST /api/slice`, `POST /api/ranks`, `POST /api/readout`, `POST /api/generate`. Eine wirklich passende Installation braucht ihre eigenen Gewichte, GGUF, ggml/llama.cpp Native-Prozesse, Python-Abhängigkeiten und gegebenenfalls Linse. Diese Komponenten **sind nicht** im Context-Forge-Paket installiert.

Bei einem **ausdrücklich beauftragten lokalen Experiment**, und nur wenn dessen Host tatsächlich erreichbar ist: README/Quickstart des Repositories mit dem aktuellen Commit selbst lesen, native Runtime prüfen, Modellidentität und Linsentyp dokumentieren, Baseline ohne Eingriff erfassen, gezielt einen einzelnen steuerbaren Parameter verändern und eine passende unbeteiligte Kontrolle laufen lassen. Starke Behauptungen über „besseres Reasoning“ benötigen robuste Wiederholungen, ähnliche Eingaben, Negativkontrollen und getrennte Bewertung der tatsächlichen Antwort. Eine Ridge-regressionsbasierte frühe J-Lens ist keine bewiesene kausale Zerlegung der gesamten Modellgedanken.

**Keinesfalls automatisch:** `native/build.sh`, `pip install`, neue Ports, Umstellen einer laufenden `llama-server`-Instanz, Modifizieren des Modellservers oder Eingriffe in Modellaktivierungen. Dazu braucht es real vorhandene Tools und Nutzerautorisierung. Ein bloßes Wort „JSpace“ im Auftrag rechtfertigt nichts davon.

## Bereits gemessene Ergebnisse in den gemeinsamen Fall aufnehmen

Für das in diesem Plugin **wirklich** vorhandene Python-Importwerkzeug muss der Anwender eine kleine, nachvollziehbare Befunddatei bereitstellen. Sie stammt aus den *echten externen Messdaten*, die ein Experimentator zuvor mit jlens-gguf erzeugt und interpretiert hat. Sie darf keine erdachten Zahlen enthalten:

```json
{
  "model": "mein-lokales-modell.gguf",
  "experiment_id": "konzept-gegenprobe-1",
  "mode": "ablate",
  "baseline": {"observed_answer": "Originalausgabe", "source": "gespeicherter realer Lauf"},
  "intervention": {"observed_answer": "Ausgabe nach realer Ablation", "layers": [4, 6]},
  "matched_control": {"observed_answer": "Kontrolllauf ohne gezielte Ablation", "source": "gespeicherter realer Lauf"}
}
```

**Nur nach realer Messung**:

```bash
python scripts/case_engine.py import-jlens --case fall.json --report lokaler-lens-befund.json
```

Das Skript prüft Mindestfelder und archiviert den **unverifiziert übernommenen** Berichtshash mit Modellname, Baseline, Intervention und Kontrollbedingung. Es berechnet **keine** Aktivierungen. Es überprüft nicht, ob die genannten Native-Läufe tatsächlich stattgefunden haben. Der Status lautet `externally_reported_not_independently_confirmed`. Der Folgeagent darf solche Befunde als Anregung für eine **prüfbare Hypothese** mitführen, nicht als J-Space-Beweis von ChatGPT ausgeben. Nur eine tatsächlich zugängliche und reproduzierbare Messumgebung könnte dies weiter erhärten.

Bei reinen Text-/Handoff-Aufträgen bringt dieser Pfad **keinen** Nutzen und bleibt unangetastet. Forschung ist hier optional als echte Datenquelle, nicht als rhetorische Pflichtstation eingebaut.


## Konkreter optionaler Leseadapter (neu in 0.8.0)

Nur wenn auf dem **gleichen berechtigten Host** bereits eine jlens-gguf-Bridge
läuft und der Nutzer deren Nutzung beauftragt hat:

```bash
python scripts/jlens_local.py --url http://127.0.0.1:8090 props
python scripts/jlens_local.py --url http://127.0.0.1:8090 readout --ctx-id EXISTING_ID --pos 0 --layer 0 --top-n 10
```

Der Adapter spricht tatsächlich die in `jlens_gguf/server.py` veröffentlichten
Endpunkte an, akzeptiert ausschließlich Loopback und folgt keinen Redirects.
Er kann eine Auswertung eines bereits existierenden lokalen Kontexts holen,
aber er baut weder native Server noch führt er Steering/Ablation aus. Die
Schnittstelle erzeugt **keine** intern beobachtbaren ChatGPT-Aktivierungen.
Ein numerischer J-Lens-Befund ist ohne ordentlichen Vergleich kein
Kausalnachweis. Für Baseline, Intervention und Kontrollbedingung weiterhin
`case_engine.py import-jlens` mit ehrlich deklarierten Originalwerten benutzen.
