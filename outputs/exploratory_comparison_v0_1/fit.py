import numpy as np,json,warnings
from collections import Counter,defaultdict
from scipy.sparse import csr_matrix,hstack
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.exceptions import ConvergenceWarning
NAMES=['prevalence','D_text','D_output','D_snapshot','D_multisnapshot','D_dynamics']
def metric(rows,p,y,split,source=None):
 indices=[i for i,r in enumerate(rows) if r['split']==split and y[i] is not None and (source is None or r['source']==source)]
 if not indices:return {'cases':0,'NLL':None,'Brier':None}
 tasks=defaultdict(list)
 for i in indices:
  q=float(np.clip(p[i],1e-15,1-1e-15));t=y[i];tasks[rows[i]['task_id']].append((-t*np.log(q)-(1-t)*np.log1p(-q),(q-t)**2))
 means=np.array([np.mean(v,axis=0) for v in tasks.values()]);return {'cases':len(indices),'tasks':len(tasks),'positive':sum(y[i] for i in indices),'negative':sum(1-y[i] for i in indices),'NLL':float(means[:,0].mean()),'Brier':float(means[:,1].mean())}
def scenario(rows,features,cases,y):
 train=[i for i,r in enumerate(rows) if r['split']=='exploratory_fit' and y[i] is not None];tune=[i for i,r in enumerate(rows) if r['split']=='exploratory_tune' and y[i] is not None]
 if set(y[i] for i in train)!={0,1} or not tune:raise ValueError('Insufficient fit classes or tune labels')
 counts=Counter(rows[i]['task_id'] for i in train);weights=np.array([1/counts[rows[i]['task_id']] for i in train]);yt=np.array([y[i] for i in train])
 texts=[];encoders=[]
 for field in ['prefix','candidate_text']:
  vectorizer=TfidfVectorizer(lowercase=True,ngram_range=(1,2),max_features=512,min_df=1)
  vectorizer.fit([cases[i][field] for i in train]);texts.append(vectorizer.transform([r[field] for r in cases]));encoders.append({'field':field,'vocabulary':vectorizer.vocabulary_,'idf':vectorizer.idf_.tolist()})
 text=hstack(texts,format='csr');mean=(float(np.dot(weights,yt))+.5)/(weights.sum()+1)
 predictions={'prevalence':np.full(len(rows),mean)};models={'prevalence':{'probability':mean}};grid=[]
 for name in NAMES[1:]:
  numeric=[]
  for f in features:
   v=list(f['shared'])
   if name!='D_text':v+=f['output']
   if name in ['D_snapshot','D_multisnapshot','D_dynamics']:v+=f['snapshots']['14']
   if name in ['D_multisnapshot','D_dynamics']:
    for l in ['7','21','28']:v+=f['snapshots'][l]
   if name=='D_dynamics':v+=f['dynamics']
   numeric.append(v)
  numeric=np.array(numeric);scaler=StandardScaler().fit(numeric[train]);X=hstack([text,csr_matrix(scaler.transform(numeric))],format='csr');choices=[]
  for C in [.01,.1,1.,10.]:
   model=LogisticRegression(C=C,penalty='l2',solver='liblinear',max_iter=2000,random_state=1729)
   with warnings.catch_warnings(record=True) as ws:
    warnings.simplefilter('always');model.fit(X[train],yt,sample_weight=weights)
   pred=model.predict_proba(X)[:,1];loss=metric(rows,pred,y,'exploratory_tune')['NLL'];bad=any(issubclass(w.category,ConvergenceWarning) for w in ws)
   grid.append({'model':name,'C':C,'tune_NLL':loss,'warnings':[str(w.message) for w in ws],'eligible':not bad})
   if not bad:choices.append((loss,C,model,pred))
  if not choices:raise ValueError('No converged candidates: '+name)
  loss,C,model,pred=min(choices,key=lambda x:(x[0],x[1]));predictions[name]=pred
  models[name]={'C':C,'tune_NLL':loss,'coef':model.coef_[0].tolist(),'intercept':float(model.intercept_[0]),'scaler_mean':scaler.mean_.tolist(),'scaler_scale':scaler.scale_.tolist(),'features':X.shape[1]}
 summary={name:{split:metric(rows,p,y,split) for split in ['exploratory_fit','exploratory_tune','exploratory_check']} for name,p in predictions.items()}
 source_slices={name:{src:metric(rows,p,y,'exploratory_check',src) for src in ['public_bfcl','synthetic']} for name,p in predictions.items()}
 return {'models':models,'encoders':encoders,'grid':grid,'metrics':summary,'check_source_slices':source_slices,'predictions':{name:p.tolist() for name,p in predictions.items()},'labels':y}
def bootstrap(rows,p1,p2,y):
 groups=defaultdict(lambda:defaultdict(list))
 for i,r in enumerate(rows):
  if r['split']!='exploratory_check' or y[i] is None:continue
  a,b=np.clip([p1[i],p2[i]],1e-15,1-1e-15);t=y[i]
  diff=(-t*np.log(a)-(1-t)*np.log1p(-a))-(-t*np.log(b)-(1-t)*np.log1p(-b))
  groups[r['group_id']][r['task_id']].append(float(diff))
 values=[np.array([np.mean(x) for x in tasks.values()]) for tasks in groups.values()];rng=np.random.default_rng(1729)
 reps=[float(np.concatenate([values[i] for i in rng.integers(len(values),size=len(values))]).mean()) for _ in range(2000)]
 return {'task_mean_NLL_gain':float(np.concatenate(values).mean()),'group_cluster_interval_95':np.quantile(reps,[.025,.975]).tolist(),'groups':len(values),'replicates':2000,'interpretation':'Exploratory interval; not a confirmatory hypothesis test'}
def run(rows,feature_rows,case_rows,prior):
 fm={r['item_id']:r for r in feature_rows};cm={r['item_id']:r for r in case_rows};rows=sorted(rows,key=lambda r:r['item_id']);features=[fm[r['item_id']] for r in rows];cases=[cm[r['item_id']] for r in rows]
 assert len(rows)==len(fm)==len(cm)==200
 splits=defaultdict(set)
 for r in rows:splits[r['group_id']].add(r['split'])
 assert all(len(s)==1 for s in splits.values())
 y=[r['binary_usefulness'] for r in rows];pm={r['item_id']:r['prior_judgment']['binary_usefulness_0_or_1'] for r in prior}
 scenarios={'current_resolved':y,'prior_overlap_replaced':[pm.get(r['item_id'],v) for r,v in zip(rows,y)],'ambiguity_excluded':[v if r['ambiguity']=='N' else None for r,v in zip(rows,y)],'unresolved_zero':[0 if v is None else v for v in y],'unresolved_one':[1 if v is None else v for v in y]}
 results={name:scenario(rows,features,cases,ys) for name,ys in scenarios.items()}
 # Meaningful held-check-label leakage test: refit primary with those labels flipped.
 altered=[1-v if v is not None and r['split']=='exploratory_check' else v for r,v in zip(rows,y)]
 replay=scenario(rows,features,cases,altered)
 assert replay['models']==results['current_resolved']['models'] and replay['encoders']==results['current_resolved']['encoders'] and replay['predictions']==results['current_resolved']['predictions']
 primary=results['current_resolved'];pairs=[('D_text','D_output'),('D_output','D_dynamics'),('D_multisnapshot','D_dynamics')]
 return {'status':'PASS_DIAGNOSTIC','row_order':[r['item_id'] for r in rows],'scenarios':results,'primary_paired_intervals':{a+'->'+b:bootstrap(rows,primary['predictions'][a],primary['predictions'][b],y) for a,b in pairs},'check_label_perturbation_invariance':True,'human_G1':'PENDING_DEFERRED','H2_H3_tested':False,'full_B1_implemented':False,'confirmatory':False}
