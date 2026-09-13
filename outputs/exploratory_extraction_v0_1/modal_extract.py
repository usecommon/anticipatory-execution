import modal
from pathlib import Path
O=Path(__file__).resolve().parent;R=O.parents[1] if modal.is_local() else Path('/')
app=modal.App('aeb-exploratory-extraction-v0-1')
base=modal.Image.debian_slim(python_version='3.11').pip_install('torch==2.5.1','transformers==4.45.2','accelerate==0.34.2','numpy==1.26.4','huggingface_hub==0.25.2')
if modal.is_local():
 import json
 freeze=json.loads((O/'FREEZE.json').read_text())
 for name,rel in freeze['local_files'].items():base=base.add_local_file(R/rel,'/src/'+name)
 base=base.add_local_file(O/'FREEZE.json','/src/FREEZE.json')
models=modal.Volume.from_name('aeb-qwen-pinned-model-v0-2')
evidence=modal.Volume.from_name('aeb-exploratory-extraction-v0-1',create_if_missing=True)
@app.function(image=base,gpu='A100-40GB',cpu=2,memory=49152,timeout=2400,retries=0,max_containers=1,single_use_containers=True,volumes={'/model':models.with_mount_options(read_only=True),'/evidence':evidence})
def extract(label):
 import subprocess,os,time,json,hashlib,threading
 root=Path('/evidence')/label;root.mkdir(exist_ok=False);start=time.time()
 hw=subprocess.run(['nvidia-smi','--query-gpu=name,uuid,driver_version','--format=csv'],capture_output=True,text=True)
 (root/'hardware.json').write_text(json.dumps({'stdout':hw.stdout,'stderr':hw.stderr,'container_id':os.getenv('MODAL_TASK_ID')},indent=2))
 env=os.environ.copy();env['CUBLAS_WORKSPACE_CONFIG']=':4096:8'
 done=threading.Event()
 def progress():
  while not done.wait(30):
   p=root/'extraction/progress.jsonl';count=sum(1 for _ in p.open()) if p.exists() else 0
   print(f'Progress: {count}/4013 saved; {time.time()-start:.0f}s worker wall time',flush=True)
 threading.Thread(target=progress,daemon=True).start()
 try:
  with (root/'worker.log').open('w') as log:
   try:code=subprocess.run(['python','-u','/src/worker.py',str(root)],env=env,stdout=log,stderr=subprocess.STDOUT,timeout=2100).returncode
   except subprocess.TimeoutExpired:code='TIMEOUT'
 finally:done.set()
 record={'exit':code,'seconds':time.time()-start,'label':label,'status':'PASS' if code==0 and (root/'WORKER_RESULT.json').exists() else 'BLOCKED'}
 (root/'EXECUTION.json').write_text(json.dumps(record,indent=2))
 # Hash all artifacts with bounded memory, including partial outputs on failure.
 hashes={}
 for p in root.rglob('*'):
  if not p.is_file():continue
  h=hashlib.sha256()
  with p.open('rb') as f:
   for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
  hashes[str(p.relative_to(root))]=h.hexdigest()
 (root/'HASHES.json').write_text(json.dumps(hashes,indent=2));evidence.commit()
 texts={str(p.relative_to(root)):p.read_text() for p in root.rglob('*') if p.is_file() and p.suffix in ['.json','.jsonl','.log']}
 return {'execution':record,'artifacts':texts,'volume':'aeb-exploratory-extraction-v0-1','path':label}
@app.function(image=base,cpu=2,memory=8192,timeout=1200,retries=0,max_containers=1,volumes={'/evidence':evidence.with_mount_options(read_only=True)})
def verify_saved(label):
 import json,hashlib,time,os,torch
 torch.set_num_threads(2);start=time.time();root=Path('/evidence')/label
 def sha(p):
  h=hashlib.sha256()
  with p.open('rb') as f:
   for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
  return h.hexdigest()
 manifest=json.loads((root/'extraction/manifest.json').read_text());inputs=[json.loads(x) for x in Path('/src/research.jsonl').read_text().splitlines()]
 preflight={r['id']:r for r in json.loads(Path('/src/preflight.json').read_text())['rows']}
 assert manifest['status']=='PASS' and manifest['partition']=='exploratory' and manifest['confirmatory'] is False
 assert len(inputs)==len(manifest['items'])==4013
 contract=manifest['contract_id'];assert contract=='95dd7686f82fc1380c02539ec14fc73ab3073fc8be7b7ca015e40fd6e4fac1b0'
 hashes=json.loads((root/'HASHES.json').read_text());bytes_total=0;checked=[]
 for r,inp in zip(manifest['items'],inputs):
  path=root/'extraction'/r['file'];actual=sha(path)
  assert actual==r['sha256']==hashes['extraction/'+r['file']]
  assert r['id']==inp['id'] and r['prefix_sha256']==hashlib.sha256(inp['prefix'].encode()).hexdigest()
  assert r['token_ids']==preflight[r['id']]['token_ids'] and r['contract_id']==contract
  d=torch.load(path,map_location='cpu',weights_only=True);n=r['active_length']
  assert set(d)=={'contract_id','input_ids','attention_mask','position_ids','active_length','hidden_last','logits_last'}
  assert d['contract_id']==contract and d['active_length']==n
  assert d['hidden_last'].shape==(29,3584) and d['logits_last'].shape==(152064,)
  assert d['hidden_last'].dtype==d['logits_last'].dtype==torch.float32
  assert torch.isfinite(d['hidden_last']).all() and torch.isfinite(d['logits_last']).all()
  assert d['input_ids'].shape==(1,128) and d['input_ids'][0,:n].tolist()==r['token_ids']
  assert (d['input_ids'][0,n:]==151643).all()
  assert d['attention_mask'].shape==(1,128) and d['attention_mask'][0,:n].all() and not d['attention_mask'][0,n:].any()
  assert torch.equal(d['position_ids'],torch.arange(128).unsqueeze(0))
  bytes_total+=path.stat().st_size;checked.append({'id':r['id'],'sha256':actual})
  if len(checked)%500==0:print(f'Independent verification: {len(checked)}/4013',flush=True)
 assert len(list((root/'extraction').glob('*.pt')))==4013
 audit=json.loads((root/'forward_audit.json').read_text());assert len(audit)==4013
 assert all(x['contract_id']==contract and x['shape']==[1,128] and x['mask_shape']==[1,1,128,128] and x['cache'] is False for x in audit)
 for name,h in hashes.items():
  if not name.endswith('.pt'):assert sha(root/name)==h
 return {'status':'PASS','checked_tensors':4013,'tensor_bytes':bytes_total,'seconds':time.time()-start,'container_id':os.getenv('MODAL_TASK_ID'),'independent_CPU_worker':True,'all_hashes_shapes_tokens_masks_positions_finite_pass':True,'checked':checked,'contract_id':contract,'manifest_sha256':sha(root/'extraction/manifest.json')}
@app.local_entrypoint()
def main():
 import json,datetime,traceback,hashlib
 run=O/('run_'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'));run.mkdir()
 (run/'REQUEST.json').write_text(json.dumps({'freeze_sha256':hashlib.sha256((O/'FREEZE.json').read_bytes()).hexdigest(),'launcher_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'plan_sha256':hashlib.sha256((O/'RUN_PLAN.json').read_bytes()).hexdigest()},indent=2))
 try:
  result=extract.remote(run.name);(run/'EXTRACTION_RESULT.json').write_text(json.dumps(result,indent=2));print('Extraction:',result['execution'],flush=True)
  if result['execution']['status']!='PASS':raise RuntimeError('Extraction blocked; all returned evidence preserved')
  checked=verify_saved.remote(run.name);(run/'VERIFICATION.json').write_text(json.dumps(checked,indent=2));print('Verification:',{k:v for k,v in checked.items() if k!='checked'},flush=True)
 except BaseException:
  (run/'LOCAL_FAILURE.txt').write_text(traceback.format_exc());raise
