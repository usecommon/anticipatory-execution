from audit_saved_tensors import load
import numpy as np,json,hashlib
from pathlib import Path
root=Path('outputs/g0_rca_v0_2');run=root/'rca_20260911T165054Z'
a=load(run/'baseline/length_0_64.pt');b=load(run/'baseline/length_0_128.pt');s=load(run/'workspace_strict/length_0_64.pt')
n=int(a['inputs']['attention_mask'].sum())
r={}
r['active_ids_identical']=np.array_equal(a['inputs']['input_ids'][:,:n],b['inputs']['input_ids'][:,:n])
r['embedding_identical']=np.array_equal(a['modules']['model.embed_tokens'][:,:n],b['modules']['model.embed_tokens'][:,:n])
r['norm_input_identical']=np.array_equal(a['modules']['model.layers.0.input_layernorm'][:,:n],b['modules']['model.layers.0.input_layernorm'][:,:n])
r['baseline_strict_hidden_identical']={str(l):np.array_equal(a['hidden'][l],s['hidden'][l]) for l in a['hidden']}
m=load(run/'baseline/isolated_qproj.pt')
r['isolated_first64_inputs_identical']=np.array_equal(m['input64'],m['input128'][:,:64])
r['isolated_native_matches_model']={str(width):np.array_equal(m[f'native{width}'][:,:n],x['modules']['model.layers.0.self_attn.q_proj'][:,:n]) for width,x in [(64,a),(128,b)]}
def bf16round(x):
 bits=np.ascontiguousarray(x,dtype=np.float32).view(np.uint32)
 return ((bits+0x7fff+((bits>>16)&1))&0xffff0000).view(np.float32)
x=m['native64'][:,:n];y=m['native128'][:,:n];changed=x!=y
r['isolated_qproj_changed_coordinates']=int(changed.sum())
r['isolated_fp32_shape_max_abs']=float(np.max(np.abs(m['fp32_64'][:,:n]-m['fp32_128'][:,:n])))
r['native_vs_rounded_fp32_mismatch']={str(width):int(np.sum(m[f'native{width}'][:,:n]!=bf16round(m[f'fp32_{width}'][:,:n]))) for width in [64,128]}
r['changed_coordinate_examples']=[{'index':list(map(int,i)),'bf16_64':float(x[tuple(i)]),'bf16_128':float(y[tuple(i)]),'fp32_64':float(m['fp32_64'][tuple(i)]),'fp32_128':float(m['fp32_128'][tuple(i)])} for i in np.argwhere(changed)[:8]]
(root/'independent_rca_audit.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
