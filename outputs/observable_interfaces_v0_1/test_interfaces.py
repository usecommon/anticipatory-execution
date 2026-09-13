import argparse,copy,hashlib,json,math,traceback
from pathlib import Path
from observable import prefix_nll,action_probabilities,canonical_action,persistence,ACTIONS
from capture import SurprisalSidecar,CONTRACT
P=Path(__file__).resolve().parent

def main(out):
    out.mkdir(parents=True,exist_ok=False);checks=[]
    def run(name,fn):
        try:fn();checks.append({'name':name,'status':'PASS'})
        except Exception:checks.append({'name':name,'status':'FAIL_PRESERVED','traceback':traceback.format_exc()})
    def equal(a,b):assert a==b,(a,b)
    def rejects(fn):
        try:fn()
        except ValueError:return
        raise AssertionError('Expected rejection')
    rows=[[0,math.log(3)],[math.log(4),0],[1000,-1000]]
    def shifted():assert abs(prefix_nll([0,1,0],rows)['sum_nll']+math.log(.75)+math.log(.8))<1e-12
    run('causal_token_shift',shifted)
    run('unused_final_row',lambda:equal(prefix_nll([0,1,0],rows),prefix_nll([0,1,0],rows[:2]+[[-1000,1000]])))
    run('singleton_unscored',lambda:equal(prefix_nll([0],[[0,0]])['mean_nll'],None))
    run('active_row_mismatch_rejected',lambda:rejects(lambda:prefix_nll([0,1],[[0,0]])))
    run('nonfinite_rejected',lambda:rejects(lambda:prefix_nll([0],[[float('nan'),0]])))
    run('vocabulary_id_rejected',lambda:rejects(lambda:prefix_nll([0,2],[[0,0],[0,0]])))
    codes=dict(zip(ACTIONS,[0,1,2]))
    def mass():
        p=action_probabilities([0,0,0,0],codes);assert p['support_mass']==.75 and p['outside_support_mass']==.25
        assert all(abs(x-1/3)<1e-12 for x in p['conditional_on_declared_codes'].values())
    run('raw_and_conditional_probability_distinction',mass)
    def tiny():
        p=action_probabilities([-1000,-1001,-1002,0],codes)
        assert p['support_mass']==0 and p['outside_support_mass']==1 and abs(sum(p['conditional_on_declared_codes'].values())-1)<1e-12
    run('tiny_support_mass_not_hidden_by_normalization',tiny)
    run('ambiguous_code_tokens_rejected',lambda:rejects(lambda:action_probabilities([0,0,0],dict(zip(ACTIONS,[0,0,1])))))
    run('missing_action_support_rejected',lambda:rejects(lambda:action_probabilities([0,0,0],{'abstain':0})))
    a={'operation':'ls','directory':'/a','a':True};b={**a,'a':False}
    run('typed_identity_independent_of_dict_order',lambda:equal(canonical_action(a,'/a'),canonical_action(dict(reversed(list(a.items()))),'/a')))
    run('argument_change_and_missing_history',lambda:equal(persistence([a,a,b,None,a],['/a']*5)['same_action_transitions'],[True,False,None,None]))
    run('other_target_rejected',lambda:rejects(lambda:canonical_action(a,'/b')))
    class IDs:
        def __init__(self,v):self.v=v
        def __len__(self):return len(self.v)
        def tolist(self):return list(self.v)
    class Padded:
        def __getitem__(self,k):return IDs([0,1][k[1]])
    class Logits:
        dtype='torch.float32';shape=(2,152064)
        def __init__(self):self.rows=[[0.]*152064,[0.]*152064]
        def __len__(self):return 2
        def __getitem__(self,i):return self.rows[i]
    class Fake:
        contract_id=CONTRACT
        def __init__(self):self.calls=0;self.state={'contract_id':CONTRACT,'active_length':2,'logits':Logits(),'input_ids':Padded(),'hidden':object()}
        def extract_ids(self,ids):self.calls+=1;self.last_ids=ids;return self.state
    def proxy():
        f=Fake();ids=IDs([0,1]);wrapper=SurprisalSidecar(f,out/'sidecar');state=wrapper.extract_ids(ids)
        assert state is f.state and f.last_ids is ids and f.calls==1
        r=json.loads((out/'sidecar/00000.json').read_text());assert r['ordinal']==0
        assert abs(r['measurement']['mean_nll']-math.log(152064))<1e-12
        assert all(v==0 for row in state['logits'].rows for v in row)
    run('capture_proxy_same_state_and_ID_objects',proxy)
    def badstate():
        f=Fake();f.state['logits'].shape=(2,2)
        rejects(lambda:SurprisalSidecar(f,out/'bad_sidecar').extract_ids(IDs([0,1])))
    run('capture_rejects_wrong_canonical_vocab',badstate)
    report={'status':'PASS_SOFTWARE_ONLY' if all(c['status']=='PASS' for c in checks) else 'FAIL_PRESERVED','checks':checks,
            'passed':sum(c['status']=='PASS' for c in checks),'real_torch_or_model_used':False,'real_model_bridge_passed':False,'full_B1_complete':False,
            'source_sha256':{n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in ['observable.py','capture.py','test_interfaces.py']}}
    (out/'QA.json').write_text(json.dumps(report,indent=2)+'\n');print(report['status'],report['passed'],'checks')
    if report['status']!='PASS_SOFTWARE_ONLY':raise SystemExit(1)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args();main(a.out)
