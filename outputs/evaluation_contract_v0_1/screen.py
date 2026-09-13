"""Frozen lexical engineering triage; no candidate generation or usefulness labels."""
import argparse,hashlib,json,re
from pathlib import Path
P=Path(__file__).resolve().parent; R=P.parents[1]
SOURCE='outputs/bfcl_public_pilot_v0_1/EVALUATOR_CONTEXT.jsonl'

def build():
    rows=[json.loads(x) for x in (R/SOURCE).read_text().splitlines()]
    assert len(rows)==200 and len({x['item_id'] for x in rows})==200
    groups={}
    for r in rows:
        normalized=' '.join(r['full_instruction'].split())
        groups.setdefault(normalized,[]).append(r)
    eligible=[]
    for text in groups:
        words=set(re.findall(r'\w+',text.lower()))
        if words & {'list','listing'} and words & {'file','files','directory','directories'}:
            eligible.append(text)
    ranked=sorted(eligible,key=lambda s:hashlib.sha256(('directory-contract-v1|'+s).encode()).hexdigest())
    selected=set(ranked[:8]); out=[]
    for text,rs in groups.items():
        for r in rs:
            out.append({'item_id':r['item_id'],'source_task_id':r['source_id'],
                        'group_sha256':hashlib.sha256(text.encode()).hexdigest(),
                        'lexical_candidate':text in eligible,'selected_for_semantic_review':text in selected,
                        'screen_reason':'lexical_list_and_files' if text in eligible else 'outside_lexical_triage',
                        'execution_admission':'PENDING_ORIGINAL_ENVIRONMENT_AND_SEMANTICS' if text in selected else 'NOT_ASSESSED',
                        'binary_usefulness':None})
    return sorted(out,key=lambda x:x['item_id']),{'screened_records':len(rows),'groups':len(groups),
        'lexical_candidate_groups':len(eligible),'selected_groups':len(selected),
        'selected_records':sum(x['selected_for_semantic_review'] for x in out),
        'executed_records':0,'research_labels_created':0,'source_path':SOURCE,
        'source_sha256':hashlib.sha256((R/SOURCE).read_bytes()).hexdigest(),
        'interpretation':'Engineering triage of exposed first-turn adaptations, not representative efficacy sampling or public task admission'}

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--out',type=Path,required=True);args=a.parse_args()
    args.out.mkdir(parents=True,exist_ok=False)
    rows,summary=build()
    (args.out/'SCREENED.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in rows))
    (args.out/'SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
