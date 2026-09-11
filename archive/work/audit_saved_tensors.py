"""Read only known tensor/OrderedDict pickle structures from our own torch.save files."""
import pickle,zipfile,io,collections,hashlib,json
from pathlib import Path
import numpy as np
DTYPES={'BFloat16Storage':'bf16','FloatStorage':'<f4','LongStorage':'<i8','BoolStorage':'?','HalfStorage':'<f2','IntStorage':'<i4'}
def load(path):
 z=zipfile.ZipFile(path);prefix=z.namelist()[0].split('/')[0]
 def rebuild(storage,offset,size,stride,*args):
  a=storage
  return np.ndarray(tuple(size),dtype=a.dtype,buffer=a,offset=offset*a.itemsize,strides=tuple(s*a.itemsize for s in stride))
 class Reader(pickle.Unpickler):
  def find_class(self,module,name):
   if module=='torch._utils' and name in ['_rebuild_tensor_v2','_rebuild_tensor']:return rebuild
   if module=='torch' and name in DTYPES:return DTYPES[name]
   if module=='collections' and name=='OrderedDict':return collections.OrderedDict
   raise ValueError((module,name))
  def persistent_load(self,pid):
   tag,dtype,key,device,count=pid
   assert tag=='storage'
   b=z.read(prefix+'/data/'+key)
   if dtype=='bf16':a=(np.frombuffer(b,dtype='<u2').astype('<u4')<<16).view('<f4')
   else:a=np.frombuffer(b,dtype=dtype)
   assert a.size==count
   return a
 return Reader(io.BytesIO(z.read(prefix+'/data.pkl'))).load()
def checksum(x):return hashlib.sha256(np.ascontiguousarray(x,dtype=np.float32).tobytes()).hexdigest()
if __name__=='__main__':
 root=Path('outputs/g0_evidence_v0_1/run_20260911T163140Z');rows=[]
 refs={r['name']:r for r in json.loads((root/'length_reproduction.json').read_text())['checks']}
 for i in range(8):
  a=load(root/f'length_{i}_64.pt');n=int(a['attention_mask'].sum())
  for width in [96,128]:
   b=load(root/f'length_{i}_{width}.pt')
   assert np.array_equal(a['input_ids'][:,:n],b['input_ids'][:,:n])
   for l in [1,7,14,21,28]:
    x=a['hidden'][l][:,n-1,:];y=b['hidden'][l][:,n-1,:];r=refs[f'length_{i}_64_vs_{width}_layer_{l}']
    assert checksum(x)==r['a_checksum_float32'] and checksum(y)==r['b_checksum_float32']
    d=x.astype('float64')-y.astype('float64')
    rows.append({'item':i,'width':width,'layer':l,'relative_l2':float(np.linalg.norm(d)/np.linalg.norm(x.astype('float64'))),'max_abs':float(np.max(np.abs(d))),'mean_abs':float(np.mean(np.abs(d))),'cosine_distance':float(1-np.dot(x.ravel().astype('float64'),y.ravel().astype('float64'))/(np.linalg.norm(x.astype('float64'))*np.linalg.norm(y.astype('float64'))))})
 Path('outputs/g0_rca_v0_2/baseline_tensor_audit.json').write_text(json.dumps({'checksums_matched':160,'active_token_ids_equal':True,'rows':rows},indent=2))
 print('160 tensor checksums match; active token IDs equal')
 for l in [1,7,14,21,28]:
  r=[x for x in rows if x['layer']==l];print(l,'relative L2 range',min(x['relative_l2'] for x in r),max(x['relative_l2'] for x in r))
