# Fresh AI judge evaluation of the 220 review cases

The judge evaluated every case in the frozen human-review selection. **Main 200: 171 reusable, 21 non-reusable, 8 unresolved.** All 200 were judged substantive. The 20 deliberately minimal boundary artifacts were judged no_material_work; they have no binary reuse label and are not counted as 20 additional negatives.

## Main results

| Source | Selected cases | Reusable | Non-reusable | Unresolved | Ambiguity flags |
| --- | ---: | ---: | ---: | ---: | ---: |
| BFCL public-source | 100 | 87 | 5 | 8 | 25 |
| Synthetic | 100 | 84 | 16 | 0 | 28 |
| Total | 200 | 171 | 21 | 8 | 53 |

The reusable shares are 87% and 84% of selected proposed artifacts. These are single-judge semantic assessments, not frozen-model accuracy, population reuse rates, measured time saved or evidence for H2/H3. Fifty-three main cases retain ambiguity flags, including 45 resolved cases; eight unresolved judgments do not mean only eight cases need attention. Single-judge labels are not ground truth.

Boundary diagnostics: 20/20 classified as no material work, with null binary/fraction fields and no ambiguity flags. This is consistency with the intended design of four elementary control types, not independent validation of the full preparation boundary or a human G1 pass. Their outcomes stay separate from the main 200.

## By checkpoint within the selected sample

| Source | Words | Selected | Reusable | Non-reusable | Unresolved |
| --- | ---: | ---: | ---: | ---: | ---: |
| BFCL | 6 | 16 | 11 | 2 | 3 |
| BFCL | 12 | 25 | 22 | 0 | 3 |
| BFCL | 18 | 59 | 54 | 3 | 2 |
| Synthetic | 6 | 49 | 33 | 16 | 0 |
| Synthetic | 12 | 30 | 30 | 0 | 0 |
| Synthetic | 18 | 21 | 21 | 0 | 0 |

All 51 selected later-checkpoint synthetic artifacts received reusable labels, but twelve retain ambiguity flags. Selection is from proposed work, checkpoint eligibility depends on whether the instruction has finished, source/task distributions differ, and variants are dependent. These rows are not a paired length-effect experiment or evidence that later work universally survives. The earlier proposal-coverage record retains all 900 scheduled opportunities; the 60 unselected pool products are not evaluated in this release.

## Judgment instability on unchanged artifacts

After the new raw judgments were frozen, we compared the 65 selected six-word products against their prior shared-policy AI adjudication. Prefix, action, product, execution class and completed instruction match exactly. **Six dispositions changed**:

| Work product | Previous | New |
| --- | --- | --- |
| Flight-comparison procedure, changed destination | Non-reusable | Reusable |
| Vegetarian shopping-list candidate narrowed to bean tacos | Reusable | Non-reusable |
| Apollo test-result discovery query | Reusable | Unresolved |
| Bag-comparison normalization, changed bag type | Non-reusable | Reusable |
| Kitchen-only staging logic, changed room | Non-reusable | Reusable |
| Technology-investment query narrowed to AAPL | Non-reusable | Unresolved |

Several differences concern whether substituting a target constant in unexecuted parameterized logic constitutes material re-execution. The new judge accepted three such adaptations; the earlier adjudication did not. It also rejected a broad shopping list as needing material replacement and left two public-query cases uncertain. Both interpretations and their rationales are preserved in PRIOR_COMPARISON.jsonl. This is a reviewer/context sensitivity finding, not proof the newer label is correct. The prior process used two ratings plus adjudication; this run used one fresh judge without supplied ratings. No old decision was changed.

## Review and reproduce

- [All exact artifacts, instructions and judge rationales](results/REVIEW.md)
- [Main 200](results/MAIN_200.jsonl), [boundary 20](results/BOUNDARY_20.jsonl), [source/checkpoint scores](results/SCORES.json)
- [Main reusable](results/MAIN_REUSABLE.jsonl), [non-reusable](results/MAIN_NON_REUSABLE.jsonl), [unresolved](results/MAIN_UNRESOLVED_REUSE.jsonl)
- [All attention cases](results/REVIEW_ATTENTION.jsonl) and [prior/new judgments](results/PRIOR_COMPARISON.jsonl)
- [Input audit](INPUT_AUDIT.md), [final arithmetic audit](FINAL_AUDIT.md), [replay check](REPLAY_QA.json)

The judge saw only a new opaque shuffle of the same 220 artifact contexts, original rubric and unchanged sufficiency clarification. Source, control identity, expected labels and prior ratings were withheld. The raw submission and input hashes were preserved before joining metadata or reading prior judgments. Isolation was instruction-based on a shared filesystem; source wording or pretraining exposure may still reveal information. See AI_PROVENANCE.json. One rating per item means no new paired inter-rater kappa.

The 200 main cases comprise 100/source from 169 tasks with dependent templates/checkpoints. The selection was frozen before these labels. Public availability/redistribution admission and a separate public release remain pending. Do not use the selected-label proportions as source-effect estimates or silently drop unfavorable cases.

All human-package files and ZIP hashes still match their original freezes. New judgments live only in this separate folder; do not share this folder, earlier AI labels or repository access with independent human annotators. The prior human-package snapshot's zero-label status describes its pre-judging state and remains unchanged. Genuine human submissions remain zero, and human G1 remains PENDING.

The scorer reproduced 12 result files byte-for-byte from the saved submission in a fresh temporary layout. This replays saved judgments; it does not reproduce stochastic model sampling. Run:

```sh
python3 outputs/checkpoint_ai_judge_v0_1/verify.py
```

No artifact was executed, repaired or removed. No research-model extraction, development/confirmatory run, training, latency measurement or thesis change occurred. The internal-state hypothesis has not been tested by this AI-labeling exercise.
