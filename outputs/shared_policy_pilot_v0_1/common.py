import collections,json,math
from pathlib import Path
P=Path(__file__).resolve().parent
def read(f):return [json.loads(x) for x in f.read_text().splitlines()]
def validate(r):
 s=r['artifact_sufficiency'];b=r['binary_usefulness_0_or_1'];f=r['fractional_utility_0_to_1'];c=r['confidence_1_to_5'];flag=r['ambiguity_flag_Y_N']
 assert s in ['substantive','no_material_work','uncertain'] and r['sufficiency_rationale'].strip()
 assert b is None or type(b) is int and b in [0,1]
 assert f is None or type(f) in [int,float] and math.isfinite(f) and 0<=f<=1
 assert type(c) is int and 1<=c<=5 and flag in ['Y','N'] and r['annotator_rationale'].strip()
 if s!='substantive':assert b is None and f is None
 if s=='uncertain' or s=='substantive' and b is None:assert flag=='Y'
def mapped(raw,mapping):
 rs=read(raw);mp={r['blind_id']:r['item_id'] for r in read(mapping)};assert len(rs)==len(mp) and {r['item_id'] for r in rs}==set(mp)
 out={}
 for r in rs:validate(r);out[mp[r['item_id']]]={**r,'item_id':mp[r['item_id']],'blind_id':r['item_id']}
 return out
def disposition(j):
 if j is None:return 'abstention'
 if j['artifact_sufficiency']=='no_material_work':return 'invalid_candidate'
 if j['artifact_sufficiency']=='uncertain':return 'uncertain_candidate'
 return {1:'reusable',0:'non_reusable',None:'unresolved_reuse'}[j['binary_usefulness_0_or_1']]
def agreement(a,b):
 assert set(a)==set(b);pairs=[(a[k]['binary_usefulness_0_or_1'],b[k]['binary_usefulness_0_or_1']) for k in a if a[k]['artifact_sufficiency']==b[k]['artifact_sufficiency']=='substantive' and a[k]['binary_usefulness_0_or_1'] is not None and b[k]['binary_usefulness_0_or_1'] is not None];n=len(pairs);same=sum(x==y for x,y in pairs);kappa=None
 if n:
  ca=collections.Counter(x for x,y in pairs);cb=collections.Counter(y for x,y in pairs);pe=sum(ca[z]*cb[z] for z in [0,1])/n**2
  if pe!=1:kappa=(same/n-pe)/(1-pe)
 return {'proposed_pairs':len(a),'sufficiency_agreements':sum(a[k]['artifact_sufficiency']==b[k]['artifact_sufficiency'] for k in a),'full_disposition_agreements':sum(disposition(a[k])==disposition(b[k]) for k in a),'complete_substantive_binary_pairs':n,'binary_agreements':same,'pairs_outside_binary_denominator':len(a)-n,'kappa':kappa,'denominator_note':'Only both-substantive resolved labels; dependent task rows, AI diagnostic not humanG1.'}
