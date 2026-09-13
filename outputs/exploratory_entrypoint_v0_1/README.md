# Exploratory entrypoint validation — v0.1

Status: **PASS_SCOPED — software checks and GPU bitwise regression passed.** This wrapper preserves the byte-identical canonical-v0.5 extractor and original QA pipeline. It permits only the exact frozen 4,013-prefix exploratory file or the separate 12-text G0 instrumentation validation file. Partition names are explicit; research inputs are never labeled QA. Confirmatory, generic development/test, changed input bytes and missing/changed exploratory preflight evidence are rejected.

The numerical contract, thesis, binary usefulness definition and H2/H3 endpoints are unchanged. Human G1 is pending/deferred. Current pilot material remains private AI-labeled diagnostic data; public source/adaptation release admission is pending. No research feature extraction or efficacy comparison is performed in this validation.

## Implementation

The wrapper independently tokenizes every prefix, enforces canonical ID/length validation and matches all exploratory token IDs to the pinned CPU preflight before its first forward. It saves the same last-position hidden states and logits as the original pipeline, retaining full per-prefix order and shared B1/B2/M provenance. This is a storage interface, not a complete implementation of all B1 observable features or M trajectory features. Candidate/action features and final probe design are separate work.

A successful manifest is written only after the complete job. Existing output directories cannot be reused; failure records retain completed-item indices and tensor hashes, while progress is saved after each item. A failure never becomes a successful partial dataset.

## Validation scope

Twenty CPU software checks cover forbidden partitions, wrong numerical contract, edited/reordered/missing/duplicated inputs, extra future-information fields, missing/changed preflight evidence, changed tokenization, a late overlength failure before any forward, validation of all 4,013 inputs before a deliberately failing synthetic forward, preservation after an injected second-forward failure, and successful synthetic roundtrip/overwrite rejection. Software tensors are fabricated test fixtures, not model evidence or labels.

The GPU bridge is limited to the 12 existing natural G0 fixtures, each passed through the old and new pipelines under the exact validated contract: 24 actual forwards. Both hidden-last tensors and complete next-token logits, plus all other saved fields, must match bitwise. The real extractor must also reject the confirmatory partition with zero additional forwards. This is scoped regression evidence, not a fresh full G0 closure or validation of full research extraction.

## Failures and resources

[FAILURES.md](FAILURES.md) preserves attempt 01's remote-import path failure and the launch-only correction. Each attempt has its own timestamped directory and log. Expected negative software cases have preserved failure records inside CPU_RESULT.json; they are successful guard checks, distinct from unexpected run failures.

One CPU validation function (one CPU, 4 GiB, 300-second timeout) precedes a single GPU validation worker (requested A100-40GB, required NVIDIA A100-SXM4-40GB, two CPUs, 48 GiB host memory, 900-second timeout, no retries). Raw regression tensors remain in the named Modal volume; returned text includes their SHA256 inventory. No billing amount is asserted without querying metered usage.

## Next boundary

After validation passes, prepare a separately bounded exploratory run against the complete pinned prefix manifest, with no labels or final instructions in model inputs. Preserve all records and failures. The validated wrapper does not itself launch that run, certify public dataset eligibility, validate probe comparisons or authorize confirmatory work. Human review must be revisited after the first bounded exploratory comparison/sensitivity report and blocks confirmatory labeling/freeze under the retained protocol.

## Completed evidence

All 20 software checks passed. All 12 old/new saved-state comparisons matched bitwise under the unchanged canonical-v0.5 contract, covering 24 actual forwards. The real confirmatory rejection made zero additional forwards. GPU worker elapsed time was 108.27 seconds including checkpoint identity/loading and output persistence work before final inventory/commit; peak allocated CUDA memory was 30,783,937,024 bytes. These are instrumentation measurements, not product latency or billing.

[Returned GPU evidence](validation_20260913T000712852354Z/GPU_RESULT.json) · [CPU checks](validation_20260913T000712852354Z/CPU_RESULT.json). Raw tensors: Modal volume `aeb-exploratory-entrypoint-v0-1`, path `validation_20260913T000712852354Z`. The local verifier checked returned text hashes, source freezes, all 12 comparisons and partition invariants; raw tensor equality was measured in the GPU worker, and tensor files were not independently downloaded.
