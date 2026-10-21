"""Regression gates for the central entry and optional specialist skills."""
from __future__ import annotations
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / 'skills' / 'context-forge-ultra'
MAIN = (SKILL_ROOT / 'SKILL.md').read_text(encoding='utf-8')
MANIFEST = json.loads((ROOT / 'plugin.json').read_text(encoding='utf-8'))
COMPAT = json.loads((ROOT / '.codex-plugin' / 'plugin.json').read_text(encoding='utf-8'))


class SkillArchitecture(unittest.TestCase):
    def test_main_and_17_specialist_skills_are_registered(self):
        roots = list((ROOT / 'skills').glob('*/SKILL.md'))
        self.assertEqual(len(roots), 18)
        names = []
        for path in roots:
            text = path.read_text(encoding='utf-8')
            match = re.search(r'^name:\s*([a-z0-9-]+)\s*$', text, re.M)
            self.assertIsNotNone(match, str(path))
            names.append(match.group(1))
            if path != SKILL_ROOT / 'SKILL.md':
                self.assertEqual(path.parent.name, match.group(1))
        self.assertEqual(len(set(names)), 18)
        self.assertEqual(set(names), {'quellenlesen', 'arbeitsauftrag', 'repo-erkenntnisse', 'gegenfragen', 'denkwerkstatt', 'perspektiven', 'uebergaben-pruefen', 'space-kitzler-kontextschmiede', 'wiedereinstieg', 'denkbruecken', 'arbeitskreislauf', 'wirkungsvergleich', 'forschung', 'kontextuebergabe', 'entscheidungsstatus', 'projektgeschichte', 'autorisierte-umsetzung', 'pluginbau'})
        self.assertIn('space-kitzler-kontextschmiede', names)
        self.assertIn('name: space-kitzler-kontextschmiede', MAIN)
        self.assertIn('@space-kitzler-kontextschmiede', MAIN)
        self.assertIn('17 ergänzenden Fachskills', MAIN)
        self.assertEqual(MANIFEST['name'], 'context-forge-ultra')
        self.assertEqual(MANIFEST['version'], '0.10.0')
        self.assertEqual(MANIFEST['extensions']['com.openai']['interface']['displayName'], 'Space-Kitzler-Kontextschmiede')

    def test_main_routes_required_deep_work_without_sacrificing_instructions(self):
        self.assertGreater(len(MAIN), 4000)
        self.assertIn('references/angewandter-forschungsfall.md', MAIN)
        self.assertIn('Forschungsmechanismen müssen wirken', MAIN)
        self.assertIn('Dieser Skill ist der zentrale allgemeine Einstieg', MAIN)
        self.assertIn('17 spezialisierte Fachskills', MAIN)

    def test_specialist_archive_and_cross_skill_routes_resolve(self):
        for skill_path in (ROOT / 'skills').glob('*/SKILL.md'):
            text = skill_path.read_text(encoding='utf-8')
            for token in re.findall(r'`([^`]+)`', text):
                if token.startswith('../context-forge-ultra/library/v07/') or re.fullmatch(r'\.\./[a-z0-9-]+/SKILL\.md', token) or token.startswith('../../tests/'):
                    target = (skill_path.parent / token).resolve()
                    with self.subTest(skill=skill_path.parent.name, target=token):
                        self.assertTrue(target.is_file() or (token.endswith('/') and target.is_dir()), token)

    def test_every_reference_route_exists(self):
        refs = set(re.findall(r'`(references/[a-z0-9-]+\.md)`', MAIN))
        self.assertGreaterEqual(len(refs), 9)
        for ref in refs:
            with self.subTest(ref=ref):
                p = SKILL_ROOT / ref
                self.assertTrue(p.is_file(), ref)
                self.assertGreater(p.stat().st_size, 100)

    def test_required_script_routes_exist(self):
        tools = set(re.findall(r'`(scripts/[a-z0-9_]+\.py)`', MAIN))
        self.assertEqual(tools, {
            'scripts/case_engine.py',
            'scripts/followup_comparison.py',
            'scripts/jlens_local.py',
        'scripts/research_flow.py',
        'scripts/forge_pipeline.py',
        })
        for tool in tools:
            self.assertTrue((SKILL_ROOT / tool).is_file(), tool)

    def test_all_output_modes_present(self):
        for fragment in ('**Anti-Masterprompt:**', '**Handoff:**', '**Ausgeführte Arbeit:**'):
            self.assertIn(fragment, MAIN)

    def test_semantics_not_replaced_by_cli(self):
        for phrase in ('semantische Synthese', 'keine automatisch verfügbare ChatGPT-Funktion', 'nicht ausgeführt'):
            self.assertIn(phrase.casefold(), MAIN.casefold())

    def test_grants_do_not_claim_authentication(self):
        for phrase in ('nicht die Zustimmung einer real berechtigten Person beweisen', 'Bei fehlender Vertrauensprüfung keine Originalvollkopien'):
            self.assertIn(phrase, MAIN)

    def test_optional_model_runtime(self):
        self.assertIn('bereits laufende und autorisierte Loopback-J-Lens-Instanzen', MAIN)
        self.assertIn('weder lokale Dienste starten', MAIN)

    def test_same_case_across_outputs(self):
        self.assertIn('**denselben evidenzgebundenen Fallzustand**', MAIN)
        self.assertIn('nur die Äußerung im belegten Gegenstands- und Geltungsbereich', MAIN)

    def test_preserved_manifest_presentation(self):
        self.assertEqual(MANIFEST['name'], COMPAT['name'])
        self.assertEqual(MANIFEST['version'], COMPAT['version'])
        self.assertRegex(MANIFEST['version'], r'^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$')
        self.assertEqual(MANIFEST['extensions']['com.openai']['interface']['defaultPrompt'], COMPAT['interface']['defaultPrompt'])
        self.assertEqual(MANIFEST['extensions']['com.openai']['interface']['displayName'], COMPAT['interface']['displayName'])
        self.assertEqual(MANIFEST['extensions']['com.openai']['interface']['category'], COMPAT['interface']['category'])

    def test_reference_tables_do_not_claim_automatic_skill_invocation(self):
        self.assertIn('Lade **nur passende Details bei Bedarf**', MAIN)
        self.assertIn('Die 17 Fachskills sind optionale aktive Zugänge', MAIN)
        self.assertIn('keine 17 Pflichtroutinen', MAIN)
        self.assertIn('kein starres formular', MAIN.lower())


if __name__ == '__main__':
    unittest.main()
