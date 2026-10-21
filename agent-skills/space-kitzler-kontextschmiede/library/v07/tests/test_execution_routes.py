import pathlib,unittest,json,re,yaml

ROOT=pathlib.Path(__file__).resolve().parents[1]
SKILLS=ROOT/'skills'

class ExecutionRoutingTests(unittest.TestCase):
    def test_two_distinct_entrypoints(self):
        act=(SKILLS/'forge-act/SKILL.md').read_text()
        master=(SKILLS/'forge-masterprompt/SKILL.md').read_text()
        h=(SKILLS/'forge-handoff/SKILL.md').read_text()
        self.assertRegex(act,r'erst(?:e|en) real nützliche(?:n)? Handlung')
        self.assertIn('--apply', (SKILLS/'forge-act/references/werkzeuge-und-aktionen.md').read_text())
        self.assertIn('fertigen Masterprompt',master)
        self.assertIn('forge-act',h)
        self.assertIn('forge-masterprompt',h)
        for key, negative in [('forge-act','nicht für reine'),('forge-masterprompt','nicht für reine')]:
            fm=yaml.safe_load((SKILLS/key/'SKILL.md').read_text().split('---',2)[1])
            self.assertIn(negative.lower(), fm['description'].lower())
    def test_sibling_references_resolve(self):
        for p in SKILLS.glob('*/SKILL.md'):
            text=p.read_text()
            for ref in re.findall(r'`(references/[\w.-]+\.md)`',text):
                self.assertTrue((p.parent/ref).exists(),f'{p.parent.name} missing {ref}')
            for ref in re.findall(r'`(\.\./forge-[\w-]+/references/[\w.-]+\.md)`',text):
                self.assertTrue((p.parent/ref).exists(),f'{p.parent.name} missing {ref}')
    def test_research_and_reentry_change_work_not_only_describe(self):
        for name in ('forge-research','forge-agent-reentry','forge-repo-practices','forge-decisions','forge-workloops'):
            s=(SKILLS/name/'SKILL.md').read_text().lower()
            self.assertTrue(('forge-act' in s) or ('tatsächlich' in s and 'ausführ' in s), name)
    def test_original_masterprompt_requirements_preserved(self):
        master=(SKILLS/'forge-masterprompt/SKILL.md').read_text()
        for k in ['vorhandenen Prompt','ersten','Quellen','Abnahmekriterien','Baseline','verbindlich','Werkzeuge']:
            self.assertIn(k.lower(),master.lower())
        self.assertIn('Plugin-Generator', (ROOT/'docs/06_WIRKUNGSLOGIK_UND_AUFTRAGSVARIANTEN.md').read_text())
    def test_no_invented_mcp_or_job(self):
        self.assertFalse((ROOT/'mcp.json').exists())
        for p in ('skills/forge-act/SKILL.md','skills/forge-masterprompt/SKILL.md'):
            text=(ROOT/p).read_text()
            self.assertIn('vorhanden',text)
    def test_manifests_and_version(self):
        root=json.loads((ROOT/'plugin.json').read_text())
        legacy=json.loads((ROOT/'.codex-plugin/plugin.json').read_text())
        self.assertEqual('0.7.0',root['version'])
        self.assertEqual(root['version'],legacy['version'])
        self.assertEqual(root['extensions']['com.openai']['interface']['defaultPrompt'],legacy['interface']['defaultPrompt'])

if __name__=='__main__':unittest.main()
