import json,math,hashlib
from pathlib import Path
from measure import lookup_measure,prefix_surprisal
O=Path(__file__).resolve().parent
A={'a':{'version':'v1','value':10},'b':{'version':'v1','value':10},'c':{'version':'v1','value':30}}
checks=[]
def case(name,initial,final,early,needed,expected,**kwargs):
 r=lookup_measure(initial,final,early,needed,**kwargs)
 for k,v in expected.items():assert r[k]==v,(name,k,r[k],v)
 assert r['binary_usefulness'] is None and not r['research_label_created']
 checks.append({'name':name,'status':'PASS','measurement':r})
case('exact_reuse',A,A,['a'],['a'],{'final_task_correct':True,'verified_consumed_fraction':1.,'fresh_lookup_units':0})
case('narrowing_keeps_work',A,A,['a','b','c'],['b'],{'final_task_correct':True,'verified_consumed_fraction':1/3,'fresh_lookup_units':0})
case('same_output_different_target',A,A,['a'],['b'],{'final_task_correct':True,'verified_consumed_early_units':0,'fresh_lookup_units':1})
case('unused_early_work_task_still_succeeds',A,A,['a'],['a'],{'final_task_correct':True,'verified_consumed_early_units':0,'fresh_lookup_units':1},use_cache=False)
case('stale_version_same_value',A,{**A,'a':{'version':'v2','value':10}},['a'],['a'],{'verified_consumed_early_units':0,'fresh_lookup_units':1})
case('stale_version_changed_value',A,{**A,'a':{'version':'v2','value':99}},['a'],['a'],{'final_task_correct':True,'verified_consumed_early_units':0,'fresh_lookup_units':1})
case('mixed_reuse_and_new_lookup',A,A,['a'],['a','c'],{'final_task_correct':True,'verified_consumed_early_units':1,'fresh_lookup_units':1})
case('changed_action_type',A,A,['a'],['a'],{'final_task_correct':True,'verified_consumed_early_units':0,'fresh_lookup_units':0},operation='count')
case('empty_early_work',A,A,[],['a'],{'verified_consumed_fraction':None,'early_lookup_units':0})
case('corrupted_cache_detected',A,A,['a'],['a'],{'final_task_correct':False,'verified_consumed_early_units':0,'avoided_lookup_units_if_task_correct':None},tamper={'a':99})
case('missing_final_environment',A,{},['a'],['a'],{'status':'UNRESOLVED_FIXTURE'})
case('missing_version_evidence',{'a':{'version':None,'value':10}},A,['a'],['a'],{'status':'UNRESOLVED_FIXTURE'})
for name,args in [('duplicate_keys',(A,A,['a','a'],['a'])),('unsupported_operation',(A,A,['a'],['a']))]:
 try:lookup_measure(*args,**({'operation':'execute_shell'} if name=='unsupported_operation' else {}))
 except ValueError:checks.append({'name':name,'status':'PASS','expected_rejection':True})
 else:raise AssertionError(name)
# Explicit distributions expose shifting mistakes; final row must not predict itself.
r=prefix_surprisal([0,1,0],[[0,math.log(3)],[math.log(4),0],[1000,-1000]])
assert abs(r['sum_nll']-(-math.log(.75)-math.log(.8)))<1e-12
r2=prefix_surprisal([0,1,0],[[0,math.log(3)],[math.log(4),0],[-1000,1000]])
assert r==r2;checks.append({'name':'surprisal_shift_and_unused_final_logit_row','status':'PASS','measurement':r})
assert prefix_surprisal([0],[[0,0]])['mean_nll'] is None;checks.append({'name':'one_token_has_no_scored_continuation','status':'PASS'})
try:prefix_surprisal([0,1],[[0,0]])
except ValueError:checks.append({'name':'active_logits_coverage_rejection','status':'PASS','expected_rejection':True})
else:raise AssertionError('shape')
report={'status':'PASS_SOFTWARE_ONLY','checks':checks,'count':len(checks),'research_cases_validated':0,'human_G1':'PENDING_DEFERRED','real_model_surprisal_computed':False,'binary_labels_created':0,'source_sha256':hashlib.sha256((O/'measure.py').read_bytes()).hexdigest()}
(O/'SOFTWARE_QA.json').write_text(json.dumps(report,indent=2)+'\n');print('PASS:',len(checks),'software checks; zero research labels or dataset validation claims')
