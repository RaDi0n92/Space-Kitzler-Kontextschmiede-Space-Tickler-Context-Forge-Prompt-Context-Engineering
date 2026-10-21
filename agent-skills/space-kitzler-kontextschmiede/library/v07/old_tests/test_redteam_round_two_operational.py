import pathlib, sys, importlib.util, hashlib, tempfile, json, unittest, contextlib, io
ROOT=pathlib.Path(__file__).resolve().parents[1]
SCRIPT=ROOT/'skills/forge-act/scripts/forge_apply.py'
spec=importlib.util.spec_from_file_location('forge_apply_r2',SCRIPT)
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
class RoundTwo(unittest.TestCase):
 def test_noncanonical_workspace_root_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   plan={'root':d+'/child/..','operations':[{'kind':'write','path':'a.md','content':'a'}]}
   (pathlib.Path(d)/'child').mkdir()
   with self.assertRaises(ValueError):mod.compile_plan(plan)
 def test_existing_source_changes_between_plan_and_commit(self):
  with tempfile.TemporaryDirectory() as d:
   root=pathlib.Path(d);p=root/'target.md';p.write_text('old')
   plan={'root':d,'operations':[{'kind':'replace','path':'target.md','sha256_before':hashlib.sha256(b'old').hexdigest(),'old':'old','new':'proposed'}]}
   plan_path=root/'plan.json';plan_path.write_text(json.dumps(plan))
   orig=mod.compile_plan
   def interrupted_plan(obj):
    result=orig(obj);p.write_text('outside edit');return result
   mod.compile_plan=interrupted_plan
   try:
    argv=sys.argv;sys.argv=['forge_apply.py',str(plan_path),'--apply']
    with contextlib.redirect_stderr(io.StringIO()): result=mod.main()
    self.assertEqual(result,1)
    self.assertEqual(p.read_text(),'outside edit')
   finally:
    mod.compile_plan=orig;sys.argv=argv
 def test_symlink_created_after_plan_does_not_escape_workspace(self):
  with tempfile.TemporaryDirectory() as d:
   root=pathlib.Path(d);(root/'sub').mkdir();(root/'outside').mkdir()
   plan={'root':d,'operations':[{'kind':'write','path':'sub/a.md','content':'should not escape'}]}
   p=root/'plan.json';p.write_text(json.dumps(plan));old=mod.compile_plan
   def switch(obj):
    stage=old(obj);(root/'sub').rmdir();(root/'sub').symlink_to(root/'outside');return stage
   mod.compile_plan=switch
   try:
    argv=sys.argv;sys.argv=['forge_apply.py',str(p),'--apply']
    with contextlib.redirect_stderr(io.StringIO()):result=mod.main()
    self.assertEqual(result,1)
    self.assertFalse((root/'outside/a.md').exists())
   finally:
    mod.compile_plan=old;sys.argv=argv
 def test_skill_metadata_excludes_wrong_kind_of_work(self):
  for name,word in [('forge-act','Masterprompt'),('forge-masterprompt','Projektzusammenfassungen'),('forge-handoff','Masterprompt')]:
   skill=(ROOT/'skills'/name/'SKILL.md').read_text()
   description=skill.split('---',2)[1]
   self.assertIn(word.lower(),description.lower(),name)
if __name__=='__main__':unittest.main()
