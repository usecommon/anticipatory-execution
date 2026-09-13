import modal
from pathlib import Path
O=Path(__file__).resolve().parent;R=O.parents[1] if modal.is_local() else Path("/")
app=modal.App('aeb-exploratory-entrypoint-validation-v0-1')
base=modal.Image.debian_slim(python_version='3.11').pip_install('torch==2.5.1','transformers==4.45.2','accelerate==0.34.2','numpy==1.26.4','huggingface_hub==0.25.2')
files={}
if modal.is_local():
 files={name:O/name for name in ['entrypoint.py','checks.py','VALIDATION_INPUT.jsonl']}
 files.update({'extractor.py':R/'outputs/g0_closure_v0_5/source/extractor.py','pipeline.py':R/'outputs/g0_closure_v0_5/source/pipeline.py','research.jsonl':R/'outputs/exploratory_preflight_v0_1/EXTRACTION_INPUT.jsonl','preflight.json':next((R/'outputs/exploratory_preflight_v0_1').glob('run_*/RESULT.json'))})
 for name,p in files.items():base=base.add_local_file(p,'/src/'+name)
models=modal.Volume.from_name('aeb-qwen-pinned-model-v0-2')
evidence=modal.Volume.from_name('aeb-exploratory-entrypoint-v0-1',create_if_missing=True)
@app.function(image=base,cpu=1,memory=4096,timeout=300,retries=0,max_containers=1)
def cpu_validate():
 import sys,json,tempfile
 sys.path.insert(0,'/src');from checks import software_checks
 with tempfile.TemporaryDirectory() as td:
  checks=software_checks(Path(td)/'tests','/src/VALIDATION_INPUT.jsonl','/src/research.jsonl','/src/preflight.json')
  artifacts={str(p.relative_to(td)):p.read_text() for p in Path(td).rglob('*') if p.is_file() and p.suffix in ['.json','.jsonl'] and p.name not in ['research.jsonl']}
 return {'status':'PASS','checks':checks,'artifacts':artifacts,'synthetic_tensors_only':True,'gpu':False}
@app.function(image=base,gpu='A100-40GB',cpu=2,memory=49152,timeout=900,retries=0,max_containers=1,single_use_containers=True,volumes={'/model':models.with_mount_options(read_only=True),'/evidence':evidence})
def gpu_validate(identity,label):
 import sys,json,os,time,traceback,subprocess,hashlib
 sys.path.insert(0,'/src');os.environ['CUBLAS_WORKSPACE_CONFIG']=':4096:8'
 root=Path('/evidence')/label;root.mkdir(exist_ok=False);start=time.time()
 hardware=subprocess.run(['nvidia-smi','--query-gpu=name,uuid,driver_version','--format=csv'],capture_output=True,text=True)
 (root/'hardware.json').write_text(json.dumps({'stdout':hardware.stdout,'stderr':hardware.stderr,'container_id':os.getenv('MODAL_TASK_ID')}))
 try:
  import torch
  from extractor import load_extractor,file_hash
  from entrypoint import run_job,CONTRACT,PINS
  from pipeline import run_prefix_job
  assert file_hash('/src/extractor.py')==PINS['extractor']['sha256']
  assert file_hash('/src/pipeline.py')==PINS['original_pipeline']['sha256']
  e=load_extractor('/model',identity);assert e.contract_id==CONTRACT
  items=[json.loads(x) for x in Path('/src/VALIDATION_INPUT.jsonl').read_text().splitlines()]
  old=run_prefix_job(e,items,root/'original',partition='qa')
  new=run_job(e,'/src/VALIDATION_INPUT.jsonl',root/'new',partition='instrumentation_validation')
  comparisons=[]
  for a,b in zip(old['items'],new['items']):
   x=torch.load(root/'original'/a['file'],weights_only=True);y=torch.load(root/'new'/b['file'],weights_only=True)
   assert x.keys()==y.keys()
   for k in x:
    equal=torch.equal(x[k],y[k]) if isinstance(x[k],torch.Tensor) else x[k]==y[k]
    assert equal,(a['id'],k)
   comparisons.append({'id':a['id'],'all_fields_bitwise_equal':True,'fields':list(x)})
  before=len(e.audit)
  try:run_job(e,'/src/VALIDATION_INPUT.jsonl',root/'confirmatory_rejection',partition='confirmatory')
  except ValueError:pass
  else:raise AssertionError('confirmatory accepted')
  assert len(e.audit)==before==24
  assert all(r['shape']==[1,128] and r['mask_shape']==[1,1,128,128] and r['cache'] is False for r in e.audit)
  result={'status':'PASS','contract_id':e.contract_id,'comparisons':comparisons,'actual_forward_count':len(e.audit),'confirmatory_rejection_zero_forwards':True,'audit':e.audit,'seconds':time.time()-start,'max_cuda_memory':torch.cuda.max_memory_allocated(),'research_extraction':False,'human_G1':'PENDING_DEFERRED'}
  (root/'RESULT.json').write_text(json.dumps(result,indent=2))
 except BaseException:
  result={'status':'BLOCKED','traceback':traceback.format_exc(),'seconds':time.time()-start,'research_extraction':False}
  (root/'FAILURE.json').write_text(json.dumps(result,indent=2))
 finally:
  inventory={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in root.rglob('*') if p.is_file()}
  (root/'HASHES.json').write_text(json.dumps(inventory,indent=2));evidence.commit()
 return {'result':result,'artifacts':{str(p.relative_to(root)):p.read_text() for p in root.rglob('*') if p.is_file() and p.suffix in ['.json','.jsonl']},'remote_volume':'aeb-exploratory-entrypoint-v0-1','remote_path':label}
@app.local_entrypoint()
def main():
 import json,datetime,hashlib,traceback
 run=O/('validation_'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'));run.mkdir()
 (run/'SOURCE_FREEZE.json').write_text(json.dumps({str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [*files.values(),Path(__file__)]},indent=2))
 try:
  cpu=cpu_validate.remote();(run/'CPU_RESULT.json').write_text(json.dumps(cpu,indent=2));assert cpu['status']=='PASS'
  print('CPU checks PASS:',len(cpu['checks']),flush=True)
  identity=json.loads((R/'outputs/g0_closure_v0_5/checkpoint_identity.json').read_text())
  gpu=gpu_validate.remote(identity,run.name);(run/'GPU_RESULT.json').write_text(json.dumps(gpu,indent=2));print(json.dumps(gpu['result'],indent=2),flush=True)
  if gpu['result']['status']!='PASS':raise RuntimeError('GPU validation blocked; evidence preserved')
 except BaseException:
  (run/'LOCAL_FAILURE.txt').write_text(traceback.format_exc());raise
