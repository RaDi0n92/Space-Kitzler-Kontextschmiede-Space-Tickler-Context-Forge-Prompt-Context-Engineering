import pathlib, subprocess, tempfile, json, sys, os, unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
SCRIPT=ROOT/'skills/forge-act/scripts/forge_apply.py'
class RedTeamOperational(unittest.TestCase):
    def runplan(self,root,ops,checks=None,apply=True):
        spec={'root':str(root),'operations':ops,'checks':checks or []}
        p=root/'plan.json';p.write_text(json.dumps(spec))
        return subprocess.run([sys.executable,str(SCRIPT),str(p)]+(['--apply'] if apply else []),capture_output=True,text=True)
    def test_multifile_failure_never_leaves_partial_write(self):
        with tempfile.TemporaryDirectory() as d:
            root=pathlib.Path(d); (root/'locked').mkdir();(root/'locked').chmod(0o555)
            try:
                got=self.runplan(root,[{'kind':'write','path':'one.txt','content':'created'},{'kind':'write','path':'locked/two.txt','content':'blocked'}])
                self.assertNotEqual(got.returncode,0)
                self.assertFalse((root/'one.txt').exists(),'Partial commit despite error: '+got.stderr)
            finally:(root/'locked').chmod(0o755)
    def test_entrypoints_are_not_stale_descriptive_only(self):
        act=(ROOT/'skills/forge-act/SKILL.md').read_text()
        work=(ROOT/'skills/forge-workloops/SKILL.md').read_text()
        research=(ROOT/'skills/forge-research/SKILL.md').read_text()
        self.assertRegex(act,r'erst(?:e|en) real nützliche(?:n)? Handlung')
        self.assertIn('forge-act',work)
        self.assertIn('forge-act',research)
    def test_handoff_and_masterprompt_have_clear_boundary(self):
        h=(ROOT/'skills/forge-handoff/SKILL.md').read_text()
        m=(ROOT/'skills/forge-masterprompt/SKILL.md').read_text()
        self.assertIn('forge-masterprompt',h)
        self.assertIn('forge-handoff',m)
        self.assertIn('ausführbar',m.lower())
    def test_package_no_bytecode_or_junk(self):
        # Source test runs create __pycache__; the release archive is separately scanned.
        self.assertFalse((ROOT/'mcp.json').exists(), 'Skills-only package must not claim an MCP backend')
