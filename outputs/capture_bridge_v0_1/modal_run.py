import modal
from pathlib import Path
O=Path(__file__).resolve().parent;R=O.parents[1] if modal.is_local() else Path('/repo')
app=modal.App('aeb-canonical-surprisal-bridge-v1')
image=modal.Image.debian_slim(python_version='3.11').pip_install('torch==2.5.1','transformers==4.45.2','accelerate==0.34.2','numpy==1.26.4','huggingface_hub==0.25.2')
files={}
if modal.is_local():
 paths=['outputs/observable_interfaces_v0_1/'+n for n in ['observable.py','capture.py','bridge.py']]+['outputs/exploratory_entrypoint_v0_1/'+n for n in ['entrypoint.py','VALIDATION_INPUT.jsonl']]+['outputs/g0_closure_v0_5/source/'+n for n in ['extractor.py','pipeline.py']]
 files={rel:R/rel for rel in paths}
 for rel,p in files.items():image=image.add_local_file(p,'/repo/'+rel)
models=modal.Volume.from_name('aeb-qwen-pinned-model-v0-2')
evidence=modal.Volume.from_name('aeb-surprisal-bridge-v0-1',create_if_missing=True)
@app.function(image=image,gpu='A100-40GB',cpu=2,memory=49152,timeout=900,retries=0,max_containers=1,single_use_containers=True,volumes={'/model':models.with_mount_options(read_only=True),'/evidence':evidence})
def validate(identity,label):
 import sys,os,json,time,traceback,hashlib,subprocess
 os.environ['CUBLAS_WORKSPACE_CONFIG']=':4096:8'
 sys.path[:0]=['/repo/outputs/observable_interfaces_v0_1','/repo/outputs/g0_closure_v0_5/source']
 root=Path('/evidence')/label;root.mkdir(exist_ok=False);start=time.time()
 device=subprocess.run(['nvidia-smi','--query-gpu=name,uuid,driver_version','--format=csv'],capture_output=True,text=True)
 (root/'hardware.json').write_text(json.dumps({'stdout':device.stdout,'stderr':device.stderr,'container_id':os.getenv('MODAL_TASK_ID')}))
 try:
  import torch
  from extractor import load_extractor
  from bridge import run_bridge
  e=load_extractor('/model',identity)
  result=run_bridge(e,Path('/repo'),root/'bridge')
  result.update(seconds=time.time()-start,peak_cuda_bytes=torch.cuda.max_memory_allocated(),audit=e.audit)
  (root/'RESULT.json').write_text(json.dumps(result,indent=2))
 except BaseException:
  result={'status':'FAIL_PRESERVED','traceback':traceback.format_exc(),'seconds':time.time()-start}
  (root/'FAILURE.json').write_text(json.dumps(result,indent=2))
 finally:
  hashes={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in root.rglob('*') if p.is_file()}
  (root/'HASHES.json').write_text(json.dumps(hashes,indent=2));evidence.commit()
 return {'result':result,'volume':'aeb-surprisal-bridge-v0-1','path':label,'artifacts':{str(p.relative_to(root)):p.read_text() for p in root.rglob('*') if p.is_file() and p.suffix in ['.json','.jsonl','.txt']}}
@app.local_entrypoint()
def main():
 import json,datetime,hashlib,traceback
 out=O/('run_'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'));out.mkdir()
 (out/'SOURCE_FREEZE.json').write_text(json.dumps({str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [*files.values(),Path(__file__)]},indent=2))
 try:
  result=validate.remote(json.loads((R/'outputs/g0_closure_v0_5/checkpoint_identity.json').read_text()),out.name)
  (out/'REMOTE_RESULT.json').write_text(json.dumps(result,indent=2));print(json.dumps(result['result'],indent=2),flush=True)
  if result['result']['status']!='PASS_CANONICAL_CAPTURE_BRIDGE':raise RuntimeError('Bridge failed; evidence preserved')
 except BaseException:
  (out/'LOCAL_FAILURE.txt').write_text(traceback.format_exc());raise
