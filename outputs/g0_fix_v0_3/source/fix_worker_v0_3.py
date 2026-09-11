import os,sys,json,time,traceback,hashlib,gc,subprocess
from pathlib import Path
OUT=Path(sys.argv[1]);OUT.mkdir(parents=True,exist_ok=False)
def write(name,obj):(OUT/name).write_text(json.dumps(obj,indent=2,default=str))
def main():
 import torch,transformers
 from canonical_g0_v0_3 import CanonicalExtractor
 import aeb_g0_qwen_qa_harness as h
 start=time.time();h.set_deterministic(1729);torch.use_deterministic_algorithms(True,warn_only=False)
 tok=transformers.AutoTokenizer.from_pretrained('/model',use_fast=True)
 def load():return transformers.AutoModelForCausalLM.from_pretrained('/model',torch_dtype=torch.float32,attn_implementation='eager',low_cpu_mem_usage=True).to('cuda').eval().requires_grad_(False)
 model=load();x=CanonicalExtractor(tok,model);records=[]
 write('environment.json',{'model_revision':'a09a35458c702b33eeacc393d103063234e8bc28','tokenizer_revision':'a09a35458c702b33eeacc393d103063234e8bc28','torch':torch.__version__,'transformers':transformers.__version__,'cuda':torch.version.cuda,'gpu':torch.cuda.get_device_name(0),'dtype':str(model.dtype),'attention':model.config._attn_implementation,'physical_shape':[1,128],'mask':'explicit 4D additive causal and padding mask','positions':'explicit arange(128)','cache':False,'workspace':os.getenv('CUBLAS_WORKSPACE_CONFIG'),'deterministic_warn_only':torch.is_deterministic_algorithms_warn_only_enabled(),'tf32':torch.backends.cuda.matmul.allow_tf32,'seed':1729,'atol':1e-5,'rtol':1e-5})
 (OUT/'pip_freeze.txt').write_text(subprocess.check_output([sys.executable,'-m','pip','freeze'],text=True));(OUT/'nvidia_smi.txt').write_text(subprocess.check_output(['nvidia-smi'],text=True))
 def save(name,r):torch.save(r,OUT/(name+'.pt'))
 def check(name,a,b,group='canonical'):
  a=a.float();b=b.float();d=(a-b).abs();ok=torch.allclose(a,b,atol=1e-5,rtol=1e-5)
  row={'name':name,'group':group,'status':'PASS' if ok else 'FAIL','max_abs':float(d.max()),'mean_abs':float(d.mean()),'bitwise_equal':torch.equal(a,b),'a_sha':h.tensor_checksum(a),'b_sha':h.tensor_checksum(b)}
  records.append(row)
  with (OUT/'checks_incremental.jsonl').open('a') as f:f.write(json.dumps(row)+'\n')
  if len(records)%100==0:write('progress.json',{'checks_completed':len(records)})
  return ok
 def states(name,a,b,n=None,group='canonical'):
  n=n or a['active_length']
  for l in range(a['hidden'].shape[0]):check(f'{name}_layer_{l}',a['hidden'][l,:n],b['hidden'][l,:n],group)
  check(name+'_logits',a['logits'][:n],b['logits'][:n],group)
 def reject(name,call):
  try:call();ok=False
  except ValueError:ok=True
  records.append({'name':name,'group':'contract','status':'PASS' if ok else 'FAIL'});write('checks.json',records)
 # Independent physical-shape backend controls retain failures; no canonical adapter.
 for i,text in enumerate(h.QA_TEXTS):
  ea,oa=h.extract(tok,model,[text],'cuda',pad_to=64)
  a={l:h.last_active_hidden(ea,oa,l).cpu() for l in [1,7,14,21,28]}
  for width in [96,128]:
   eb,ob=h.extract(tok,model,[text],'cuda',pad_to=width)
   for l in a:check(f'native_length_{i}_64_{width}_layer_{l}',a[l],h.last_active_hidden(eb,ob,l).cpu(),'native_unrestricted')
  del oa,ob
 refs=[]
 for i,text in enumerate(h.QA_TEXTS):
  ref=x.extract_text(text);refs.append(ref);save(f'canonical_{i}',ref)
  states(f'repeat_{i}',ref,x.extract_text(text))
  ids=tok(text)['input_ids'];n=len(ids)
  check(f'alignment_{i}',ref['input_ids'][0,:n],torch.tensor(ids));check(f'mask_{i}',ref['attention_mask'],torch.tensor([[1]*n+[0]*(128-n)]));check(f'positions_{i}',ref['position_ids'],torch.arange(128).unsqueeze(0))
  # Four serialized input widths feed a single enforced physical layout.
  for width in [n,64,96,128]:
   padded=ids+[tok.pad_token_id]*(width-n);mask=[1]*n+[0]*(width-n)
   r=x.extract_ids(padded,mask);states(f'input_padding_{i}_{width}',ref,r)
  # Real masked-content change at the model input, bypassing normalization.
  e=x.encode(ids);e['input_ids'][e['attention_mask']==0]=1
  r=x.forward_canonical(e);save(f'masked_content_{i}',r);states(f'masked_content_{i}',ref,r)
  # Unmasked future tokens: require all original active positions invariant.
  extension=ids+tok(' with additional details')['input_ids']
  r=x.extract_ids(extension);save(f'causal_extension_{i}',r);states(f'causal_extension_{i}',ref,r,n)
  restored=torch.load(OUT/f'canonical_{i}.pt',weights_only=True);states(f'serialize_{i}',ref,restored)
  check(f'finite_{i}',torch.isfinite(ref['hidden']).float(),torch.ones_like(ref['hidden']))
 # Batch-interface order and context controls; physical batching explicitly unsupported.
 for order in [list(range(8)),list(reversed(range(8)))]:
  batch=x.extract_batch([h.QA_TEXTS[i] for i in order])
  for i,r in zip(order,batch):states(f'canonical_batch_order_{order[0]}_item_{i}',refs[i],r)
 # Every completed-word prefix tested against full QA utterance at same physical shape.
 prefix_counts=[]
 for i,text in enumerate(h.QA_TEXTS):
  words=text.split();count=0
  for k in range(1,len(words)+1):
   p=' '.join(words[:k]);ids=tok(p)['input_ids']
   # A word-boundary tokenization need not be a token-prefix: only compare truly aligned states.
   full_ids=refs[i]['input_ids'][0,:len(ids)].tolist()
   r=x.extract_text(p);save(f'word_prefix_{i}_{k}',r)
   if ids!=full_ids:
    records.append({'name':f'word_prefix_{i}_{k}_alignment','group':'token_boundary','status':'DIAGNOSTIC','detail':'Independent word-prefix tokenization differs from corresponding full-token prefix; no equality is mathematically required.'})
   else:states(f'word_prefix_{i}_{k}',r,refs[i])
   count+=1
  prefix_counts.append(count)
 write('prefix_counts.json',prefix_counts)
 # Sensitivity control: changing observed input must change hidden states.
 different=x.extract_text('Translate a short poem into Korean')
 changed=not torch.equal(refs[0]['hidden'][:,-1],different['hidden'][:,-1])
 records.append({'name':'active_content_sensitivity','group':'canonical','status':'PASS' if changed else 'FAIL'})
 reject('reject_empty',lambda:x.extract_ids([]));reject('reject_overflow_no_truncation',lambda:x.extract_ids([1]*129));reject('reject_holey_mask',lambda:x.extract_ids([1,2,3],[1,0,1]));reject('reject_left_padding',lambda:x.extract_ids([1,2],[0,1]));reject('reject_cache',lambda:x.extract_ids([1],use_cache=True));reject('reject_past',lambda:x.extract_ids([1],past_key_values=object()))
 # Native batch and actual KV cache controls remain real numerical tests.
 eb,ob=h.extract(tok,model,h.QA_TEXTS[:4],'cuda',pad_to=128)
 for i,text in enumerate(h.QA_TEXTS[:4]):
  es,os_=h.extract(tok,model,[text],'cuda',pad_to=128)
  for l in [1,7,14,21,28]:check(f'native_batch_{i}_{l}',h.last_active_hidden(eb,ob,l)[i].cpu(),h.last_active_hidden(es,os_,l)[0].cpu(),'native_unrestricted')
  del os_
 ids=tok(h.QA_TEXTS[3],return_tensors='pt')['input_ids'].cuda();n=ids.shape[1];cut=n//2
 with torch.inference_mode():
  full=model(input_ids=ids,attention_mask=torch.ones_like(ids),use_cache=False,output_hidden_states=True)
  pre=model(input_ids=ids[:,:cut],attention_mask=torch.ones_like(ids[:,:cut]),use_cache=True,output_hidden_states=True)
  tail=model(input_ids=ids[:,cut:],attention_mask=torch.ones_like(ids),past_key_values=pre.past_key_values,use_cache=True,output_hidden_states=True)
 torch.save({'full_hidden':{l:full.hidden_states[l].cpu() for l in [1,7,14,21,28]},'tail_hidden':{l:tail.hidden_states[l].cpu() for l in [1,7,14,21,28]},'ids':ids.cpu(),'full_logits':full.logits.cpu(),'tail_logits':tail.logits.cpu()},OUT/'native_cache.pt')
 for l in [1,7,14,21,28]:check(f'native_cache_{l}',full.hidden_states[l][:,cut:].cpu(),tail.hidden_states[l].cpu(),'native_unrestricted')
 check('native_cache_logits',full.logits[:,cut:].cpu(),tail.logits.cpu(),'native_unrestricted')
 del full,pre,tail,ob,model,x;gc.collect();torch.cuda.empty_cache()
 model=load();x=CanonicalExtractor(tok,model)
 for i,text in enumerate(h.QA_TEXTS):states(f'reload_{i}',refs[i],x.extract_text(text))
 write('checks.json',records)
 fails=[r for r in records if r['status']=='FAIL'];canonfails=[r for r in fails if r['group']!='native_unrestricted']
 write('summary.json',{'gate':'G0','status':'BLOCKED','canonical_contract_status':'FAIL' if canonfails else 'PASS','native_unrestricted_status':'FAIL' if any(r['group']=='native_unrestricted' for r in fails) else 'PASS','canonical_failures':len(canonfails),'native_failures':sum(r['group']=='native_unrestricted' for r in fails),'total_checks':len(records),'elapsed_seconds':time.time()-start,'confirmatory_extraction':False,'thesis_changed':False,'note':'Supported-contract validation is separate from full-gate approval; native failures are preserved.'})
if __name__=='__main__':
 try:main()
 except BaseException:
  (OUT/'failure.txt').write_text(traceback.format_exc());traceback.print_exc();sys.exit(1)
 finally:write('sha256.json',{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in OUT.iterdir() if p.is_file() and p.name!='sha256.json'})
