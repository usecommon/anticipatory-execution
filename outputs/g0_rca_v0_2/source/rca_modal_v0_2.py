import modal
from pathlib import Path
app=modal.App('aeb-g0-rca-v0-2')
image=(modal.Image.debian_slim(python_version='3.11')
 .pip_install('torch==2.5.1','transformers==4.45.2','accelerate==0.34.2','numpy==1.26.4','huggingface_hub==0.25.2')
 .add_local_file(Path(__file__).with_name('aeb_g0_qwen_qa_harness.py'),'/src/aeb_g0_qwen_qa_harness.py')
 .add_local_file(Path(__file__).with_name('rca_worker_v0_2.py'),'/src/rca_worker_v0_2.py'))
models=modal.Volume.from_name('aeb-qwen-pinned-model-v0-2',create_if_missing=True)
evidence=modal.Volume.from_name('aeb-g0-rca-v0-2',create_if_missing=True)
@app.function(image=image,timeout=900,volumes={'/model':models},retries=0)
def prepare():
 from huggingface_hub import snapshot_download
 snapshot_download('Qwen/Qwen2.5-7B-Instruct',revision='a09a35458c702b33eeacc393d103063234e8bc28',local_dir='/model',allow_patterns=['*.json','*.safetensors','*.txt'],max_workers=4)
 models.commit()
@app.function(image=image,gpu='A100-40GB',cpu=2,memory=49152,timeout=1500,volumes={'/model':models,'/evidence':evidence},max_containers=1,retries=0)
def investigate():
 import subprocess,os,time,json,tarfile,hashlib
 from pathlib import Path
 runid=time.strftime('rca_%Y%m%dT%H%M%SZ',time.gmtime());root=Path('/evidence')/runid;root.mkdir(exist_ok=False)
 cases=['baseline','workspace_strict','bf16_eager','bf16_math','bf16_no_reduced','fp32_eager'];results=[]
 start=time.time()
 for case in cases:
  env=os.environ.copy()
  if case=='baseline':env.pop('CUBLAS_WORKSPACE_CONFIG',None)
  else:env['CUBLAS_WORKSPACE_CONFIG']=':4096:8'
  t=time.time();print('Starting',case,flush=True)
  with (root/(case+'.log')).open('w') as log:
   try:r=subprocess.run(['python','-u','/src/rca_worker_v0_2.py',str(root/case),case],env=env,stdout=log,stderr=subprocess.STDOUT,timeout=200);code=r.returncode
   except subprocess.TimeoutExpired:code='TIMEOUT'
  results.append({'case':case,'exit':code,'seconds':time.time()-t});(root/'progress.json').write_text(json.dumps(results,indent=2));evidence.commit();print(results[-1],flush=True)
 (root/'execution.json').write_text(json.dumps({'run_id':runid,'cases':results,'wall_seconds':time.time()-start,'gpu':'A100-40GB','confirmatory':False},indent=2))
 (root/'sha256.json').write_text(json.dumps({str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in root.rglob('*') if p.is_file()},indent=2))
 evidence.commit()
 archive=Path('/tmp/rca.tar.gz')
 with tarfile.open(archive,'w:gz',compresslevel=1) as tar:tar.add(root,arcname=runid)
 return archive.read_bytes()
@app.local_entrypoint()
def main():
 prepare.remote()
 result=investigate.remote()
 Path('outputs/g0_rca_v0_2/rca_run_01.tar.gz').write_bytes(result)
