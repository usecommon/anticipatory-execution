# Canonical surprisal capture bridge — v0.1

**PASS for all 12 paired instrumentation cases (24 model forwards).** Every legacy saved field matched bitwise between the original guarded entrypoint and the same entrypoint with the new sidecar proxy. Surprisal agreed with an independent vectorized binary64 formula on the baseline full active logits, with maximum per-token absolute error 3.552713678800501e-15. The predeclared formula threshold was 1e-10; no existing G0 tolerance changed.

The scoped canonical configuration remains unchanged: pinned Qwen model, A100-SXM4-40GB, FP32 eager, fixed [1,128], serial/no cache. The confirmatory rejection check passed with zero extra forwards. These are instrumentation cases, not a research feature rerun or H2/H3 test.

Worker elapsed time was 46.85 seconds, with peak CUDA allocation 30,783,937,024 bytes. This is not metered billing or achieved product latency. The raw tensor evidence remains on Modal volume aeb-surprisal-bridge-v0-1 at run_20260913T104749232872Z. JSON/text evidence and hashes are retained in the local run folder; tensor equality was measured in the worker, not independently downloaded/recomputed locally. Returned text hashes were independently checked.

See VERIFICATION.json and run_20260913T104749232872Z/REMOTE_RESULT.json for paired checks, source freeze, full audit, hardware and sidecar evidence. The expected rejected confirmatory request retains its failure record. No unexpected bridge failure occurred. Local logs are byte-preserved.

This validates the sidecar on the declared 12 fixtures, not arbitrary future prompt formats or all of B1. New action prompts still require a versioned allowlisted entrypoint and corresponding checks before research extraction. Semantic argument completeness, comparison controls, human G1 and public dataset admission remain pending. The original 4,013-prefix tensors and negative result are unchanged.
