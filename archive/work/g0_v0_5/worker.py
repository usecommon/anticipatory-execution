import sys,os,time,json,traceback,hashlib,gc,re,random,platform,subprocess
from pathlib import Path
OUT=Path(sys.argv[1]);OUT.mkdir(parents=True,exist_ok=False)
MANIFEST=json.loads(Path(sys.argv[2]).read_text())
FIXTURES=json.loads(Path('/src/fixtures.json').read_text())
records=[];compact={};call_audit=[]
def write(name,value):(OUT/name).write_text(json.dumps(value,indent=2,default=str))
def main():
 import torch
 from extractor import load_extractor,ContractError,CanonicalExtractor,digest,file_hash,WIDTH
 from pipeline import run_prefix_job,word_prefixes
 from original_harness import QA_TEXTS
 start=time.time();x=load_extractor('/model',MANIFEST)
 model=x._CanonicalExtractor__model;tok=x._CanonicalExtractor__tok
 write('contract.json',x.contract);write('identity.json',MANIFEST)
 write('environment.json',{'python':sys.version,'platform':platform.platform(),'hostname':platform.node(),'container_id':os.getenv('MODAL_TASK_ID'),'torch':torch.__version__,'cuda':torch.version.cuda,'gpu':torch.cuda.get_device_name(0),'code_hashes':{p.name:file_hash(p) for p in Path('/src').iterdir() if p.is_file()},'contract_id':x.contract_id})
 (OUT/'nvidia_smi.txt').write_text(subprocess.check_output(['nvidia-smi'],text=True));(OUT/'pip_freeze.txt').write_text(subprocess.check_output([sys.executable,'-m','pip','freeze'],text=True))
 def audit(module,args,kw):
  ids=kw['input_ids'];pos=kw['position_ids'];mask=kw['attention_mask'];n=int((mask[0,0,-1,:]==0).sum())
  rr=torch.arange(128,device=ids.device)[:,None];cc=torch.arange(128,device=ids.device)[None,:]
  expected=torch.where((cc<=rr)&(cc<n),torch.tensor(0.,device=ids.device),torch.tensor(torch.finfo(torch.float32).min,device=ids.device))[None,None]
  ok=tuple(ids.shape)==(1,128) and tuple(mask.shape)==(1,1,128,128) and torch.equal(mask,expected) and torch.equal(pos,torch.arange(128,device=ids.device)[None]) and kw.get('use_cache') is False and kw.get('past_key_values') is None and not torch.is_autocast_enabled()
  rec={'index':len(call_audit),'shape':list(ids.shape),'active_length':n,'ids':ids[0,:n].cpu().tolist(),'mask_valid':bool(ok)};call_audit.append(rec)
  if not ok:raise AssertionError('Actual forward violates numerical contract')
 hook=model.register_forward_pre_hook(audit,with_kwargs=True)
 def flag(name,ok,detail='',group='supported'):
  records.append({'name':name,'group':group,'status':'PASS' if ok else 'FAIL','detail':detail})
 def comp(name,a,b,group='supported'):
  a=a.float();b=b.float();d=(a-b).abs();ok=bool(torch.isfinite(a).all() and torch.isfinite(b).all()) and torch.allclose(a,b,atol=1e-5,rtol=1e-5)
  records.append({'name':name,'group':group,'status':'PASS' if ok else 'FAIL','bitwise_equal':torch.equal(a,b),'max_abs':float(d.max()),'a_sha':hashlib.sha256(a.contiguous().numpy().tobytes()).hexdigest(),'b_sha':hashlib.sha256(b.contiguous().numpy().tobytes()).hexdigest()})
  if not ok:torch.save({'a':a,'b':b},OUT/(name.replace('/','_')+'_FAIL.pt'))
 def states(name,a,b,n=None,group='supported'):
  n=n or a['active_length']
  for l in range(29):comp(f'{name}_layer_{l}',a['hidden'][l,:n],b['hidden'][l,:n],group)
  comp(name+'_logits',a['logits'][:n],b['logits'][:n],group)
 def snapshot(name,r):
  compact[name]={'input_ids':r['input_ids'],'attention_mask':r['attention_mask'],'position_ids':r['position_ids'],'active_length':r['active_length'],'hidden_last':r['hidden'][:,-1,:].clone(),'logits_last':r['logits'][-1,:].clone(),'hidden_all_sha':hashlib.sha256(r['hidden'].contiguous().numpy().tobytes()).hexdigest(),'logits_all_sha':hashlib.sha256(r['logits'].contiguous().numpy().tobytes()).hexdigest()}
 def reject(name,fn):
  before=len(call_audit)
  try:fn();flag(name,False,'Accepted invalid request')
  except ContractError as e:flag(name,len(call_audit)==before,str(e),'rejection')
 # Regression bridge to previously validated FP32 canonical states. Different BF16 versions never pooled.
 for i,text in enumerate(QA_TEXTS):
  r=x.extract_text(text);old=torch.load(f'/prior/fix_20260911T171625Z/canonical_{i}.pt',weights_only=True)
  states(f'bridge_v03_{i}',r,old);snapshot(f'original_{i}',r)
  if i==0:torch.save(r,OUT/'representative_original.pt')
 # Boundary suite selected before any outcomes. All inputs remain fixed physical width 128.
 pool=[]
 for text in FIXTURES['natural_qa']:pool.extend(x.tokenize(text))
 rng=random.Random(FIXTURES['seed'])
 families={'repeated':(x.tokenize(' the')*128)[:128],'mixed':[pool[rng.randrange(len(pool))] for _ in range(128)]}
 for family,ids in families.items():
  full=x.extract_ids(ids);snapshot(f'boundary_{family}_128',full)
  for n in FIXTURES['boundary_lengths']:
   r=x.extract_ids(ids[:n]);states(f'boundary_{family}_{n}',r,full,n);snapshot(f'boundary_{family}_{n}',r)
   comp(f'boundary_ids_{family}_{n}',r['input_ids'][0,:n],torch.tensor(ids[:n]));comp(f'boundary_mask_{family}_{n}',r['attention_mask'],torch.tensor([[1]*n+[0]*(128-n)]))
  states('boundary_repeat_'+family,full,x.extract_ids(ids))
 # New held-out QA natural texts; preserve each original prefix string exactly.
 natural=[];alignment=[];coverage=[]
 for i,text in enumerate(FIXTURES['natural_qa']):
  ids=x.tokenize(text);full=x.extract_text(text);snapshot(f'natural_full_{i}',full);coverage.append({'id':i,'tokens':len(ids)})
  for j,prefix in enumerate(word_prefixes(text)):
   pid=x.tokenize(prefix);r=x.extract_text(prefix);snapshot(f'natural_{i}_{j}',r)
   aligned=pid==ids[:len(pid)];alignment.append({'id':f'natural_{i}_{j}','aligned':aligned,'prefix_ids':pid,'full_token_prefix':ids[:len(pid)]})
   if aligned:states(f'natural_causal_{i}_{j}',r,full,len(pid))
   else:records.append({'name':f'natural_causal_{i}_{j}','group':'tokenization','status':'DIAGNOSTIC','detail':'Retokenization prevents causal equality; independently extracted state retained.'})
   # Every prefix is still evaluated, even if an equality is inapplicable.
   states(f'natural_repeat_{i}_{j}',r,x.extract_text(prefix))
   natural.append({'id':f'natural_{i}_{j}','prefix':prefix})
 write('alignment.json',alignment);write('qa_length_coverage.json',{'fixture_counts':coverage,'scope':'QA-only; no development benchmark or confirmatory set was inspected','development_coverage':'UNKNOWN; first future development job must preflight and block on overflow'})
 # Real masked-ID perturbation at fixed shape, independent of encoder normalization.
 ids=x.tokenize(QA_TEXTS[0]);ref=x.extract_ids(ids);n=len(ids)
 inp=ref['input_ids'].cuda().clone();inp[0,n:]=1
 rr=torch.arange(128,device='cuda')[:,None];cc=torch.arange(128,device='cuda')[None,:]
 mask=torch.where((cc<=rr)&(cc<n),0.,torch.finfo(torch.float32).min)[None,None]
 with torch.inference_mode():o=model(input_ids=inp,attention_mask=mask,position_ids=torch.arange(128,device='cuda')[None],use_cache=False,output_hidden_states=True,return_dict=True)
 masked={'active_length':n,'hidden':torch.stack([h[0,:n].cpu() for h in o.hidden_states]),'logits':o.logits[0,:n].cpu()};states('actual_masked_content',ref,masked);del o
 for width in [n,64,96,128,256]:states(f'normalized_input_width_{width}',ref,x.extract_ids(ids+[tok.pad_token_id]*(width-n),[1]*n+[0]*(width-n)))
 # All public entrypoints fail closed; none of these requests may invoke the model.
 invalid=[('empty',lambda:x.extract_ids([])),('overflow129',lambda:x.extract_ids([1]*129)),('rank2',lambda:x.extract_ids([[1,2],[3,4]])),('scalar',lambda:x.extract_ids(1)),('float_ids',lambda:x.extract_ids([1.0,2.0])),('bool_ids',lambda:x.extract_ids([True])),('float_mask',lambda:x.extract_ids([1,2],[1.0,0.0])),('mask_rank2',lambda:x.extract_ids([1,2],[[1,1]])),('mask_size',lambda:x.extract_ids([1,2],[1])),('nonbinary',lambda:x.extract_ids([1,2],[1,2])),('holey',lambda:x.extract_ids([1,2,3],[1,0,1])),('left_padding',lambda:x.extract_ids([1,2],[0,1])),('negative_id',lambda:x.extract_ids([-1])),('vocab_overflow',lambda:x.extract_ids([model.config.vocab_size])),('cache',lambda:x.extract_ids([1],use_cache=True)),('past',lambda:x.extract_ids([1],past_key_values=object())),('empty_text',lambda:x.extract_text('  ')),('non_text',lambda:x.extract_text(12)),('batch_string',lambda:x.extract_batch('a string')),('unsafe_constructor',lambda:CanonicalExtractor(tok,model,MANIFEST))]
 for name,fn in invalid:reject('reject_'+name,fn)
 def mutate(name,setter,restore):
  setter()
  try:reject(name,lambda:x.extract_ids([1]))
  finally:restore()
 mutate('reject_training',lambda:model.train(),lambda:model.eval())
 p=next(model.parameters());mutate('reject_gradient',lambda:p.requires_grad_(True),lambda:p.requires_grad_(False))
 mutate('reject_attention',lambda:setattr(model.config,'_attn_implementation','sdpa'),lambda:setattr(model.config,'_attn_implementation','eager'))
 mutate('reject_tf32',lambda:setattr(torch.backends.cuda.matmul,'allow_tf32',True),lambda:setattr(torch.backends.cuda.matmul,'allow_tf32',False))
 mutate('reject_warn_only',lambda:torch.use_deterministic_algorithms(True,warn_only=True),lambda:torch.use_deterministic_algorithms(True,warn_only=False))
 mutate('reject_determinism_off',lambda:torch.use_deterministic_algorithms(False),lambda:torch.use_deterministic_algorithms(True,warn_only=False))
 mutate('reject_workspace',lambda:os.environ.__setitem__('CUBLAS_WORKSPACE_CONFIG',':16:8'),lambda:os.environ.__setitem__('CUBLAS_WORKSPACE_CONFIG',':4096:8'))
 mutate('reject_tokenizer_side',lambda:setattr(tok,'padding_side','left'),lambda:setattr(tok,'padding_side','right'))
 with torch.autocast('cuda',dtype=torch.bfloat16):reject('reject_autocast',lambda:x.extract_ids([1]))
 # Pipeline preflight: overflow or forbidden partition must block the whole job before any forward.
 good=[{'id':'a','prefix':QA_TEXTS[0]}];bad=good+[{'id':'long','prefix':' token'*150}]
 before=len(call_audit)
 try:run_prefix_job(x,bad,OUT/'overflow_job');flag('overflow_job_rejected',False)
 except ContractError:flag('overflow_job_rejected',not list((OUT/'overflow_job').glob('*.pt')) and not (OUT/'overflow_job/manifest.json').exists() and len(call_audit)==before)
 for part in ['development','confirmatory']:
  reject('reject_partition_'+part,lambda part=part:run_prefix_job(x,good,OUT/('forbidden_'+part),partition=part))
 reject('reject_future_field',lambda:run_prefix_job(x,[{'id':'a','prefix':'hello','full_instruction':'future'}],OUT/'future_field_job'))
 reject('reject_duplicate_id',lambda:run_prefix_job(x,good+good,OUT/'duplicate_job'))
 # The real public job entrypoint stores last-active states only, with immutable item alignment.
 manifest=run_prefix_job(x,natural,OUT/'pipeline_job')
 for row in manifest['items']:
  saved=torch.load(OUT/'pipeline_job'/row['file'],weights_only=True);expected=compact[row['id']]
  comp('pipeline_hidden_'+row['id'],saved['hidden_last'],expected['hidden_last']);comp('pipeline_logits_'+row['id'],saved['logits_last'],expected['logits_last']);flag('pipeline_contract_'+row['id'],saved['contract_id']==x.contract_id)
 # Reverse-order and batch-interface checks on a fixed subset, not new numerical settings.
 subset=natural[::max(1,len(natural)//12)]
 for item,r in zip(reversed(subset),x.extract_batch([q['prefix'] for q in reversed(subset)])):
  comp('batch_hidden_'+item['id'],r['hidden'][:,-1,:],compact[item['id']]['hidden_last']);comp('batch_logits_'+item['id'],r['logits'][-1],compact[item['id']]['logits_last'])
 r=x.extract_text('Describe a different task about geology')
 flag('active_content_sensitivity',not torch.equal(r['hidden'][:,-1],compact['original_0']['hidden_last']))
 flag('all_actual_forwards_valid',all(a['mask_valid'] for a in call_audit))
 write('forward_audit.json',call_audit);write('checks.json',records)
 torch.save(compact,OUT/'comparison_states.pt')
 write('comparison_digests.json',{name:{'hidden_all_sha':r['hidden_all_sha'],'logits_all_sha':r['logits_all_sha'],'active_length':r['active_length']} for name,r in compact.items()})
 write('summary.json',{'status':'PASS' if not any(r['status']=='FAIL' for r in records) else 'FAIL','checks':len(records),'failures':sum(r['status']=='FAIL' for r in records),'natural_prefixes':len(natural),'natural_texts':len(FIXTURES['natural_qa']),'actual_forwards':len(call_audit),'contract_id':x.contract_id,'wall_seconds':time.time()-start,'max_cuda_allocated_bytes':torch.cuda.max_memory_allocated(),'confirmatory_extraction':False,'development_extraction':False})
if __name__=='__main__':
 try:main()
 except BaseException:
  (OUT/'failure.txt').write_text(traceback.format_exc());write('checks_partial.json',records);traceback.print_exc();sys.exit(1)
 finally:
  write('remote_manifest.json',{str(p.relative_to(OUT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in OUT.rglob('*') if p.is_file() and p.name!='remote_manifest.json'})
