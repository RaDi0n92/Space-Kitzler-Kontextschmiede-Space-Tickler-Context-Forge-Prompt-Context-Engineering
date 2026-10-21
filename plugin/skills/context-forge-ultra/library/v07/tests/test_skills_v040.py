import re, json, unittest
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
EXPECTED={"forge-handoff","forge-perspectives","forge-audit","forge-source-reading","forge-history","forge-decisions","forge-research","forge-bridges","forge-socratic","forge-workloops","forge-compare","forge-agent-reentry","forge-repo-practices","forge-plugin-autopilot","forge-act","forge-masterprompt","forge-reasoning-lab"}

class ExpandedSkillTests(unittest.TestCase):
    def test_skill_inventory(self):
        real={p.parent.name for p in ROOT.glob('skills/*/SKILL.md')}
        self.assertEqual(EXPECTED,real)

    def test_metadata_descriptions_distinct(self):
        seen=set()
        for p in ROOT.glob('skills/*/SKILL.md'):
            content=p.read_text(encoding='utf-8')
            self.assertTrue(content.startswith('---\n'))
            fm=yaml.safe_load(content.split('---',2)[1])
            self.assertEqual(p.parent.name,fm['name'])
            description=fm['description']
            self.assertGreater(len(description),95)
            self.assertNotIn(description,seen)
            seen.add(description)
            self.assertLess(p.stat().st_size,1048576)

    def test_deep_references_and_enough_material(self):
        for p in ROOT.glob('skills/*/SKILL.md'):
            content=p.read_text(encoding='utf-8')
            # Original three had their own documented references; newcomers must not be stubs.
            self.assertGreater(len(content),2300,p.parent.name)
            refs=list((p.parent/'references').glob('*.md'))
            self.assertGreaterEqual(len(refs),1,p.parent.name)
            for r in refs:
                self.assertGreater(len(r.read_text(encoding='utf-8')),350,r.name)

    def test_new_local_reference_paths(self):
        for p in ROOT.glob('skills/*/SKILL.md'):
            txt=p.read_text(encoding='utf-8')
            for ref in re.findall(r'`(references/[\w.-]+\.md)`',txt):
                self.assertTrue((p.parent/ref).exists(),(p.parent.name,ref))
            for ref in re.findall(r'`(\.\./forge-[\w-]+/references/[\w.-]+\.md)`',txt):
                self.assertTrue((p.parent/ref).exists(),(p.parent.name,ref))

    def test_old_and_new_must_be_coherent(self):
        mf=json.loads((ROOT/'plugin.json').read_text(encoding='utf-8'))
        legacy=json.loads((ROOT/'.codex-plugin/plugin.json').read_text(encoding='utf-8'))
        self.assertEqual(mf['version'],legacy['version'])
        self.assertEqual(mf['name'],legacy['name'])
        self.assertEqual(mf['extensions']['com.openai']['interface']['defaultPrompt'],legacy['interface']['defaultPrompt'])
        self.assertEqual(mf['extensions']['com.openai']['interface']['displayName'],legacy['interface']['displayName'])
        self.assertLessEqual(len(mf['extensions']['com.openai']['interface']['shortDescription']),30)

    def test_no_self_proclaimed_neural_measurement(self):
        alltext='\n'.join(p.read_text(encoding='utf-8') for p in ROOT.glob('skills/*/SKILL.md'))
        self.assertIn('kein',alltext.lower())
        self.assertIn('J-Space',alltext)
        self.assertIn('Folgeagent',alltext)

    def test_golden_prompt_set_present(self):
        p=ROOT/'docs'/'SKILL_TRIGGER_PROBEN.md'
        self.assertTrue(p.exists())
        txt=p.read_text()
        for k in ['Direkt','Indirekt','Negativ','forge-history','forge-decisions','forge-agent-reentry','nicht ausgeführt']:
            self.assertIn(k,txt)

if __name__=='__main__': unittest.main()
