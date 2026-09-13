import modal
from pathlib import Path
O=Path(__file__).resolve().parent
app=modal.App('aeb-exploratory-diagnostic-fit-recovery-v0-1')
base=modal.Image.debian_slim(python_version='3.11').pip_install('torch==2.5.1','numpy==1.26.4','scipy==1.14.1','scikit-learn==1.5.2')
if modal.is_local():base=base.add_local_file(O/'fit.py','/src/fit.py')
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
 import json,datetime,hashlib,traceback
 run=O/"run_20260913T013948081119Z"
 recovery=O/('fit_recovery_'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'));recovery.mkdir()
 (recovery/'REQUEST.json').write_text(json.dumps({'feature_sha256':hashlib.sha256((run/'FEATURES.json').read_bytes()).hexdigest(),'fit_source_sha256':hashlib.sha256((O/'fit.py').read_bytes()).hexdigest(),'launcher_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'source_run':run.name,'change':'JSON scalar serialization only'},indent=2))
 conversions=[]
 def clean(obj,path='root'):
  if isinstance(obj,dict):return {k:clean(v,path+'.'+str(k)) for k,v in obj.items()}
  if isinstance(obj,list):return [clean(v,path+'['+str(i)+']') for i,v in enumerate(obj)]
  if type(obj).__module__.startswith('numpy') and hasattr(obj,'item'):
   conversions.append({'path':path,'type':type(obj).__name__});return obj.item()
  return obj
 try:
  result=fit_diagnostic.remote(json.loads((O/'LABELS.json').read_text()),json.loads((run/'FEATURES.json').read_text()),json.loads((O/'CASES.json').read_text()),json.loads((O/'PRIOR_LABELS.json').read_text()))
  result=clean(result);destination=run/'RESULT.json'
  if destination.exists():raise FileExistsError(destination)
  destination.write_text(json.dumps(result,indent=2));(recovery/'SERIALIZATION.json').write_text(json.dumps({'status':'PASS','conversions':conversions},indent=2));print(result['status'],flush=True)
 except BaseException:
  (recovery/'FAILURE.txt').write_text(traceback.format_exc());raise
