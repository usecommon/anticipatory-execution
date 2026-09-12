# BFCL public pilot adapter audit

Audited 2026-09-12. **Source-admission and prefix QA pass within the limited scope below.** No proposer execution, reuse judgment, model extraction, human G1 assessment, or owner-gold access was performed. No adapter code or existing data was modified. This audit read `build.py`, the manifest and preserved license, evaluator context, both proposer inputs and mappings, the all-word inventory, the locally preserved upstream source and license, and only the earlier synthetic expansion's README for comparison.

## Verified checks

| Check | Result |
|---|---|
| Source identity | Local BFCL source SHA-256 is `1a21a995d06fd6f20ba55de7bced30ef953ec35e998f502ec2ecf4d66ef1c43a`, matching the manifest and builder's required hash. |
| Source coverage | All 200 distinct original conversation IDs appear exactly once as 200 distinct evaluator item IDs. No source conversation was dropped or duplicated. |
| Retained text | Every evaluator full instruction equals the sole user message in the original conversation's first turn, character for character. |
| Anchor boundary | All 200 anchors equal the literal source substring ending at the sixth `\S+` word, contain six whitespace-delimited words, and are strictly shorter than their full instructions. First-turn lengths range from 7 to 155 words. |
| Word-prefix inventory | All 7,415 rows independently reconstructed from source match the stored inventory exactly, including order, item ID, word index and literal substring. Each anchor appears at index 6. The inventory intentionally includes each instruction's final word position; only the six-word anchors are required to be incomplete. |
| Proposer input isolation | Each of the two 100-row input files contains exactly `item_id` and `prefix`. IDs are opaque sequential `P1-001`–`P1-100` and `P2-001`–`P2-100`; no source IDs, full instructions, domain tags, task-specific tool catalogs, state, references or future dialogue are fields in these inputs. Source wording naturally visible inside the prefix remains visible. |
| Mapping integrity | Each mapping has 100 distinct blind IDs, exactly `blind_id` and `item_id` fields, and resolves every corresponding prefix correctly. Combined mappings cover all 200 evaluator IDs once, without overlap. |
| Adapter data flow | Code inspection confirms proposer records are constructed only from the assigned opaque ID and six-word prefix. The adapter does not derive per-task tool information from completed instructions. Evaluator context has the expected fixed columns and records future dialogue, initial state and reference-path use as false; source text equality and code inspection support those flags. |
| License preservation | Preserved Apache-2.0 text is byte-identical to the locally retained repository license, with SHA-256 `c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4`, matching the manifest and builder. Source and license URLs pin commit `6ea57973c7a6097fd7c5915698c54c17c5b1b6c8`; the manifest records attribution and the adaptation. |

Independent verification used a separate read-only Python reconstruction against the local original source, not a rerun of `build.py`. Every enumerated structural assertion passed. This establishes consistency with the preserved source and license bytes; it is not an independent online retrieval or a legal determination about downstream release.

## Preserved findings and limitations

**There are 200 conversations but only 199 distinct retained instructions and 199 distinct anchor prefixes.** Original records `multi_turn_base_40` and `multi_turn_base_43` both retain:

> Arrange a complete listing of all files and directories presently located here, making sure you don't overlook the hidden ones too.

Their shared anchor is `Arrange a complete listing of all`. Both records correctly remain in the adapter to preserve exhaustive source coverage. This is an observed dependence issue, not a row-coverage failure. The two records currently have different conversation-based `family_group` values. They must be linked for any later train/development/confirmatory splitting or independence-sensitive analysis; broader template dependence remains unassessed. No claim of 200 independent language tasks is justified.

The six-word rule supplies a literal incomplete text boundary, not proof that every prefix is semantically ambiguous or permits useful anticipatory work. Omitting later dialogue and original execution state changes the task being studied: this is a first-turn public-source adaptation, not a full official BFCL multi-turn evaluation. Missing fixtures can prevent verifying a candidate artifact or its reuse; those cases need explicit handling during subsequent annotation rather than assumed outcomes.

Blinding is established for the contents of the proposer input files. It additionally requires the execution workflow to keep evaluator context, mappings and the all-word inventory out of proposer context: those files are not themselves blind. This audit does not attest to future agent context isolation or public-source memorization resistance.

The 7,415 word positions are an inventory of available checkpoints, not 7,415 rated predictions, completed artifacts, independent tasks or automatic negative examples. This audit supplies no extraction accuracy, calibration, utility, latency savings, human agreement or human G1 evidence.

## Comparison with the earlier synthetic 200

The earlier README describes 200 candidate-review items from 100 full-instruction variants in 50 related synthetic families, with two candidate products per variant and 1,677 word observations. This adapter supplies 200 original public-source conversation records, one six-word anchor per record, and 7,415 word-prefix observations. These counts measure different units. Raw sample size or a later reuse-label percentage cannot establish improvement over the earlier set: source distribution, family dependence, checkpoint selection and candidate construction differ. The earlier labels were provisional AI judgments of fictional stipulated artifacts, not frozen-model predictions or independent-human validation.

No structural failures were encountered or suppressed. The duplicate-instruction finding and all scope limitations above remain recorded; no judging or benchmark-eligibility decision is implied by this admission audit.
