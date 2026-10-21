"""Case and delivery regression checks; actual LLM/host behavior is separate."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
FILE=ROOT/'skills/context-forge-ultra/scripts/case_engine.py'
spec=importlib.util.spec_from_file_location('cfucase',FILE)
case=importlib.util.module_from_spec(spec)
spec.loader.exec_module(case)

class Case90(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.d=Path(self.temp.name)
        self.src=self.d/'inputs';self.src.mkdir()
        (self.src/'main.md').write_text('Nutzer: Erst baue eine Pluginfabrik.\nNutzer: Nein, nur Context Forge Ultra.\n',encoding='utf8')
        (self.src/'private.md').write_text('Interne Quelle: darf nicht übertragen werden.\n',encoding='utf8')
        self.casefile=self.d/'case.json'
        case.command_inventory(SimpleNamespace(root=str(self.src),out=str(self.casefile),sources=['main.md','private.md'],force=False))
        self.obj=case.load(self.casefile)
        self.draft=self.d/'draft.md'
        self.draft.write_text('Der gültige Auftrag ist die Weiterentwicklung eines einzelnen Context-Forge-Plugins. '
                              'Die frühe Fabrikidee wurde später ausdrücklich korrigiert. '
                              'Quellen müssen wirklich zugänglich sein. [[S001]] '
                              'Eigenständige Deutung ist erwünscht, aber keine erfundenen Rechte. '*3,encoding='utf8')
    def pack(self,**kw):
        a={'case':str(self.casefile),'draft':str(self.draft),'out':str(self.d/'out'),
           'kind':'anti-masterprompt','include_sources':False,'recipient':None,'grants':None,'require_all':False}
        a.update(kw)
        return case.command_package(SimpleNamespace(**a))
    def grants(self,*ids,recipient='folger-1'):
        rows=[]
        for x in ids:
            s=next(s for s in self.obj['sources'] if s['id']==x)
            rows.append({'source_id':x,'path':s['path'],'source_sha256':s['sha256'],'recipient':recipient,
                         'mode':'full','authority':'user-explicit-for-recipient','approved':True})
        p=self.d/'grants.json';p.write_text(json.dumps({'schema':case.TRANSFER_SCHEMA,'grants':rows}))
        return str(p)
    def test_ref_only_redacts_case_claims_and_absolute_root(self):
        case.command_record(SimpleNamespace(case=str(self.casefile),source='S002',kind='observation',actor='assistant',
                      quote='darf nicht übertragen werden',scope='private',supersedes=None,meaning='Geheime interne Quelle'))
        self.pack()
        payload=(self.d/'out'/'CASE.json').read_text()
        self.assertNotIn('Geheime interne Quelle',payload)
        self.assertNotIn('darf nicht übertragen werden',payload)
        self.assertNotIn(str(self.src),payload)
        self.assertNotIn('private.md',payload)
        self.assertFalse((self.d/'out'/'sources').exists())
    def test_include_sources_no_grants_denied_before_output(self):
        with self.assertRaisesRegex(ValueError,'--grants'):
            self.pack(include_sources=True,recipient='folger-1')
        self.assertFalse((self.d/'out').exists())
    def test_matching_only_source_is_transferred(self):
        self.pack(include_sources=True,recipient='folger-1',grants=self.grants('S001'))
        self.assertTrue((self.d/'out'/'sources'/'main.md').exists())
        self.assertFalse((self.d/'out'/'sources'/'private.md').exists())
        delivery=json.loads((self.d/'out'/'DELIVERY_CHECK.json').read_text())
        self.assertEqual(delivery['included_source_ids'],['S001'])
        self.assertEqual(delivery['excluded_sources'][0]['source_id'],'S002')
    def test_strict_all_sources_requires_two_grants(self):
        with self.assertRaisesRegex(ValueError,'Require-all'):
            self.pack(include_sources=True,recipient='folger-1',grants=self.grants('S001'),require_all=True)
        self.assertFalse((self.d/'out').exists())
    def test_wrong_recipient_is_rejected(self):
        with self.assertRaisesRegex(ValueError,'recipient'):
            self.pack(include_sources=True,recipient='someone-else',grants=self.grants('S001'))
        self.assertFalse((self.d/'out').exists())
    def test_stale_version_rejected_before_export(self):
        old=self.grants('S001')
        (self.src/'main.md').write_text('AFTER SNAPSHOT',encoding='utf8')
        with self.assertRaisesRegex(ValueError,'(?i)(?:source changed|changed source)'):
            self.pack(include_sources=True,recipient='folger-1',grants=old)
        self.assertFalse((self.d/'out').exists())
    def test_no_secret_in_draft(self):
        self.draft.write_text('A'*250+' sk-proj-THISISNOTAREALKEYEXAMPLE2026')
        with self.assertRaisesRegex(ValueError,'credential'):
            self.pack()
        self.assertFalse((self.d/'out').exists())
    def test_no_secret_in_granted_source(self):
        (self.src/'private.md').write_text('GitHub token: ghp_ABCDEFABCDEFABCDEFABCDEFABCDEF1234567')
        self.obj['sources'][1]['sha256']=case.sha((self.src/'private.md').read_bytes())
        case.save(self.casefile,self.obj)
        with self.assertRaisesRegex(ValueError,'credential'):
            self.pack(include_sources=True,recipient='folger-1',grants=self.grants('S002'))
        self.assertFalse((self.d/'out').exists())
    def test_compose_kinds_from_claims(self):
        case.command_record(SimpleNamespace(case=str(self.casefile),source='S001',kind='user_intent',actor='user',
                      quote='Erst baue eine Pluginfabrik',scope='produkt',supersedes=None,meaning='Eine Pluginfabrik'))
        case.command_record(SimpleNamespace(case=str(self.casefile),source='S001',kind='correction',actor='user',
                      quote='Nein, nur Context Forge Ultra',scope='produkt',supersedes='C001',meaning='Nur Context Forge Ultra'))
        obj=case.load(self.casefile);active,conflicts=case.decision_summary(obj)
        self.assertEqual([c['id'] for c in active],['C002'])
        self.assertFalse(conflicts)
        for kind in ('anti-masterprompt','handoff'):
            out=self.d/(kind+'.md')
            case.command_compose(SimpleNamespace(case=str(self.casefile),kind=kind,out=str(out)))
            text=out.read_text()
            self.assertIn('Nur Context Forge Ultra',text)
            self.assertNotIn('Eine Pluginfabrik',text)
            self.assertIn('keine Datei automatisch übertragen',text)
    def test_cross_scope_correction_refused(self):
        case.command_record(SimpleNamespace(case=str(self.casefile),source='S001',kind='user_intent',actor='user',
                     quote='Erst baue eine Pluginfabrik',scope='produkt',supersedes=None,meaning='Fabrik'))
        with self.assertRaisesRegex(ValueError,'exact nonempty prior scope'):
            case.command_record(SimpleNamespace(case=str(self.casefile),source='S001',kind='correction',actor='user',
                     quote='Nein, nur Context Forge Ultra',scope='musik',supersedes='C001',meaning='Unrelated'))
    def test_observed_read_does_not_claim_comprehension(self):
        case.command_record_read(SimpleNamespace(case=str(self.casefile),source='S001',quote='Nutzer: Erst',actor='assistant'))
        event=case.load(self.casefile)['read_events'][0]
        self.assertEqual(event['semantic_understanding'],'not_independently_verified')
        self.assertNotIn('host_attested',event['proof'].split('not_')[0])
    def test_output_atomic_when_source_changes_at_commit(self):
        original=case.read_text
        counter={'i':0}
        def change_on_second(root,rel):
            counter['i']+=1
            if counter['i']==2:
                (self.src/'main.md').write_text('changed mid export')
            return original(root,rel)
        with patch.object(case,'read_text',side_effect=change_on_second):
            with self.assertRaisesRegex(ValueError,'(?i)(?:source changed|changed source)'):
                self.pack(include_sources=True,recipient='folger-1',grants=self.grants('S001'))
        self.assertFalse((self.d/'out').exists())
        self.assertFalse(list(self.d.glob('.cfu-stage-*')))
    def test_handoff_output_filename(self):
        self.pack(kind='handoff')
        self.assertTrue((self.d/'out'/'HANDOFF.md').exists())
        self.assertFalse((self.d/'out'/'ANTI_MASTERPROMPT.md').exists())

if __name__=='__main__':unittest.main()
