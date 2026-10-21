import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class PluginTests(unittest.TestCase):
    def test_manifest(self):
        obj=json.loads((ROOT/'plugin.json').read_text())
        self.assertEqual(obj['name'],'context-forge-ultra')
        self.assertEqual(obj['$schema'],'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json')
        self.assertLessEqual(len(obj['extensions']['com.openai']['interface']['shortDescription']),30)
        self.assertEqual(len(obj['extensions']['com.openai']['interface']['defaultPrompt']),3)

    def test_skill_structure(self):
        for name in ('forge-handoff','forge-perspectives','forge-audit'):
            skill=ROOT/'skills'/name/'SKILL.md'
            data=skill.read_text(encoding='utf-8')
            self.assertTrue(data.startswith('---\n'))
            self.assertIn(f'name: {name}\n',data)
            self.assertIn('description:',data)
        self.assertIn('kein', (ROOT/'skills/forge-perspectives/SKILL.md').read_text().lower())

    def test_structural_audit_valid(self):
        script=ROOT/'skills/forge-audit/scripts/audit_handoff.py'
        fixture=ROOT/'skills/forge-audit/fixtures/valid.json'
        r=subprocess.run([sys.executable,str(script),str(fixture)],capture_output=True,text=True)
        self.assertEqual(r.returncode,0,r.stdout+r.stderr)
        self.assertTrue(json.loads(r.stdout)['passed'])

    def test_structural_audit_invalid(self):
        script=ROOT/'skills/forge-audit/scripts/audit_handoff.py'
        fixture=ROOT/'skills/forge-audit/fixtures/invalid.json'
        r=subprocess.run([sys.executable,str(script),str(fixture)],capture_output=True,text=True)
        self.assertEqual(r.returncode,1,r.stdout+r.stderr)
        self.assertFalse(json.loads(r.stdout)['passed'])
        self.assertGreater(len(json.loads(r.stdout)['issues']),0)

if __name__=='__main__':unittest.main()
