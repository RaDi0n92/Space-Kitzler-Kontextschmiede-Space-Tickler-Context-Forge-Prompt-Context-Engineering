import copy
import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/forge-audit/scripts/audit_handoff.py'
spec = importlib.util.spec_from_file_location('forge_auditor', SCRIPT)
aud = importlib.util.module_from_spec(spec)
spec.loader.exec_module(aud)


def good():
    return {
      'sources': [
        {'id':'S1','locator':'chat:1','read_status':'gelesen_voll','actually_read':True,'read_evidence':'current chat text','accessible_to_next':'unbekannt'},
        {'id':'S2','locator':'docs/vision.md#3','read_status':'gelesen_teilweise','actually_read':True,'read_evidence':'file read ranges','read_extent':'L1-L20','accessible_to_next':'ja'},
        {'id':'S3','locator':'docs/unknown.md','read_status':'nur_erwähnt','actually_read':False,'accessible_to_next':'unbekannt'}],
      'decisions': [
        {'id':'D1','statement':'Plugin generator','status':'ersetzt','superseded_by':'D2','source_ids':['S1']},
        {'id':'D2','statement':'Context Forge handoff','status':'aktuell','source_ids':['S1']},
        {'id':'D3','statement':'Harness integration someday','status':'vertagt','reason':'future option','source_ids':['S1']}],
      'read_again': [{'source_id':'S2','why':'revisit original','accessible_to_next':'ja'}],
      'claims': [{'statement':'Discussion considered original-reading paths','status':'belegt','supported':True,'source_ids':['S1']}],
      'perspectives': [
        {'id':'P1','label':'historical motives','source_ids':['S1']},
        {'id':'P2','label':'possible reverse assumption','hypothetical':True,'source_ids':[]}],
      'relations': [{'from':'P1','to':'P2','relation':'may challenge earlier assumption'}]
    }

class TestAdversarial(unittest.TestCase):
    def check(self, mutate, expected):
        obj = good()
        mutate(obj)
        issues, warnings = aud.audit(obj)
        self.assertEqual(bool(issues), expected, '\n'.join(issues))
        return issues, warnings

    def test_good(self): self.check(lambda x:None, False)
    def test_empty_root(self): self.assertTrue(aud.audit({})[0])
    def test_empty_lists(self): self.assertTrue(aud.audit({'sources':[],'decisions':[],'read_again':[]})[0])
    def test_unverified_full_read(self): self.check(lambda x:x['sources'][0].pop('read_evidence'),True)
    def test_false_read_flag(self): self.check(lambda x:x['sources'][0].update(actually_read=False),True)
    def test_partial_without_extent(self): self.check(lambda x:x['sources'][1].pop('read_extent'),True)
    def test_unread_marked_read(self): self.check(lambda x:x['sources'][2].update(actually_read=True),True)
    def test_invalid_access(self): self.check(lambda x:x['sources'][1].update(accessible_to_next='maybe'),True)
    def test_duplicate_source(self): self.check(lambda x:x['sources'].append(copy.deepcopy(x['sources'][0])),True)
    def test_unknown_decision_source(self): self.check(lambda x:x['decisions'][1].update(source_ids=['NOTTHERE']),True)
    def test_current_from_unread(self): self.check(lambda x:x['decisions'][1].update(source_ids=['S3']),True)
    def test_conflicting_reread_access(self): self.check(lambda x:x['sources'][1].update(accessible_to_next='nein'),True)
    def test_missing_reread(self): self.check(lambda x:x.update(read_again=[]),True)
    def test_cycle(self): self.check(lambda x:x['decisions'][1].update(status='ersetzt',superseded_by='D1'),True)
    def test_self_cycle(self): self.check(lambda x:x['decisions'][0].update(superseded_by='D1'),True)
    def test_unknown_successor(self): self.check(lambda x:x['decisions'][0].update(superseded_by='D400'),True)
    def test_unsupported_claim(self): self.check(lambda x:x['claims'][0].update(supported=False),True)
    def test_unread_claim(self): self.check(lambda x:x['claims'][0].update(source_ids=['S3']),True)
    def test_duplicate_perspective(self): self.check(lambda x:x['perspectives'][1].update(label=' HISTORICAL  MOTIVES '),True)
    def test_no_perspective_anchor(self): self.check(lambda x:x['perspectives'][1].pop('hypothetical'),True)
    def test_broken_graph_edge(self): self.check(lambda x:x['relations'][0].update(to='nonexistent'),True)
    def test_next_source_referenced(self): self.check(lambda x:x['read_again'][0].update(source_id='999'),True)
    def test_valid_without_optional_perspective_structure(self):
        def remove(x): x.pop('perspectives'); x.pop('relations'); x.pop('claims')
        self.check(remove,False)
    def test_only_secondary_has_warning(self):
        def mutate(x): x['decisions'][1].update(source_ids=['S4']);x['sources'].append({'id':'S4','locator':'summary.md','read_status':'zitiert_aus_zweitquelle','actually_read':False})
        issues,warnings=self.check(mutate,False)
        self.assertTrue(any('Sekundärquellen' in w for w in warnings))
    def test_bad_json_is_unscorable_not_fail(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'broken.json';p.write_text('{')
            r=subprocess.run([sys.executable,str(SCRIPT),str(p)],capture_output=True,text=True)
            self.assertEqual(r.returncode,2)
            self.assertEqual(json.loads(r.stdout)['verdict'],'unscorable')
    def test_output_disclaims_semantic_truth(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'valid.json';p.write_text(json.dumps(good()))
            r=subprocess.run([sys.executable,str(SCRIPT),str(p)],capture_output=True,text=True)
            self.assertEqual(r.returncode,0)
            obj=json.loads(r.stdout)
            self.assertEqual(obj['verdict'],'structurally_passed_not_semantically_verified')

if __name__=='__main__':unittest.main()
