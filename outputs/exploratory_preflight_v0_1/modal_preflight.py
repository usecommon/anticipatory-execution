"""CPU-only exact tokenizer preflight. No model loading or extraction."""
import modal
from pathlib import Path
app=modal.App('aeb-exploratory-tokenizer-preflight-v0-1')
image=modal.Image.debian_slim(python_version='3.11').pip_install('transformers==4.45.2','tokenizers==0.20.3','huggingface_hub==0.25.2')
models=modal.Volume.from_name('aeb-qwen-pinned-model-v0-2')
@app.function(image=image,volumes={'/model':models.with_mount_options(read_only=True)},cpu=1,memory=2048,timeout=300,retries=0,max_containers=1)
def preflight(rows,identity,expected_backend):
 import hashlib,json,time,os,shutil,transformers,tokenizers
 from pathlib import Path
 start=time.time();root=Path('/tmp/tokenizer');root.mkdir()
 hashes={}
 # Only verified tokenizer files are visible to AutoTokenizer. No weight load.
 for name in ['tokenizer.json','tokenizer_config.json','vocab.json','merges.txt','config.json']:
  data=(Path('/model')/name).read_bytes();actual=hashlib.sha256(data).hexdigest()
  if actual!=identity['files'][name]:raise ValueError('Pinned file hash mismatch: '+name)
  (root/name).write_bytes(data);hashes[name]=actual
 tok=transformers.AutoTokenizer.from_pretrained(root,use_fast=True,local_files_only=True)
 backend=hashlib.sha256(tok.backend_tokenizer.to_str().encode()).hexdigest()
 if backend!=expected_backend:raise ValueError('G0 tokenizer backend mismatch: '+backend)
 lengths=[]
 for r in rows:
  if set(r)!={'id','prefix'} or not isinstance(r['prefix'],str) or not r['prefix'].strip():raise ValueError('Invalid or non-prefix payload')
  ids=tok(r['prefix'],add_special_tokens=True)['input_ids']
  lengths.append({'id':r['id'],'prefix_sha256':hashlib.sha256(r['prefix'].encode()).hexdigest(),'active_length':len(ids),'token_ids':ids,'fits_128':1<=len(ids)<=128})
 return {'status':'PASS' if all(r['fits_128'] for r in lengths) else 'BLOCKED_LENGTH','rows':lengths,'max_active_length':max(r['active_length'] for r in lengths),'overlength_count':sum(not r['fits_128'] for r in lengths),'file_hashes':hashes,'tokenizer_backend_sha256':backend,'transformers':transformers.__version__,'tokenizers':tokenizers.__version__,'revision':identity['revision'],'cpu_seconds_wall':time.time()-start,'container_id':os.getenv('MODAL_TASK_ID'),'gpu':False,'model_loaded':False,'extraction':False,'pad_token_id':tok.pad_token_id,'eos_token_id':tok.eos_token_id,'padding_side':tok.padding_side}
@app.local_entrypoint()
def main():
 import json,hashlib,datetime,traceback
 out=Path(__file__).resolve().parent;root=out.parents[1]
 run=out/('run_'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'));run.mkdir()
 src=out/'EXTRACTION_INPUT.jsonl'
 identity=json.loads((root/'outputs/g0_closure_v0_5/checkpoint_identity.json').read_text())
 contract=json.loads((root/'outputs/g0_closure_v0_5/closure_c_20260911T180932Z/contract.json').read_text())
 (run/'REQUEST.json').write_text(json.dumps({'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'launcher_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'contract_id':'95dd7686f82fc1380c02539ec14fc73ab3073fc8be7b7ca015e40fd6e4fac1b0','resource_limits':{'cpu':1,'memory_mib':2048,'timeout_seconds':300,'gpu':0,'retries':0}},indent=2)+'\n')
 try:
  result=preflight.remote([json.loads(x) for x in src.read_text().splitlines()],identity,contract['tokenizer_hash'])
  (run/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
  print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2));print('Evidence:',run)
 except BaseException:
  (run/'FAILURE.txt').write_text(traceback.format_exc());raise
