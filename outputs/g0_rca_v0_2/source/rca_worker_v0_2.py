import os,sys,json,time,traceback,hashlib,inspect
from pathlib import Path
OUT=Path(sys.argv[1]);OUT.mkdir(parents=True,exist_ok=False)
CASE=sys.argv[2]
def write(n,v):(OUT/n).write_text(json.dumps(v,indent=2,default=str))
def main():
 import torch,transformers
 from torch.nn.attention import sdpa_kernel,SDPBackend
 from contextlib import nullcontext
 import aeb_g0_qwen_qa_harness as h
 h.set_deterministic(1729)
 if CASE!='baseline':torch.use_deterministic_algorithms(True,warn_only=False)
 if CASE=='bf16_no_reduced':torch.backends.cuda.matmul.allow_bf16_reduced_precision_reduction=False
 dtype=torch.float32 if CASE=='fp32_eager' else torch.bfloat16
 attn='eager' if CASE in ['bf16_eager','fp32_eager'] else 'sdpa'
 revision='a09a35458c702b33eeacc393d103063234e8bc28'
 tok=transformers.AutoTokenizer.from_pretrained('/model',use_fast=True)
 model=transformers.AutoModelForCausalLM.from_pretrained('/model',torch_dtype=dtype,attn_implementation=attn,low_cpu_mem_usage=True).to('cuda').eval().requires_grad_(False)
 meta={'case':CASE,'revision':revision,'torch':torch.__version__,'transformers':transformers.__version__,'gpu':torch.cuda.get_device_name(0),'dtype':str(dtype),'attention':attn,'workspace':os.getenv('CUBLAS_WORKSPACE_CONFIG'),'warn_only':torch.is_deterministic_algorithms_warn_only_enabled(),'bf16_reduced_precision_reduction':torch.backends.cuda.matmul.allow_bf16_reduced_precision_reduction,'fp16_reduced_precision_reduction':torch.backends.cuda.matmul.allow_fp16_reduced_precision_reduction,'tf32':torch.backends.cuda.matmul.allow_tf32,'seed':1729,'atol':1e-5,'rtol':1e-5}
 write('environment.json',meta)
 (OUT/'modeling_qwen2.py').write_text(inspect.getsource(sys.modules[model.__class__.__module__]))
 layers=[1,7,14,21,28];records=[];snapshots={};hooks=[];current={}
 names=['model.embed_tokens','model.layers.0.input_layernorm','model.layers.0.self_attn.q_proj','model.layers.0.self_attn.k_proj','model.layers.0.self_attn.v_proj','model.layers.0.self_attn','model.layers.0.post_attention_layernorm','model.layers.0.mlp','model.layers.0','model.norm']
 def hook(name):
  def f(m,args,out):
   t=out[0] if isinstance(out,tuple) else out
   if isinstance(t,torch.Tensor):current[name]=t.detach().cpu()
  return f
 for n,m in model.named_modules():
  if n in names:hooks.append(m.register_forward_hook(hook(n)))
 def enc(texts,width=None):
  e=tok(texts,return_tensors='pt',padding='max_length' if width else True,max_length=width,truncation=False)
  return {k:v.to('cuda') for k,v in e.items()}
 def forward(label,e,**kw):
  current.clear()
  ctx=sdpa_kernel(SDPBackend.MATH) if CASE=='bf16_math' else nullcontext()
  with torch.inference_mode(),ctx:o=model(**e,output_hidden_states=True,return_dict=True,**kw)
  snap={'inputs':{k:v.cpu() for k,v in e.items()},'hidden':{l:o.hidden_states[l].cpu() for l in layers},'modules':dict(current),'logits':o.logits.cpu() if label.startswith('cache_') else o.logits[:,-1,:].cpu()}
  torch.save(snap,OUT/(label+'.pt'));snapshots[label]=snap
  return o,snap
 def cmp(name,a,b):
  a=a.float();b=b.float();d=(a-b).abs();norm=float(a.norm());r={'name':name,'status':'PASS' if torch.allclose(a,b,atol=1e-5,rtol=1e-5) else 'FAIL','max_abs':d.max().item(),'mean_abs':d.mean().item(),'relative_l2':float(d.norm())/max(norm,1e-30),'unequal_elements':int((a!=b).sum()),'elements':a.numel()};records.append(r);write('checks.json',records);return r
 texts=h.QA_TEXTS[:2]
 for i,text in enumerate(texts):
  e=enc([text],64);_,a=forward(f'length_{i}_64',e,use_cache=False)
  _,b=forward(f'length_{i}_128',enc([text],128),use_cache=False)
  active=int(e['attention_mask'].sum())
  for l in layers:cmp(f'length_{i}_layer_{l}',a['hidden'][l][:,active-1],b['hidden'][l][:,active-1])
  for n in names:cmp(f'localize_length_{i}_{n}',a['modules'][n][:,:active],b['modules'][n][:,:active])
  if i==0:
   _,repeat=forward('repeat',e,use_cache=False)
   for l in layers:cmp(f'repeat_{l}',a['hidden'][l],repeat['hidden'][l])
   altered={k:v.clone() for k,v in e.items()};altered['input_ids'][altered['attention_mask']==0]=1
   _,mask=forward('masked_content',altered,use_cache=False)
   for l in layers:cmp(f'masked_content_{l}',a['hidden'][l][:,:active],mask['hidden'][l][:,:active])
 _,batch=forward('batch64',enc(texts,64),use_cache=False)
 for i,text in enumerate(texts):
  n=len(tok(text)['input_ids']);a=snapshots[f'length_{i}_64']
  for l in layers:cmp(f'batch_{i}_layer_{l}',a['hidden'][l][:,n-1],batch['hidden'][l][i:i+1,n-1])
  for name in names:cmp(f'localize_batch_{i}_{name}',a['modules'][name][:,:n],batch['modules'][name][i:i+1,:n])
 e=enc([h.QA_TEXTS[3]]);n=e['input_ids'].shape[1];cut=n//2
 _,full=forward('cache_full',e,use_cache=False)
 pre={k:v[:,:cut] for k,v in e.items()};po,_=forward('cache_prefix',pre,use_cache=True)
 tail={'input_ids':e['input_ids'][:,cut:],'attention_mask':e['attention_mask']}
 _,cached=forward('cache_tail',tail,past_key_values=po.past_key_values,use_cache=True)
 for l in layers:cmp(f'cache_layer_{l}',full['hidden'][l][:,cut:],cached['hidden'][l])
 cmp('cache_logits',full['logits'][:,cut:],cached['logits'])
 # Isolate the first attention projection on IDENTICAL layer-normalized inputs.
 # Changing only GEMM row count cannot be explained by attention masks or cache logic.
 a=snapshots['length_0_64']['modules']['model.layers.0.input_layernorm'].to('cuda');n=len(tok(texts[0])['input_ids'])
 x=torch.cat([a,torch.zeros_like(a)],dim=1)
 proj=model.model.layers[0].self_attn.q_proj
 with torch.inference_mode():
  y1=proj(a).cpu();y2=proj(x).cpu()
  z1=torch.nn.functional.linear(a.float(),proj.weight.float(),proj.bias.float()).cpu()
  z2=torch.nn.functional.linear(x.float(),proj.weight.float(),proj.bias.float()).cpu()
 cmp('isolated_qproj_native_shape',y1[:,:n],y2[:,:n]);cmp('isolated_qproj_fp32_shape',z1[:,:n],z2[:,:n])
 torch.save({'input64':a.cpu(),'input128':x.cpu(),'native64':y1,'native128':y2,'fp32_64':z1,'fp32_128':z2},OUT/'isolated_qproj.pt')
 write('summary.json',{'case':CASE,'counts':{s:sum(r['status']==s for r in records) for s in ['PASS','FAIL']},'complete':True})
if __name__=='__main__':
 try:main()
 except BaseException:
  (OUT/'failure.txt').write_text(traceback.format_exc());traceback.print_exc();sys.exit(1)
 finally:write('sha256.json',{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in OUT.iterdir() if p.is_file() and p.name!='sha256.json'})
