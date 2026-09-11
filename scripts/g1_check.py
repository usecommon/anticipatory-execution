"""Read independent G1 sheets without Excel formula caches; never certify independence."""
import argparse, hashlib, json, math
from collections import Counter
from fractions import Fraction
from pathlib import Path

LABEL = 'binary_usefulness_0_or_1'
CONTEXT = ('item_id', 'task_id', 'domain', 'prefix', 'candidate_action_type',
           'candidate_action', 'proposed_arguments', 'execution_class', 'full_instruction')
SECONDARY = ('fractional_utility_0_to_1', 'confidence_1_to_5', 'ambiguity_flag_Y_N', 'annotator_rationale')

def blank(value):
    return value is None or isinstance(value, str) and not value.strip()

def numeric(value):
    return type(value) in (int, float) and math.isfinite(value)

def index_rows(rows):
    result = {}
    for row in rows:
        key = row.get('item_id')
        if not isinstance(key, str) or not key or key in result:
            raise ValueError('Missing or duplicate item_id')
        result[key] = row
    return result

def evaluate(reference, a_rows, b_rows):
    ref, a, b = [index_rows(rows) for rows in (reference, a_rows, b_rows)]
    if len(ref) != 200 or set(a) != set(ref) or set(b) != set(ref):
        raise ValueError('Expected exactly the 200 original item IDs in each sheet')
    missing = {'A': [], 'B': []}; secondary_missing = {'A': [], 'B': []}
    for role, rows in [('A', a), ('B', b)]:
        for key, row in rows.items():
            if any(row.get(f) != ref[key].get(f) for f in CONTEXT):
                raise ValueError('Changed annotation context: ' + role + '/' + key)
            label = row.get(LABEL)
            if blank(label): missing[role].append(key)
            elif not numeric(label) or label not in (0, 1):
                raise ValueError('Invalid explicit binary label: ' + role + '/' + key)
            absent = [f for f in SECONDARY if blank(row.get(f))]
            if absent: secondary_missing[role].append({'item_id': key, 'fields': absent})
            f = row.get(SECONDARY[0]); c = row.get(SECONDARY[1]); flag = row.get(SECONDARY[2]); rationale = row.get(SECONDARY[3])
            if not blank(f) and (not numeric(f) or not 0 <= f <= 1): raise ValueError('Invalid fractional utility')
            if not blank(c) and (not numeric(c) or c != int(c) or not 1 <= c <= 5): raise ValueError('Invalid confidence')
            if not blank(flag) and flag not in ('Y', 'N'): raise ValueError('Invalid ambiguity flag')
            if not blank(rationale) and not isinstance(rationale, str): raise ValueError('Invalid rationale')
    paired = [k for k in ref if not blank(a[k].get(LABEL)) and not blank(b[k].get(LABEL))]
    result = {'G1': 'PENDING', 'expected_items': 200, 'completed_pairs': len(paired),
              'missing_binary_labels': missing, 'missing_secondary_fields': secondary_missing,
              'binary_reliability': 'PENDING', 'kappa': None,
              'independence_verified': False, 'third_party_adjudication_verified': False,
              'development_extraction_authorized': False, 'confirmatory_extraction_authorized': False}
    if len(paired) != 200:
        result['reason'] = 'All 200 independent label pairs are required; blanks are not zeros.'
        return result
    counts = Counter((int(a[k][LABEL]), int(b[k][LABEL])) for k in paired)
    n = len(paired); n_a1 = sum(int(a[k][LABEL]) for k in paired); n_b1 = sum(int(b[k][LABEL]) for k in paired)
    po = Fraction(counts[0,0] + counts[1,1], n)
    pe = Fraction(n_a1 * n_b1 + (n - n_a1) * (n - n_b1), n*n)
    result.update({'contingency': {f'{x}{y}': counts[x,y] for x in (0,1) for y in (0,1)},
                   'observed_agreement': float(po), 'expected_agreement': float(pe),
                   'positive_labels': {'A': n_a1, 'B': n_b1},
                   'disagreement_ids': [k for k in paired if a[k][LABEL] != b[k][LABEL]]})
    if pe == 1 or n_a1 in (0,n) or n_b1 in (0,n):
        result['binary_reliability'] = 'DEGENERATE'
        result['reason'] = 'Degenerate rater prevalence cannot establish label validity; undefined kappa is not one.'
        return result
    kappa = (po-pe)/(1-pe)
    result['kappa'] = float(kappa)
    result['binary_reliability'] = 'MEETS_THRESHOLD' if kappa >= Fraction(7,10) else 'BELOW_THRESHOLD'
    result['reason'] = 'Binary statistic only. Check independence, all required fields, prevalence and third-party adjudication before G1 closure.'
    return result

def read_sheet(path, name):
    from openpyxl import load_workbook
    w = load_workbook(path, read_only=True, data_only=False)
    try:
        sheet = w[name]; it = sheet.iter_rows(values_only=True); header = next(it)
        if len(header) != len(set(header)) or not set(CONTEXT + (LABEL,) + SECONDARY) <= set(header):
            raise ValueError('Invalid annotation headers')
        return [dict(zip(header, row)) for row in it if any(not blank(v) for v in row)]
    finally: w.close()

def main():
    root = Path(__file__).resolve().parents[1]
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--a', type=Path, required=True); p.add_argument('--b', type=Path, required=True)
    p.add_argument('--sheet-a', default='Annotator_A'); p.add_argument('--sheet-b', default='Annotator_B')
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    if args.output.exists(): p.error('Output already exists; use a new versioned result path')
    reference = root/'handoff/aeb_g1_annotation_pilot_200.xlsx'
    try:
        report = evaluate(read_sheet(reference,'Annotator_A'), read_sheet(args.a,args.sheet_a), read_sheet(args.b,args.sheet_b))
    except (ValueError, KeyError) as e:
        report = {'G1':'BLOCKED','error':str(e),'development_extraction_authorized':False,'confirmatory_extraction_authorized':False}
    report['source_sha256'] = {role:hashlib.sha256(path.read_bytes()).hexdigest() for role,path in [('reference',reference),('A',args.a),('B',args.b)]}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2))
    print(json.dumps({k:report.get(k) for k in ('G1','completed_pairs','binary_reliability','kappa','error')},indent=2))
    if report['G1']=='BLOCKED': raise SystemExit(2)

if __name__ == '__main__': main()
