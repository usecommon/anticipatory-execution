# Public datasets for Anticipatory Execution

## Recommendation

**Use Berkeley Function Calling Leaderboard (BFCL) as the first public source for an executable development adapter, and Schema-Guided Dialogue (SGD) as the complementary source for broader language and service variation. Add inCLINC as an incremental-ambiguity diagnostic.** This is a recommendation about construction feasibility, not evidence that any dataset will produce a positive internal-state result.

No inspected release is a verified, drop-in dataset of **partial instruction → independently proposed action → concrete work product → usefulness after the completed instruction**. Public task text, final intent annotations, reference tool calls and task-success evaluators can substantially reduce construction work. They do not automatically supply that action-level target.

The immediate priority is a small, reproducible BFCL adapter that preserves literal word prefixes and tests whether a recorded early result can be reused. Broader sources should follow once this target has a validated interpretation. Do not replace the full benchmark with 200 BFCL conversations, conflate multi-turn dialogue with within-utterance anticipation, or transfer the pilot’s owner labels onto new examples.

The governing scientific question remains whether a frozen foundation model’s temporal and cross-layer internal dynamics improve prediction of action non-revision beyond observable signals and a single hidden-state snapshot. An improvement in ordinary function-calling accuracy would not answer that question. Public data may improve verifiability while simultaneously reducing, eliminating or reversing an apparent internal-state advantage.

## Fit to the experiment

A usable source must support a fixed final instruction, an honest sequence of observed prefixes, an available action space and enough semantics to judge the survival of work. Stronger candidates also offer replayable environments, concrete tool outputs, dependency structure and persistent record identifiers. Public access must include the exact version, not only an accessible paper or a moving dataset card.

This assessment distinguishes four levels of readiness:

1. **Documented:** primary documentation describes relevant data or methods.
2. **File-verified:** a pinned file has been obtained and its structure checked.
3. **Adapter-validated:** the transformed observations and action-usefulness evaluator have been tested against known cases and independent judgments.
4. **Experiment-eligible:** public provenance, labeling, splits, numerical coverage and the project’s research gates are satisfied.

Several sources reach the second level. None reaches the third or fourth for this project. The assessment covers primary repositories, dataset cards and papers available at the time of review; repository manifests record retrieval timestamps. It does not estimate label prevalence or semantic quality from convenience samples.

## Ranked comparison

The ordering below is an analytical judgment about suitability and effort. It is not a numerical benchmark score.

| Priority | Source | Best role | Main obstacle | Current disposition |
|---|---|---|---|---|
| 1 | BFCL, pinned multi-turn base and related executable categories | First reusable-output adapter | Existing evaluator scores trajectories, not each speculative action | Base data and references parsed; new adapter required |
| 2 | SGD / SGD-X | Broader domains, dialogue variation and schema robustness | Recorded service results are not an arbitrary-call simulator | One training shard and schema verified |
| 3 | ToolSandbox | Dependency, insufficient-information and invalid-action stress tests | Interactive user simulation changes the future unless controlled | Source and license inspected; no runtime validation |
| Diagnostic | inCLINC | Human uncertainty at partial utterances | Intent labels, no work products or action utility | Official release and license link verified; raw-file retrieval unresolved |
| Conditional | ComplexFuncBench | Multi-step, constrained tool work; comparison with early-tool prior art | Long inputs, live API dependencies and incomplete local transfer | Public pinned data identified; download not admitted |
| Conditional | TinyAgent dataset | Small action vocabulary and dependency plans | Concrete environment fixtures and action-output labels still needed | Public pinned files identified; download not admitted |
| Stress study | Lost in Conversation | Progressive disclosure and partial-work robustness | Shards are transformed dialogue units; source-specific rights | 627 records parsed despite “600” filename |
| Stress method | EvolvingIntent | Controlled argument revision and goal changes | Released construction pipeline is not a frozen completed dataset | Code and source-ID lists found; generation required |
| Later systems | τ-bench / current τ³-bench | Interactive policy and latency evaluation | Policy-dependent dialogue and changing evaluators | Current documentation assessed; full source-tree fetch failed |
| Secondary | SMCalFlow | Semantic dependencies, reference and revision | Original execution library unavailable; hidden official test set | Documentation and license distinction verified |
| Secondary | MultiWOZ 2.2, Taskmaster-1 | Human language and task constraints | No ready action-survival evaluator | Documentation assessed; MultiWOZ version pinned |
| Lower priority | APIGen / xLAM 60k | Large function-calling source pool | Gated access and synthetic complete-query targets | Card assessed; no terms accepted or data acquired |

The source-specific evidence and qualifications follow. None of the listed priorities changes the preregistered source composition, domain count, split sizes or endpoints.

## BFCL: best first executable source

BFCL’s multi-turn work provides custom API implementations, initial state and reference trajectories. Its authors describe base, missing-parameter, missing-function, long-context and composite conditions. The base category intentionally resolves ambiguity and supplies sufficient information through the request, prior interaction or environment. Its categories therefore should not be treated as interchangeable samples from natural user behavior.[^1]

At revision `6ea57973c7a6097fd7c5915698c54c17c5b1b6c8`, the base input and reference files each contain **200 unique, matching IDs**. Inputs expose `question`, `initial_config`, `path`, `involved_classes` and `excluded_function`. These checks establish structural compatibility; they do not establish that all reference trajectories are semantically correct.[^2]

The inspected checker compares state and accumulated execution results. Earlier outputs can satisfy later response checks. This is useful infrastructure for reuse research, but a passing trajectory does not identify which extra action was useful, unnecessary or wasted. A result-matching test can also miss equivalent alternative work.[^3]

**Proposed adaptation:** freeze a context and simulator state before one target user turn, then reveal that turn at every completed-word boundary. Supply the same legitimate prior context to every comparison model. Generate candidates from the observed prefix and available tools only. Execute eligible read-only actions in isolated state copies, retaining outputs and dependencies. Judge whether the exact retained result serves the completed target request without material re-execution.

For the first adapter, use a prospectively declared simulator/API scope rather than selecting examples whose labels favor the thesis. Preserve every sampled case, including abstentions, missing arguments, tool failures and uncertain usefulness. Class 4 operations remain simulated or unexecuted; real messages, purchases or bookings are unnecessary.

**Result sensitivity:** a source emphasizing well-specified tool arguments may reward ordinary slot completeness. Deterministic APIs may favor exact matching. Restricting to easy read-only operations may produce high reuse but little latency benefit. These are reasons to report coverage and source-stratified results, not reasons to manufacture difficult negatives.

Gorilla’s repository declares Apache 2.0. Retain the applicable license and source notices, and verify any separately imported content before redistribution.[^4]

## SGD: strongest broad complementary source

SGD documents more than 20,000 conversations across 20 domains, created through simulation and crowd work. It supplies service schemas, user state, actions, service calls and recorded results. SGD-X adds five schema paraphrase variants. Both datasets are released under CC BY-SA 4.0.[^5]

At revision `e852981ae34990f4358979625854259302feaa78`, `train/dialogues_001.json` parses as **128 dialogues** with **321 service-call frames and 321 service-result frames**. The training schema also downloads successfully. These are measured shard counts, not a count or quality audit of the complete corpus.[^6]

**Proposed adaptation:** use literal prefixes of an individual user turn with only the dialogue history already available before that turn. Existing slot annotations can help audit argument changes, but must remain evaluator-only when derived from the completed turn. Recorded results can support a narrowly defined replay fixture for supported calls; they cannot justify invented outputs for arbitrary arguments.

SGD provides useful breadth for testing whether findings survive changes in wording, domain and service schema. Its release does not guarantee sufficient within-turn reversals for the preregistered late-revision requirement. Measure that property rather than assuming dialogue-state changes imply instruction revisions.

SGD-X is a particularly useful robustness design: change the schema wording while holding the underlying task semantics fixed. Keep all variants of the same dialogue in the same split. This can reveal dependence on tool-description phrasing, but adding it to the confirmatory analysis requires a prospective specification.

## ToolSandbox: complementary dependency testing

ToolSandbox supports stateful execution, implicit dependencies and milestone-based evaluation across conversational trajectories. The inspected repository provides a built-in user simulator; milestone success is not itself an action-level reuse label.[^7]

Its pinned Apple license expressly permits use, reproduction, modification and redistribution subject to its stated conditions. It is a custom license; do not relabel it MIT or Apache. Revision `c8571d7854316d2e1c5f288e59fe1e34e53f6dd1` was inspected.[^8]

**Recommended role:** stress cases where a seemingly valid action depends on an earlier state change, lacks essential information or leaves an invalid state. Replaying a fixed user sequence can isolate action non-revision; allowing the simulator to respond differently to different policies instead measures an interactive policy effect. Both are useful, but they require separate analyses.

A later adapter must trace the particular artifact being reused and distinguish semantic usefulness from permitted behavior. Harmless extra work can still be waste. State preservation can still coexist with an irrelevant result. These distinctions are central to the thesis.

## inCLINC: reuse the existing ambiguity labels

The official release contains **121 distinct utterances and 538 complete/partial stimuli**, with six to nine judgments per stimulus across 37 intent categories plus out-of-scope. The official license link resolves to CC BY 4.0. The CSV and README links did not yield usable raw files in this assessment.[^9]

The paper’s cleaning procedure removed ambiguous full utterances using classifier agreement and human majority criteria. This limits how well the resulting sample represents naturally unresolved instructions.[^10]

Use this resource to test whether a pipeline respects uncertainty at short prefixes and to compare observable uncertainty signals. Existing human intent judgments need not be recreated for that purpose. They do not determine whether a concrete retrieval, calculation or draft survives, so they cannot replace action-reusability annotation or close G1.

Do not train the frozen foundation model to reproduce the original paper’s classifier experiment. The relevant diagnostic is the relationship between currently justified interpretations, observable signals and later revision—not a renewed claim that early intent classification is novel.

## ComplexFuncBench and SHANKS

ComplexFuncBench describes 1,000 samples covering multi-step calls, constraints, implicit argument reasoning and long inputs. Its documented response-based setup uses a Booking API subscription. The Hugging Face card declares Apache 2.0, but its viewer reports a mixed-type `content` column error.[^11][^12]

The exact dataset revision is `5dc7739343f8c87aee465931ba66db13a0fb5dd4`. The received file ends in an unterminated string after 182 valid JSONL records. Publisher metadata reports 40,195,573 bytes, compared with 5,672,116 received. This confirms an incomplete transfer, **not evidence that the upstream dataset contains only 182 records or is itself malformed**. Preserve the received bytes and do not admit the valid prefix as a silently filtered dataset.

SHANKS uses ComplexFuncBench for early tool calling. It is relevant prior art and a possible comparability source, but its publicly inspected project page did not establish a downloadable, licensed release of the complete derived timing annotations.[^13]

**Recommended role:** later constraint and multi-step robustness, after full download verification, tool-fixture design and context-length QA. It is a poor first match for the current 128-token numerical scope. Longer prompt schemas cannot be removed or abbreviated based on favorable outcomes; any new width requires the appropriate G0 revalidation.

## TinyAgent and naturalistic speculative-interaction data

TinyAgent uses a compact set of 16 assistant functions and publishes a dataset link through its official project. The Hugging Face metadata declares MIT and exposes training and testing files at revision `07aae41269776824bba82519a84301648f726f2d`.[^14][^15]

Its testing-file transfer ends mid-string and fails JSON parsing: 6,117,020 bytes were received, versus 12,806,644 in publisher metadata. No complete record count or locally verified full-file hash was established. The hash in the evidence manifest identifies the received bytes only.

This source is attractive for dependency plans and bounded action vocabulary. The model’s plan must still be separated from actual outputs and usefulness. Use fixture contacts, files and calendars rather than a researcher’s live desktop state. Plan exact match is neither necessary nor sufficient for work survival.

Hooper and colleagues’ current paper, titled *Speculative Interaction Agents*, describes **177 naturalistic utterances** based on TinyAgent, including hesitations, clarifications and corrections. This is a close behavioral match. A public, licensed downloadable release of that specific 177-item set was not established from the inspected sources, so it is a watchlist candidate rather than the basis for immediate work.[^16]

## Lost in Conversation and EvolvingIntent

Lost in Conversation publishes sharded instructions and task evaluators. Its README describes 600 instructions and explicitly cautions against treating the simulations as realistic human interaction or replacements for human annotation.[^17]

The pinned file at `c865793fe34a929d316119b0451d01bd9183bcfd` contains **627 unique records**: 100 code, 107 database, 105 actions, 103 math, 120 data-to-text and 92 summary. Preserve the discrepancy between the artifact and its “600” description. The local license-file request timed out; component-specific source rights also need checking before redistribution.[^18]

**Recommended role:** a controlled disclosure stress study. Shards are not automatically literal prefixes of one original user instruction. Concatenating them or removing intervening assistant turns creates a new input construction, which must be declared. Native final-answer tests cannot determine whether every intermediate computation was reusable.

EvolvingIntent, published in July 2026, constructs argument revisions and function changes while retaining source-task verifiers. Its repository includes generation machinery and fixed source-ID lists; the inspected tree did not contain the completed `final_dataset` artifacts described by its construction instructions.[^19][^20]

This is a strong methodological lead for controlled revision conditions, but using a public generation script does not guarantee a publicly reproducible generated dataset. Freeze and release actual generated transcripts, prompts, model versions, seeds, failed attempts and transformations. The method’s reuse of final-task verifiers without new annotation does **not** establish action-level non-revision supervision. Its presence reinforces the need to keep the novelty claim about incremental internal-state information narrow.

## Other sources and why they are secondary

**SMCalFlow.** Dataflow programs encode references, revisions and composed operations. The current official README specifies CC BY-SA 4.0 for data, while the repository’s software license is MIT; the paper has a different licensing statement. Use the exact release’s dataset terms, not a blanket code-license assumption. The official test set is not public, and the original execution library is not supplied. OpenDF is an explicitly incomplete alternative implementation. These limitations make this a semantic-structure source rather than the fastest reproducible executor.[^21][^22][^23]

**MultiWOZ 2.2.** Useful for realistic constraints and dialogue-state annotations, with version-specific corrections documented in its README. Corrections and missing annotations make the exact version consequential. The source repository is MIT-licensed; it still lacks this experiment’s action-output survival target. Do not treat a turn-level slot change as proof that all earlier work became useless.[^24]

**Taskmaster-1.** Its CC BY 4.0 release contains 13,215 task dialogues, including spoken Wizard-of-Oz and written self-dialogue subsets. API-argument annotations help identify constraints. The two collection methods should be kept distinguishable; neither supplies a ready work-survival oracle.[^25]

**APIGen / xLAM 60k.** Offers synthetic function-calling examples with described execution and semantic verification. The card declares CC BY 4.0 but requires acknowledgment/login for file access, and records a regeneration of 1,896 affected examples. This is not frictionless anonymous availability. It can be a later source pool after access and release terms are documented; no acceptance or download was performed.[^26]

**τ-bench / τ³-bench.** Best reserved for later interactive systems evaluation. The current repository documents task fixes and warns that some pre/post grading-update scores are not comparable. This directly supports treating dataset/evaluator fixes as potentially result-changing. Pin tasks, policies, simulator and grader together. Its interactive future cannot simply be substituted for a fixed final instruction.[^27]

**SovereignPA-Bench.** A recent paper describes evolving-intent and consent scenarios, but its target is broader personal-agent behavior. It was screened at the paper level only; source admission and exact reuse-label compatibility are unverified. It is not necessary for the first adapter.[^28]

## Recommended construction path

### A public development adapter

Create a source-admission record for BFCL’s pinned base release, including source and reference hashes, license, simulator revision and the exact paths used. Preserve the current source-ID exposure log. Select development cases by a fixed rule and keep inspected examples out of any later untouched holdout. The 200 conversations and their augmented variants are not independent sources of thousands of new tasks.

For each selected target turn, retain the preceding context exactly as declared by the adapter. Choose and document how the pre-turn simulator state is obtained. If it uses a reference trajectory to establish context, disclose that as an oracle-context condition and keep that same context across B1/B2/M. It must not expose later-turn information or hidden state directly to the candidate generator.

Build the completed-word prefix schedule from the target turn’s actual text. Validate exact string starts, nesting, final-text equality and Unicode offsets. Do not use semantic fragments, isolated corrections or counterfactual alternatives as cumulative prefixes. Do not concatenate a multi-turn conversation into a single instruction without declaring a distinct adaptation.

Freeze a prefix-only candidate policy. Record tool name, arguments, dependencies, execution class, policy version and abstention. Select the available tool inventory independently of future reference calls; revealing only the eventually correct tools can leak the answer. Keep full instruction, reference path, total final length and evaluator labels outside prefix-time inputs.

Record each concrete work product, simulator state version and relevant dependencies. Define exact-match reuse only for functions where exact equality captures the intended semantics. For retrieval, specify the actual returned records, query limits and snapshot; for drafts, preserve the actual text. A generic label such as “search hotels” remains insufficiently specified.

Validate the reuse interpretation against matched cases: preserved result, changed relevant argument, irrelevant late constraint, invalidated dependency, equivalent alternative output, harmless-but-unused work, failed tool call and abstention. An action can succeed but be useless; it can be partial work that remains useful while the overall task changes. Unresolved is a distinct evidence state, not a convenient negative.

These checks establish whether an adapter measures the intended target. They do not waive two independent human raters and the prescribed G1 agreement/adjudication process. Existing reference calls can reduce annotation burden, but any automatic label rule needs validation and an explicit prospective protocol decision before replacing human supervision.

### Breadth and external validity

Once the adapter works, add SGD tasks under an explicit shared action/work-product specification. Audit the proportion of actual late constraints and revisions. Do not select the source mix based on observed H2/H3 performance. Report unsupported examples and differences in what each simulator can express.

Retain the frozen benchmark’s 3,000-task, domain, source-composition and split requirements unless a documented prospective amendment changes them. A restricted two-source development pilot is not that benchmark. Create task/template groups before prefix expansion, including augmented versions, paraphrases and related source records. Hold all descendants in one split.

Publicness does not guarantee absence from foundation-model training. Record publication dates and exposure uncertainty. Use held-out task/template groups and a second source or model family for the frozen generalization questions, while avoiding claims that an inaccessible training corpus has been conclusively decontaminated.

### Numerical and systems compatibility

Preflight the full intended model input with the frozen tokenizer: instructions, legitimate history, schemas and formatting all count. Word counts are not token counts. No candidate source has been shown here to fit the canonical physical shape `[1,128]`.

If coverage requires a new shape, select it independently of observed efficacy and rerun the required G0 checks before extraction. Preserve previous failures and do not combine feature versions as if numerically neutral. B1, B2 and M must share the validated extraction configuration.

Measure latency benefit separately from predictive quality. A correct cached lookup may save negligible time, while a large reusable retrieval may matter. Public text alone contains no measured typing rate, API latency or concurrency behavior. Any synthetic timing schedule must be labeled as simulated and subjected to sensitivity analysis before product claims.

## How data can change the result

| Data decision | Potential distortion | Required treatment |
|---|---|---|
| Complete, unambiguous tool requests | Ordinary argument completeness may solve most cases | Report ambiguity/revision mix and compare against strong B1 |
| Broad retrieval counted as reusable | Almost all early work may receive positive labels | Preserve concrete result bounds and report useful coverage and waste |
| Exact reference-call matching | Equivalent useful alternatives may become false negatives | Validate semantic equivalence rules before scoring |
| Synthetic revision templates | Models may exploit “actually” or fixed-position cues | Preserve natural and synthetic strata; inspect simple baselines |
| Repeated prefixes or augmented task families across splits | Leakage and overstated effective sample size | Group by source task/template before expansion |
| Short-input filtering | Harder late constraints and dependencies disappear | Report coverage; no favorable exclusions or silent truncation |
| Changing grader or tool snapshot | Labels change without the predictor changing | Version and compare on matched cases where possible |
| Mostly trivial prepare actions | Strong reuse prediction but negligible latency savings | Report action class, work cost and matched-risk systems utility |
| Mixing datasets without source-level reporting | Aggregate advantage reflects source composition | Freeze source weights; report per-source effects and uncertainty |

Keep the frozen primary H2 comparison B1→M and H3 comparison B2→M. Sensitivity analyses supplement those endpoints; they do not replace an unfavorable primary result. When data and numerical implementation both change, report the confounding and avoid attributing the score shift to either one alone.

A null internal-state result remains scientifically valid. Useful anticipatory behavior from observable signals would support a different product conclusion without supporting internal-state novelty.

## Readiness conclusion

**BFCL is the best first source for a reproducible adapter; SGD is the strongest complementary source for broader language and service coverage.** ToolSandbox is valuable for dependencies, while inCLINC supplies an existing human ambiguity diagnostic. ComplexFuncBench, TinyAgent and the revision-focused sources deserve later controlled studies after their specific access, execution and construction limitations are resolved.

The next deliverable should be an admitted public-source manifest and validated action-reuse adapter, not a confirmatory model run. G0 remains scoped, G1 remains pending, and neither development nor confirmatory extraction was performed. No dataset was automatically promoted to experiment-eligible status, and no historical pilot label was transferred.

## Sources

[^1]: Mao et al., Berkeley/Gorilla, [BFCL V3: Multi-Turn & Multi-Step Function Calling](https://gorilla.cs.berkeley.edu/blogs/13_bfcl_v3_multi_turn.html), released September 19, 2024; page notes later V4 composition.
[^2]: Gorilla contributors, [pinned BFCL base data](https://github.com/ShishirPatil/gorilla/blob/6ea57973c7a6097fd7c5915698c54c17c5b1b6c8/berkeley-function-call-leaderboard/bfcl_eval/data/BFCL_v4_multi_turn_base.json) and [reference calls](https://github.com/ShishirPatil/gorilla/blob/6ea57973c7a6097fd7c5915698c54c17c5b1b6c8/berkeley-function-call-leaderboard/bfcl_eval/data/possible_answer/BFCL_v4_multi_turn_base.json). Counts derived from these files; see FILE_AUDIT.json.
[^3]: Gorilla contributors, [pinned multi-turn checker](https://github.com/ShishirPatil/gorilla/blob/6ea57973c7a6097fd7c5915698c54c17c5b1b6c8/berkeley-function-call-leaderboard/bfcl_eval/eval_checker/multi_turn_eval/multi_turn_checker.py), source inspection; not executed.
[^4]: Gorilla contributors, [pinned license](https://github.com/ShishirPatil/gorilla/blob/6ea57973c7a6097fd7c5915698c54c17c5b1b6c8/LICENSE).
[^5]: Google Research, [SGD and SGD-X repository documentation](https://github.com/google-research-datasets/dstc8-schema-guided-dialogue), releases 2019–2021; current README inspected.
[^6]: Google Research, [pinned training shard](https://github.com/google-research-datasets/dstc8-schema-guided-dialogue/blob/e852981ae34990f4358979625854259302feaa78/train/dialogues_001.json) and [schema](https://github.com/google-research-datasets/dstc8-schema-guided-dialogue/blob/e852981ae34990f4358979625854259302feaa78/train/schema.json). Counts derived locally.
[^7]: Apple, [ToolSandbox README](https://github.com/apple-aiml-research/ToolSandbox/blob/c8571d7854316d2e1c5f288e59fe1e34e53f6dd1/README.md), 2024 project.
[^8]: Apple, [ToolSandbox license](https://github.com/apple-aiml-research/ToolSandbox/blob/c8571d7854316d2e1c5f288e59fe1e34e53f6dd1/LICENSE).
[^9]: Hrycyk, Zarcone and Hahn, [inCLINC official dataset record](https://fordatis.fraunhofer.de/handle/fordatis/213?locale=en), September 2021; linked [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
[^10]: Hrycyk, Zarcone and Hahn, [Not So Fast, Classifier](https://aclanthology.org/2021.nlp4convai-1.6.pdf), 2021, data-cleaning section.
[^11]: Zhong et al., [ComplexFuncBench repository](https://github.com/zai-org/ComplexFuncBench), 2025.
[^12]: Z.ai, [ComplexFuncBench dataset card](https://huggingface.co/datasets/zai-org/ComplexFuncBench) and [pinned data](https://huggingface.co/datasets/zai-org/ComplexFuncBench/blob/5dc7739343f8c87aee465931ba66db13a0fb5dd4/ComplexFuncBench.jsonl). Download limitations are recorded separately.
[^13]: Chiang et al., [SHANKS project](https://d223302.github.io/SHANKS/), associated [paper](https://arxiv.org/abs/2510.06917), initially October 2025.
[^14]: Erdogan et al., [TinyAgent official project](https://github.com/SqueezeAILab/TinyAgent), EMNLP 2024 demo.
[^15]: Squeeze AI Lab, [TinyAgent dataset card](https://huggingface.co/datasets/squeeze-ai-lab/TinyAgent-dataset/blob/07aae41269776824bba82519a84301648f726f2d/README.md), [publisher metadata](https://huggingface.co/api/datasets/squeeze-ai-lab/TinyAgent-dataset) and [pinned testing file](https://huggingface.co/datasets/squeeze-ai-lab/TinyAgent-dataset/blob/07aae41269776824bba82519a84301648f726f2d/testing_data.json).
[^16]: Hooper et al., [Speculative Interaction Agents](https://arxiv.org/html/2605.13360v2), May 14, 2026 revision, section 5.4 and Appendix D. Earlier version used a shorter title.
[^17]: Microsoft, [Lost in Conversation README](https://github.com/microsoft/lost_in_conversation), 2025 project; current repository inspected.
[^18]: Microsoft, [pinned sharded instructions file](https://github.com/microsoft/lost_in_conversation/blob/c865793fe34a929d316119b0451d01bd9183bcfd/data/sharded_instructions_600.json). Record and task counts derived locally.
[^19]: Tack, Laban and Neville, [LLMs Get Lost in Evolving User Intent](https://arxiv.org/abs/2607.20734), July 22, 2026; [repository](https://github.com/microsoft/evolving-intent).
[^20]: Microsoft, [intent construction documentation](https://github.com/microsoft/evolving-intent/blob/main/intent_construction/README.md) and [evaluation documentation](https://github.com/microsoft/evolving-intent/blob/main/evaluation/README.md). Repository tree inspected at `993d6be9597ac03854b46362ccd647eb1bfd267a`.
[^21]: Microsoft, [SMCalFlow official dataset page](https://microsoft.github.io/task_oriented_dialogue_as_dataflow_synthesis/) and [pinned README](https://github.com/microsoft/task_oriented_dialogue_as_dataflow_synthesis/blob/bbd16fe69687b1052a7b5937ee7d20b641f2e642/README.md); Semantic Machines et al., [2020 paper](https://aclanthology.org/2020.tacl-1.36.pdf).
[^22]: Microsoft, [SMCalFlow program semantics](https://github.com/microsoft/task_oriented_dialogue_as_dataflow_synthesis/blob/master/README-SEMANTICS.md) and [executor discussion](https://github.com/microsoft/task_oriented_dialogue_as_dataflow_synthesis/issues/62), 2021–2022.
[^23]: Telepathy Labs, [OpenDF README](https://github.com/telepathylabsai/OpenDF), alternative incomplete implementation.
[^24]: MultiWOZ contributors, [pinned MultiWOZ 2.2 README](https://github.com/budzianowski/multiwoz/blob/fe0c8e65cfcd8462bd33c86e35f21addc84ca82b/data/MultiWOZ_2.2/README.md) and [license](https://github.com/budzianowski/multiwoz/blob/fe0c8e65cfcd8462bd33c86e35f21addc84ca82b/LICENSE).
[^25]: Byrne et al., Google, [Taskmaster-1 release documentation](https://github.com/google-research-datasets/Taskmaster/blob/master/TM-1-2019/README.md), 2019.
[^26]: Salesforce, [APIGen / xLAM function-calling dataset card](https://huggingface.co/datasets/Salesforce/xlam-function-calling-60k), 2024 release with subsequent corrections and current access conditions.
[^27]: Sierra Research, [current τ-bench repository](https://github.com/sierra-research/tau2-bench), including τ³-bench and July 2026 grading-update notice.
[^28]: Liu, [SovereignPA-Bench](https://arxiv.org/abs/2607.05363), July 6, 2026; paper-level screening only.
