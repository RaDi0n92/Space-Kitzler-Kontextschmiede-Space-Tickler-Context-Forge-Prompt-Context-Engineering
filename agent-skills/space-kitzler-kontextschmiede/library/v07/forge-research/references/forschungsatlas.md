# Ausführlicher Forschungsatlas für Context Forge Ultra

    Diese Übersicht ist aus den ursprünglichen Chat- und VPS-Recherchen vom 17.10.2026 rekonstruiert. Sie ist kein Nachweis, dass die hier verlinkten Quellen im aktuellen Durchlauf erneut gelesen wurden. Bei strittigen Aussagen das Original neu öffnen.

    ## Context und temporales Verstehen

    **Context Rot (Chroma)** https://www.trychroma.com/research/context-rot : Länge, ähnliche Distraktoren und Position von Information können die zuverlässige Nutzung stören. *In der Arbeit*: Leseziel nach Inhalt auswählen, relevante Passagen und Quellen zurückverlinken, am Rand liegende Details erneut ansehen. *Prüfung*: Wurde eine frühe Korrektur übergangen?

    **LongMemEval** https://proceedings.iclr.cc/paper_files/paper/2025/hash/d813d324dbf0598bbdc9c8e79740ed01-Abstract-Conference.html : sich ändernde Fakten, zeitliche Abhängigkeiten, Nichtwissen. *In der Arbeit*: Geltungsbereich, Version und offene Entscheidung getrennt dokumentieren, bei Mehrdeutigkeit nicht raten.

    **Progressive Disclosure** https://arxiv.org/abs/2607.17598 : bedarfsweises Laden, nicht verschachtelte Pfadakrobatik. *In der Arbeit*: aktiv nur relevantes Wissen, umfangreiche Originalquellen als abrufbare Leseziele. Nicht aus Dateinamen bereits Lektüre ableiten.

    **SkillJuror** https://arxiv.org/abs/2606.11543 : Aufbau beeinflusst Skillnutzung. *In der Arbeit*: klare Beschreibungen mit Auslöser und Nicht-Auslöser; Skillreferenzen werden bei passenden Entscheidungspunkten tatsächlich geladen. Erfolg nicht allein an Vorhandensein messen.

    **Evaluating AGENTS.md** https://arxiv.org/abs/2602.11988 : mehr Anleitung kann schlechtere Resultate liefern. *In der Arbeit*: umfangreiche Forschung speichern, aber keine endlosen Pflichtschritte in jedes aktive Skill pressen; gegen einfache Vergleichsvariante testen.

    **Reflection in the Dark** https://arxiv.org/abs/2603.18388 : automatisierte Promptänderungen können verschlechtern. *In der Arbeit*: echte Regressionstests, nicht nur schönere Textausgabe.

    ## Ausführung und Evaluation

    **DSPy/GEPA** https://github.com/stanfordnlp/dspy / https://arxiv.org/abs/2507.19457 : optimieren gegen konkrete Datensätze/Metriken; hier **nicht installiert oder betrieben**.

    **Promptfoo** https://github.com/promptfoo/promptfoo : Vergleich, Assertions, Attackenszenarien; im Plugin selbst kein Promptfoo-Server. Trenne Testfail von Toolfail und nicht bewertbar.

    **Claude Code Issues** https://github.com/anthropics/claude-code/issues/19471 und https://github.com/anthropics/claude-code/issues/39502 : Berichte über verlorene Anweisungen durch Kompression bzw. während einer Sitzung. Anekdotische Erfahrungen, keine repräsentativen Fehlerraten.

    ## Denkperspektiven und JSpace

    **SELF-DISCOVER** https://arxiv.org/abs/2402.03620 : Auswahl und Zusammensetzung von Denkmodulen passend zur Aufgabe. Übersetzung: dem Zielagenten Material/Denkmöglichkeiten geben, ihm aber die eigene Struktur lassen.

    **Tree of Thoughts** https://arxiv.org/abs/2305.10601 : Alternativen verfolgen und vergleichend bewerten.

    **Graph of Thoughts** https://arxiv.org/abs/2308.09687 : Alternativen dürfen wieder zusammenlaufen, rückkoppeln und einander verändern; kein direkter neuronaler Graph.

    **Coconut** https://arxiv.org/abs/2412.06769 : trainierter latenter Reasoning-Ansatz, nicht in herkömmliche Prompttexte hineininstallierbar. Gegenprüfung https://arxiv.org/abs/2512.21711 .

    **J-Space/Global Workspace** https://transformer-circuits.pub/2026/workspace/index.html : interne Repräsentationen, Jacobian-Lens-Methode; einzelne Resultate und Interpretationen umstritten. Kritische Texte https://www.lesswrong.com/posts/zFJ3ZdQwrTWE9jT5S und https://www.lesswrong.com/posts/pnDjvdo6cX2H7Ddsy ; Issue https://github.com/anthropics/jacobian-lens/issues/5 . JSpace ist kein durch Skill steuerbarer zusätzlicher Prozessor.

    **Latent Recurrent Thoughts** https://arxiv.org/abs/2609.01117 : weitere Forschungsnachbarschaft für latente zusätzliche Verarbeitung, nicht Bestandteil der Pluginarchitektur.

    ### Was mit den Studien *nicht* bewiesen ist

    Kein eingehender Beleg, dass Context Forge tieferes neuronales Reasoning freischaltet. Kein Beleg, dass viele Perspektiven automatisch mehr Einsicht bringen. Kein Beleg, dass eine lange Liste schöner Zitierungen einen wirksameren Folgeagenten erzeugt. Für all das sind echte Vergleiche nötig.
