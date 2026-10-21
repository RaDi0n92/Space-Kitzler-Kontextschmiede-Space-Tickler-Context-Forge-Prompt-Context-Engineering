import importlib.util, json, pathlib, subprocess, sys, tempfile, unittest, hashlib

ROOT=pathlib.Path(__file__).resolve().parents[1]
SCRIPT=ROOT/'skills/forge-act/scripts/forge_apply.py'

def sha(text):return hashlib.sha256(text.encode()).hexdigest()

class ActionRunnerTests(unittest.TestCase):
    def invoke(self,work,plan,apply=False):
        p=work/'plan.json';p.write_text(json.dumps(plan,ensure_ascii=False))
        return subprocess.run([sys.executable,str(SCRIPT),str(p)]+(['--apply'] if apply else []),text=True,capture_output=True)
    def test_write_is_dry_run_then_real_and_verified(self):
        with tempfile.TemporaryDirectory() as d:
            w=pathlib.Path(d);plan={'root':str(w),'operations':[{'kind':'write','path':'result.md','content':'Bearbeitet und geprüft'}],'checks':[{'path':'result.md','contains':['geprüft']}]} 
            self.assertEqual(self.invoke(w,plan).returncode,0)
            self.assertFalse((w/'result.md').exists())
            self.assertEqual(self.invoke(w,plan,True).returncode,0)
            self.assertEqual((w/'result.md').read_text(),'Bearbeitet und geprüft')
            self.assertEqual(self.invoke(w,plan,True).returncode,1) # refuses overwrite
    def test_exact_replace_precondition_and_readback(self):
        with tempfile.TemporaryDirectory() as d:
            w=pathlib.Path(d);(w/'doc.md').write_text('ALT: verworfen\n')
            plan={'root':str(w),'operations':[{'kind':'replace','path':'doc.md','sha256_before':sha('ALT: verworfen\n'),'old':'ALT: verworfen','new':'NEU: gültig'}],'checks':[{'path':'doc.md','contains':['NEU: gültig']}]} 
            self.assertEqual(self.invoke(w,plan,True).returncode,0)
            self.assertEqual((w/'doc.md').read_text(),'NEU: gültig\n')
            self.assertEqual(self.invoke(w,plan,True).returncode,1)
    def test_fails_closed_on_wrong_hash_and_check(self):
        with tempfile.TemporaryDirectory() as d:
            w=pathlib.Path(d);(w/'a').write_text('abc')
            plan={'root':str(w),'operations':[{'kind':'replace','path':'a','sha256_before':'0'*64,'old':'abc','new':'foo'}]}
            self.assertEqual(self.invoke(w,plan,True).returncode,1)
            self.assertEqual((w/'a').read_text(),'abc')
            plan={'root':str(w),'operations':[{'kind':'write','path':'b','content':'truth'}],'checks':[{'path':'b','contains':['fabrication']}]} 
            self.assertEqual(self.invoke(w,plan,True).returncode,1)
            self.assertFalse((w/'b').exists())
    def test_rejects_path_traversal_and_symlink(self):
        with tempfile.TemporaryDirectory() as d:
            w=pathlib.Path(d);(w/'link').symlink_to('/tmp')
            for bad in ['../escape','/etc/passwd','link/hack','foo//bar','a/./b']:
                plan={'root':str(w),'operations':[{'kind':'write','path':bad,'content':'bad'}]}
                self.assertEqual(self.invoke(w,plan,True).returncode,1,bad)
    def test_rejects_duplicate_actions_and_ambiguous_replace(self):
        with tempfile.TemporaryDirectory() as d:
            w=pathlib.Path(d);(w/'a').write_text('x x')
            plan={'root':str(w),'operations':[{'kind':'replace','path':'a','sha256_before':sha('x x'),'old':'x','new':'y'}]}
            self.assertEqual(self.invoke(w,plan,True).returncode,1)
            plan={'root':str(w),'operations':[{'kind':'write','path':'z','content':'a'},{'kind':'write','path':'z','content':'b'}]}
            self.assertEqual(self.invoke(w,plan,True).returncode,1)

if __name__=='__main__': unittest.main()
