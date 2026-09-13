# Measurement quality — v0.1

The user prioritized measurement quality after the first negative exploratory diagnostic. The [work plan](PLAN.md) preserves the frozen thesis, endpoints, labels, check partition and prior results. Measurement improvements may change future results in either direction.

- **17 software checks passed:** a small in-memory reuse harness separates task correctness, actual consumption, freshness and required new work. An analytic token-surprisal check verifies causal alignment. These are software fixtures, not research-case validation.
- **200 records audited:** none currently contains all proposed structured environment/receipt/trace fields. This is a structural readiness gap, not a usefulness judgment. Existing textual artifacts and labels are unchanged.
- **Full B1 remains incomplete:** actual full-prefix surprisal capture/bridge, action probabilities, semantic argument completeness and action persistence remain pending.
- **Coverage remains limited:** the existing public check slice has 16 positives and no negatives; the synthetic slice has 14 positives and two negatives. Preserve the split and report this limitation.

Next: implement one typed public-source development adapter with pinned environment, execution receipts, consumption traces and an independent task check. Select the small development set before new scoring. Prepare versioned surprisal capture and numerical bridge separately. See [PLAN.md](PLAN.md) for prospective sampling requirements and acceptance evidence.

Human G1 remains pending/deferred for exploratory work, with review revisited after a concrete adapter exists. It still gates confirmatory labeling/final freeze. No confirmatory extraction is authorized. This package ran no GPU extraction or probe fitting and created no research labels.

Reproduce locally with standard-library Python:

```sh
python3 outputs/measurement_quality_v0_1/test_measure.py
python3 outputs/measurement_quality_v0_1/audit.py
```

Evidence: [software QA](SOFTWARE_QA.json), [readiness audit](READINESS.json), [per-case inventory](CASE_READINESS.jsonl), [status](STATUS.json). Symbolic lookup counts are not measured compute or latency; consumed fraction is not the rubric's fractional utility or a binary-label rule. The audit examines these case records only, not every possible external evidence source.
