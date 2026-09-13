import modal
from pathlib import Path
O=Path(__file__).resolve().parent;R=O.parents[1] if modal.is_local() else Path('/')
app=modal.App('aeb-action-response-tokenizer-v1')
image=modal.Image.debian_slim(python_version='3.11').pip_install('transformers==4.45.2','tokenizers==0.20.3','huggingface_hub==0.25.2')
models=modal.Volume.from_name('aeb-qwen-pinned-model-v0-2')
@app.function(image=image,volumes={'/model':models.with_mount_options(read_only=True)},cpu=1,memory=2048,timeout=300,retries=0,max_containers=1)
def check(rows,codes,identity,backend_expected):
 import hashlib,time,transformers,tokenizers
 from pathlib import Path
 start=time.time();root=Path('/tmp/tokenizer');root.mkdir();hashes={}
 for name in ['tokenizer.json','tokenizer_config.json','vocab.json','merges.txt','config.json']:
  b=(Path('/model')/name).read_bytes();h=hashlib.sha256(b).hexdigest();assert h==identity['files'][name]
  (root/name).write_bytes(b);hashes[name]=h
 tok=transformers.AutoTokenizer.from_pretrained(root,use_fast=True,local_files_only=True)
 backend=hashlib.sha256(tok.backend_tokenizer.to_str().encode()).hexdigest();assert backend==backend_expected
 result=[]
 for row in rows:
  ids=tok(row['prefix'],add_special_tokens=True)['input_ids'];mapping={};checks={}
  for action,text in codes.items():
   whole=tok(row['prefix']+text,add_special_tokens=True)['input_ids'];ok=whole[:-1]==ids and len(whole)==len(ids)+1
   mapping[action]=whole[-1] if ok else None;checks[action]=ok
  result.append({'id':row['id'],'input_sha256':hashlib.sha256(row['prefix'].encode()).hexdigest(),'token_ids':ids,'active_length':len(ids),'fits_128':1<=len(ids)<=128,'code_token_ids':mapping,'code_append_checks':checks,'distinct_codes':None not in mapping.values() and len(set(mapping.values()))==3})
 return {'status':'PASS' if all(x['fits_128'] and all(x['code_append_checks'].values()) and x['distinct_codes'] for x in result) else 'FAIL_PRESERVED','rows':result,'max_length':max(x['active_length'] for x in result),'tokenizer_hash':backend,'file_hashes':hashes,'gpu':False,'model_loaded':False,'seconds':time.time()-start}
@app.local_entrypoint()
def main():
 import json,hashlib,datetime,traceback
 out=O/('run_'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'));out.mkdir()
 plan=json.loads((O/'PLAN.json').read_text());rows=[json.loads(x) for x in (O/'PROMPTS.jsonl').read_text().splitlines()]
 (out/'SOURCE_FREEZE.json').write_text(json.dumps({n:hashlib.sha256((O/n).read_bytes()).hexdigest() for n in ['PLAN.json','PROMPTS.jsonl','modal_run.py']},indent=2))
 try:
  identity=json.loads((R/'outputs/g0_closure_v0_5/checkpoint_identity.json').read_text());contract=json.loads((R/'outputs/g0_closure_v0_5/closure_c_20260911T180932Z/contract.json').read_text())
  result=check.remote(rows,plan['codes'],identity,contract['tokenizer_hash']);(out/'RESULT.json').write_text(json.dumps(result,indent=2));print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2),flush=True)
  if result['status']!='PASS':raise RuntimeError('preflight failed; preserve original mapping/prompt')
 except BaseException:
  (out/'FAILURE.txt').write_text(traceback.format_exc());raise
