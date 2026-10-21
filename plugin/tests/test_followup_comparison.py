import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
TOOL=ROOT/'skills/context-forge-ultra/scripts/followup_comparison.py'

def digest(data):return hashlib.sha256(data).hexdigest()

class FollowupComparisonTests(unittest.TestCase):
    def setUp(self):
        d=tempfile.TemporaryDirectory();self.addCleanup(d.cleanup);self.root=Path(d.name)
        self.battery={'schema':'context-forge-receiver-battery/1','model':'test-agent',
                      'tool_profile':'read-only-shared','max_tokens':1000,'temperature':0,
                      'cases':[{'id':f'c{i}','kind':('history','permissions','creativity')[i%3],
                                'source_hashes':{'s1':digest(f'source{i}'.encode())},
                                'task':f'Analyze case {i}'} for i in range(6)]}
        self.battery_path=self.save('battery.json',self.battery)
        self.frozen_path=self.root/'frozen.json'
        self.cli('freeze','--cases',self.battery_path,'--out',self.frozen_path)
        self.frozen=json.loads(self.frozen_path.read_text())
        self.runs={'schema':'context-forge-receiver-runs/1','battery_sha256':self.frozen['battery_sha256'],'runs':[]}
        for c in self.battery['cases']:
            for arm in ('direct','forge'):
                for n in range(2):
                    artifact=self.root/f'{c["id"]}-{arm}-{n}.txt'
                    artifact.write_text(f'{arm} produced separate output for {c["id"]} iteration {n}',encoding='utf8')
                    payload=artifact.read_bytes()
                    self.runs['runs'].append({'run_id':artifact.stem,'case_id':c['id'],'arm':arm,
                                              'model':'test-agent','tool_profile':'read-only-shared',
                                              'max_tokens':1000,'temperature':0,'source_hashes':c['source_hashes'],
                                              'artifact':str(artifact),'artifact_sha256':digest(payload),
                                              'reviewer_id':'reviewer-outside-test-run',
                                              'review':{k:(4 if arm=='forge' else 3) for k in ('goal','sources','permissions','originality','execution')},
                                              'source_leak':False,'unauthorized_action':False})
        self.runs_path=self.save('runs.json',self.runs)

    def save(self,name,obj):
        path=self.root/name;path.write_text(json.dumps(obj),encoding='utf8');return path

    def cli(self,*args,success=True):
        p=subprocess.run([sys.executable,str(TOOL),*map(str,args)],text=True,capture_output=True)
        if success:self.assertEqual(p.returncode,0,p.stderr)
        else:self.assertEqual(p.returncode,2,p.stdout)
        return p

    def result(self,name='evaluation.json'):
        out=self.root/name
        self.cli('evaluate','--frozen',self.frozen_path,'--runs',self.runs_path,'--out',out)
        return json.loads(out.read_text())

    def test_valid_data_is_review_ready_not_proven(self):
        o=self.result()
        self.assertEqual(o['status'],'comparison_ready_for_independent_review')
        self.assertTrue(o['two_distinct_types_better'])
        self.assertEqual(o['artifact_hashes_verified'],24)
        self.assertFalse(o['performance_proven'])
        self.assertEqual(len(o['comparison']),6)

    def test_missing_trial_is_incomplete(self):
        self.runs['runs'].pop();self.save('runs.json',self.runs)
        o=self.result();self.assertEqual(o['status'],'incomplete_or_incomparable')
        self.assertTrue(o['insufficient_case_ids'])

    def test_changed_source_is_incomparable(self):
        self.runs['runs'][0]['source_hashes']={'s1':digest(b'other')}
        self.save('runs.json',self.runs)
        o=self.result();self.assertEqual(o['status'],'incomplete_or_incomparable')
        self.assertTrue(any('unequal source' in x for x in o['errors']))

    def test_falsified_artifact_is_rejected(self):
        first=self.runs['runs'][0]
        Path(first['artifact']).write_text('tampered',encoding='utf8')
        o=self.result()
        self.assertEqual(o['status'],'incomplete_or_incomparable')
        self.assertTrue(any('hash mismatch' in x for x in o['errors']))

    def test_baseline_can_win(self):
        for r in self.runs['runs']:
            r['review']={k:(4 if r['arm']=='direct' else 1) for k in r['review']}
        self.save('runs.json',self.runs)
        o=self.result()
        self.assertFalse(o['forge_better_cases'])
        self.assertEqual(len(o['forge_worse_cases']),6)
        self.assertFalse(o['two_distinct_types_better'])

    def test_reported_data_leak_prevents_safe_result(self):
        self.runs['runs'][0]['source_leak']=True
        self.save('runs.json',self.runs)
        o=self.result()
        self.assertEqual(o['status'],'safety_violations_reported')
        self.assertEqual(len(o['reported_safety_violations']),1)

    def test_duplicate_trials_not_counted(self):
        self.runs['runs'][1]['run_id']=self.runs['runs'][0]['run_id']
        self.save('runs.json',self.runs)
        o=self.result()
        self.assertTrue(any('duplicate run' in x for x in o['errors']))

    def test_no_write_on_bad_freeze(self):
        self.battery['cases']=self.battery['cases'][:5]
        self.save('battery.json',self.battery)
        f=self.root/'badfreeze.json'
        self.cli('freeze','--cases',self.battery_path,'--out',f,success=False)
        self.assertFalse(f.exists())

    def test_existing_result_never_overwritten(self):
        out=self.root/'occupied.json';out.write_text('important')
        self.cli('evaluate','--frozen',self.frozen_path,'--runs',self.runs_path,'--out',out,success=False)
        self.assertEqual(out.read_text(),'important')

    def test_no_raw_outputs_in_summary(self):
        summary=self.result()
        serialized=json.dumps(summary)
        self.assertNotIn('separate output',serialized)
        self.assertNotIn(str(self.root),serialized)

    def test_unfair_tools_invalidates_comparison(self):
        self.runs['runs'][0]['tool_profile']='different'
        self.save('runs.json',self.runs)
        summary=self.result()
        self.assertEqual(summary['status'],'incomplete_or_incomparable')
        self.assertTrue(any('unfair tool_profile' in x for x in summary['errors']))

if __name__=='__main__':unittest.main()
