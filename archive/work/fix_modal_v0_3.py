import modal
from pathlib import Path
app=modal.App('aeb-g0-fix-v0-3')
image=(modal.Image.debian_slim(python_version='3.11')
 .pip_install('torch==2.5.1','transformers==4.45.2','accelerate==0.34.2','numpy==1.26.4','huggingface_hub==0.25.2')
 .add_local_file(Path(__file__).with_name('aeb_g0_qwen_qa_harness.py'),'/src/aeb_g0_qwen_qa_harness.py')
 .add_local_file(Path(__file__).with_name('canonical_g0_v0_3.py'),'/src/canonical_g0_v0_3.py')
 .add_local_file(Path(__file__).with_name('fix_worker_v0_3.py'),'/src/fix_worker_v0_3.py'))
models=modal.Volume.from_name('aeb-qwen-pinned-model-v0-2')
evidence=modal.Volume.from_name('aeb-g0-fix-v0-3',create_if_missing=True)
@app.function(image=image,gpu='A100-40GB',cpu=2,memory=49152,timeout=1200,volumes={'/model':models,'/evidence':evidence},max_containers=1,retries=0)
def validate():
 import os,time,subprocess,json,tarfile,hashlib
 from pathlib import Path
 runid=time.strftime('fix_%Y%m%dT%H%M%SZ',time.gmtime());root=Path('/evidence')/runid
 env=os.environ.copy();env['CUBLAS_WORKSPACE_CONFIG']=':4096:8';start=time.time()
 logpath=Path('/evidence')/(runid+'.log')
 with logpath.open('w') as log:
  try:p=subprocess.run(['python','-u','/src/fix_worker_v0_3.py',str(root)],env=env,stdout=log,stderr=subprocess.STDOUT,timeout=1080);code=p.returncode
  except subprocess.TimeoutExpired:code='TIMEOUT'
 root.mkdir(exist_ok=True);(root/'worker.log').write_bytes(logpath.read_bytes())
 (root/'execution.json').write_text(json.dumps({'run_id':runid,'exit':code,'wall_seconds':time.time()-start,'gpu':'A100-40GB','retries':0,'timeout':1200},indent=2))
 (root/'remote_manifest.json').write_text(json.dumps({p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in root.iterdir() if p.is_file()},indent=2));evidence.commit()
 archive=Path('/tmp/evidence_subset.tar.gz')
 with tarfile.open(archive,'w:gz',compresslevel=1) as tar:
  for path in root.iterdir():
   if path.suffix!='.pt' or path.name in ['canonical_0.pt','masked_content_0.pt','causal_extension_0.pt','native_cache.pt']:tar.add(path,arcname=runid+'/'+path.name)
 return archive.read_bytes()
@app.local_entrypoint()
def main():
 Path('outputs/g0_fix_v0_3/evidence_subset.tar.gz').write_bytes(validate.remote())
