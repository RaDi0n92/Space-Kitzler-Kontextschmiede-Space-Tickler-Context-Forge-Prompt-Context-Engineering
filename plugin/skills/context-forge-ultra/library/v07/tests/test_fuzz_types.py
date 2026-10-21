import copy
import random
import unittest
from test_adversarial import aud,good

class DefensiveTypes(unittest.TestCase):
    def test_many_malformed_values_never_crash(self):
        random.seed(17)
        paths=[('sources',0,'id'),('sources',0,'read_status'),('sources',0,'actually_read'),('sources',0,'accessible_to_next'),('sources',0,'read_evidence'),('decisions',0,'id'),('decisions',0,'source_ids'),('decisions',0,'status'),('decisions',0,'superseded_by'),('read_again',0,'source_id'),('read_again',0,'accessible_to_next'),('claims',0,'source_ids'),('claims',0,'status'),('perspectives',0,'source_ids'),('perspectives',0,'id'),('relations',0,'from'),('relations',0,'relation')]
        invalid=[[],[1],{'x':'y'},None,42,False,'',123.5]
        for j in range(300):
            obj=copy.deepcopy(good())
            collection,idx,key=random.choice(paths)
            obj[collection][idx][key]=random.choice(invalid)
            with self.subTest(index=j,key=key):
                issues,warnings=aud.audit(obj)
                self.assertIsInstance(issues,list)
                self.assertIsInstance(warnings,list)

if __name__=='__main__':unittest.main()
