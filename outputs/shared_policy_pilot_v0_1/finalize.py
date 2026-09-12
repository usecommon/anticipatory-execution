import argparse,collections,hashlib,json,shutil
from pathlib import Path
from common import P as p,read,mapped,disposition,agreement
ap=argparse.ArgumentParser();ap.add_argument('--judge',type=Path,required=True);a=ap.parse_args()
for inv in ['INPUT_FREEZE.json','PROPOSAL_FREEZE.json','REVIEW_FREEZE.json','RATINGS_FREEZE.json','JUDGE_FREEZE.json']:
 for f,h in json.loads((p/inv).read_text()).items():assert hashlib.sha256((p/f).read_bytes()).hexdigest()==h,(inv,f)
ratings={n:mapped(p/f'shared_rater_{n}.jsonl',p/f'RATER_{n}_MAPPING.jsonl') for n in ['A','B']};judge=mapped(a.judge,p/'JUDGE_MAPPING.jsonl');rows=read(p/'ALL_OPPORTUNITIES.jsonl');assert set(judge)=={r['item_id'] for r in rows if r['proposal_status']=='proposed'}
full=[]
for r in rows:
 k=r['item_id'];j=judge.get(k)
 if j:assert j['decision_reason'].strip()
 full.append({**r,'rater_A':ratings['A'].get(k),'rater_B':ratings['B'].get(k),'adjudication':j,'disposition':disposition(j),'label_status':'AI_development_only_not_human_gold'})
states=['reusable','non_reusable','unresolved_reuse','invalid_candidate','uncertain_candidate','abstention']
def summarize(rs):
 c=collections.Counter(r['disposition'] for r in rs);n=len(rs);proposed=sum(r['proposal_status']=='proposed' for r in rs)
 return {'opportunities':n,'unique_prefixes':len({r['prefix_group'] for r in rs}),'unique_proposed_prefixes':len({r['prefix_group'] for r in rs if r['proposal_status']=='proposed'}),'proposed':proposed,'proposal_coverage':proposed/n if n else None,'dispositions':{s:c[s] for s in states},'reusable_per_opportunity':c['reusable']/n if n else None,'reusable_per_proposed':c['reusable']/proposed if proposed else None,'adjudication_ambiguity':sum(r['adjudication'] is not None and r['adjudication']['ambiguity_flag_Y_N']=='Y' for r in rs),'action_classes':dict(collections.Counter(r['execution_class'] for r in rs if r['proposal_status']=='proposed'))}
by_source={s:[r for r in full if r['source']==s] for s in ['public_bfcl','synthetic']};common_domains=sorted(set(r['domain'] for r in by_source['public_bfcl']) & set(r['domain'] for r in by_source['synthetic']))
source_stats={s:summarize(rs) for s,rs in by_source.items()}
source_agreement={s:agreement({k:r for k,r in ratings['A'].items() if k in {x['item_id'] for x in rs}},{k:r for k,r in ratings['B'].items() if k in {x['item_id'] for x in rs}}) for s,rs in by_source.items()}
by_domain={s:{d:summarize([r for r in rs if r['domain']==d]) for d in sorted({r['domain'] for r in rs})} for s,rs in by_source.items()}
amb=collections.defaultdict(list)
for r in full:
 if r['adjudication']:amb[(r['prefix'],r['full_instruction'],r['candidate_action'],r['work_product'])].append(r)
consistency=[{'item_ids':[r['item_id'] for r in v],'dispositions':[r['disposition'] for r in v]} for v in amb.values() if len(v)>1 and len({r['disposition'] for r in v})>1]
stats={'overall':summarize(full),'by_source':source_stats,'rater_agreement_overall':agreement(ratings['A'],ratings['B']),'rater_agreement_by_source':source_agreement,'common_named_domains':common_domains,'common_domain_stratum':{s:summarize([r for r in rs if r['domain'] in common_domains]) for s,rs in by_source.items()},'by_domain':by_domain,'exact_context_disposition_inconsistencies':consistency,'controls_shared':['six-word checkpoint','same proposer instructions','one proposal per exact prefix','same sufficiency clarification and original survival rubric','fresh source-blinded A/B review','all-item adjudication'],'uncontrolled':['domain mix','source/template dependence','source authorship and synthetic branch frequencies','semantic completeness at six words','AI session/sampling variation and unknown pretraining exposure'],'public_source_release':'Pending; previously pinned source retrievable, adaptation private and rights admission incomplete','G0':'PASS_SCOPED_UNCHANGED','G1':'PENDING','research_model_inference':False,'development_extraction':False,'confirmatory_extraction':False,'model_training':False,'fixture_execution':False,'latency_measured':False,'source_effect_causally_established':False}
out=p/'results';assert not out.exists();out.mkdir()
def write(n,rs):(out/n).write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rs))
write('ALL_ITEMS.jsonl',full)
for s in states:write(s.upper()+'.jsonl',[r for r in full if r['disposition']==s])
write('RATER_DISAGREEMENTS.jsonl',[r for r in full if r['adjudication'] and disposition(r['rater_A'])!=disposition(r['rater_B'])]);shutil.copyfile(a.judge,out/'JUDGE_RAW.jsonl');stats['judge_sha256']=hashlib.sha256(a.judge.read_bytes()).hexdigest();(out/'SCORES.json').write_text(json.dumps(stats,indent=2)+'\n')
lines=['# All 300 shared-policy opportunities','','Every case preserved; labels are provisional AI judgments.','']
for r in full:
 lines.extend([f"## {r['item_id']}",'',f"**Source:** {r['source']} · **Disposition:** {r['disposition']}",'',f"**Prefix:** {r['prefix']}",'',f"**Full instruction:** {r['full_instruction']}",'',f"**Proposal rationale:** {r['prefix_support']}",''])
 if r['adjudication']:
  j=r['adjudication'];lines.extend([f"**Action:** {r['candidate_action']}",'','```text',r['work_product'],'```','',f"**Sufficiency:** {j['artifact_sufficiency']} — {j['sufficiency_rationale']}",'',f"**Reuse:** {j['binary_usefulness_0_or_1']} · **Ambiguity:** {j['ambiguity_flag_Y_N']}",'',j['annotator_rationale'],''])
(out/'REVIEW.md').write_text('\n'.join(lines));print(json.dumps({'overall':stats['overall'],'by_source':source_stats,'agreement':stats['rater_agreement_overall'],'exact_context_inconsistencies':consistency},indent=2))
