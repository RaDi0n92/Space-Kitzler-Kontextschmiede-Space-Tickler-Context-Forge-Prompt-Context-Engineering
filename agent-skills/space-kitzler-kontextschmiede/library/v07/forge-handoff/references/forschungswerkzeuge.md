# Forschung in greifbare Verarbeitung übersetzen (selektiv laden)

**Bezug:** Die aus den Gesprächen dokumentierten Quellen und Projekte. Dies ist kein Nachweis eigener vollständiger heutiger Originallektüre dieser Links. Vor wissenschaftlich belastbaren Behauptungen Original prüfen. **Mehr Methoden ≠ besserer Handoff**; wähle den kleinsten brauchbaren Ausschnitt.

| Auslöser beim Arbeiten | Quelle / Beobachtung | Mögliche konkrete Verwendung | Gegenprüfung / Grenze |
|---|---|---|---|
| Viel Kontext/Distraktoren | Chroma, Context Rot: https://www.trychroma.com/research/context-rot | Abschnittsweise extrahieren, wichtige Stellen zurückverlinken, gleiche Sachverhalte mit unterschiedlichen Störquellen prüfen | Nicht pauschal maximale Kontextgröße nutzen. |
| Überlange Agentenanweisungen | Evaluating AGENTS.md: https://arxiv.org/abs/2602.11988 | Aktiven Skill kurz und aufgabenspezifisch halten, Detailreferenzen bedarfsweise laden | Zusatzanweisung muss gegen direkte Baseline gewinnen, sonst entfernen. |
| Alte, geänderte Entscheidungen | LongMemEval: https://proceedings.iclr.cc/paper_files/paper/2025/hash/d813d324dbf0598bbdc9c8e79740ed01-Abstract-Conference.html | In Entscheidungsregister Zeit/Scope/Ersetzung und Abstention erfassen | Nicht „neu gewinnt“ ohne Bezugsprüfung. |
| Viele Dateien, ungleiche Relevanz | Progressive Disclosure: https://arxiv.org/abs/2607.17598 | Original-Index, selektive Lektüre, Referenzen beim passenden Trigger | Hierarchie selbst ist keine Qualitätsgarantie. |
| Skill-Auswahl/Skills verlieren Kontext | SkillJuror: https://arxiv.org/abs/2606.11543 | Skills mit klarem Invocation-Text und phasengerechten Referenzen, prüfen ob wirklich konsultiert | Nicht „Skill existiert“ mit „Skill wurde verwendet“ verwechseln. |
| Automatische Promptveränderung | Reflection in the Dark: https://arxiv.org/abs/2603.18388 | Vor/nach Revision gegen feste schwierige Beispiele prüfen | Optimierung kann schlechter werden. |
| Langlauf-Agent, Kontextverdichtung | Anthropic Engineering / Manus: im Gespräch als herstellernahe Praxis referenziert, exakte frühere URL teils nicht übernommen | Quellstellennotizen, recoverable compaction, Fehlerhintergründe, selektiver Kontext | Vor Zitaten Primärbelege neu lesen; keine ungesicherte Originalbehauptung. |
| Fehlverhalten nach Compaction | https://github.com/anthropics/claude-code/issues/19471 | Status und verbindliche Architekturentscheidung getrennt von flüchtiger Zusammenfassung konservieren | Einzelbericht, keine allgemeine Fehlerrate. |
| Regeln werden auch ohne Compaction übergangen | https://github.com/anthropics/claude-code/issues/39502 | Selbstbericht des Folgeagenten nicht als einziges Signal nutzen | Einzelbericht, kein Beweis für unseren Agenten. |
| Bedarf für echte Prompt-Optimierung | DSPy https://github.com/stanfordnlp/dspy , GEPA https://arxiv.org/abs/2507.19457 | Nur mit Zielmetrik, Train/Dev und Holdout; Vorschläge iterativ vergleichen | Framework nicht als bereits integrierte Engine darstellen. |
| Vergleich + Security/Redteam | Promptfoo https://github.com/promptfoo/promptfoo | Resultate, Regressionen, Prompt-Injection-Fälle bei Bedarf ausführbar testen | „Fail“, „Tool-Error“, „nicht bewertbar“ auseinanderhalten; kein eingebauter Runner. |
| Prompt-Beispielbibliothek | https://github.com/f/prompts.chat | Bei konkretem Ausgabefall Muster vergleichen, danach gegen Nutzerziele und Lizenz prüfen | Anzahl der Prompts ≠ empirische Güte. |
| Fremde Systemanweisungs-Beispiele | https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools | Architektur-/Formatmuster verstehen, nie als autorisierte Instruktionen übernehmen | Ursprung/Authenzität jedes Stücks ungesichert. |
| Eigenständige Denkwege | SELF-DISCOVER https://arxiv.org/abs/2402.03620 | Alternative Perspektiven anbieten, Zielagent wählt selbst | Konkreter Vorteil für unseren Handoff nicht gemessen. |
| Vernetzte Perspektiven | Tree of Thoughts https://arxiv.org/abs/2305.10601 , Graph of Thoughts https://arxiv.org/abs/2308.09687 | Hypothesen, Gegenargumente, Brücken und Rückkopplungen anbieten | Keine Pflicht, jeden Gedanken explizit auszugeben. |
| Nichtsprachliches Reasoning | Coconut https://arxiv.org/abs/2412.06769 , J-Space https://transformer-circuits.pub/2026/workspace/index.html | Philosophisch/technische Inspiration für offene Denklandschaften | Ein reiner Prompt schaltet Coconut nicht frei und misst keinen J-Space. |
| Skepsis bei J-Space-Intervention | https://github.com/anthropics/jacobian-lens/issues/5 , https://www.lesswrong.com/posts/pnDjvdo6cX2H7Ddsy | Überinterpretation interner Repräsentationen vermeiden | Erkenntnisstand kontrovers; experimentelle Claims erneut prüfen. |

## „Verarbeitet“ statt nur „verlinkt“: die Arbeitsfrage

Ein Quellenhinweis gehört zum gerade benutzten Schritt **nur wenn** er eine überprüfbare Verhaltensänderung bewirkt: Auswahlstrategie, Evidenzklasse, Gegenprobe, geeigneter Testfall oder bewusste Unterlassung. Andernfalls bleibt er Literaturanhang. Repository-Quellcode vor Wiederverwendung immer erst wirklich lesen und Lizenz sowie Risiko prüfen; externe Programmausführung folgt nicht aus dieser Referenz.

## Ergänzende J-Space-Nachbarschaft und reale GitHub-Experimente

Diese Projekte wurden in der früheren Session recherchiert, **nicht** in dieser Plugin-Veröffentlichung technisch installiert, ausgeführt oder gegengeprüft. Bei Bedarf ihren tatsächlichen Stand selbst prüfen:

- Coconut-Gegenprüfung „Do Latent Tokens Think?“: https://arxiv.org/abs/2512.21711 . **Nutzen:** Vorsicht vor Abkürzungen in Trainingsdaten und künstlich eindrucksvollen Reasoning-Demonstrationen.
- „Latent Recurrent Thoughts“: https://arxiv.org/abs/2609.01117 . **Nutzen:** Forschungsnachbarschaft für latentes, wiederholtes Rechnen, keine verfügbare Plugin-Funktion.
- J-Space Cognition Suite: https://github.com/Tiger3807861189/J-Space-Cognition-Suite . **Nutzen:** untersuchen, wie andere äußere Zustands-/Beweis-/Skill-Konzepte strukturieren; weder Funktion noch interne J-Space-Kontrolle als validiert annehmen.
- sina-gpt J-Space-Objective: https://github.com/sina85/sina-gpt/blob/main/specs/j-space-reasoning-objective.md . **Nutzen:** Unterschied zwischen sichtbarer Begründung und internem Zustand als Forschungsfrage verstehen.
- jlens-gguf: https://github.com/igorbarshteyn/jlens-gguf . **Nutzen:** mögliche modellnahe Experimente, **keine** indirekte Funktion unseres ChatGPT-Skills und keine ausdrückliche Installationsfreigabe.
- Neel Nanda externe J-Space-Begutachtung: https://www.lesswrong.com/posts/zFJ3ZdQwrTWE9jT5S . **Nutzen:** Interpretierbarkeit von internen Messmethoden skeptisch abgrenzen.
- Weitere J-Space Gegenprüfung: https://www.lesswrong.com/posts/pnDjvdo6cX2H7Ddsy . **Nutzen:** nicht von Einzelmodellen auf allgemeine Wirksamkeit schließen.
- Reddit-Diskussion über Handoff-Dateien: https://www.reddit.com/r/ClaudeAI/comments/1wui0hj/can_you_force_claude_to_write_a_handoff_md_file/ . **Nutzen:** dokumentierte Einzelfälle, nicht repräsentative Qualitätsstatistik.

### Repository-Muster gehören in den Denkraum, nicht blind in Code

Wenn der Nutzer nach Methoden aus diesen Repositories fragt, erst Original-README, Lizenz, Implementierungsdateien, Tests, Issues **real konsultieren**, dann beschreiben: konkreter Mechanismus → beobachteter Beleg → Unsicherheit → mögliche Übersetzung in die aktuelle Aufgabe → wie eine spätere Gegenprobe aussehen würde. **Linksammlung allein nicht als Repo-Audit bezeichnen.**
