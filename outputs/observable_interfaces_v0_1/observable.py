"""Observable measurement components, not a complete B1 implementation."""
import math
ACTIONS=('list_current_all','list_current_visible','abstain')

def prefix_nll(token_ids,rows):
    if not token_ids or any(type(i) is not int or i<0 for i in token_ids):raise ValueError('nonempty valid token IDs required')
    if len(rows)!=len(token_ids):raise ValueError('active position count mismatch')
    losses=[];width=None
    for i in range(len(rows)):
        row=rows[i].tolist() if hasattr(rows[i],'tolist') else rows[i]
        if width is None:width=len(row)
        if not width or len(row)!=width or any(not math.isfinite(x) for x in row):raise ValueError('invalid logits')
        if token_ids[i]>=width:raise ValueError('token ID outside vocabulary')
        if i<len(token_ids)-1:
            target=token_ids[i+1]
            if target>=width:raise ValueError('target outside vocabulary')
            maximum=max(row);losses.append(maximum+math.log(math.fsum(math.exp(x-maximum) for x in row))-row[target])
    total=math.fsum(losses)
    return {'scored_tokens':len(losses),'sum_nll':total,'mean_nll':total/len(losses) if losses else None,
            'per_token_nll':losses,'first_token_scored':False,'arithmetic':'CPU Python binary64; fsum reduction'}

def action_probabilities(next_logits,code_token_ids):
    """Probability of declared one-token response codes, plus mass outside support.
    Mapping/prompt/tokenizer semantics require a separately frozen capture contract.
    """
    if set(code_token_ids)!=set(ACTIONS):raise ValueError('exact declared action support required')
    ids=list(code_token_ids.values())
    if any(type(i) is not int or not 0<=i<len(next_logits) for i in ids) or len(set(ids))!=len(ids):raise ValueError('distinct single-token response codes required')
    if any(not math.isfinite(v) for v in next_logits):raise ValueError('nonfinite logit')
    top=max(next_logits);logz=top+math.log(math.fsum(math.exp(v-top) for v in next_logits))
    code_top=max(next_logits[i] for i in ids);code_logz=code_top+math.log(math.fsum(math.exp(next_logits[i]-code_top) for i in ids))
    raw={a:math.exp(next_logits[i]-logz) for a,i in code_token_ids.items()}
    conditional={a:math.exp(next_logits[i]-code_logz) for a,i in code_token_ids.items()}
    mass=min(1.,math.fsum(raw.values()))
    return {'response_code_probabilities':raw,'support_mass':mass,'outside_support_mass':1.-mass,
            'conditional_on_declared_codes':conditional,'event':'next token is the declared code, not action usefulness',
            'calibrated_action_usefulness':False}

def canonical_action(candidate,cwd):
    if type(cwd) is not str or not cwd:raise ValueError('visible cwd string required')
    if candidate is None:return None
    if type(candidate) is not dict or set(candidate)!={'operation','directory','a'}:raise ValueError('typed ls candidate required')
    if candidate['operation']!='ls' or candidate['directory']!=cwd or type(candidate['a']) is not bool:raise ValueError('unsupported current-directory action')
    return ('ls',cwd,candidate['a'])

def persistence(candidates,cwds):
    if not candidates or len(candidates)!=len(cwds):raise ValueError('aligned history required')
    canon=[canonical_action(c,d) for c,d in zip(candidates,cwds)]
    transitions=[None if a is None or b is None else a==b for a,b in zip(canon,canon[1:])]
    return {'canonical_history':canon,'same_action_transitions':transitions,
            'missing_observations':sum(c is None for c in canon),'interpretation':'Missing/abstained candidates are not evidence of stable action identity'}
