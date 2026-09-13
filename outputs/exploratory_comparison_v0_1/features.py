import numpy as np,re
LAYERS=(7,14,21,28)
def cosine(a,b):return float(np.dot(a,b)/max(float(np.linalg.norm(a)*np.linalg.norm(b)),1e-12))
def probs(logits):
 a=np.asarray(logits,dtype=np.float64);a=a-a.max();p=np.exp(a);return p/p.sum()
def entropy(p):return float(-np.sum(p*np.log(np.maximum(p,1e-300))))
def js(p,q):
 m=(p+q)/2
 return float(.5*np.sum(p*np.log(np.maximum(p,1e-300)/np.maximum(m,1e-300)))+.5*np.sum(q*np.log(np.maximum(q,1e-300)/np.maximum(m,1e-300))))
def build(case,states):
 assert len(states)==3
 hs=[d['hidden_last'].numpy().astype(np.float64) for d in states]
 ps=[probs(d['logits_last'].numpy()) for d in states];es=[entropy(p) for p in ps];p=ps[-1];top=np.sort(p)[-2:]
 words=case['prefix'].split();shared=[len(words),states[-1]['active_length'],len(case['prefix']),len(case['candidate_text']),case['execution_class'],len(re.findall(r'\d+',case['prefix'])),int(words[-1].lower() in {'and','or','to','for','with','in','of','from','by','before','after'}),int(case['prefix'].rstrip()[-1:] in '.?!;:')]
 output=[es[-1],float(top[-1]),float(top[-1]-top[-2]),int(ps[-2].argmax()==p.argmax()),js(ps[-2],p),es[-1]-es[-2],float(np.mean(es))]
 projection=np.random.default_rng(1729).normal(size=(3584,64))/8
 snapshots={str(l):(hs[-1][l]@projection).tolist() for l in LAYERS}
 dynamics=[]
 for l in LAYERS:
  a,b,c=[h[l] for h in hs];v=c-b;old=b-a
  dynamics.extend([float(np.linalg.norm(v)),cosine(b,c),float(np.linalg.norm(v-old)),1-cosine(v,old)])
 dynamics.extend(cosine(hs[-1][a],hs[-1][b]) for a,b in [(7,14),(14,21),(21,28)])
 assert np.isfinite(shared+output+dynamics+sum(snapshots.values(),[])).all()
 return {'item_id':case['item_id'],'shared':shared,'output':output,'snapshots':snapshots,'dynamics':dynamics}
def selftest():
 assert abs(entropy(probs([0,0]))-np.log(2))<1e-12
 assert abs(js(np.array([1.,0]),np.array([0.,1]))-np.log(2))<1e-12
 assert js(np.array([.2,.8]),np.array([.2,.8]))==0
 assert abs(cosine(np.array([1.,0]),np.array([1.,0]))-1)<1e-12
 assert cosine(np.zeros(2),np.ones(2))==0
 a=np.array([0.,0]);b=np.array([1.,0]);c=np.array([2.,0]);assert np.linalg.norm((c-b)-(b-a))==0
 return {'status':'PASS','analytic_cases':6}
