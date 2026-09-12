import argparse,collections,hashlib,json,math,statistics,shutil
from pathlib import Path
p=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--judge',type=Path,required=True);a=ap.parse_args()
read=lambda f:[json.loads(x) for x in f.read_text().splitlines()]
for inventory in ['INPUT_FREEZE.json','PROPOSAL_FREEZE.json','REVIEW_INPUT_FREEZE.json','RATINGS_FREEZE.json','JUDGE_INPUT_FREEZE.json']:
 for f,h in json.loads((p/inventory).read_text()).items():assert hashlib.sha256((p/f).read_bytes()).hexdigest()==h,(inventory,f)
items=read(p/'ALL_OPPORTUNITIES.jsonl');by={r['item_id']:r for r in items};props={k:r for k,r in by.items() if r['proposal_status']=='proposed'}
def valid(rs,mp):
 assert len(rs)==len(mp) and {r['item_id'] for r in rs}==set(mp)
 result={}
 for r in rs:
  b=r['binary_usefulness_0_or_1'];f=r['fractional_utility_0_to_1'];c=r['confidence_1_to_5']
  assert b is None or type(b) is int and b in [0,1]
  assert f is None or type(f) in [int,float] and math.isfinite(f) and 0<=f<=1
  assert type(c) is int and 1<=c<=5 and r['ambiguity_flag_Y_N'] in ['Y','N'] and r['annotator_rationale'].strip()
  assert b is not None or r['ambiguity_flag_Y_N']=='Y'
  result[mp[r['item_id']]]={**r,'blind_id':r['item_id'],'item_id':mp[r['item_id']]}
 return result
ratings={}
for n in ['A','B']:
 mp={r['blind_id']:r['item_id'] for r in read(p/f'RATER_{n}_MAPPING.jsonl')};ratings[n]=valid(read(p/f'bfcl_rater_{n}.jsonl'),mp)
mp={r['blind_id']:r['item_id'] for r in read(p/'JUDGE_MAPPING.jsonl')};judge=valid(read(a.judge),mp);assert set(judge)==set(props)
tags=read(p/'DOMAIN_TAGS.jsonl');assert len(tags)==200 and {r['item_id'] for r in tags}==set(by);domains={r['item_id']:r for r in tags}
for j in judge.values():assert j['decision_reason'].strip() and j['survival_mechanism'] in ['reusable_unchanged','reusable_narrowing','target_change','action_change','constraint_conflict','argument_change','insufficient_evidence','preparation_materiality','other']
def counts(rs):
 c=collections.Counter(r['binary_usefulness_0_or_1'] for r in rs);return {'reusable':c[1],'non_reusable':c[0],'unresolved':c[None],'ambiguity_flags':sum(r['ambiguity_flag_Y_N']=='Y' for r in rs)}
def agreement(aa,bb):
 pairs=[(aa[k]['binary_usefulness_0_or_1'],bb[k]['binary_usefulness_0_or_1']) for k in aa if aa[k]['binary_usefulness_0_or_1'] is not None and bb[k]['binary_usefulness_0_or_1'] is not None];n=len(pairs);same=sum(x==y for x,y in pairs)
 if n:
  ca=collections.Counter(x for x,y in pairs);cb=collections.Counter(y for x,y in pairs);po=same/n;pe=sum(ca[z]*cb[z] for z in [0,1])/n**2;k=(po-pe)/(1-pe) if pe!=1 else None
 else:po=pe=k=None
 return {'total_proposed':len(aa),'complete_binary_pairs':n,'pairs_with_unresolved':len(aa)-n,'binary_agreements':same,'binary_disagreements':n-same,'observed_agreement':po,'kappa':k,'degenerate_or_no_pairs':k is None,'denominator_policy':'Only paired resolved labels; all unresolved and abstentions reported separately. AI agreement is not human G1.'}
full=[]
for r in items:
 k=r['item_id'];full.append({**r,'domain_annotation':domains[k],'rater_A':ratings['A'].get(k),'rater_B':ratings['B'].get(k),'adjudication':judge.get(k),'label_status':'AI_provisional_not_human_gold' if k in judge else 'ABSTENTION_NO_REUSE_LABEL'})
synthetic=read(p.parent/'synthetic_expansion_v0_1/results/JUDGED_ITEMS.jsonl');synlabels=[r['adjudication'] for r in synthetic]
c=counts(list(judge.values()));syn=counts(synlabels)
public_domain=collections.Counter(r['domain'] for r in tags);syn_domain=collections.Counter(r['domain'] for r in synthetic)
scores={'source_records':200,'distinct_full_instructions':len({r['full_instruction'] for r in items}),'proposal_opportunities':200,'proposed_items':len(props),'abstentions':200-len(props),'proposal_coverage':len(props)/200,'checkpoint_words':6,'rater_A':counts(list(ratings['A'].values())),'rater_B':counts(list(ratings['B'].values())),'adjudication':c,'rater_agreement':agreement(ratings['A'],ratings['B']),'reusable_per_opportunity':c['reusable']/200,'reusable_per_proposed':c['reusable']/len(props),'reusable_per_resolved':c['reusable']/(c['reusable']+c['non_reusable']) if c['reusable']+c['non_reusable'] else None,'public_domains_opportunities':dict(public_domain),'public_domains_proposed':dict(collections.Counter(domains[k]['domain'] for k in props)),'public_action_classes':dict(collections.Counter(r['execution_class'] for r in props.values())),'survival_mechanisms':dict(collections.Counter(j['survival_mechanism'] for j in judge.values())),'synthetic_comparator':{'review_items':len(synthetic),'tasks':len({r['task_id'] for r in synthetic}),'families':len({r['family_id'] for r in synthetic}),'adjudication':syn,'domains_review_items':dict(syn_domain),'action_classes':dict(collections.Counter(r['execution_class'] for r in synthetic)),'checkpoint_words_min_median_max':[min(len(r['prefix'].split()) for r in synthetic),statistics.median(len(r['prefix'].split()) for r in synthetic),max(len(r['prefix'].split()) for r in synthetic)],'candidate_coverage':'Not measured under a prefix-only proposer; hand-authored work at selected anchors.'},'G1':'PENDING','G0':'PASS_SCOPED_UNCHANGED','public_source_retrieval_verified':True,'adaptation_publicly_released':False,'research_model_inference':False,'development_extraction':False,'confirmatory_extraction':False,'matched_source_effect_estimate':False,'latency_measured':False}
out=p/'results';assert not out.exists();out.mkdir()
def write(name,rs):(out/name).write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rs))
write('ALL_ITEMS.jsonl',full)
for name,pred in [('REUSABLE.jsonl',lambda r:r['adjudication'] is not None and r['adjudication']['binary_usefulness_0_or_1']==1),('NON_REUSABLE.jsonl',lambda r:r['adjudication'] is not None and r['adjudication']['binary_usefulness_0_or_1']==0),('UNRESOLVED.jsonl',lambda r:r['adjudication'] is not None and r['adjudication']['binary_usefulness_0_or_1'] is None),('ABSTENTIONS.jsonl',lambda r:r['adjudication'] is None)]:write(name,[r for r in full if pred(r)])
write('RATING_DISAGREEMENTS.jsonl',[r for r in full if r['adjudication'] is not None and r['rater_A']['binary_usefulness_0_or_1']!=r['rater_B']['binary_usefulness_0_or_1']])
shutil.copyfile(a.judge,out/'JUDGE_RAW.jsonl');scores['judge_raw_sha256']=hashlib.sha256(a.judge.read_bytes()).hexdigest();(out/'SCORES.json').write_text(json.dumps(scores,indent=2)+'\n')
lines=['# All 200 public-source proposal opportunities','','AI provisional labels; abstentions have no work product and no reuse label. No source tasks executed.','']
for r in full:
 j=r['adjudication'];lines.extend([f"## {r['item_id']}",'',f"**Prefix:** {r['prefix']}",'',f"**Full first instruction:** {r['full_instruction']}",'',f"**Proposal:** {r['proposal_status']}",'',f"**Prefix support:** {r['prefix_support']}",''])
 if j:lines.extend([f"**Action:** {r['candidate_action']}",'','```text',r['work_product'],'```','',f"**Reuse:** {j['binary_usefulness_0_or_1']} · **Ambiguity:** {j['ambiguity_flag_Y_N']}",'',j['annotator_rationale'],''])
(out/'REVIEW.md').write_text('\n'.join(lines));print(json.dumps(scores,indent=2))
