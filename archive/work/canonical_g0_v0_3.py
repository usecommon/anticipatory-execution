"""Bounded deterministic extraction contract; no data-dependent shape or KV reuse."""
import torch
class CanonicalExtractor:
    WIDTH=128
    def __init__(self,tokenizer,model):
        self.tokenizer=tokenizer;self.model=model
        if model.dtype!=torch.float32:raise ValueError('Contract requires FP32')
        if model.config._attn_implementation!='eager':raise ValueError('Contract requires eager attention')
        self.device=next(model.parameters()).device
        self.positions=torch.arange(self.WIDTH,device=self.device).unsqueeze(0)
        self.causal=torch.triu(torch.full((self.WIDTH,self.WIDTH),torch.finfo(torch.float32).min,device=self.device),diagonal=1)[None,None]
    def encode(self,ids,mask=None):
        ids=torch.as_tensor(ids,dtype=torch.long).flatten()
        mask=torch.ones_like(ids) if mask is None else torch.as_tensor(mask,dtype=torch.long).flatten()
        if mask.shape!=ids.shape or not bool(((mask==0)|(mask==1)).all()):raise ValueError('Invalid mask')
        n=int(mask.sum())
        if n<1 or n>self.WIDTH:raise ValueError('Active prefix must contain 1..128 tokens; no truncation')
        if not bool(mask[:n].all()) or bool(mask[n:].any()):raise ValueError('Only contiguous right padding supported')
        active=ids[:n]
        if not bool(((active>=0)&(active<self.model.config.vocab_size)).all()):raise ValueError('Invalid active token ID')
        canonical=torch.full((1,self.WIDTH),self.tokenizer.pad_token_id,dtype=torch.long,device=self.device)
        canonical[0,:n]=active.to(self.device)
        padmask=torch.zeros((1,self.WIDTH),dtype=torch.long,device=self.device);padmask[:,:n]=1
        return {'input_ids':canonical,'attention_mask':padmask,'position_ids':self.positions.clone(),'active_length':n}
    def forward_canonical(self,e):
        mask=self.causal.clone();mask[:,:,:,e['active_length']:]=torch.finfo(torch.float32).min
        with torch.inference_mode():
            o=self.model(input_ids=e['input_ids'],attention_mask=mask,position_ids=e['position_ids'],use_cache=False,output_hidden_states=True,return_dict=True)
        n=e['active_length']
        return {'input_ids':e['input_ids'].cpu(),'attention_mask':e['attention_mask'].cpu(),'position_ids':e['position_ids'].cpu(),'causal_mask':mask.cpu(),'active_length':n,'hidden':torch.stack([h[0,:n].cpu() for h in o.hidden_states]),'logits':o.logits[0,:n].cpu()}
    def extract_ids(self,ids,mask=None,*,use_cache=False,past_key_values=None):
        if use_cache or past_key_values is not None:raise ValueError('KV reuse is outside the validated contract')
        return self.forward_canonical(self.encode(ids,mask))
    def extract_text(self,text):return self.extract_ids(self.tokenizer(text)['input_ids'])
    def extract_batch(self,texts):return [self.extract_text(text) for text in texts]
