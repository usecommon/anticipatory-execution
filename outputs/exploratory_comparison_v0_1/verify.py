"""Independent stdlib audit: reconstruct metrics from saved predictions."""
import ast,json,math,hashlib
from collections import defaultdict
from pathlib import Path
O=Path(__file__).resolve().parent;R=O.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for p,h in json.loads((O/'SOURCE_HASHES.json').read_text()).items():assert sha(R/p)==h,p
for p in O.glob('*.py'):ast.parse(p.read_text())
cases={r['item_id']:r for r in json.loads((O/'CASES.json').read_text())};labels={r['item_id']:r for r in json.loads((O/'LABELS.json').read_text())}
prior={r['item_id']:r['prior_judgment']['binary_usefulness_0_or_1'] for r in json.loads((O/'PRIOR_LABELS.json').read_text())}
tm=json.loads((O/'TENSOR_MANIFEST.json').read_text());hashes={r['id']:r['sha256'] for r in tm['items']}
found=[]
for run in O.glob('run_*'):
 if not (run/'RESULT.json').exists():continue
 for p,h in json.loads((run/'PRE_FIT_FREEZE.json').read_text()).items():assert sha(O/p)==h,p
 assert sha(run/'FEATURES.json')==json.loads((run/'FEATURE_FREEZE.json').read_text())['sha256']
 features=json.loads((run/'FEATURES.json').read_text());assert len(features)==200 and {r['item_id'] for r in features}==set(cases)==set(labels)
 used=set();parts=[]
 for p in sorted(run.glob('features_*.json')):
  d=json.loads(p.read_text());assert d['status']=='PASS' and d['analytic_QA']['status']=='PASS' and not d['GPU'];parts+=d['rows']
  for id,h in d['tensor_hashes'].items():assert hashes[id]==h;used.add(id)
 assert parts==features and used=={i for c in cases.values() for i in c['input_ids']}
 for f in features:
  assert len(f['shared'])==8 and len(f['output'])==7 and len(f['dynamics'])==19 and set(f['snapshots'])=={'7','14','21','28'}
  assert all(len(v)==64 for v in f['snapshots'].values())
  nums=f['shared']+f['output']+f['dynamics']+sum(f['snapshots'].values(),[]);assert all(math.isfinite(v) for v in nums)
  assert -1e-12<=f['output'][4]<=math.log(2)+1e-12
 d=json.loads((run/'RESULT.json').read_text());assert d['status']=='PASS_DIAGNOSTIC' and d['check_label_perturbation_invariance'] and not d['H2_H3_tested'] and not d['full_B1_implemented'] and not d['confirmatory']
 order=d['row_order'];assert order==sorted(labels)
 expected={
 'current_resolved':[labels[i]['binary_usefulness'] for i in order],
 'prior_overlap_replaced':[prior.get(i,labels[i]['binary_usefulness']) for i in order],
 'ambiguity_excluded':[labels[i]['binary_usefulness'] if labels[i]['ambiguity']=='N' else None for i in order],
 'unresolved_zero':[0 if labels[i]['binary_usefulness'] is None else labels[i]['binary_usefulness'] for i in order],
 'unresolved_one':[1 if labels[i]['binary_usefulness'] is None else labels[i]['binary_usefulness'] for i in order]}
 for name,result in d['scenarios'].items():
  y=result['labels'];assert y==expected[name]
  for model,pred in result['predictions'].items():
   assert len(pred)==200 and all(0<=p<=1 and math.isfinite(p) for p in pred)
   for split,reported in result['metrics'][model].items():
    tasks=defaultdict(list);n=pos=0
    for id,p,t in zip(order,pred,y):
     if labels[id]['split']!=split or t is None:continue
     p=min(1-1e-15,max(1e-15,p));tasks[labels[id]['task_id']].append((-t*math.log(p)-(1-t)*math.log1p(-p),(p-t)**2));n+=1;pos+=t
    assert reported['cases']==n
    if n:
     assert reported['tasks']==len(tasks) and reported['positive']==pos and reported['negative']==n-pos
     for j,key in enumerate(['NLL','Brier']):
      val=sum(sum(x[j] for x in rows)/len(rows) for rows in tasks.values())/len(tasks)
      assert abs(val-reported[key])<1e-12,(name,model,split,key)
   if model!='prevalence':
    grid=[r for r in result['grid'] if r['model']==model and r['eligible']];best=min(grid,key=lambda x:(x['tune_NLL'],x['C']))
    assert best['C']==result['models'][model]['C'] and abs(best['tune_NLL']-result['metrics'][model]['exploratory_tune']['NLL'])<1e-12
 primary=d['scenarios']['current_resolved']['metrics']
 for pair,interval in d['primary_paired_intervals'].items():
  a,b=pair.split('->');gain=primary[a]['exploratory_check']['NLL']-primary[b]['exploratory_check']['NLL'];assert abs(gain-interval['task_mean_NLL_gain'])<1e-12
 # Check result-recovery identity without changing the frozen fitting source.
 recovery=list(O.glob('fit_recovery_*/REQUEST.json'));assert len(recovery)==1
 rr=json.loads(recovery[0].read_text())
 assert rr['feature_sha256']==sha(run/'FEATURES.json') and rr['fit_source_sha256']==sha(O/'fit.py') and rr['launcher_sha256']==sha(O/'modal_fit_recovery.py')
 for scenario_name,result in d['scenarios'].items():
  for model,slices in result['check_source_slices'].items():
   for src,reported in slices.items():
    ts=defaultdict(list);n=pos=0
    for id,pred,y in zip(order,result['predictions'][model],result['labels']):
     r=labels[id]
     if r['split']!='exploratory_check' or r['source']!=src or y is None:continue
     q=min(1-1e-15,max(1e-15,pred));ts[r['task_id']].append((-y*math.log(q)-(1-y)*math.log1p(-q),(q-y)**2));n+=1;pos+=y
    assert reported['cases']==n
    if n:
     assert reported['positive']==pos and reported['negative']==n-pos
     for j,key in enumerate(['NLL','Brier']):assert abs(sum(sum(v[j] for v in a)/len(a) for a in ts.values())/len(ts)-reported[key])<1e-12
 found.append(run.name)
assert len(found)==1,found
print('PASS: frozen source/plan/features, 548 pinned tensor inputs, all 200 cases, unchanged labels and exact sensitivity rules, finite features, independent NLL/Brier recomputation, tune-only C selection, and reported check-label invariance.')
