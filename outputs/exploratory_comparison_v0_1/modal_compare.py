import modal
from pathlib import Path
O=Path(__file__).resolve().parent
app=modal.App('aeb-exploratory-diagnostic-comparison-v0-1')
base=modal.Image.debian_slim(python_version='3.11').pip_install('torch==2.5.1','numpy==1.26.4','scipy==1.14.1','scikit-learn==1.5.2')
if modal.is_local():
 for name in ['features.py','fit.py','CASES.json','TENSOR_MANIFEST.json']:base=base.add_local_file(O/name,'/src/'+name)
evidence=modal.Volume.from_name('aeb-exploratory-extraction-v0-1')
@app.function(image=base,cpu=2,memory=8192,timeout=600,retries=0,max_containers=4,volumes={'/evidence':evidence.with_mount_options(read_only=True)})
def derive(start,end):
 import sys,json,hashlib,io,torch,time,os
 sys.path.insert(0,'/src');from features import build,selftest
 torch.set_num_threads(2);t=time.time();qa=selftest()
 cases=json.loads(Path('/src/CASES.json').read_text());manifest=json.loads(Path('/src/TENSOR_MANIFEST.json').read_text());records={r['id']:r for r in manifest['items']}
 assert 0<=start<end<=200 and end-start<=10
 cache={};out=[];used={}
 for case in cases[start:end]:
  assert set(case)=={'item_id','prefix','candidate_text','execution_class','input_ids'} and len(case['input_ids'])==3
  states=[]
  for id in case['input_ids']:
   if id not in cache:
    r=records[id];p=Path('/evidence/run_20260913T003027625834Z/extraction')/r['file'];blob=p.read_bytes();h=hashlib.sha256(blob).hexdigest();assert h==r['sha256']
    d=torch.load(io.BytesIO(blob),map_location='cpu',weights_only=True);assert d['contract_id']==manifest['contract_id']=='95dd7686f82fc1380c02539ec14fc73ab3073fc8be7b7ca015e40fd6e4fac1b0'
    assert d['input_ids'][0,:d['active_length']].tolist()==r['token_ids']
    cache[id]=d;used[id]=h
   states.append(cache[id])
  assert records[case['input_ids'][-1]]['prefix_sha256']==hashlib.sha256(case['prefix'].encode()).hexdigest()
  out.append(build(case,states))
 return {'status':'PASS','rows':out,'tensor_hashes':used,'analytic_QA':qa,'start':start,'end':end,'seconds':time.time()-t,'container_id':os.getenv('MODAL_TASK_ID'),'GPU':False}
@app.function(image=base,cpu=2,memory=8192,timeout=600,retries=0,max_containers=1)
def fit_diagnostic(rows,features,cases,prior):
 import sys,time,sklearn,numpy,scipy,threadpoolctl
 sys.path.insert(0,'/src');from fit import run
 assert sklearn.__version__=='1.5.2' and numpy.__version__=='1.26.4' and scipy.__version__=='1.14.1'
 t=time.time()
 with threadpoolctl.threadpool_limits(limits=2):result=run(rows,features,cases,prior)
 result['seconds']=time.time()-t;result['versions']={'sklearn':sklearn.__version__,'numpy':numpy.__version__,'scipy':scipy.__version__}
 return result
@app.local_entrypoint()
def main():
 import json,datetime,hashlib,traceback,concurrent.futures
 run=O/('run_'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'));run.mkdir()
 paths=[p for p in O.iterdir() if p.suffix in ['.py','.json','.md']]
 (run/'PRE_FIT_FREEZE.json').write_text(json.dumps({p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},indent=2))
 try:
  def one(i):
   r=derive.remote(i,i+10);(run/f'features_{i:03}.json').write_text(json.dumps(r,indent=2));print(f'Features {i}:{i+10} PASS',flush=True);return r
  with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:parts=list(pool.map(one,range(0,200,10)))
  features=[r for p in parts for r in p['rows']];assert len(features)==len({r['item_id'] for r in features})==200
  f=run/'FEATURES.json';f.write_text(json.dumps(features,indent=2));(run/'FEATURE_FREEZE.json').write_text(json.dumps({'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'rows':200,'before_any_fit':True},indent=2))
  result=fit_diagnostic.remote(json.loads((O/'LABELS.json').read_text()),features,json.loads((O/'CASES.json').read_text()),json.loads((O/'PRIOR_LABELS.json').read_text()))
  (run/'RESULT.json').write_text(json.dumps(result,indent=2));print(result['status'],flush=True)
  print(json.dumps({k:v['metrics'] for k,v in result['scenarios'].items()},indent=2),flush=True)
 except BaseException:
  (run/'FAILURE.txt').write_text(traceback.format_exc());raise
