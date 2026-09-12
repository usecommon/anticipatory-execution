# Shared-policy adapter structural audit

Status: PASS for the frozen input adapter. This is an independent structural and arithmetic check, not blind labeling, a proposal-quality assessment, or human G1 validation.

## Auditor exposure and scope

This reused agent session previously adjudicated the 59 BFCL public proposals using both frozen AI ratings. That exposure is acknowledged and prevents representing this audit as a new blind annotation. The present audit inspected the shared-policy policy, builder, evaluator contexts, prefix mapping, proposer instructions and input files, build QA, input freeze, and the three source files named in SOURCE_HASHES.json. It did not read owner gold or any source outside that allowlist. Source records contain prior candidate fields; the audit checked source structure and selected task fields without using prior products to generate or label any proposal.

The builder was inspected but not executed. Separate read-only Python assertions independently checked the existing outputs. No source, input, policy, or builder was modified; this report is the sole authored output. No fixtures or candidate actions were executed and no external service was contacted.

## Verified arithmetic and correspondence

| Check | Verified result |
| --- | --- |
| Task opportunities | 300 unique evaluator item IDs |
| Public source | All 200 source records retained, matched by source ID with unchanged full instruction and domain |
| Synthetic source | All 100 task IDs retained from 200 original item rows; each task occurs twice in the source |
| Synthetic consistency | Both source rows for every task agree on full instruction, family, domain, and resulting task identity |
| Distinct synthetic full tasks | 100 distinct full instructions across 50 families |
| Distinct public full tasks | 199 distinct full instructions in 200 public records; duplicate retained |
| Checkpoints | All 300 are literal initial substrings ending at the sixth whitespace-delimited word |
| Proper prefixes | All 300 full instructions have more than six words, so every prefix is strictly shorter than its instruction |
| Unique exact prefixes | 258: 199 public and 59 synthetic; no cross-source exact-prefix overlap |
| Group multiplicity | 216 singleton groups and 42 two-opportunity groups; 216 + 42 × 2 = 300 |
| Proposer allocation | Two disjoint shards of 129 records; all 258 prefix IDs covered once |
| Prefix mappings | Every opportunity appears exactly once in its correct group, with matching prefix and evaluator prefix_group |
| Assignment reconstruction | Sorted unique prefixes, the documented shuffle seed, opaque numbering, and alternating shard assignment reproduce the files exactly |
| Instruction grouping hashes | All 300 exact_instruction_group hashes match their full instruction bytes |

The retained public duplicate and correlated synthetic families mean 300 opportunities are not 300 independent tasks. The adapter preserves these correlations rather than silently deduplicating or replacing opportunities.

## Proposer input boundary

Every proposer row has exactly two keys: `item_id` and `prefix`. IDs match the opaque `U` plus three digits format and do not encode source IDs. The prefix value is exactly the independently recomputed six-word substring. No future text, source or domain field, source ID, multiplicity, mapping, old candidate action, execution class, work product, annotation, initial state, or tool/reference inventory is included as an additional field.

Builder inspection confirms explicit construction of those two-key records from prefixes freshly derived from full instructions. Old source prefixes and candidate products are not copied into proposer payloads. The evaluator projection selects task identity, source, family, domain, and full instruction, then adds newly calculated checkpoint and grouping metadata. The generic proposer instructions disclose neither item mappings nor old labels/products and explicitly prohibit access to other files and future text.

This verifies non-transmission through the prepared input files and their instructions. It does not independently attest to live proposer-session prompts, tool access, isolation, or receipt of those files; no session transcript is within this audit's authorized evidence. The one-proposal-per-prefix mapping is structurally ready, but actual proposal reuse and compliance require downstream output checks. Opaque IDs do not prevent recognition of source style from prefix text or prior model exposure to public data.

## Hash verification

All three source hashes in SOURCE_HASHES.json match current file bytes. All ten entries in INPUT_FREEZE.json match current file bytes, including the policy, builder, proposer instructions, original rubric, both proposer shards, evaluator contexts, prefix mappings, source-hash manifest, and build QA. No frozen-file mismatch was found.

INPUT_FREEZE.json contains hashes for its ten listed inputs; it does not hash itself or this later audit. Hash equality establishes agreement with that manifest, not independent timestamping, provenance authentication, or proof against coordinated replacement of files and manifest.

## Interpretation

No structural adapter defect was found in the requested checks. The six-word checkpoint and clarified artifact-sufficiency policy are documented development choices informed by prior diagnostics. This audit makes no independent preregistration, human-validation, efficacy, latency, licensing, distribution-matching, or statistical source-effect claim. Existing research gates remain unchanged.
