import json
import re
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT=Path(__file__).resolve().parents[1]
ENTRY=ROOT/'skills'/'context-forge-ultra'
SCRIPT=ENTRY/'scripts'/'case_engine.py'


class RuntimeTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.d=Path(self.tmp.name)
        self.source=self.d/'sources';self.source.mkdir()
        (self.source/'original.md').write_text('Zuerst: Baue eine Pluginfabrik.\nDann: Nein, ich will einen Kontextcompiler.\nDies ist die entscheidende Korrektur.\n',encoding='utf8')
        (self.source/'zweite.md').write_text('Die andere Perspektive ist ein offen gebliebener Denkweg.\n',encoding='utf8')
        self.case=self.d/'case.json'

    def cli(self,*args,ok=True):
        x=subprocess.run([sys.executable,str(SCRIPT),*map(str,args)],text=True,capture_output=True)
        if ok:
            self.assertEqual(x.returncode,0,x.stderr)
        else:
            self.assertNotEqual(x.returncode,0,x.stdout)
        return x

    def inventory(self):
        self.cli('inventory','--root',self.source,'--out',self.case,'original.md','zweite.md')

    def test_inventory_does_not_pretend_reading(self):
        self.inventory();c=json.loads(self.case.read_text());self.assertEqual(len(c['sources']),2)
        self.assertEqual(c['sources'][0]['capture'],'mechanical_read_not_semantic_read')
        self.assertEqual(c['sources'][0]['read_ranges'],[])
    def test_no_overwrite(self):
        self.inventory();self.cli('inventory','--root',self.source,'--out',self.case,'original.md',ok=False)
    def test_reject_traversal(self):
        self.cli('inventory','--root',self.source,'--out',self.case,'../escape.md',ok=False)
    def test_reject_absolute(self):
        self.cli('inventory','--root',self.source,'--out',self.case,self.source/'original.md',ok=False)
    def test_reject_symlink(self):
        (self.source/'link.md').symlink_to('original.md');self.cli('inventory','--root',self.source,'--out',self.case,'link.md',ok=False)
    def test_record_quote_verified(self):
        self.inventory();self.cli('record','--case',self.case,'--source','S001','--kind','correction','--actor','user','--quote','Nein, ich will einen Kontextcompiler.','--meaning','Neue Produktabsicht');c=json.loads(self.case.read_text());self.assertEqual(c['claims'][0]['source'],'S001');self.assertTrue(c['sources'][0]['read_ranges'])
    def test_record_unfounded_quote_rejected(self):
        self.inventory();self.cli('record','--case',self.case,'--source','S001','--kind','decision','--actor','user','--quote','Nicht im Text','--meaning','erfunden',ok=False)
    def test_record_stale_refused(self):
        self.inventory();(self.source/'original.md').write_text('NEU');self.cli('record','--case',self.case,'--source','S001','--kind','decision','--actor','user','--quote','NEU','--meaning','aus falschem Snapshot',ok=False)
    def test_verify_catches_source_change(self):
        self.inventory();self.cli('verify','--case',self.case);(self.source/'zweite.md').write_text('VERÄNDERT');self.cli('verify','--case',self.case,ok=False)
    def test_invalid_supersede_rejected(self):
        self.inventory();self.cli('record','--case',self.case,'--source','S001','--kind','correction','--actor','user','--quote','Nein, ich will einen Kontextcompiler.','--meaning','Wende','--supersedes','C999',ok=False)
    def test_relation_binds_claims(self):
        self.inventory()
        for phrase in ['Baue eine Pluginfabrik','Nein, ich will einen Kontextcompiler']:
            self.cli('record','--case',self.case,'--source','S001','--kind','observation','--actor','user','--quote',phrase,'--meaning',phrase)
        self.cli('relate','--case',self.case,'--left','C001','--right','C002','--type','contradicts','--reason','Gegenstand verändert')
        self.assertEqual(json.loads(self.case.read_text())['relations'][0]['type'],'contradicts')
    def test_duplicate_source_rejected(self):
        self.cli('inventory','--root',self.source,'--out',self.case,'original.md','original.md',ok=False)
    def battery(self):
        p=self.d/'probes.json';p.write_text(json.dumps([{
             'id':'P1','base':'Ändere nur Prompt','relevant_intervention':'Ändere Plugin',
             'irrelevant_paraphrase':'Verfasse nur einen Prompt','expected_base':'prompt','expected_changed':'plugin'}]))
        return p
    def test_freeze_and_score(self):
        p=self.battery();fr=self.d/'frozen.json';self.cli('freeze-probes','--battery',p,'--out',fr)
        p.write_text('[]')
        res=self.d/'results.json';res.write_text(json.dumps({'P1':{'base':'prompt','relevant':'plugin','irrelevant':'prompt'}}))
        got=self.cli('score-probes','--frozen',fr,'--results',res)
        self.assertEqual(json.loads(got.stdout)['passing'],1)
    def test_freeze_refuses_repeated(self):
        p=self.battery();fr=self.d/'frozen.json';self.cli('freeze-probes','--battery',p,'--out',fr);self.cli('freeze-probes','--battery',p,'--out',fr,ok=False)
    def test_invalid_battery(self):
        p=self.battery();rows=json.loads(p.read_text());rows[0]['expected_changed']='prompt';p.write_text(json.dumps(rows))
        self.cli('freeze-probes','--battery',p,'--out',self.d/'frozen.json',ok=False)
    def test_score_missing_is_not_pass(self):
        p=self.battery();fr=self.d/'frozen.json';self.cli('freeze-probes','--battery',p,'--out',fr);res=self.d/'empty.json';res.write_text('{}')
        x=self.cli('score-probes','--frozen',fr,'--results',res)
        self.assertEqual(json.loads(x.stdout)['passing'],0)
    def test_import_jlens_marked_not_replicated(self):
        self.inventory();j=self.d/'lens.json';j.write_text(json.dumps({'model':'m.gguf','experiment_id':'A1','mode':'ablate','baseline':{'observed_answer':'eins'},'intervention':{'observed_answer':'zwei'},'matched_control':{'observed_answer':'eins'}}))
        self.cli('import-jlens','--case',self.case,'--report',j)
        self.assertIn('not_replicated',json.loads(self.case.read_text())['lens_observations'][0]['provenance'])
    def test_bad_import_rejected(self):
        self.inventory();j=self.d/'lens.json';j.write_text('{}');self.cli('import-jlens','--case',self.case,'--report',j,ok=False)
    def test_package_omits_sources_without_optin(self):
        self.inventory();draft=self.d/'draft.md';draft.write_text('Eine belegte Geschichte mit ersten Wendungen [[S001]] und einer offenen Alternative [[S002]]. '+('Erkläre aktuelle Ziele und historische Korrekturen. '*7))
        out=self.d/'handoff';self.cli('package','--case',self.case,'--draft',draft,'--out',out)
        self.assertTrue((out/'ANTI_MASTERPROMPT.md').exists());self.assertFalse((out/'sources').exists())
        self.assertEqual(json.loads((out/'DELIVERY_CHECK.json').read_text())['source_transfer'],'references_only_not_access_grant')
    def test_package_with_sources(self):
        self.inventory();draft=self.d/'draft.md';draft.write_text('Alles belegt [[S001]]. '+('Hintergründe und weiterdenkbare Fragen. '*10))
        manifest=self.d/'grants.json'
        src=json.loads(self.case.read_text())['sources'][0]
        manifest.write_text(json.dumps({'schema':'context-forge-transfer-grants/1','grants':[{'source_id':src['id'],'path':src['path'],'source_sha256':src['sha256'],'recipient':'agent-1','mode':'full','authority':'user-explicit','approved':True}]}))
        self.cli('package','--case',self.case,'--draft',draft,'--out',self.d/'out','--include-sources','--recipient','agent-1','--grants',manifest)
        self.assertTrue((self.d/'out'/'sources'/'original.md').exists())
    def test_package_blocks_unknown_id(self):
        self.inventory();draft=self.d/'draft.md';draft.write_text('[[S999]] '+('Gesicherte Projekthintergründe und denkbare Tests. '*9))
        self.cli('package','--case',self.case,'--draft',draft,'--out',self.d/'out',ok=False)
    def test_cli_help(self):
        self.cli('--help')


class PackagingTests(unittest.TestCase):
    def test_main_and_17_specialist_entries_are_active(self):
        skill_files=list((ROOT/'skills').glob('*/SKILL.md'))
        self.assertEqual(len(skill_files),18)
        names=[]
        for path in skill_files:
            text=path.read_text(encoding='utf-8')
            match=re.search(r'^name:\s*([a-z0-9-]+)\s*$',text,re.M)
            self.assertIsNotNone(match,str(path))
            if path != ENTRY/'SKILL.md':
                self.assertEqual(path.parent.name,match.group(1))
            names.append(match.group(1))
        self.assertEqual(len(set(names)),18)
        self.assertEqual(set(names), {'quellenlesen', 'arbeitsauftrag', 'repo-erkenntnisse', 'gegenfragen', 'denkwerkstatt', 'perspektiven', 'uebergaben-pruefen', 'space-kitzler-kontextschmiede', 'wiedereinstieg', 'denkbruecken', 'arbeitskreislauf', 'wirkungsvergleich', 'forschung', 'kontextuebergabe', 'entscheidungsstatus', 'projektgeschichte', 'autorisierte-umsetzung', 'pluginbau'})
        self.assertIn('space-kitzler-kontextschmiede',names)
    def test_archived_source_entries_are_preserved(self):
        historical=list((ENTRY/'library'/'v07').glob('forge-*/old_entry.md'))
        self.assertEqual(len(historical),17)
        self.assertFalse(list((ENTRY/'library'/'v07').glob('forge-*/SKILL.md')))
    def test_manifest_identity_consistent(self):
        a=json.loads((ROOT/'plugin.json').read_text());b=json.loads((ROOT/'.codex-plugin/plugin.json').read_text())
        self.assertRegex(a['version'],r'^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$')
        self.assertEqual(b['version'],a['version']);self.assertEqual(a['name'],b['name'])
        self.assertEqual(a['extensions']['com.openai']['interface']['defaultPrompt'],b['interface']['defaultPrompt'])
    def test_source_repos_distinct_methods(self):
        s=(ENTRY/'references'/'drei-repositories-im-einsatz.md').read_text();self.assertIn('J-Space Cognition Suite',s);self.assertIn('sina-gpt',s);self.assertIn('jlens-gguf',s)
        for label in ['drei-repositories-im-einsatz','sina-kontrastpruefung','lokales-jlens-instrument']:
            self.assertTrue((ENTRY/'references'/f'{label}.md').is_file())
    def test_all_local_refs_exist(self):
        import re
        s=(ENTRY/'SKILL.md').read_text()
        for f in re.findall(r'`(references/[^`\s]+\.md)`',s):self.assertTrue((ENTRY/f).is_file(),f)

if __name__=='__main__':unittest.main()
