# BFCL public-source pilot and synthetic comparison

The 200-opportunity BFCL pilot is complete as a source-adapter and AI-labeling diagnostic. At a fixed six-word checkpoint, prefix-only proposers created **59 work products and abstained 141 times**. Two independent AI ratings and all-item adjudication yielded **24 reusable, 7 non-reusable and 28 unresolved products**. Nothing was discarded. This is not 200 labeled work products, an executed BFCL benchmark, a human G1 pass, or a model-performance experiment.

## Read the results

- [All 200 opportunities, exact instructions, work products and rationales](results/REVIEW.md)
- [Machine-readable all-item results](results/ALL_ITEMS.jsonl) and [scores](results/SCORES.json)
- [Reusable](results/REUSABLE.jsonl), [non-reusable](results/NON_REUSABLE.jsonl), [unresolved](results/UNRESOLVED.jsonl), [abstentions](results/ABSTENTIONS.jsonl)
- [Domain coverage and conventions](DOMAIN_NOTES.md)
- [Independent adapter audit](ADAPTER_AUDIT.md) and [independent review audit](REVIEW_AUDIT.md)
- [Prospective workflow and qualifications](PLAN.md), [source admission](SOURCE_ADMISSION.json), [source attribution and hashes](SOURCE_MANIFEST.json)

## Public versus synthetic: descriptive comparison

| Measure | BFCL public-source adaptation | Earlier synthetic set |
| --- | ---: | ---: |
| Source/task units | 200 conversations; 199 distinct first instructions | 100 task variants in 50 related families |
| Candidate work products reviewed | 59 | 200 |
| Abstentions | 141 of 200 opportunities | Not measured with a prefix-only proposer |
| Reusable | 24/59 (40.7%) | 136/200 (68.0%) |
| Non-reusable | 7/59 (11.9%) | 59/200 (29.5%) |
| Unresolved | 28/59 (47.5%) | 5/200 (2.5%) |
| Adjudicator ambiguity flags, overlapping above | 39/59 (66.1%) | 19/200 (9.5%) |
| Preparation / speculation / staging artifacts | 58 / 1 / 0 | 40 / 92 / 68 |
| Primary domain coverage | 7 of 12 named domains + Other/Unclear | All 12 |
| Prefix checkpoint | Fixed 6 words | Selected anchors: 3–12 words, median 7.5 |

The 24 reusable artifacts represent 12% of all 200 proposal opportunities, 40.7% of proposed work, or 77.4% of the 31 resolved judgments. These are different denominators; the last figure omits substantial uncertainty. None is frozen-model predictive accuracy or a latency result. Do not collapse abstentions into negative labels.

**This is not a matched source-effect estimate.** The public side uses a new prefix-only AI proposer and very early fixed checkpoints; the synthetic side used hand-authored selected actions and stipulated outputs, with two actions per full task. Artifact type, task mix, prefix policy, source dependence and label uncertainty all differ. The 665-positive wording-variant collection is deliberately not the comparator. No statistical significance, independent sample-size claim, or source quality ranking follows from this table.

## What the review exposed

Twenty-three unresolved products concern the materiality of preparation, such as whether a mostly blank worksheet or repeated entity label constitutes useful saved work; five lack sufficient evidence. Seven invalidated products concern an action mismatch (five) or argument mismatch (two). Ten reusable products preserve work unchanged and fourteen remain useful under narrowing. These are AI tags of artifact survival, not measured natural user revision frequencies. Comparable mechanism tags have not been applied to the earlier synthetic set, so a matched revision-type comparison remains pending.

Both raters produced 32 positive, 7 negative and 20 unresolved labels, but not on exactly the same rows. They agreed on all 37 complete binary pairs (30 positive, 7 negative; κ=1.0). Eighteen pairs were both unresolved and four were positive-versus-unresolved. Thus 22 of 59 pairs fall outside the binary agreement denominator. The adjudicator left those four disagreements unresolved and also made six both-positive pairs unresolved. High agreement on the resolved subset does not establish reliable coverage, independent-human agreement, or a G1 pass.

BFCL first-turn domains cluster around files, vehicles, stocks and travel. The fixed ontology classifies 25 stock-write requests and one unclear account-budget write as Other/Unclear because its finance category explicitly covers read-only analysis. This classification is recorded rather than disguising these tasks as read-only. Five named primary domains are absent; complementary public sources are still needed. The source is publicly obtainable benchmark data, not established naturally collected user input.

## Source, leakage boundary and reproducibility

Source: [BFCL v4 multi-turn base at commit 6ea57973](https://github.com/ShishirPatil/gorilla/blob/6ea57973c7a6097fd7c5915698c54c17c5b1b6c8/berkeley-function-call-leaderboard/bfcl_eval/data/BFCL_v4_multi_turn_base.json). The exact file and repository license were anonymously downloaded again and their hashes match the prior pins. The repository Apache-2.0 notice is preserved in SOURCE_LICENSE.txt; complete dataset redistribution eligibility remains pending, including separately imported-content rights. The private adaptation package is not publicly released or research-eligible.

Only first-turn user text was retained; later dialogue, initial state, reference paths and task-specific tool inventories were excluded from proposer context. All 200 prefixes are literal proper initial substrings ending after six completed words. The 7,415-word-prefix inventory includes later/full text for evaluation bookkeeping, and was not available to proposers. Proposer input schemas contain only an opaque ID and prefix. Full instructions are joined only after the raw proposal hash freeze. Rater A/B inputs were separately shuffled; mappings and raw submissions are retained. Model-family independence is not established; procedural isolation cannot rule out source memorization from pretraining.

Two source records share the same first instruction. Both remain; MINIMUM_SPLIT_GROUPS.jsonl groups exact duplicates, but broader template clustering remains required before any independence-sensitive split. These exposed development records cannot become untouched confirmatory data. Prefix checkpoint choice followed a length audit and is disclosed; this workflow is not preregistration.

[AI generation provenance](AI_PROVENANCE.json) and the [normalized agent task instructions](AGENT_PROMPTS.md) record the workflow and configuration limitations. The proposer and judge sessions are preserved AI-authored outputs, not claimed deterministically reproducible model sampling. Source adaptation rebuilt byte-identically in a fresh directory (REBUILD_CHECK.json); scripts, seeds, inputs, mappings, raw outputs and hash inventories support replay of deterministic transformations and scoring. No live source APIs or research-model forwards were used. Source text contains credential-like benchmark fixtures; their authenticity was not assessed, and none was used to authenticate or perform any task.

Run the offline integrity checks:

```sh
python3 outputs/bfcl_public_pilot_v0_1/verify.py
```

To rebuild, obtain the source and license at the exact URLs in SOURCE_MANIFEST.json and run build.py in a fresh directory with `--source /path/to/source --license /path/to/license`. prepare_review.py consumes preserved proposer submissions; prepare_adjudication.py consumes preserved A/B ratings; finalize.py consumes the preserved judge submission and domain tags. They refuse existing principal outputs. Never rerun into this evidence directory.

Preserved issues include initial path errors, Python certificate-store fetch failures followed by successful normally verified curl retrieval, duplicate source records, and a documented provenance-placeholder metadata correction. Raw labels and frozen inputs were not edited. Read FAILURES.md, PUBLIC_ACCESS_RECHECK.json, PUBLIC_ACCESS_RECHECK_CURL.json and METADATA_CORRECTION.json.

## What remains before thesis testing

First, prospectively clarify what minimum concrete preparation counts as material reusable work, using these disagreements without overwriting this release. Then apply the same checkpoint schedule, prefix-only proposer and artifact policy to new public and synthetic development versions. Preserve abstentions, negatives and unknowns, and report common-domain and source-specific coverage. Add executable frozen tool fixtures where an output-based utility decision is needed; this pilot did not implement the previously proposed executable reuse oracle. Add SGD for missing breadth and audit wider template grouping and source rights.

Independent-human G1 and development-length preflight remain pending. G0 stays scoped to canonical-v0.5. No training, research-model inference, development extraction, confirmatory extraction, or latency/compute-benefit evaluation occurred. The frozen thesis and H2/H3 endpoints are unchanged; data and annotation changes may alter or reverse future results.
