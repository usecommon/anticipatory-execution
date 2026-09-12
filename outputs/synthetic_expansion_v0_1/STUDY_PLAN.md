# Public plus synthetic dataset plan and synthetic review

## Authorized scope and frozen constraints

The current task authorizes a public-plus-synthetic data plan, expansion from the 125 owner-accepted reusable pilot items, and renewed judging/rescoring. This release creates 200 new action-review items. It preserves all 200 old owner binary decisions, including the 125 accepted positives. It does not treat those positives as complete secondary annotations, independent human ratings or evidence that their original fragments form valid cumulative input.

The frozen thesis, H2/H3 endpoints and G0 numerical contract remain unchanged. No model training, development extraction or confirmatory extraction is authorized or performed here. G1 remains pending. AI team review is a diagnostic activity under the previously authorized team labeling workflow.

## Public plus synthetic composition proposal

The full benchmark remains a target of 3,000 tasks across 12 domains, with the protocol's 1,000 development / 500 calibration / 1,000 confirmatory / 500 generalization task allocation. Propose at least 1,500 tasks adapted from admitted public sources and at most 1,500 newly synthetic tasks. A provisional 50:50 allocation in each partition would be 500/500, 250/250, 500/500 and 250/250 public/synthetic respectively. This allocation is a plan, not a frozen implemented split or a power justification.

Prioritize BFCL for executable task state, SGD for broader services/language and ToolSandbox for dependency stress tests. Use inCLINC separately for an existing human ambiguity diagnostic; its intent labels do not count as new action-usefulness labels. Do not inflate the public quota by counting every prefix or augmented variant as an independent original task. Related turns, augmented variants and templates must remain grouped. Source capacity and domain coverage still require admission audits; if the target cannot be met, record the shortfall and make any amendment explicit rather than relabeling synthetic tasks as public adaptations.

Use the 12 protocol domains and target approximately 250 tasks per domain across the whole benchmark. Measure the required late-constraint/revision coverage, rather than infer it from the number of synthetic pairs. Keep source-specific results, source weights, natural versus synthetic revision rates, prevalence and action coverage visible. Do not select quotas to maximize the internal-state effect.

## Current synthetic expansion

There are 50 scenario families inspired by 50 distinct accepted pilot actions, covering all 12 pilot domains. Each has one shared prefix, two authored continuations and two concrete candidate work products, producing 100 full task variants and 200 review items. STYLE_LINEAGE links every item to its accepted style anchor; no old label is transferred. All 125 accepted items were considered as an anchor pool; the selection intentionally covers one anchor per original task and is not a random or representative sample of the 125.

The builder also generates every whitespace-delimited completed-word observation for all 100 full instructions. The 200 reviewed pairs are a deliberately sparse candidate/work-product set at 100 task-level anchor observations, not a complete candidate policy over all word prefixes. Unpopulated prefix positions are not labeled negative or silently treated as policy abstentions. This release is a development stress set, not the complete preregistered dataset.

All names, prices, documents, catalogs and environment states are fictional fixtures. Artifact text is stipulated by the author; no flight search, legal retrieval, code execution, API call, physical-device action or model forward was performed to produce it. Stage actions remain unapplied. Quantitative latency or compute claims cannot be derived from these fixture strings.

Preserve candidate proposals that may be premature or poorly justified; judge that separately from whether their actual work survives. A mistaken prediction about the emerging request can happen to produce reusable work, and permitted work can be wasted. Do not repair such examples after seeing ratings unless producing a separate, fully versioned dataset revision with fresh labels.

## Review and rescore protocol

Freeze input files and author expectations before ratings. Two AI raters receive the same rubric and all 200 work products, with different random orders and opaque IDs. They do not receive old labels, mappings, author expectations or each other's ratings. Their isolation is instruction-based on a shared filesystem, not a technical security guarantee; they are AI sessions of the same inherited model family, not independent human annotators or demonstrated model-family diversity.

Each rater supplies binary 0/1 or explicit unresolved, fractional utility, confidence, ambiguity and an item-specific rationale. Preserve each raw submission and its hash before comparison. Validate every ID and field before computing agreement. Report disagreements and unresolved cases, not just kappa on a convenient subset. No human G1 pass may be inferred from AI agreement.

A separate AI judge reviews all 200 items with the two frozen ratings and original artifact context. The judge may accept, change or mark a decision unresolved. It receives no author expectations or old owner labels. Preserve judge decisions separately; never overwrite the two ratings.

AUTHOR_EXPECTATIONS is a deliberately coarse construction heuristic: expect target-specific work to fail in the revision branch and otherwise expect survival. It is not an independent model prediction or ground truth. Rescoring compares author expectations, A/B decisions and adjudicated decisions. Its match rate is label-review consistency, not predictive accuracy, not H1/H2/H3 and not proof that the thesis is true.

## Interpretation limits and sensitivity

Identical prefixes and actions with different authored futures must stay in one family split. The frozen model sees identical inputs across such matched branches, so it cannot identify which unseen continuation was selected. Differences in outcomes estimate conditional risk under the synthetic branch distribution, not hidden access to future information. The chosen branch frequency is artificial; it is not an estimate of real user revision prevalence.

The contrastive construction makes lexical cues and template structure predictable. Simple wording, action-type and length baselines may be strong. A positive result on this release would not establish generalization to natural instructions. Do not tune away unfavorable cases or revise the primary endpoints to favor a source.

Public-source adapters must generate candidates from prefix-only inputs. Full instruction, final length, reference tool paths and future-derived tool inventories are evaluator-only. IDs containing branch information are bookkeeping and must never become model features. This synthetic release's hand-authored candidates are not a validated deployable prefix-only proposer.

Preflight complete model inputs with the frozen tokenizer once labeling gates permit extraction. No 128-token coverage has been established for this release. Longer context requires outcome-independent numerical-scope revision and G0 revalidation; no silent truncation, exclusions or mixed feature versions.

## Public release status

This dataset is stored in the existing private research repository. It is not yet publicly available and cannot be claimed to satisfy the public-data eligibility requirement. Prepare a separate public release package containing only admitted data, synthetic fixtures, generation provenance, final annotation process and applicable notices after blind review is frozen. Do not publish the private repository, owner-only gold key or identifying rater information wholesale. Public source data must retain their original licenses; a new blanket license cannot override them.

Retain old and new results as separate releases. Changes in task construction, output specificity, labeling, source mix and numerical configuration can change or reverse the results. Current work does not make a numerical-neutrality or scientific-efficacy claim.
