"""G0 evidence wrapper v0.1; original harness stays byte-for-byte unchanged."""
import os,sys,json,time,hashlib,subprocess,traceback
from pathlib import Path
OUT=Path('/evidence'); OUT.mkdir(exist_ok=True)
def write(name,obj): (OUT/name).write_text(json.dumps(obj,indent=2,default=str))
def main():
 import torch,transformers,numpy
 from huggingface_hub import HfApi
 import aeb_g0_qwen_qa_harness as h
 start=time.time(); revision=HfApi().model_info('Qwen/Qwen2.5-7B-Instruct').sha
 write('resolved_revision.json',{'model':'Qwen/Qwen2.5-7B-Instruct','model_revision':revision,'tokenizer_revision':revision,'historical_revision':'not supplied'})
 (OUT/'pip_freeze.txt').write_text(subprocess.check_output([sys.executable,'-m','pip','freeze'],text=True))
 (OUT/'nvidia_smi.txt').write_text(subprocess.check_output(['nvidia-smi'],text=True))
 h.set_deterministic(1729)
 tok,model=h.load('Qwen/Qwen2.5-7B-Instruct',revision,'bfloat16','cuda');model.requires_grad_(False)
 layers=[1,7,14,21,28]
 write('environment.json',{'revision':revision,'tokenizer_revision':revision,'torch':torch.__version__,'transformers':transformers.__version__,'numpy':numpy.__version__,'python':sys.version,'cuda':torch.version.cuda,'gpu':torch.cuda.get_device_name(0),'dtype':str(model.dtype),'attention_implementation':model.config._attn_implementation,'padding_side':tok.padding_side,'position_ids':'implicit arange sequence positions in baseline; explicit arange verified separately','cache':False,'seed':1729,'atol':1e-5,'rtol':1e-5,'deterministic_algorithms':torch.are_deterministic_algorithms_enabled(),'warn_only':torch.is_deterministic_algorithms_warn_only_enabled(),'tf32':torch.backends.cuda.matmul.allow_tf32,'model_training':model.training,'parameters_require_grad':any(p.requires_grad for p in model.parameters()),'cublas_workspace_config':os.getenv('CUBLAS_WORKSPACE_CONFIG')})
 (OUT/'qa_texts.json').write_text(json.dumps(h.QA_TEXTS,indent=2))
 records=[]
 def comp(name,a,b,kind='blocking'):
  ok,mx,mn=h.compare(a,b,1e-5,1e-5)
  rec={'name':name,'status':('PASS' if ok else 'FAIL') if kind=='blocking' else 'DIAGNOSTIC','within_tolerance':ok,'max_abs_diff':mx,'mean_abs_diff':mn,'a_checksum_float32':h.tensor_checksum(a),'b_checksum_float32':h.tensor_checksum(b)}
  records.append(rec);write('checks_incremental.json',records);print(json.dumps(rec),flush=True)
 def save(name,e,o):
  payload={'input_ids':e['input_ids'].cpu(),'attention_mask':e['attention_mask'].cpu(),'position_ids':torch.arange(e['input_ids'].shape[1]).unsqueeze(0),'hidden':{l:o.hidden_states[l].cpu() for l in layers},'last_logits':o.logits[:,-1,:].cpu()}
  torch.save(payload,OUT/(name+'.pt'));return payload
 # First numerical experiment: reconstructed length sensitivity, no mitigation.
 # 8 texts x 2 padded-length contrasts x 5 layers = 80, not an exact historical replay.
 for i,text in enumerate(h.QA_TEXTS):
  e,a=h.extract(tok,model,[text],'cuda',pad_to=64);save(f'length_{i}_64',e,a)
  for length in [96,128]:
   eb,b=h.extract(tok,model,[text],'cuda',pad_to=length);save(f'length_{i}_{length}',eb,b)
   for l in layers:comp(f'length_{i}_64_vs_{length}_layer_{l}',h.last_active_hidden(e,a,l),h.last_active_hidden(eb,b,l),'diagnostic')
  del a,b
 write('length_reproduction.json',{'status':'DIAGNOSTIC','historical_reported_failures':24,'historical_total':80,'exact_historical_reproduction':False,'limitation':'Historical script, inputs, revisions, shape pairs, GPU and raw outputs absent. This is a prospective reconstruction with eight supplied QA texts, 64->96 and 64->128, five layers.','outside_tolerance':sum(not r['within_tolerance'] for r in records),'total':len(records),'checks':records.copy()})
 del model;torch.cuda.empty_cache()
 # Run unmodified supplied harness, retain its nonzero exit without aborting evidence capture.
 cmd=[sys.executable,'/src/aeb_g0_qwen_qa_harness.py','--revision',revision,'--output',str(OUT/'original_harness_report.json')]
 with (OUT/'original_harness.log').open('w') as f:r=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT)
 write('original_harness_exit.json',{'command':cmd,'returncode':r.returncode})
 print('Original harness returncode:',r.returncode,flush=True)
 # Additional required controls absent from the supplied harness.
 tok,model=h.load('Qwen/Qwen2.5-7B-Instruct',revision,'bfloat16','cuda');model.requires_grad_(False)
 e,o=h.extract(tok,model,h.QA_TEXTS[:4],'cuda',pad_to=96);saved=save('supplemental_batch',e,o)
 def forward(enc,**kw):
  with torch.inference_mode():return model(**enc,output_hidden_states=True,return_dict=True,**kw)
 pos=torch.arange(e['input_ids'].shape[1],device='cuda').unsqueeze(0).expand(e['input_ids'].shape[0],-1)
 explicit=forward(e,position_ids=pos,use_cache=False)
 for l in layers:comp(f'explicit_position_layer_{l}',h.last_active_hidden(e,o,l),h.last_active_hidden(e,explicit,l))
 alignment=[]
 for i,text in enumerate(h.QA_TEXTS[:4]):
  ids=tok(text)['input_ids'];mask=e['attention_mask'][i].cpu();active=e['input_ids'][i].cpu()[mask.bool()].tolist()
  alignment.append({'item':i,'status':'PASS' if active==ids and mask.tolist()==[1]*len(ids)+[0]*(96-len(ids)) else 'FAIL','tokens':tok.convert_ids_to_tokens(ids),'active_ids':active,'singleton_ids':ids,'last_active_index':int(mask.sum())-1})
 write('alignment_masks.json',alignment)
 loaded=torch.load(OUT/'supplemental_batch.pt',weights_only=True)
 for l in layers:
  comp(f'save_reload_layer_{l}',saved['hidden'][l],loaded['hidden'][l])
  comp(f'finite_layer_{l}',torch.isfinite(saved['hidden'][l]).float(),torch.ones_like(saved['hidden'][l],dtype=torch.float32))
 # Actual unmasked future tokens cannot affect earlier positions under causal attention.
 ids=tok(h.QA_TEXTS[3],return_tensors='pt')['input_ids'].to('cuda');n=ids.shape[1]
 prefix={'input_ids':ids[:,:n//2],'attention_mask':torch.ones_like(ids[:,:n//2])}
 full={'input_ids':ids,'attention_mask':torch.ones_like(ids)}
 po=forward(prefix,use_cache=False);fo=forward(full,use_cache=False)
 save('causal_prefix',prefix,po);save('causal_full',full,fo)
 for l in layers:comp(f'causal_suffix_layer_{l}',po.hidden_states[l],fo.hidden_states[l][:,:n//2])
 cache=forward(prefix,use_cache=True)
 tail={'input_ids':ids[:,n//2:],'attention_mask':torch.ones_like(ids)}
 co=forward(tail,past_key_values=cache.past_key_values,use_cache=True)
 torch.save({'hidden':{l:co.hidden_states[l].cpu() for l in layers},'logits':co.logits.cpu()},OUT/'cache_tail.pt')
 for l in layers:comp(f'cache_vs_full_layer_{l}',co.hidden_states[l],fo.hidden_states[l][:,n//2:])
 comp('cache_vs_full_logits',co.logits,fo.logits[:,n//2:])
 # Same-shape singleton control supplements original unequal-shape batch control.
 for i,text in enumerate(h.QA_TEXTS[:4]):
  se,so=h.extract(tok,model,[text],'cuda',pad_to=96);save(f'single_fixed_{i}',se,so)
  for l in layers:comp(f'fixed_width_batch_single_{i}_layer_{l}',h.last_active_hidden(e,o,l)[i:i+1],h.last_active_hidden(se,so,l))
 write('run_summary.json',{'gate':'G0','status':'BLOCKED','reason':'Full gate adjudication required; no auto-pass based on original harness status.','original_exit':r.returncode,'supplemental_failures':[x['name'] for x in records if x['status']=='FAIL'],'elapsed_seconds':time.time()-start,'confirmatory_extraction':False,'resolution_attempted':False})
if __name__=='__main__':
 try:main()
 except BaseException:
  (OUT/'worker_failure.txt').write_text(traceback.format_exc());traceback.print_exc()
 finally:
  write('SHA256SUMS.json',{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in OUT.iterdir() if p.is_file() and p.name!='SHA256SUMS.json'})
