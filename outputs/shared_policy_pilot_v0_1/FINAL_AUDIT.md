# Final frozen-result arithmetic audit

Status: PASS. Independent recomputation matches the published scores, mapped ratings, source/domain summaries, and all six disposition files. No data or rating was changed.

## Exposure and scope

This reused auditor session previously adjudicated the older BFCL pilot with both AI ratings visible and audited the shared-policy source adapter. This is an arithmetic/provenance audit, not a fresh blind labeler or an independent human G1 assessment. The current shared-policy folder and files named by its source manifest were inspected; no owner gold or old owner key was accessed. Frozen raw A/B and judge outputs were mapped independently to opportunity IDs. Pipeline scoring modules were read but not imported or executed; separate assertions recomputed the results. No candidate or fixture ran.

## Complete accounting

| Source | Opportunities | Proposed | Reusable | Non-reusable | Unresolved reuse | Abstention | Ambiguity Y |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Public BFCL | 200 | 21 | 15 | 4 | 2 | 179 | 9 |
| Synthetic | 100 | 66 | 43 | 21 | 2 | 34 | 21 |
| Total | 300 | 87 | 58 | 25 | 4 | 213 | 30 |

All 87 adjudicated task rows are labeled substantive; invalid_candidate and uncertain_candidate both contain zero rows. The 58 reusable, 25 non-reusable, 4 unresolved, and 213 abstention rows form a disjoint, exact 300-ID union. The four unresolved labels retain ambiguity Y. All 30 adjudication ambiguity flags are counted, including resolved cases. These are verified recorded judgments, not auditor endorsement of their semantic correctness.

The 300 opportunities retain exactly one raw proposal or abstention per each of 258 prefix groups. The 62 unique proposed artifacts expand unchanged to 87 proposed task rows; the 196 unique-prefix abstentions expand to 213 task abstentions. Every original opportunity field and every raw proposal field matches the final record. All A/B/judge mappings are 87-ID bijections, and every embedded rating equals its mapped raw record. Judge input preserves both frozen rating payloads. All rating schemas, numeric bounds, null rules, and required rationales pass.

Proposal coverage is 21/200 (10.5%) public and 66/100 (66.0%) synthetic. Recorded reusable work per opportunity is 15/200 (7.5%) and 43/100 (43.0%); per proposed task it is 15/21 (71.43%) and 43/66 (65.15%). Overall reusable work per opportunity is 58/300 (19.33%), and per proposed task is 58/87 (66.67%). Abstentions are excluded from labeling denominators but retained in coverage denominators.

## Paired AI agreement

| Scope | Proposed pairs | Complete substantive binary pairs | Binary agreement | Full disposition agreement | Cohen kappa |
| --- | ---: | ---: | ---: | ---: | ---: |
| Overall | 87 | 84 | 81/84 | 82/87 | 0.913580246914 |
| Public BFCL | 21 | 19 | 19/19 | 20/21 | 1.000000000000 |
| Synthetic | 66 | 65 | 62/65 | 62/66 | 0.893150684932 |

All 87 pairs agree on recorded sufficiency. Overall there are three binary-vs-binary disagreements, two binary-vs-null disagreements, and one both-null pair. The three pairs outside the binary denominator are the two binary/null pairs plus the both-null pair. Consequently, full-disposition disagreements total five, whereas binary disagreements total three. The disagreement file contains exactly those five disposition mismatches.

Exact arithmetic details (table keys are A label, B label):

```json
{
  "overall": {
    "table": {
      "(0, 0)": 23,
      "(0, 1)": 1,
      "(1, 0)": 2,
      "(1, 1)": 58
    },
    "expected_agreement": "115/196",
    "kappa_exact": "74/81",
    "both_null": 1,
    "binary_vs_null": 2
  },
  "public_bfcl": {
    "table": {
      "(0, 0)": 4,
      "(1, 1)": 15
    },
    "expected_agreement": "241/361",
    "kappa_exact": "1",
    "both_null": 1,
    "binary_vs_null": 1
  },
  "synthetic": {
    "table": {
      "(0, 0)": 19,
      "(0, 1)": 1,
      "(1, 0)": 2,
      "(1, 1)": 43
    },
    "expected_agreement": "96/169",
    "kappa_exact": "326/365",
    "both_null": 0,
    "binary_vs_null": 1
  }
}
```

Overall kappa is recomputed from the 84 complete pairs using observed agreement 81/84 and empirical marginal expected agreement, with no null-as-negative recoding. Public kappa uses 19 pairs and synthetic kappa uses 65. These are dependent task-row AI diagnostics; neither high kappa nor unanimous sufficiency establishes independent human G1 or artifact correctness.

## Domain and common-stratum checks

Every numeric field in all source and domain summaries was independently recomputed, including counts, distinct prefix counts, proposal and reusable fractions, ambiguity, and declared action-class distributions. Seven domain names are shared: Communication, Device/Home Control, Document Work, Finance-like Read-only Analysis, General Productivity, Information Retrieval, Travel. These are matching domain names, not matched task distributions.

| Source / shared-domain stratum | Opportunities | Proposed | Reusable | Non-reusable | Unresolved | Abstention |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| public_bfcl | 174 | 20 | 15 | 3 | 2 | 154 |
| synthetic | 58 | 32 | 20 | 10 | 2 | 26 |

Outside the shared-name stratum, the public source retains 26 Other/Unclear opportunities (one non-reusable proposal, 25 abstentions). The synthetic source retains 42 opportunities in Coding, Local Search, Media, Scheduling, and Shopping/Research (34 proposals: 23 reusable and 11 non-reusable; eight abstentions). These omitted domains remain in overall accounting.

| Source | Domain | Opportunities | Proposed | Reusable / non-reusable / unresolved / abstention |
| --- | --- | ---: | ---: | --- |
| public_bfcl | Communication | 3 | 0 | 0 / 0 / 0 / 3 |
| public_bfcl | Device/Home Control | 30 | 1 | 1 / 0 / 0 / 29 |
| public_bfcl | Document Work | 25 | 7 | 7 / 0 / 0 / 18 |
| public_bfcl | Finance-like Read-only Analysis | 24 | 3 | 2 / 1 / 0 / 21 |
| public_bfcl | General Productivity | 11 | 3 | 2 / 0 / 1 / 8 |
| public_bfcl | Information Retrieval | 18 | 4 | 3 / 0 / 1 / 14 |
| public_bfcl | Other/Unclear | 26 | 1 | 0 / 1 / 0 / 25 |
| public_bfcl | Travel | 63 | 2 | 0 / 2 / 0 / 61 |
| synthetic | Coding | 8 | 4 | 3 / 1 / 0 / 4 |
| synthetic | Communication | 8 | 3 | 2 / 1 / 0 / 5 |
| synthetic | Device/Home Control | 8 | 4 | 2 / 2 / 0 / 4 |
| synthetic | Document Work | 8 | 2 | 2 / 0 / 0 / 6 |
| synthetic | Finance-like Read-only Analysis | 8 | 8 | 4 / 2 / 2 / 0 |
| synthetic | General Productivity | 8 | 4 | 2 / 2 / 0 / 4 |
| synthetic | Information Retrieval | 10 | 6 | 5 / 1 / 0 / 4 |
| synthetic | Local Search | 8 | 8 | 6 / 2 / 0 / 0 |
| synthetic | Media | 8 | 8 | 5 / 3 / 0 / 0 |
| synthetic | Scheduling | 8 | 4 | 4 / 0 / 0 / 4 |
| synthetic | Shopping/Research | 10 | 10 | 5 / 5 / 0 / 0 |
| synthetic | Travel | 8 | 5 | 3 / 2 / 0 / 3 |

## Exact-context consistency

The recomputed exact-context disposition inconsistency list is `[]`. Its key is the exact tuple of prefix, full instruction, candidate action, and work product. There are 0 repeated groups among adjudicated contexts under this key. Therefore, the empty list does not demonstrate replicated judgment consistency where no repeated judged context exists. The retained exact public duplicate is an abstained opportunity pair and has no adjudication. Identical prefixes with different full instructions are deliberately allowed to have different survival labels.

## Frozen-byte checks

All manifest entries match: 3 source, 10 input, 2 proposal, 7 reviewer-input, 2 raw-rating, and 2 judge-input/mapping entries (26 total). The saved raw judge output SHA-256 equals SCORES.json: `f643817d4d2159e0045c0cf1eeafd255fa74486de1c8ec97218cd715261120ae`. JUDGE_FREEZE.json freezes judge inputs and mapping, not the judge output; the output hash is recorded separately in SCORES.json. All checks were repeated after writing this report.

Manifest equality verifies present byte consistency, not independent timestamping, authenticity, or protection against coordinated changes to data and manifests. No separate frozen result-manifest is asserted. Final result JSONL files were instead checked by complete record equality against independent reconstruction and exact subset partitioning.

The audit found no arithmetic or provenance-join defect. It does not infer causal source differences, latency savings, model efficacy, independent sampling, public redistribution admission, or completed research gates. G1 remains pending.
