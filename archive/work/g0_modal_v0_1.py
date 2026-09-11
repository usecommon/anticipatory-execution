import modal
from pathlib import Path
app=modal.App('aeb-g0-qa-v0-1')
image=(modal.Image.debian_slim(python_version='3.11')
 .pip_install('torch==2.5.1','transformers==4.45.2','accelerate==0.34.2','numpy==1.26.4','huggingface_hub==0.25.2')
 .add_local_file(Path(__file__).with_name('aeb_g0_qwen_qa_harness.py'),'/src/aeb_g0_qwen_qa_harness.py')
 .add_local_file(Path(__file__).with_name('g0_worker_v0_1.py'),'/src/g0_worker_v0_1.py'))
volume=modal.Volume.from_name('aeb-g0-evidence-v0-1',create_if_missing=True)
@app.function(image=image,gpu='A10',timeout=1800,volumes={'/persist':volume},max_containers=1,retries=0)
def run_qa():
 import subprocess,os,tarfile,time,hashlib,json
 from pathlib import Path
 run_id=time.strftime('run_%Y%m%dT%H%M%SZ',time.gmtime())
 out=Path('/persist')/run_id;out.mkdir(exist_ok=False)
 Path('/evidence').symlink_to(out,target_is_directory=True)
 started=time.time()
 with (out/'worker.log').open('w') as f:
  try:
   p=subprocess.run(['python','-u','/src/g0_worker_v0_1.py'],stdout=f,stderr=subprocess.STDOUT,timeout=1650)
   code=p.returncode
  except subprocess.TimeoutExpired:code='TIMEOUT'
 (out/'execution.json').write_text(json.dumps({'run_id':run_id,'exit':code,'wall_seconds':time.time()-started,'gpu_request':'A10','gpu_timeout_seconds':1800,'retries':0}))
 volume.commit()
 archive=Path('/tmp')/(run_id+'.tar.gz')
 with tarfile.open(archive,'w:gz') as tar:tar.add(out,arcname=run_id)
 return archive.read_bytes()
