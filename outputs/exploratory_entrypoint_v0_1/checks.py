"""Software tests use synthetic tensors only; never research labels/features."""
import json,shutil,tempfile
from pathlib import Path
import torch
from entrypoint import run_job,CONTRACT
from extractor import ContractError
class Fake:
 contract_id=CONTRACT
 def __init__(self,late_long=False,fail_at=None,tokens=None):self.calls=0;self.token_calls=0;self.late_long=late_long;self.fail_at=fail_at;self.tokens=tokens
 def tokenize(self,text):
  self.token_calls+=1
  if self.late_long and self.token_calls==12:return [1]*129
  return self.tokens[text] if self.tokens is not None else [1,2]
 def _validated_ids(self,ids):
  if not 1<=len(ids)<=128:raise ContractError('outside length')
  return torch.tensor(ids,dtype=torch.long)
 def extract_ids(self,ids):
  self.calls+=1
  if self.calls==self.fail_at:raise RuntimeError('injected forward failure')
  n=len(ids)
  return {'contract_id':CONTRACT,'active_length':n,'hidden':torch.ones(29,n,4),'logits':torch.ones(n,16),'input_ids':ids}
def software_checks(root,qa,research,preflight):
 root=Path(root);root.mkdir();checks=[]
 def reject(name,f,inp=qa,partition='instrumentation_validation',pf=None,expected_completed=0):
  out=root/name
  try:run_job(f,inp,out,partition=partition,preflight_file=pf)
  except (ContractError,RuntimeError):pass
  else:raise AssertionError(name+' accepted')
  failure=json.loads((out/'failure.json').read_text());assert failure['completed_items']==expected_completed
  assert not (out/'manifest.json').exists()
  if expected_completed==0 and name!='full_preflight_before_forward':assert f.calls==0
  checks.append({'name':name,'pass':True,'forward_calls':f.calls,'token_calls':f.token_calls})
 for part in ['confirmatory','development','qa','test','',None]:reject('partition_'+str(part),Fake(),partition=part)
 f=Fake();f.contract_id='wrong';reject('wrong_contract',f)
 original=Path(qa).read_text()
 cases={'suffix_field':original.replace('"prefix":','"full_instruction":"future", "prefix":',1),'reordered':'\n'.join(reversed(original.splitlines()))+'\n','missing_item':'\n'.join(original.splitlines()[1:])+'\n','duplicate':original+original.splitlines()[0]+'\n','empty':'','edited_prefix':original.replace('Find','Seek',1)}
 for name,text in cases.items():
  inp=root/(name+'.jsonl');inp.write_text(text);reject(name,Fake(),inp=inp)
 reject('late_overlength',Fake(late_long=True))
 reject('research_missing_preflight',Fake(),inp=research,partition='exploratory')
 badpf=root/'bad_preflight.json';badpf.write_text('{}');reject('research_changed_preflight',Fake(),inp=research,partition='exploratory',pf=badpf)
 reject('research_changed_tokens',Fake(),inp=research,partition='exploratory',pf=preflight)
 data=json.loads(Path(preflight).read_text());mapping={r['id']:r['token_ids'] for r in data['rows']}
 tokens={r['prefix']:mapping[r['id']] for r in (json.loads(x) for x in Path(research).read_text().splitlines())}
 f=Fake(fail_at=1,tokens=tokens);reject('full_preflight_before_forward',f,inp=research,partition='exploratory',pf=preflight);assert f.token_calls==4013 and f.calls==1
 f=Fake(fail_at=2);reject('partial_failure_preserved',f,expected_completed=1)
 assert (root/'partial_failure_preserved/00000.pt').exists() and len((root/'partial_failure_preserved/progress.jsonl').read_text().splitlines())==1
 f=Fake();out=root/'valid_software_only';m=run_job(f,qa,out,partition='instrumentation_validation');assert len(m['items'])==12
 before=(out/'manifest.json').read_bytes()
 try:run_job(f,qa,out,partition='instrumentation_validation')
 except FileExistsError:pass
 else:raise AssertionError('overwrite allowed')
 assert (out/'manifest.json').read_bytes()==before
 checks.append({'name':'valid_software_roundtrip_and_overwrite_rejection','pass':True,'forward_calls':12,'synthetic_tensors_only':True})
 return checks
