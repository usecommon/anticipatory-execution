"""Prepared canonical QA bridge. Requires validated real extractor and pinned repository.
No launcher or automatic job execution. This module has not run on real tensors yet.
"""
import hashlib,json,sys,traceback
from pathlib import Path

def run_bridge(extractor,repo,out):
    import torch
    repo=Path(repo);out=Path(out);out.mkdir(parents=True,exist_ok=False)
    sys.path.insert(0,str(repo/'outputs/exploratory_entrypoint_v0_1'))
    from entrypoint import run_job,PINS
    from capture import SurprisalSidecar
    class Recorder:
        def __init__(self,e):self.e=e;self.states=[]
        def __getattr__(self,n):return getattr(self.e,n)
        def extract_ids(self,ids):
            state=self.e.extract_ids(ids);self.states.append(state);return state
    try:
        for name in ['extractor','original_pipeline','instrumentation_validation']:
            pin=PINS[name]
            assert hashlib.sha256((repo/pin['path']).read_bytes()).hexdigest()==pin['sha256']
        input_file=repo/PINS['instrumentation_validation']['path'];rec=Recorder(extractor)
        count_before=len(extractor.audit)
        a=run_job(rec,input_file,out/'baseline',partition='instrumentation_validation')
        wrapped=SurprisalSidecar(extractor,out/'surprisal')
        b=run_job(wrapped,input_file,out/'wrapped',partition='instrumentation_validation')
        assert len(a['items'])==len(b['items'])==len(rec.states)==wrapped.count==12
        checks=[]
        for i,(left,right,state) in enumerate(zip(a['items'],b['items'],rec.states)):
            assert left['id']==right['id'] and left['token_ids']==right['token_ids']
            x=torch.load(out/'baseline'/left['file'],weights_only=True);y=torch.load(out/'wrapped'/right['file'],weights_only=True)
            assert x.keys()==y.keys()
            for k in x:assert torch.equal(x[k],y[k]) if isinstance(x[k],torch.Tensor) else x[k]==y[k],k
            side=json.loads((out/'surprisal'/f'{i:05d}.json').read_text());tokens=left['token_ids'];n=len(tokens)
            assert side['ordinal']==i and side['token_ids_sha256']==hashlib.sha256(json.dumps(tokens,separators=(',',':')).encode()).hexdigest()
            # Independent vectorized formula on baseline full active logits, not captured summaries.
            logits=state['logits'][:-1].to(dtype=torch.float64)
            target=torch.tensor(tokens[1:],dtype=torch.long)
            losses=(torch.logsumexp(logits,dim=-1)-logits[torch.arange(n-1),target]).tolist()
            measured=side['measurement'];assert measured['scored_tokens']==n-1
            assert len(losses)==len(measured['per_token_nll'])
            max_error=max([abs(v-w) for v,w in zip(losses,measured['per_token_nll'])]+[0.])
            assert max_error<=1e-10
            assert abs(sum(losses)-measured['sum_nll'])<=max(1,n-1)*1e-10
            assert measured['mean_nll'] is None if n==1 else abs(measured['mean_nll']-sum(losses)/(n-1))<=1e-10
            checks.append({'id':left['id'],'legacy_fields_bitwise_equal':True,'nll_max_abs_error':max_error,'token_hash_matched':True})
        count_after=len(extractor.audit);assert count_after-count_before==24
        try:run_job(wrapped,input_file,out/'confirmatory_rejection',partition='confirmatory')
        except Exception:pass
        else:raise AssertionError('confirmatory partition accepted')
        failure=json.loads((out/'confirmatory_rejection/failure.json').read_text())
        assert failure['error_type']=='ContractError' and 'Partition not authorized' in failure['error']
        assert len(extractor.audit)==count_after and wrapped.count==12
        result={'status':'PASS_CANONICAL_CAPTURE_BRIDGE','checks':checks,'forward_count':24,
                'confirmatory_rejected_zero_forwards':True,'research_extraction':False,'full_B1_complete':False}
        (out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');return result
    except Exception:
        (out/'FAILURE.txt').write_text(traceback.format_exc());raise
