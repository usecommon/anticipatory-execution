"""Software-only lookup fixture instrumentation; NOT a research labeling oracle."""
import math

def prefix_surprisal(token_ids,active_logits):
 """Teacher-forced prefix NLL: logits[i-1] predicts token_ids[i]; no future text."""
 if not isinstance(token_ids,list) or not token_ids or len(active_logits)!=len(token_ids):raise ValueError('Require exactly the active prefix positions')
 width=len(active_logits[0])
 if not width or any(len(row)!=width for row in active_logits):raise ValueError('Invalid logits shape')
 if any(type(t) is not int or not 0<=t<width for t in token_ids):raise ValueError('Invalid token IDs')
 if any(not math.isfinite(v) for row in active_logits for v in row):raise ValueError('Nonfinite logits')
 losses=[]
 for i in range(1,len(token_ids)):
  row=active_logits[i-1];m=max(row);logz=m+math.log(sum(math.exp(v-m) for v in row));losses.append(logz-row[token_ids[i]])
 return {'scored_tokens':len(losses),'sum_nll':sum(losses),'mean_nll':sum(losses)/len(losses) if losses else None,'per_token_nll':losses,'first_token_scored':False}

def lookup_measure(initial,final,early_keys,final_keys,*,operation='lookup',use_cache=True,tamper=None):
 """Explicit in-memory snapshots and typed operations only. Does not parse/execute artifact code."""
 if operation not in ['lookup','count']:raise ValueError('Unsupported operation')
 if len(set(early_keys))!=len(early_keys) or len(set(final_keys))!=len(final_keys):raise ValueError('Fixture keys must be unique')
 if any(k not in initial for k in early_keys) or any(k not in final for k in final_keys):
  return {'status':'UNRESOLVED_FIXTURE','reason':'Missing environment facts','binary_usefulness':None,'research_label_created':False}
 if any(set(record)!={'version','value'} or record['version'] is None for store in [initial,final] for record in store.values()):
  return {'status':'UNRESOLVED_FIXTURE','reason':'Missing version/value evidence','binary_usefulness':None,'research_label_created':False}
 cache={k:dict(initial[k]) for k in early_keys}
 for k,v in (tamper or {}).items():cache[k]['value']=v
 trace=[];fresh=0;actual=[]
 if operation=='count':actual=len(final_keys);expected=len(final_keys);baseline_fresh=0
 else:
  # Independent fresh reference defines final correctness, not reuse by itself.
  expected=[final[k]['value'] for k in final_keys];baseline_fresh=len(final_keys)
  for k in final_keys:
   reusable=use_cache and k in cache and cache[k]['version']==final[k]['version']
   if reusable:
    value=cache[k]['value'];trace.append({'key':k,'origin':'early_cache','value_matches_reference':value==final[k]['value']})
   else:
    value=final[k]['value'];fresh+=1;trace.append({'key':k,'origin':'fresh_lookup','value_matches_reference':True})
   actual.append(value)
 correct=actual==expected
 consumed={r['key'] for r in trace if r['origin']=='early_cache'}
 verified={r['key'] for r in trace if r['origin']=='early_cache' and r['value_matches_reference']}
 return {'status':'MEASURED_SOFTWARE_FIXTURE','scope':'synthetic unit fixture only','final_task_correct':correct,'early_lookup_units':len(cache),'consumed_early_units':len(consumed),'verified_consumed_early_units':len(verified),'verified_consumed_fraction':len(verified)/len(cache) if cache else None,'fresh_lookup_units':fresh,'fresh_reference_lookup_units':baseline_fresh,'avoided_lookup_units_if_task_correct':baseline_fresh-fresh if correct else None,'trace':trace,'actual':actual,'reference':expected,'binary_usefulness':None,'research_label_created':False,'cost_unit':'symbolic lookup count; excludes oracle/validation overhead; not latency or measured compute'}
