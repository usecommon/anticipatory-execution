"""Hash-checked projection of selected public source; omits all non-filesystem states."""
import argparse,hashlib,json
from pathlib import Path
P=Path(__file__).resolve().parent;R=P.parents[1]

def restore(source,out):
    out.mkdir(parents=True,exist_ok=False)
    manifest=json.loads((P/'SOURCE_MANIFEST.json').read_text())
    raw=source.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=manifest['dataset']['sha256']:raise ValueError('Source hash mismatch')
    source_rows={r['id']:r for r in [json.loads(x) for x in raw.decode().splitlines()]}
    triage=[json.loads(x) for x in (R/'outputs/evaluation_contract_v0_1/SEMANTIC_TRIAGE.jsonl').read_text().splitlines()]
    retained={r['item_id']:r for r in [json.loads(x) for x in (R/'outputs/bfcl_public_pilot_v0_1/EVALUATOR_CONTEXT.jsonl').read_text().splitlines()]}
    projected=[];specs=[]
    target={4:('tmp','explicit_tmp'),40:('alex','initial_cwd'),43:('alex','initial_cwd'),49:('temp','explicit_temp')}
    for t in triage:
        old=retained[t['item_id']];src=source_rows[old['source_id']]
        assert src['question'][0][0]['content']==old['full_instruction']
        fs=src['initial_config']['GorillaFileSystem']
        row={'item_id':t['item_id'],'source_id':src['id'],'instruction_group':t['instruction_group'],
             'source_sha256':manifest['dataset']['sha256'],'filesystem_config':fs,'question':src['question'],
             'involved_classes':src['involved_classes'],'reference_path':src['path'],
             'excluded_functions':src.get('excluded_function',[]),
             'omitted_initial_state_classes':[k for k in src['initial_config'] if k!='GorillaFileSystem'],
             'scope_assessment':t['scope_assessment'],'origin':'public_first_turn_adaptation_with_original_filesystem_context'}
        projected.append(row)
        n=int(src['id'].split('_')[-1])
        if n in target:
            directory,basis=target[n]
            assert t['scope_assessment']=='POTENTIALLY_SUPPORTED_PENDING_CONTEXT'
            specs.append({'item_id':t['item_id'],'schema':'directory-task-1','source_instruction_sha256':hashlib.sha256(old['full_instruction'].encode()).hexdigest(),
                          'target_root_name':directory,'target_basis':basis,'include_hidden':True,'recursive':False,
                          'include_files':True,'include_directories':True,'no_mutation':True,
                          'scope':'first-turn final directory entry set; not exact answer prose or official multi-turn evaluation',
                          'specification_origin':'Coordinator explicit semantic mapping before replay; not an official BFCL answer label'})
    assert len(projected)==9 and len(specs)==4
    for name,rows in [('SOURCE_PROJECTION.jsonl',projected),('TASK_SPECS.jsonl',specs)]:
        (out/name).write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows))
    (out/'RESTORATION.json').write_text(json.dumps({'restored_records':9,'first_turn_specs':4,'unsupported_retained':5,
        'source_sha256':manifest['dataset']['sha256'],'initial_nonfilesystem_states_omitted':True,
        'full_selected_dialogue_preserved_evaluator_only':True,'research_usefulness_labels_created':0},indent=2)+'\n')
    print('Restored nine original filesystem contexts and evaluator dialogues; froze four independent first-turn task specifications.')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    try:restore(a.source,a.out)
    except Exception:
        import traceback
        if a.out.exists():(a.out/'FAILURE.txt').write_text(traceback.format_exc())
        raise
