"""QA-only transactional entrypoint; no development or confirmatory extraction."""
import hashlib,json,re,time
from pathlib import Path
import torch
from extractor import ContractError,digest,file_hash

def word_prefixes(text):
 # Preserve original whitespace and punctuation; independently tokenize each prefix.
 return [text[:m.end()] for m in re.finditer(r'\S+',text)]

def run_prefix_job(extractor,items,output_dir,partition='qa'):
 out=Path(output_dir);out.mkdir(parents=True,exist_ok=False);start=time.time();rows=[]
 try:
  if partition!='qa':raise ContractError('Only instrumentation QA is authorized; research extraction is blocked')
  if not isinstance(items,list) or not items:raise ContractError('Nonempty item list required')
  prepared=[];seen=set()
  for item in items:
   if not isinstance(item,dict) or set(item)!={'id','prefix'} or not isinstance(item['id'],str) or not item['id'] or item['id'] in seen:raise ContractError('Invalid/duplicate item or unexpected future-information field')
   seen.add(item['id']);ids=extractor._validated_ids(extractor.tokenize(item['prefix']))
   prepared.append((item,ids))
  for i,(item,ids) in enumerate(prepared):
   state=extractor.extract_ids(ids);path=out/f'{i:05d}.pt'
   stored={k:v for k,v in state.items() if k not in ['hidden','logits']}
   stored['hidden_last']=state['hidden'][:,-1,:].clone();stored['logits_last']=state['logits'][-1,:].clone()
   torch.save(stored,path)
   rows.append({'id':item['id'],'prefix_sha256':hashlib.sha256(item['prefix'].encode()).hexdigest(),'token_ids':ids.tolist(),'active_length':state['active_length'],'file':path.name,'sha256':file_hash(path),'contract_id':extractor.contract_id})
  manifest={'status':'PASS','partition':'qa','contract_id':extractor.contract_id,'items':rows,'seconds':time.time()-start}
  (out/'manifest.json').write_text(json.dumps(manifest,indent=2));return manifest
 except Exception as e:
  (out/'failure.json').write_text(json.dumps({'status':'BLOCKED','error_type':type(e).__name__,'error':str(e),'completed_items':len(rows),'successful_manifest':False},indent=2));raise
