"""Versioned wrapper around unchanged canonical-v0.5 forwards."""
import hashlib,json,time
from pathlib import Path
import torch
from extractor import ContractError,file_hash
CONTRACT='95dd7686f82fc1380c02539ec14fc73ab3073fc8be7b7ca015e40fd6e4fac1b0'
# Hashes of exact job inputs are embedded before validation, not caller supplied.
PINS = {
  "exploratory": {
    "path": "outputs/exploratory_preflight_v0_1/EXTRACTION_INPUT.jsonl",
    "sha256": "a2b4cb69d993433603e06cb6536b2579f994acbde7bdda8a92734cdfdc0709ba"
  },
  "instrumentation_validation": {
    "path": "outputs/exploratory_entrypoint_v0_1/VALIDATION_INPUT.jsonl",
    "sha256": "da1aec4b17a771adc1d2554d17fbca7b5e8c7f476370819da8e3d457aec3caa2"
  },
  "preflight_result": {
    "path": "outputs/exploratory_preflight_v0_1/run_20260913T000004720678Z/RESULT.json",
    "sha256": "40e522157a51e1d16d0b5aef4501189d8fc4267087e5c6c8ef1fc0fd9d301b22"
  },
  "extractor": {
    "path": "outputs/g0_closure_v0_5/source/extractor.py",
    "sha256": "f7b871a69dbb7aa165743f2e25f24680cb2d4118844135498cb1fb9a2ac22283"
  },
  "original_pipeline": {
    "path": "outputs/g0_closure_v0_5/source/pipeline.py",
    "sha256": "a17ad5acc77e26b4b5f40e0b5b2a6b6b3220dcc4bae2059b6345f2a655b5b690"
  }
}

def run_job(extractor,input_file,output_dir,*,partition,preflight_file=None):
 out=Path(output_dir);out.mkdir(parents=True,exist_ok=False);start=time.time();rows=[]
 try:
  if partition not in ('exploratory','instrumentation_validation'):
   raise ContractError('Partition not authorized; confirmatory extraction prohibited')
  if extractor.contract_id!=CONTRACT:raise ContractError('Wrong numerical contract')
  path=Path(input_file)
  if file_hash(path)!=PINS[partition]['sha256']:raise ContractError('Input is not the frozen allowlisted job')
  items=[json.loads(line) for line in path.read_text().splitlines()]
  if not items:raise ContractError('Empty job')
  expected=None
  if partition=='exploratory':
   if preflight_file is None or file_hash(preflight_file)!=PINS['preflight_result']['sha256']:raise ContractError('Missing or changed pinned length preflight')
   result=json.loads(Path(preflight_file).read_text())
   if result['status']!='PASS':raise ContractError('Preflight not passed')
   expected={r['id']:r for r in result['rows']}
   if len(expected)!=len(items):raise ContractError('Preflight coverage mismatch')
  prepared=[];seen=set()
  # Finish all validation and tokenization before the first extract_ids call.
  for item in items:
   if not isinstance(item,dict) or set(item)!={'id','prefix'} or not isinstance(item['id'],str) or not item['id'] or item['id'] in seen:
    raise ContractError('Invalid/duplicate item or future-information field')
   seen.add(item['id']);ids=extractor._validated_ids(extractor.tokenize(item['prefix']))
   if expected is not None:
    prior=expected.get(item['id'])
    if prior is None or prior['token_ids']!=ids.tolist() or prior['prefix_sha256']!=hashlib.sha256(item['prefix'].encode()).hexdigest():raise ContractError('Tokenization changed since frozen preflight')
   prepared.append((item,ids))
  for i,(item,ids) in enumerate(prepared):
   state=extractor.extract_ids(ids)
   if state['contract_id']!=CONTRACT or state['active_length']!=len(ids):raise ContractError('Forward provenance mismatch')
   stored={k:v for k,v in state.items() if k not in ['hidden','logits']}
   stored['hidden_last']=state['hidden'][:,-1,:].clone();stored['logits_last']=state['logits'][-1,:].clone()
   target=out/f'{i:05d}.pt';torch.save(stored,target)
   rows.append({'id':item['id'],'prefix_sha256':hashlib.sha256(item['prefix'].encode()).hexdigest(),'token_ids':ids.tolist(),'active_length':state['active_length'],'file':target.name,'sha256':file_hash(target),'contract_id':CONTRACT})
   # Retain a durable index of every completed item even if a later item fails.
   with (out/'progress.jsonl').open('a') as f:f.write(json.dumps(rows[-1])+'\n')
  manifest={'status':'PASS','partition':partition,'contract_id':CONTRACT,'input_sha256':PINS[partition]['sha256'],'entrypoint_sha256':file_hash(__file__),'items':rows,'seconds':time.time()-start,'human_G1':'PENDING_DEFERRED','evidence_kind':'instrumentation_only' if partition=='instrumentation_validation' else 'AI_labeled_exploratory_diagnostic','confirmatory':False}
  (out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');return manifest
 except Exception as e:
  (out/'failure.json').write_text(json.dumps({'status':'BLOCKED','error_type':type(e).__name__,'error':str(e),'completed_items':len(rows),'items':rows,'successful_manifest':False},indent=2)+'\n');raise
