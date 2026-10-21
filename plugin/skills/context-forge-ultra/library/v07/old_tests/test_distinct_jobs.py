import unittest, pathlib, yaml, re, json
ROOT=pathlib.Path(__file__).resolve().parents[1]
class DistinctJobs(unittest.TestCase):
    def test_autopilot_and_repo_research_have_opposite_entry_conditions(self):
        a=(ROOT/'skills/forge-plugin-autopilot/SKILL.md').read_text()
        b=(ROOT/'skills/forge-repo-practices/SKILL.md').read_text()
        self.assertIn('ausdrücklich',a.split('---',2)[1])
        self.assertIn('Kein allgemeiner Plugin-Generator',b)
        self.assertIn('nicht',a.lower())
    def test_repo_literature_is_reachable_when_relevant(self):
        s=(ROOT/'skills/forge-repo-practices/SKILL.md').read_text()
        self.assertIn('references/github-lernpfade.md',s)
        self.assertTrue((ROOT/'skills/forge-repo-practices/references/github-lernpfade.md').exists())
    def test_meta_skill_keeps_autopilot_originals_navigable(self):
        s=(ROOT/'skills/forge-plugin-autopilot/SKILL.md').read_text()
        for slug in ['agentic-repo-discovery','workflow-to-skill-compiler','plugin-experience-architect']:
            self.assertIn(slug,s)
        self.assertIn('forge-history',s)
    def test_manifest_and_compatibility_version_stay_coherent(self):
        v=json.loads((ROOT/'plugin.json').read_text())
        c=json.loads((ROOT/'.codex-plugin/plugin.json').read_text())
        self.assertEqual('0.7.0',v['version'])
        self.assertEqual(v['version'],c['version'])
    def test_not_a_mandatory_twelve_step_pipeline(self):
        s=(ROOT/'skills/forge-handoff/SKILL.md').read_text()
        self.assertIn('Nicht sämtliche Spezialskills zwangsläufig aktivieren',s)
    def test_refs_in_new_skill_exist(self):
        p=ROOT/'skills/forge-plugin-autopilot/SKILL.md'
        t=p.read_text()
        for f in re.findall(r'`(references/[\w.-]+\.md)`',t):
            self.assertTrue((p.parent/f).exists(),f)
if __name__=='__main__':unittest.main()
