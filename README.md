# WIP
# Anticipatory Execution

**Do not predict what the user will type next. Predict what work will not need to be undone.**

Research on whether temporal and cross-layer states of a frozen foundation model predict future action non-revision beyond prefix text, observable outputs (B1), and a single hidden-state representation (B2). The thesis, hypotheses and scientific endpoints are frozen. Generic early intent prediction, early tools and speculative execution are not novelty claims.

For ChatGPT or Codex Cloud continuation, use the [detailed handoff and copy-ready startup prompt](docs/CHATGPT_CODEX_CLOUD_HANDOFF.md).

The additional full raw-evidence upload is currently **incomplete**; see [transfer status and recovery instructions](docs/GITHUB_EVIDENCE_RESTORE.md). All source/report material is available in Git, including `archive/work/`.

Use the [corrected G1 annotation workbook](outputs/g1_workbook_fix_v0_2/aeb_g1_annotation_pilot_200_v0_2.xlsx) for labeling; see its [calculation changes and validation](outputs/g1_workbook_fix_v0_2/CHANGELOG.md). The original workbook remains preserved.

The [public dataset audit](outputs/public_dataset_audit_v0_1/AUDIT.md) identifies reusable task sources and potential executable supervision; it does not waive G1 or change the protocol.

The [detailed public-dataset suitability research](outputs/public_dataset_research_v0_2/REPORT.md) recommends a BFCL development adapter with SGD for breadth, records pinned source checks and failures, and explains why new action-reuse validation is still needed.

The owner's [public-data and result-sensitivity requirement](docs/PUBLIC_DATA_AND_RESULT_SENSITIVITY.md) requires exact public source versions, traceable transformations and reproducible evaluation artifacts. Dataset changes may alter or reverse results. The current 50-task pilot candidate has unverified public provenance and remains diagnostic only.

The [200-item AI annotation trial](outputs/g1_ai_trial_v0_1/TRIAL_REPORT.md) is rubric-diagnostic work only. It does not close G1; keep its labels away from independent annotators until their submissions are preserved.

The [three-agent annotation and judgment study](outputs/g1_team_v0_1/TEAM_REPORT.md) preserves 600 AI ratings, original agreement and 26 unresolved judgments. High AI agreement does not close human G1 or establish dataset validity.

The [literal-prefix dataset candidate](outputs/prefix_dataset_candidate_v0_1/README.md) reconstructs 703 word-boundary observations from the 50 exposed pilot tasks. It has no new actions or labels and does not change the research gates.

The [public-plus-synthetic plan and 200-item expansion](outputs/synthetic_expansion_v0_1/README.md) preserves the original owner labels and records fresh AI adjudication: 136 reusable, 59 non-reusable and 5 unresolved. It remains private development material; public release, source adapters and human G1 are pending.

The [1,000-item synthetic curation](outputs/synthetic_curation_1000_v0_1/README.md) retains 665 reusable wording variants, archives 305 non-reusable items and quarantines 30. These derive from 50 substantive templates and have one AI judgment each; the positive-only subset is not a thesis evaluation dataset.

The [BFCL public-source pilot and synthetic comparison](outputs/bfcl_public_pilot_v0_1/README.md) covers 200 six-word proposal opportunities: 59 proposed artifacts, 141 abstentions; AI adjudication yields 24 reusable, 7 non-reusable and 28 unresolved. Differences from synthetic construction are confounded; no matched source-effect or model-efficacy result is claimed.

The [shared-policy public/synthetic pilot](outputs/shared_policy_pilot_v0_1/README.md) now uses the same six-word checkpoint and proposal/rating policy on 200 public and 100 synthetic tasks: 87 proposed products, 58 reusable, 25 non-reusable, 4 unresolved and 213 abstentions. Source/domain differences and dependent variants remain; human G1 and model efficacy testing are still pending.

The [later-checkpoint and human-review package](outputs/checkpoint_human_pilot_v0_1/README.md) adds 12/18-word proposals and prepares two blind 220-case review packages (200 main + 20 boundary diagnostics). The combined pool has 260 work products across 900 scheduled opportunities; no new reuse labels or genuine human submissions exist yet.

The [fresh AI judge of the 220 review cases](outputs/checkpoint_ai_judge_v0_1/README.md) rated the main 200 as 171 reusable, 21 non-reusable and 8 unresolved, with 53 ambiguity flags. The 20 boundary cases were separately judged insufficient work. Six of 65 unchanged six-word cases changed disposition versus prior AI adjudication; human packages remain blank and unchanged.

The [exploratory manifest and Modal tokenizer preflight](outputs/exploratory_preflight_v0_1/README.md) preserves all 900 scheduled opportunities across 300 tasks. All 4,013 distinct prefix inputs fit the validated width (maximum 52/128 tokens). Splits are outcome-independent; only two negative labels land in the exploratory check split. No model extraction ran; versioned entrypoint validation and public dataset admission remain pending.

The [exploratory entrypoint validation](outputs/exploratory_entrypoint_v0_1/README.md) passed 20 software checks and 12 GPU bitwise comparisons against the original G0 pipeline (24 QA forwards). It pins exact inputs, validates the whole job before inference, preserves partial failures and rejects confirmatory requests. The failed initial launcher attempt is retained. No research feature extraction ran.

The [first bounded exploratory extraction](outputs/exploratory_extraction_v0_1/README.md) completed all 4,013 prefixes under the unchanged G0 contract. All 4,013 tensors (4.13 GB on Modal) passed independent CPU checks. The interrupted serial audit, one verification timeout and exact raw-log recovery are preserved; GPU extraction was not repeated. No probes were fitted during that extraction. The [feature-coverage audit](outputs/exploratory_extraction_v0_1/FEATURE_COVERAGE.md) records remaining strong-baseline requirements.

The [first exploratory diagnostic comparison](outputs/exploratory_comparison_v0_1/README.md) found no advantage from the tested internal-state features: current-label check NLL is 0.20553 for text+candidate, 0.24177 with available output signals, and 0.32225 with the tested dynamics. These are not full B1/B2/M or H2/H3 tests. All 16 public check cases are positive; both negatives are synthetic. Five label sensitivities and all failures are preserved. The planned checkpoint to revisit human review has been reached.

The [measurement-first work package](outputs/measurement_quality_v0_1/README.md) is the current priority: 17 software checks passed and 200 case records were structurally audited. No research cases were validated or labels changed. Build executable reuse evidence, complete missing observable measurements and plan prospective source coverage before further comparisons; preserve the first negative result.

The [fresh-eyes evaluation council](outputs/evaluation_council_v0_1/REPORT.md) supports measurement development and recommends defining decision time and the reuse construct before implementing the narrow adapter. Three separate AI reviews found no demonstrated result corruption in inspected material; they identified inference limits, not a passed thesis evaluation or human G1. Recommendations remain prospective.

The [accepted council recommendations](outputs/evaluation_contract_v0_1/README.md) now have a decision-time/reuse contract, bounded adapter/comparison specifications and 25 passing software checks. A mutable-payload failure is preserved. All 200 source records were screened; nine selected records remain unadmitted pending original context and semantic checks. No research labels or old results changed.

The [original-context directory adapter](outputs/public_directory_adapter_v0_1/README.md) restores all nine selected filesystem contexts. Four first-turn final-task replays passed; five unsupported cases remain. None of the four targets contains hidden entries, so flag variants are observationally equivalent. This creates no usefulness labels or thesis result; isolated prefix-only candidate construction is next.

The [prefix-only directory reuse run](outputs/prefix_directory_reuse_v0_1/README.md) produced 12 proposals and 15 abstentions across 27 checkpoints. Eight early listings supported correct final tasks without another listing, across four records/three instruction groups. Four early actions lack a final checker. These are authored-rule, static-oracle execution witnesses, not new usefulness labels or model evidence.

The [separate authored directory challenges](outputs/directory_challenges_v0_1/README.md) matched all 14 mechanical expectations: 12 correct tasks, one exposed stale-result failure, one unresolved environment. The mocked metadata guard distinguishes refusal, consumption and offline reuse witnesses. No public cases or labels changed; actual provider freshness and full B1 remain open.

The [observable-interface package](outputs/observable_interfaces_v0_1/README.md) implements a full-prefix NLL capture proxy, response-code probability accounting and typed action persistence; 15 software checks passed. Real tensor/model bridging, action prompts and semantic completeness remain pending. BFCL is explicitly scoped to offline static snapshots because it lacks revision metadata.

The [canonical surprisal bridge](outputs/capture_bridge_v0_1/README.md) passed all 12 paired cases/24 QA forwards with bitwise legacy-output equality. The [action-prompt preflight](outputs/action_prompt_preflight_v0_1/README.md) passed all 27 prompts (maximum 61 tokens) and fixed distinct single-token response codes. New prompted extraction and full B1 remain pending; no research comparison or confirmatory extraction ran.

## Current state

- **G0 PASS, scoped:** canonical-v0.5, frozen Qwen2.5-7B-Instruct, NVIDIA A100-SXM4-40GB, FP32 eager, physical shape [1,128], active length 1..128, serial prefixes, explicit positions/masks, cache off. Two fresh Modal containers passed 8,427 checks each; 155 cross-container cases matched bitwise.
- **G1 PENDING:** two independent annotators and prescribed agreement/adjudication are still required.
- **AI-only exploratory preparation AUTHORIZED:** see the [temporary gate-timing amendment](docs/AI_ONLY_EXPLORATORY_AMENDMENT_v0_1.md). Human G1 is deferred for this separate track, not passed. Length preflight and the separate versioned entrypoint have passed scoped validation; the preserved executable remains QA-only. The first bounded exploratory extraction and complete stored-output verification have passed; a first diagnostic probe comparison is complete; full strong-baseline testing and public data admission remain pending. Human G1 blocks confirmatory labeling/freeze. **No confirmatory extraction.**
- Corrections are **not presumed numerically neutral**. Historical failures remain failures. Changes may reduce or eliminate the apparent internal-state advantage.

Start with [closure report](outputs/g0_closure_v0_5/G0_CLOSURE_REPORT.md), [research safeguards](outputs/g0_closure_v0_5/RESEARCH_SAFEGUARDS.md), and [runbook](outputs/g0_closure_v0_5/RUNBOOK.md). Machine-readable current status: [CURRENT_STATUS.json](CURRENT_STATUS.json). The [G0 closure status](outputs/g0_closure_v0_5/STATUS.json) is the preserved historical phase record.

## Repository contents

- `handoff/`: byte-preserved original handoff, protocol, literature review, annotation package and originating status. Historical status documents describe their own time, not the current gate.
- `outputs/g0_evidence_v0_1/`: reconstructed sequence-length failure before mitigation.
- `outputs/g0_rca_v0_2/`: projection-level RCA and preserved unsuccessful interventions.
- `outputs/g0_fix_v0_3/`: initial canonical candidate and native failures.
- `outputs/g0_unblocking_analysis_v0_4.md`: scoped gate analysis.
- `outputs/g0_closure_v0_5/`: validated source, frozen plans, safeguards, all closure attempts and adjudication.
- `provenance/`: imported-file hashes and inventory of large external artifacts.

Validated code stays at its original relative layout to avoid modifying the hashed implementation merely for repository organization. No GPU job, annotation, development extraction or confirmatory run is triggered by this migration. No Actions workflow launches paid computation.

## Verify the migration locally

```sh
python3 scripts/verify_import.py
```

This uses only the standard library and verifies every imported file against its migration checksum, parses Python source, and checks the recorded gate state. It does not substitute for G0 or rerun inference.

For a later authorized QA rerun, read the runbook and create a versioned launcher with a unique run label/output path; retained launchers have already-used filenames and must not overwrite evidence. Modal authentication and access to the named private volumes are required. Dependencies are pinned in the preserved Modal image definitions. Model weights are not in Git.

## Evidence and annotation access

Large tensors and duplicate compressed archives remain outside Git with SHA256 inventories; see [artifact storage](provenance/ARTIFACT_STORAGE.md). This is a source/report repository, not a self-contained copy of all raw tensors. Original local evidence is unchanged.

Keep this repository private. The owner-only gold key in `handoff/aeb_g1_pilot_gold_key.jsonl` must remain inaccessible to independent annotators; give annotators only their blind workbooks/rubric, not repository access. The key does not constitute independent annotation. No open-source license or public release is implied by this migration.
