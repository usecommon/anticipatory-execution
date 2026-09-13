# Separate authored directory challenges — v0.1

**The measurement distinguishes reuse, refusal, irrelevant reads and stale-result failures on 14 frozen authored cases.** These are engineering counterexamples, separate from public records and research labels.

All 14 matched their predeclared mechanical expectations. This means **12 correct final tasks, one deliberately exposed incorrect task, and one unresolved task**. It does not mean 14 successful executions or a measured speculation-success rate.

| Challenge | Observed outcome |
|---|---|
| Exact reusable listing | Reused; correct final task |
| Different target, identical names | Receipt refused; fresh task succeeds |
| Hidden-inclusive listing narrowed to visible only | Subset reused correctly |
| Visible-only listing expanded to include hidden entries | Coverage refusal; fresh task succeeds |
| New entry with changed revision | Stale receipt refused |
| Unrelated directory changed | Target listing reused |
| File contents changed, listing dependencies unchanged | Names-only listing reused |
| Useful receipt deliberately ignored | Fresh work performed; offline reuse witness still exists |
| Irrelevant receipt read | Read count positive, contribution zero |
| Corrupted receipt | Integrity refusal |
| Missing revision metadata | Conservative refusal; offline witness can still exist |
| Provider changes names without changing revision | Guard accepts stale data; independent task check fails |
| Replacement directory reuses the same revision | Incarnation mismatch prevents reuse |
| Final environment unavailable | Unresolved, not a negative label |

The missing-metadata case illustrates why no reuse decision is not automatically label 0. The broken-provider case illustrates why a passing gate is not automatically a correct final task. The independent checker retains that failure visibly in [results](attempt_01/RESULTS.jsonl); its detection satisfies the challenge expectation but never changes its final_task_correct=false outcome.

## Scope and evidence

[Plan](PLAN.md) and [cases/expectations](CASES.json) were frozen before execution; [run freeze](RUN_FREEZE.json) pins implementation too. [Summary](attempt_01/SUMMARY.json) separates task outcomes from expected-mechanics checks. [Independent stored-evidence audit](VERIFICATION.json) verifies source hashes, frozen expectations, required entry sets and the distinctions above. No unexpected harness failure occurred; the intended task failure and missing-environment outcome remain preserved.

The guard receives a typed final requirement, receipt and only directory/incarnation/revision metadata. It cannot receive final entry sets through that metadata interface; an extra-field rejection check passed. The independent evaluator can inspect final entries. This is a mocked provider contract, not a new capability of the pinned BFCL tool or deployed freshness validation. The earlier prefix policy and public source records were not rerun or altered. Challenge receipt requests are authored fixtures, not new prefix-model outputs.

Symbolic enumeration and metadata-call counts are retained per case; they omit simulator/oracle overhead and establish neither measured cost nor latency savings. Fixture frequencies cannot estimate natural prevalence, calibrated risk, H2/H3 or S1. Binary usefulness and fractional utility remain null throughout.

The [proposed freshness interface](FRESHNESS_CONTRACT.md) records the remaining dependency, identity, concurrent-change and cost requirements. A truthful revision service is a premise, not a result of these tests. Non-directory preparation and draft materiality remain outside this harness and require rubric alignment.

## Reproduce and next step

```sh
python3 outputs/directory_challenges_v0_1/run.py --out /tmp/aeb-directory-challenges-new
```

Use a fresh output directory; prior attempts are never overwritten. No external calls, shell execution of task text, host-directory enumeration, GPU, model fitting or research judging occur.

Next resolve the actual provider/measurement scope and complete the missing observable-baseline capture and action-feature interfaces before another model comparison. Do not enlarge this small challenge set simply to accumulate pass counts. Human G1 remains pending; source/adaptation admission and full B1 remain incomplete. The frozen thesis, prior negative result, public examples and original labels are unchanged. No confirmatory extraction.
