"""Read-only sidecar wrapper for the existing guarded extraction job.
Not launchable by itself; real canonical tensor bridge remains mandatory.
"""
import hashlib,json
from pathlib import Path
from observable import prefix_nll
CONTRACT='95dd7686f82fc1380c02539ec14fc73ab3073fc8be7b7ca015e40fd6e4fac1b0'

class SurprisalSidecar:
    def __init__(self,extractor,out):
        if extractor.contract_id!=CONTRACT:raise ValueError('canonical contract required')
        self.wrapped=extractor;self.out=Path(out);self.out.mkdir(parents=True,exist_ok=False);self.count=0
    def __getattr__(self,name):return getattr(self.wrapped,name)
    def extract_ids(self,ids):
        # Do not tokenize again or change forwarded IDs, masks, positions or numerical settings.
        state=self.wrapped.extract_ids(ids)
        n=len(ids);tokens=ids.tolist()
        if state['contract_id']!=CONTRACT or state['active_length']!=n:raise ValueError('forward provenance mismatch')
        if tuple(state['logits'].shape)!=(n,152064) or str(state['logits'].dtype)!='torch.float32':raise ValueError('canonical active logits required')
        if state['input_ids'][0,:n].tolist()!=tokens:raise ValueError('saved input alignment mismatch')
        result=prefix_nll(tokens,state['logits'])
        record={'ordinal':self.count,'contract_id':CONTRACT,'token_ids_sha256':hashlib.sha256(json.dumps(tokens,separators=(',',':')).encode()).hexdigest(),
                'measurement_version':'prefix-nll-sidecar-v1','measurement':result}
        with (self.out/f'{self.count:05d}.json').open('x') as f:f.write(json.dumps(record,indent=2)+'\n')
        self.count+=1
        return state  # identical state object; existing entrypoint still owns saved-tensor writes and gates
