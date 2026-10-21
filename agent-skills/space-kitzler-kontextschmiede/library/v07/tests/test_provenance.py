import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT/'skills/forge-audit/scripts/verify_quotes.py'
FIXTURE = ROOT/'skills/forge-audit/fixtures/provenance'

class ProvenanceTests(unittest.TestCase):
    def call(self, obj, root=None):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)/'proof.json'
            p.write_text(json.dumps(obj,ensure_ascii=False), encoding='utf-8')
            proc = subprocess.run([sys.executable,str(SCRIPT),str(p),'--root',str(root or FIXTURE)],capture_output=True,text=True)
            return proc.returncode,json.loads(proc.stdout)

    def valid(self):
        return json.loads((FIXTURE/'proof_valid.json').read_text(encoding='utf-8'))

    def test_original_excerpt_and_hash(self):
        code,output=self.call(self.valid())
        self.assertEqual(code,0,output)
        self.assertEqual(output['verdict'],'excerpt_verified_not_reading')
        self.assertEqual([x['status'] for x in output['results']],['verified_excerpt','verified_excerpt'])

    def test_fabricated_quote(self):
        obj=self.valid(); obj['evidence'][0]['quote']='Die vertagte Controller-Verbindung ist bereits Pflicht.'
        code,output=self.call(obj)
        self.assertEqual(code,1,output)

    def test_wrong_line(self):
        obj=self.valid(); obj['evidence'][0]['start_line']=3; obj['evidence'][0]['end_line']=3
        self.assertEqual(self.call(obj)[0],1)

    def test_tampered_version(self):
        obj=self.valid(); obj['evidence'][0]['sha256']='0'*64
        self.assertEqual(self.call(obj)[0],1)

    def test_missing_file_unscorable(self):
        obj=self.valid(); obj['evidence'][0]['path']='missing.md'
        code,output=self.call(obj)
        self.assertEqual(code,2,output)
        self.assertEqual(output['verdict'],'unscorable')

    def test_path_traversal_rejected(self):
        obj=self.valid(); obj['evidence'][0]['path']='../quelle.md'
        self.assertEqual(self.call(obj)[0],2)

    def test_absolute_path_rejected(self):
        obj=self.valid(); obj['evidence'][0]['path']='/etc/passwd'
        self.assertEqual(self.call(obj)[0],2)

    def test_duplicate_id_rejected(self):
        obj=self.valid(); obj['evidence'][1]['id']='E1'
        self.assertEqual(self.call(obj)[0],2)

    def test_no_empty_proof_success(self):
        self.assertEqual(self.call({'evidence':[]})[0],2)

    def test_boolean_line_numbers_rejected(self):
        obj=self.valid(); obj['evidence'][0]['start_line']=True
        self.assertEqual(self.call(obj)[0],2)

    def test_symlink_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)
            (path/'jump.md').symlink_to(FIXTURE/'quelle.md')
            obj=self.valid();obj['evidence']=[dict(obj['evidence'][0],path='jump.md')]
            self.assertEqual(self.call(obj,root=path)[0],2)

    def test_invalid_unicode_is_unscorable(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)
            (path/'bin.md').write_bytes(b'\xff\xfe')
            obj=self.valid();obj['evidence']=[dict(obj['evidence'][0],path='bin.md',sha256=None)]
            self.assertEqual(self.call(obj,root=path)[0],2)

    def test_valid_only_proves_excerpt_not_mental_reading(self):
        code,output=self.call(self.valid())
        self.assertEqual(code,0)
        self.assertIn('weder Leseakt noch Interpretation',output['limit'])

if __name__=='__main__':unittest.main()
