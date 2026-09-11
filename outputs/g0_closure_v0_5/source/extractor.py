"""Canonical Qwen extraction v0.5. Only the factory is a supported constructor."""
import hashlib,json,os,random
from pathlib import Path
import numpy as np
import torch
import transformers
REVISION='a09a35458c702b33eeacc393d103063234e8bc28'
WIDTH=128
GPU='NVIDIA A100-SXM4-40GB'
class ContractError(ValueError):pass
def digest(value):return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def file_hash(path):
 h=hashlib.sha256()
 with open(path,'rb') as f:
  for chunk in iter(lambda:f.read(8*1024*1024),b''):h.update(chunk)
 return h.hexdigest()
def runtime_check():
 if WIDTH!=128 or torch.is_autocast_enabled():raise ContractError('Canonical width/autocast contract changed')
 if torch.__version__!='2.5.1+cu124' or transformers.__version__!='4.45.2':raise ContractError('Unvalidated framework version')
 if not torch.cuda.is_available() or torch.cuda.get_device_name(0)!=GPU:raise ContractError('Unvalidated GPU')
 if os.environ.get('CUBLAS_WORKSPACE_CONFIG')!=':4096:8':raise ContractError('CuBLAS workspace mismatch')
 if not torch.are_deterministic_algorithms_enabled() or torch.is_deterministic_algorithms_warn_only_enabled():raise ContractError('Strict determinism required')
 if torch.backends.cuda.matmul.allow_tf32 or torch.backends.cudnn.allow_tf32 or torch.backends.cudnn.benchmark:raise ContractError('Unvalidated numerical flags')
def configure():
 # Workspace must already be set by the launcher before CUDA initialization.
 random.seed(1729);np.random.seed(1729);torch.manual_seed(1729);torch.cuda.manual_seed_all(1729)
 torch.use_deterministic_algorithms(True,warn_only=False)
 torch.backends.cuda.matmul.allow_tf32=False;torch.backends.cudnn.allow_tf32=False;torch.backends.cudnn.benchmark=False
 runtime_check()
_FACTORY_KEY=object()
class CanonicalExtractor:
 def __init__(self,tokenizer,model,identity,key=None):
  if key is not _FACTORY_KEY:raise ContractError('Use load_extractor with verified checkpoint manifest')
  self.__tok=tokenizer;self.__model=model;self.__identity=identity
  self.__parameters=tuple(model.parameters())
  self.__param_state=tuple((id(p),p.data_ptr(),p._version,tuple(p.shape)) for p in self.__parameters)
  self.__config=digest(model.config.to_dict())
  self.__tokenizer_hash=hashlib.sha256(tokenizer.backend_tokenizer.to_str().encode()).hexdigest()
  self.__tokenizer_flags=(tokenizer.pad_token_id,tokenizer.eos_token_id,tokenizer.padding_side,len(tokenizer))
  self.__contract={'implementation':'canonical-v0.5','code_sha256':file_hash(__file__),'revision':REVISION,'files':identity['files'],'gpu':GPU,'torch':torch.__version__,'transformers':transformers.__version__,'dtype':'float32','attention':'eager','shape':[1,WIDTH],'positions':'explicit arange','cache':False,'seed':1729,'atol':1e-5,'rtol':1e-5,'model_config':self.__config,'tokenizer_hash':self.__tokenizer_hash}
  self.__contract_id=digest(self.__contract);self.audit=[];self.verify()
 @property
 def contract(self):return json.loads(json.dumps(self.__contract))
 @property
 def contract_id(self):return self.__contract_id
 def verify(self):
  runtime_check();m=self.__model
  if m.training or m.dtype!=torch.float32 or m.config._attn_implementation!='eager':raise ContractError('Model execution contract changed')
  if digest(m.config.to_dict())!=self.__config:raise ContractError('Model configuration changed')
  for p,record in zip(self.__parameters,self.__param_state):
   if p.requires_grad or p.dtype!=torch.float32 or p.device!=torch.device('cuda:0') or (id(p),p.data_ptr(),p._version,tuple(p.shape))!=record:raise ContractError('Frozen parameter contract changed')
  if tuple(id(p) for p in m.parameters())!=tuple(v[0] for v in self.__param_state):raise ContractError('Parameter set changed')
  t=self.__tok
  if (t.pad_token_id,t.eos_token_id,t.padding_side,len(t))!=self.__tokenizer_flags:raise ContractError('Tokenizer configuration changed')
  if hashlib.sha256(t.backend_tokenizer.to_str().encode()).hexdigest()!=self.__tokenizer_hash:raise ContractError('Tokenizer backend changed')
 def tokenize(self,text):
  self.verify()
  if not isinstance(text,str) or not text.strip():raise ContractError('A nonempty observed prefix string is required')
  return self.__tok(text,add_special_tokens=True)['input_ids']
 def _validated_ids(self,ids,mask=None):
  try:a=torch.as_tensor(ids)
  except (ValueError,TypeError,RuntimeError) as e:raise ContractError('Invalid token IDs') from e
  ints=(torch.uint8,torch.int8,torch.int16,torch.int32,torch.int64)
  if a.ndim!=1 or a.numel()==0 or a.dtype not in ints:raise ContractError('IDs must be a nonempty 1-D integer sequence')
  if mask is None:b=torch.ones_like(a)
  else:
   try:b=torch.as_tensor(mask)
   except (ValueError,TypeError,RuntimeError) as e:raise ContractError('Invalid attention mask') from e
   if b.ndim!=1 or b.shape!=a.shape or b.dtype not in ints+(torch.bool,):raise ContractError('Mask must be a matching 1-D binary integer/bool sequence')
  if not bool(((b==0)|(b==1)).all()):raise ContractError('Mask is not binary')
  n=int(b.sum())
  if n<1 or n>WIDTH:raise ContractError('Active prefix length outside 1..128; no truncation')
  if not bool(b[:n].all()) or bool(b[n:].any()):raise ContractError('Only contiguous right padding is supported')
  if not bool(((a>=0)&(a<self.__model.config.vocab_size)).all()):raise ContractError('Token ID outside vocabulary')
  return a[:n].to(device='cpu',dtype=torch.long).clone()
 def extract_ids(self,ids,mask=None,*,use_cache=False,past_key_values=None):
  self.verify()
  if use_cache is not False or past_key_values is not None:raise ContractError('Cache execution is unsupported')
  active=self._validated_ids(ids,mask);n=active.numel()
  inp=torch.full((1,WIDTH),self.__tok.pad_token_id,dtype=torch.long,device='cuda');inp[0,:n]=active.cuda()
  positions=torch.arange(WIDTH,device='cuda').unsqueeze(0)
  causal=torch.triu(torch.full((WIDTH,WIDTH),torch.finfo(torch.float32).min,device='cuda'),diagonal=1)[None,None];causal[:,:,:,n:]=torch.finfo(torch.float32).min
  pad=torch.zeros((1,WIDTH),dtype=torch.long);pad[:,:n]=1
  if inp.shape!=(1,WIDTH) or positions.shape!=(1,WIDTH) or causal.shape!=(1,1,WIDTH,WIDTH):raise ContractError('Internal canonical shape violation')
  with torch.inference_mode():o=self.__model(input_ids=inp,attention_mask=causal,position_ids=positions,use_cache=False,output_hidden_states=True,return_dict=True)
  self.audit.append({'contract_id':self.contract_id,'shape':list(inp.shape),'mask_shape':list(causal.shape),'active_length':n,'position_sha':hashlib.sha256(positions.cpu().numpy().tobytes()).hexdigest(),'cache':False})
  return {'contract_id':self.contract_id,'input_ids':inp.cpu(),'attention_mask':pad,'position_ids':positions.cpu(),'active_length':n,'hidden':torch.stack([h[0,:n].cpu() for h in o.hidden_states]),'logits':o.logits[0,:n].cpu()}
 def extract_text(self,text):return self.extract_ids(self.tokenize(text))
 def extract_batch(self,texts):
  if not isinstance(texts,(list,tuple)):raise ContractError('Batch must be a sequence of strings')
  encoded=[self._validated_ids(self.tokenize(t)) for t in texts] # preflight before any forward
  return [self.extract_ids(ids) for ids in encoded]
def load_extractor(model_dir,manifest):
 configure();root=Path(model_dir)
 if manifest.get('revision')!=REVISION or manifest.get('repo')!='Qwen/Qwen2.5-7B-Instruct':raise ContractError('Unvalidated checkpoint identity')
 required={'config.json','tokenizer.json','tokenizer_config.json','model.safetensors.index.json',*[f'model-{i:05d}-of-00004.safetensors' for i in range(1,5)]}
 if not required.issubset(manifest.get('files',{})):raise ContractError('Incomplete checkpoint manifest')
 for name,sha in manifest['files'].items():
  if '/' in name or name in ['.','..'] or file_hash(root/name)!=sha:raise ContractError('Checkpoint file mismatch: '+name)
 tok=transformers.AutoTokenizer.from_pretrained(root,use_fast=True,local_files_only=True)
 model=transformers.AutoModelForCausalLM.from_pretrained(root,torch_dtype=torch.float32,attn_implementation='eager',low_cpu_mem_usage=True,local_files_only=True).to('cuda').eval().requires_grad_(False)
 if model.config.model_type!='qwen2' or model.config.num_hidden_layers!=28:raise ContractError('Unexpected model architecture')
 return CanonicalExtractor(tok,model,manifest,_FACTORY_KEY)
