# 1,000-item synthetic curation

Created 1,000 new wording variants and obtained one fresh AI judgment per item across three disjoint reviewer assignments. The active collection retains **665 reusable items**. **305 non-reusable items** are excluded and archived; **30 items** are quarantined for uncertainty or inconsistency. All 1,000 candidates and original judgments are preserved.

| Stage | Count |
| --- | ---: |
| Candidate items | 1,000 |
| Raw AI reusable judgments | 680 |
| Raw AI non-reusable judgments | 305 |
| Raw AI unresolved judgments | 15 |
| Active reusable after consistency screening | 665 |
| Excluded non-reusable | 305 |
| Quarantine (15 unresolved + 15 otherwise-positive) | 30 |

## Files

- [Readable retained items](results/ACTIVE_REVIEW.md)
- [Active reusable JSONL](results/ACTIVE_REUSABLE.jsonl)
- [Excluded non-reusable items and rationales](results/EXCLUDED_NON_REUSABLE.jsonl)
- [Quarantined items](results/QUARANTINE.jsonl)
- [All candidates](ALL_CANDIDATES.jsonl), [all judgments](results/ALL_JUDGMENTS.jsonl), [item dispositions](results/DISPOSITION.jsonl)
- [Machine-readable status](results/STATUS.json), [curation policy](CURATION_POLICY.md), [independent audit](INDEPENDENT_AUDIT.md)

## What these counts mean

These are five request-framing paraphrases of each previous 200-item synthetic fixture: 500 task variants, 250 scenario variants, and **50 substantive template groups**. They are not 1,000 independent semantic tasks. The active collection represents 133 parent action items across those 50 templates. Related families must remain together in any future split. The BUILD_QA field `independent_template_groups` counts lineage groups; it does not establish statistical independence.

Reviewers received only their shuffled item fixtures and the rubric, without previous labels or source mappings. Each item has one AI rating, not three; no paired inter-rater agreement is measured. A parent group's five variants must all be rated reusable without ambiguity to enter the active set. This consistency check quarantines 15 otherwise-positive ratings and does not rewrite any raw label. Ambiguity-flagged negative judgments remain in the exclusion archive. Missing conditional state is not converted into a negative label.

The 9,585 word-boundary prefixes cover all 500 task variants, including initial framing words. They are a complete bookkeeping inventory, not a frozen eligible observation schedule or a claim that every prefix has a labeled candidate action. The 1,000 judged rows use their specified anchor prefixes.

## Research status and reproducibility

This is private AI curation for development/examples. A positive-only collection cannot evaluate false speculation or establish the frozen internal-dynamics thesis. Removing negatives changes the distribution and can alter or reverse apparent results. Keep the complete candidate pool available for separately designed evaluation; do not report retention as model accuracy.

Human G1 remains pending. Public release, public-source adapters, executable outcome validation and broader semantic diversity remain pending. No research-model feature extraction, training, or confirmatory extraction was run. The frozen thesis, H2/H3 comparisons, G0 scope, numerical tolerances and prior labels remain unchanged.

Run `python3 verify_prefix_inventory.py` to reconstruct and compare the full word-prefix inventory. [Group consistency details](GROUP_CONSISTENCY.json) preserve mixed labels and ambiguity; reviewer and wording differences are confounded, so these are not controlled paraphrase-sensitivity measurements.

`INPUT_HASHES.json` freezes generation inputs, code and policy. Raw submissions and hashes are retained in `results/`. `HASHES.json` inventories final artifacts. The written policy was saved after reviewer dispatch but before completed submissions were inspected; this is not preregistration. The initial candidate generation is reproducible with `build.py` in a fresh directory preserving its repository-relative source layout. It intentionally refuses overwrites. AI judgments are preserved outputs, not claimed deterministic regeneration.

To reproduce filtering, copy the folder to a new version, preserve the original `results/` elsewhere, and run:

```sh
python3 curate.py --submissions /absolute/path/to/preserved/raw/submissions
```

The script verifies frozen input hashes and refuses an existing results directory. It needs only the Python standard library. No fixture or external action is executed.
