import unittest
from test_adversarial import aud, good

class RedTeamRound2(unittest.TestCase):
    def test_malformed_source_id_must_not_crash(self):
        d=good();d['sources'][0]['id']=['unhashable']
        self.assertTrue(aud.audit(d)[0])
    def test_malformed_source_id_in_decision_reference(self):
        d=good();d['decisions'][1]['source_ids']=[['unhashable']]
        self.assertTrue(aud.audit(d)[0])
    def test_malformed_decision_id_must_not_crash(self):
        d=good();d['decisions'][0]['id']=['unhashable']
        self.assertTrue(aud.audit(d)[0])
    def test_malformed_re_read_id_must_not_crash(self):
        d=good();d['read_again'][0]['source_id']=['unhashable']
        self.assertTrue(aud.audit(d)[0])
    def test_malformed_claim_reference_must_not_crash(self):
        d=good();d['claims'][0]['source_ids']=[['unhashable']]
        self.assertTrue(aud.audit(d)[0])
    def test_malformed_perspective_anchor_must_not_crash(self):
        d=good();d['perspectives'][0]['source_ids']=[['unhashable']]
        self.assertTrue(aud.audit(d)[0])
    def test_malformed_edge_id_must_not_crash(self):
        d=good();d['relations'][0]['from']=['unhashable']
        self.assertTrue(aud.audit(d)[0])
    def test_duplicate_perspective_ids(self):
        d=good();d['perspectives'][1]['id']='P1'
        self.assertTrue(aud.audit(d)[0])
    def test_bad_claim_status(self):
        d=good();d['claims'][0]['status']='i_am_a_verified_oracle'
        self.assertTrue(aud.audit(d)[0])
    def test_research_claim_needs_read_footprint(self):
        d=good();d['claims'][0]['status']='belegt';d['claims'][0]['source_ids']=['S3']
        self.assertTrue(aud.audit(d)[0])
    def test_missing_source_evidence_not_fixed_by_self_report(self):
        d=good();d['sources'][0]['read_evidence']=''
        self.assertTrue(aud.audit(d)[0])
    def test_empty_required_reread_reason(self):
        d=good();d['read_again'][0]['why']=' '
        self.assertTrue(aud.audit(d)[0])

if __name__=='__main__':unittest.main()
