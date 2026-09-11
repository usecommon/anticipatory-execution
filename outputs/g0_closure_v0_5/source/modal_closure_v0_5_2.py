import modal
from pathlib import Path
app=modal.App('aeb-g0-closure-v0-5')
image=(modal.Image.debian_slim(python_version='3.11')
 .pip_install('torch==2.5.1','transformers==4.45.2','accelerate==0.34.2','numpy==1.26.4','huggingface_hub==0.25.2'))
for name in ['extractor.py','pipeline.py','worker.py','fixtures.json','original_harness.py']:
 image=image.add_local_file(Path(__file__).with_name(name),'/src/'+name)
models=modal.Volume.from_name('aeb-qwen-pinned-model-v0-2')
prior=modal.Volume.from_name('aeb-g0-fix-v0-3')
evidence=modal.Volume.from_name('aeb-g0-closure-v0-5',create_if_missing=True)
@app.function(image=image,volumes={'/model':models.with_mount_options(read_only=True)},timeout=600,retries=0)
def verify_checkpoint():
 import hashlib,json,time,sys
 sys.path.insert(0,'/src')
 from pathlib import Path
 from huggingface_hub import HfApi
 from extractor import REVISION,file_hash
 info=HfApi().model_info('Qwen/Qwen2.5-7B-Instruct',revision=REVISION,files_metadata=True)
 if info.sha!=REVISION:raise RuntimeError('Repository revision mismatch')
 files={};checks=[]
 for s in info.siblings:
  p=Path('/model')/s.rfilename
  if not p.is_file() or '/' in s.rfilename:continue
  sha=file_hash(p)
  if s.lfs:
   expected=s.lfs['sha256'] if isinstance(s.lfs,dict) else s.lfs.sha256
   ok=sha==expected;method='sha256_lfs'
  else:
   h=hashlib.sha1();h.update(('blob '+str(p.stat().st_size)+'\0').encode())
   with p.open('rb') as f:
    for chunk in iter(lambda:f.read(8*1024*1024),b''):h.update(chunk)
   ok=h.hexdigest()==s.blob_id;method='git_blob_sha1'
  if not ok:raise RuntimeError('Upstream file identity mismatch: '+s.rfilename)
  files[s.rfilename]=sha;checks.append({'file':s.rfilename,'upstream_identity_verified':ok,'method':method,'bytes':p.stat().st_size})
 return {'repo':'Qwen/Qwen2.5-7B-Instruct','revision':REVISION,'files':files,'upstream_checks':checks}
@app.function(image=image,gpu='A100-40GB',cpu=2,memory=49152,timeout=1200,retries=0,max_containers=1,single_use_containers=True,volumes={'/model':models.with_mount_options(read_only=True),'/prior':prior.with_mount_options(read_only=True),'/evidence':evidence})
def run(manifest,label):
 import time,os,json,subprocess,tarfile,hashlib
 from pathlib import Path
 runid=label+'_'+time.strftime('%Y%m%dT%H%M%SZ',time.gmtime());root=Path('/evidence')/runid
 m=Path('/tmp/identity.json');m.write_text(json.dumps(manifest));env=os.environ.copy();env['CUBLAS_WORKSPACE_CONFIG']=':4096:8'
 hardware=subprocess.run(['nvidia-smi','--query-gpu=name,uuid,driver_version,memory.total','--format=csv'],capture_output=True,text=True)
 start=time.time();logpath=Path('/tmp/worker.log')
 with logpath.open('w') as log:
  try:r=subprocess.run(['python','-u','/src/worker.py',str(root),str(m)],env=env,stdout=log,stderr=subprocess.STDOUT,timeout=1080);code=r.returncode
  except subprocess.TimeoutExpired:code='TIMEOUT'
 root.mkdir(exist_ok=True);(root/'allocation.json').write_text(json.dumps({'container_id':os.getenv('MODAL_TASK_ID'),'stdout':hardware.stdout,'stderr':hardware.stderr,'exit':hardware.returncode},indent=2));(root/'worker.log').write_bytes(logpath.read_bytes());(root/'execution.json').write_text(json.dumps({'run_id':runid,'exit':code,'seconds':time.time()-start,'single_use_container':True,'gpu':'A100-40GB','retries':0},indent=2))
 (root/'final_manifest.json').write_text(json.dumps({str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in root.rglob('*') if p.is_file()},indent=2));evidence.commit()
 tarpath=Path('/tmp/subset.tar.gz')
 with tarfile.open(tarpath,'w:gz',compresslevel=1) as tar:
  for p in root.rglob('*'):
   if p.is_file() and (p.suffix!='.pt' or p.name in ['comparison_states.pt','representative_original.pt'] or p.name.endswith('_FAIL.pt')):tar.add(p,arcname=runid+'/'+str(p.relative_to(root)))
 return tarpath.read_bytes()
@app.local_entrypoint()
def main():
 import json
 out=Path('outputs/g0_closure_v0_5')
 manifest=json.loads((out/'checkpoint_identity.json').read_text())
 for label in ['closure_c']:
  print('Starting fresh-container closure:',label,flush=True)
  (out/(label+'.tar.gz')).write_bytes(run.remote(manifest,label))
