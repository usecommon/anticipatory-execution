"""Build literal word-boundary observations from the exposed 50-task pilot.

No model calls, candidate actions, inferred labels or experiment gate changes.
Run from any directory with Python 3 and openpyxl installed.
"""
import argparse,hashlib,json,re,sys
from pathlib import Path
REPO=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(REPO/'scripts'))
from g1_check import read_sheet
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,default=Path(__file__).resolve().parent)
    args=p.parse_args();out=args.output;out.mkdir(parents=True,exist_ok=True)
    names=['PREFIX_INPUTS.jsonl','EVALUATOR_TASKS.jsonl','OBSERVATION_MAPPING.jsonl','STRUCTURE_QA.json','STATUS.json','HASHES.json']
    if any((out/name).exists() for name in names):raise SystemExit('Output exists: choose a new output directory; no overwrite permitted.')
    source=REPO/'outputs/g1_workbook_fix_v0_2/aeb_g1_annotation_pilot_200_v0_2.xlsx'
    before=digest(source);rows=read_sheet(source,'Annotator_A')
    tasks={}
    for r in rows:
        key=r['task_id']
        if key not in tasks:tasks[key]={'task_id':key,'domain':r['domain'],'full_instruction':r['full_instruction'],'historical_item_ids':[]}
        t=tasks[key]
        assert t['full_instruction']==r['full_instruction'] and t['domain']==r['domain']
        t['historical_item_ids'].append(r['item_id'])
    assert len(tasks)==50 and len(rows)==200
    observations=[];mapping=[];checks=[]
    # Every supplied instruction begins with an action verb. No selection depends on outcomes.
    initial_verbs={'Calculate','Check','Compare','Create','Debug','Draft','Find','Lock','Look','Make','Move','Plan','Prioritize','Recommend','Refactor','Remind','Research','Rewrite','Schedule','Set','Start','Summarize','Turn','Write'}
    for key,task in sorted(tasks.items()):
        full=task['full_instruction'];words=list(re.finditer(r'\S+',full));assert words and words[0].group() in initial_verbs
        previous='';local=[]
        for index,word in enumerate(words,1):
            end=word.end();prefix=full[:end];oid=f'pc1-{key}-w{index:03d}'
            assert full.startswith(prefix) and prefix.startswith(previous) and len(prefix)>len(previous)
            assert prefix==full[:end] and (end==len(full) or full[end].isspace())
            observations.append({'observation_id':oid,'prefix':prefix})
            mapping.append({'observation_id':oid,'task_id':key,'observed_word_count':index,'char_end_exclusive':end,'boundary_units':'Unicode code points; whitespace-delimited word units'})
            local.append(prefix);previous=prefix
        assert local[-1]==full
        checks.append({'task_id':key,'word_boundary_observations':len(local),'all_prefixes_literal':True,'strictly_nested':True,'last_observation_equals_full_instruction':True})
    assert len({r['observation_id'] for r in observations})==len(observations)
    assert all(set(r)=={'observation_id','prefix'} for r in observations)
    assert digest(source)==before
    def write_lines(name,data):
        (out/name).write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in data))
    write_lines('PREFIX_INPUTS.jsonl',observations)
    write_lines('EVALUATOR_TASKS.jsonl',[tasks[k] for k in sorted(tasks)])
    write_lines('OBSERVATION_MAPPING.jsonl',mapping)
    qa={'source_tasks':50,'historical_items':200,'observations':len(observations),'distinct_prefix_texts':len({r['prefix'] for r in observations}),
        'literal_prefix_failures':0,'nested_sequence_failures':0,'word_boundary_failures':0,'source_unchanged':True,
        'full_instruction_matches_at_last_boundary':50,'prefix_input_keys':['observation_id','prefix'],
        'model_token_lengths_measured':False,'model_inference':False,'per_task':checks}
    (out/'STRUCTURE_QA.json').write_text(json.dumps(qa,indent=2)+'\n')
    status={'state':'DESIGN_CANDIDATE_ONLY','G0':'PASS_SCOPED_UNCHANGED','G1':'PENDING','source_tasks':50,'observations':len(observations),
        'candidate_actions_generated':0,'new_action_reusability_labels':0,'owner_labels_transferred':0,'historical_source_instruction_bytes_changed':False,
        'public_dataset_requirement_met':False,'full_3000_task_benchmark_completed':False,'split_status':'Exposed pilot material; not a confirmatory or generalization holdout',
        'source_sha256':before,'prefix_policy':'All whitespace-delimited completed-word boundaries, starting immediately after the initial action verb. Preserve exact text and punctuation; include final full-text boundary.',
        'future_information_policy':'Only prefix text is admissible to the candidate proposer/model. IDs are bookkeeping. Full instruction and historical item IDs are evaluator-only. No suffix, total length, final-word marker or domain is passed in PREFIX_INPUTS.',
        'limitations':['Word units are not model tokens or recorded typing events.','Final instructions were already exposed during pilot review.','50 task families do not replace the preregistered 3000-task benchmark.','No candidate action, concrete output, reusability label or model feature exists for these new observations.','Actual model input token coverage is unknown.'],
        'pending':['Prefix-only candidate policy and action-output contract','Concrete work products and versioned labels for changed examples','G1 process completion','Task/template grouping and prospective splits','Full model-input tokenizer preflight','Any necessary G0 scope revalidation'],
        'development_extraction':False,'confirmatory_extraction':False}
    (out/'STATUS.json').write_text(json.dumps(status,indent=2)+'\n')
    hashes={name:digest(out/name) for name in names if name!='HASHES.json'}
    hashes['build.py']=digest(Path(__file__))
    (out/'HASHES.json').write_text(json.dumps(hashes,indent=2)+'\n')
    print(json.dumps({k:qa[k] for k in ('source_tasks','observations','distinct_prefix_texts','literal_prefix_failures','nested_sequence_failures','source_unchanged')},indent=2))
if __name__=='__main__':main()
