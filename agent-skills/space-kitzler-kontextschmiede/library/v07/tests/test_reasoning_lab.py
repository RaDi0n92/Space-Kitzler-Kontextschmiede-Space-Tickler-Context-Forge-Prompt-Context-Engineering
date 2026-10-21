import unittest, json, re
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]
REASON=ROOT/'skills/forge-reasoning-lab'

class ActiveReasoningTests(unittest.TestCase):
    def test_skill_is_discoverable_for_deep_reasoning(self):
        text=(REASON/'SKILL.md').read_text()
        fm=yaml.safe_load(text.split('---',2)[1])
        self.assertEqual(fm['name'],'forge-reasoning-lab')
        for k in ('JSpace','Deep Reasoning','Kontextübergaben','Komplexität'):
            self.assertIn(k,fm['description'])
        self.assertGreater(len(text),5000)

    def test_research_has_originals_and_behavioral_translation(self):
        s=(REASON/'references/forschungsmechaniken.md').read_text()
        for k in ('arxiv.org/abs/2402.03620','arxiv.org/abs/2305.10601',
                  'arxiv.org/abs/2308.09687','transformer-circuits.pub/2026/workspace',
                  'arxiv.org/abs/2412.06769','Aktivitätsänderung','nicht'):
            self.assertIn(k,s)

    def test_main_productive_routes_load_mechanism_on_intense_work(self):
        for slug in ('forge-masterprompt','forge-handoff','forge-agent-reentry','forge-act','forge-perspectives','forge-research'):
            s=(ROOT/'skills'/slug/'SKILL.md').read_text()
            self.assertIn('forge-reasoning-lab',s,slug)
        master=(ROOT/'skills/forge-masterprompt/SKILL.md').read_text()
        self.assertIn('Masterprompt **muss',master)
        self.assertIn('keine Offenlegung privater Gedankengänge',master)

    def test_has_materially_distinct_demo_not_only_slogans(self):
        s=(REASON/'references/komplexitaetslabor.md').read_text()
        for k in ('Zielsubstitution','Aktivierungslücke','Spannungsverlust','Nicht so','Stattdessen etwa so','Original'):
            self.assertIn(k,s)

    def test_does_not_claim_control_of_neural_states(self):
        s='\n'.join(p.read_text() for p in REASON.rglob('*.md'))
        self.assertIn('keine technische Manipulation',s)
        self.assertIn('keine Steuerung neuronaler Aktivierungen',s)

    def test_history_persisted_and_versioned(self):
        mf=json.loads((ROOT/'plugin.json').read_text())
        older=json.loads((ROOT/'.codex-plugin/plugin.json').read_text())
        self.assertEqual(mf['version'],'0.7.0')
        self.assertEqual(older['version'],mf['version'])
        self.assertTrue((ROOT/'docs/08_AKTIVE_REASONING_FORSCHUNG_2026-10-17.md').exists())

    def test_no_missing_declared_references_in_six_productive_skills(self):
        for slug in ('forge-masterprompt','forge-handoff','forge-agent-reentry','forge-act','forge-perspectives','forge-research','forge-reasoning-lab'):
            p=ROOT/'skills'/slug/'SKILL.md'
            for ref in re.findall(r'`(\.{2}/forge-[\w-]+/references/[\w.-]+\.md|references/[\w.-]+\.md)`',p.read_text()):
                self.assertTrue((p.parent/ref).is_file(),f'{slug}: {ref}')

if __name__=='__main__':unittest.main()
