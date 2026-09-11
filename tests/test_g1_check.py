import copy,sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from g1_check import evaluate,CONTEXT,LABEL,SECONDARY

def fixtures():
    rows=[]
    for i in range(200):
        row={k:str(i) for k in CONTEXT};row[LABEL]=None
        row.update(dict(zip(SECONDARY,[None,None,None,None])));rows.append(row)
    return rows

def label(rows,values):
    rows=copy.deepcopy(rows)
    for r,v in zip(rows,values):
        r[LABEL]=v;r.update(dict(zip(SECONDARY,[float(v),3,'N','Synthetic test only'])))
    return rows

class G1Checks(unittest.TestCase):
    def setUp(self):self.ref=fixtures()
    def test_empty_is_pending(self):
        r=evaluate(self.ref,self.ref,self.ref);self.assertEqual(r['completed_pairs'],0);self.assertIsNone(r['kappa'])
    def test_identical_nondegenerate(self):
        a=label(self.ref,[0]*100+[1]*100);r=evaluate(self.ref,a,list(reversed(a)))
        self.assertEqual(r['kappa'],1);self.assertEqual(r['G1'],'PENDING')
    def test_degenerate_not_one(self):
        a=label(self.ref,[0]*200);r=evaluate(self.ref,a,a);self.assertIsNone(r['kappa']);self.assertEqual(r['binary_reliability'],'DEGENERATE')
    def test_exact_threshold(self):
        a=label(self.ref,[0]*100+[1]*100);b=label(self.ref,[1]*15+[0]*85+[0]*15+[1]*85)
        r=evaluate(self.ref,a,b);self.assertEqual(r['kappa'],.7);self.assertEqual(r['binary_reliability'],'MEETS_THRESHOLD')
    def test_below_threshold(self):
        a=label(self.ref,[0]*100+[1]*100);b=label(self.ref,[1]*16+[0]*84+[0]*16+[1]*84)
        self.assertEqual(evaluate(self.ref,a,b)['binary_reliability'],'BELOW_THRESHOLD')
    def test_missing_one_blocks_statistic(self):
        a=label(self.ref,[0]*100+[1]*100);b=copy.deepcopy(a);b[0][LABEL]=None
        self.assertIsNone(evaluate(self.ref,a,b)['kappa'])
    def test_invalid_labels_rejected(self):
        for value in [True,'=Other!A1','0',-1,2,float('nan')]:
            a=copy.deepcopy(self.ref);a[0][LABEL]=value
            with self.assertRaises(ValueError):evaluate(self.ref,a,self.ref)
    def test_duplicate_rejected(self):
        with self.assertRaises(ValueError):evaluate(self.ref,self.ref[:-1]+[self.ref[0]],self.ref)
    def test_context_change_rejected(self):
        a=copy.deepcopy(self.ref);a[0]['candidate_action']='changed'
        with self.assertRaises(ValueError):evaluate(self.ref,a,self.ref)
    def test_secondary_missing_retained(self):
        a=label(self.ref,[0]*100+[1]*100);a[0][SECONDARY[3]]=None
        r=evaluate(self.ref,a,a);self.assertEqual(len(r['missing_secondary_fields']['A']),1);self.assertEqual(r['G1'],'PENDING')

if __name__ == '__main__':unittest.main()
