# G0 evidence wrapper v0.1

Frozen thesis: **Do not predict what the user will type next. Predict what work will not need to be undone.**

The user authorized G0 on Modal, historical sensitivity reproduction before resolution, preservation of failures, and no confirmatory extraction. Attached documents supply research context; their broader Stage 1/confirmatory roadmap is not authorization to execute it.

The supplied harness and protocol are unchanged. Additive wrapper first runs 80 sequence-length comparisons: 8 supplied QA texts × 2 contrasts (64→96, 64→128 masked lengths) × 5 original probe layers. This grid was chosen prospectively to characterize sensitivity, not to recreate a failure count. Exact historical reproduction is unavailable because the archive lacks the historical code, raw tensors, versions, GPU, tolerance and shape grid. Reported 24/80 remains historical evidence, not a result generated here.

Then run the original harness as a subprocess and retain its report, logs and exit code, including failure. Supplementary checks cover token alignment, masks, explicit positions, serialization, finite hidden states, causal suffix invariance, incremental KV-cache vs full forward, and fixed-width batch vs singleton. Persist selected-layer full raw tensors, token IDs, masks, positions, checksums and environment information. Comparisons keep the original atol=rtol=1e-5. No mitigation, tolerance adjustment, feature selection or model training is included.

Environment choice: one A10, BF16, Python 3.11, torch 2.5.1, Transformers 4.45.2, accelerate 0.34.2, numpy 1.26.4, huggingface_hub 0.25.2. These are new reproducibility pins, not recovered historical versions. Model/tokenizer main is resolved once to a commit before loading; both loads use that commit. Original default attention implementation and warn-only determinism are retained and logged. No CUBLAS workaround is applied before reproduction.

Gate interpretation: original harness INFO is retained. Wrapper labels length tests DIAGNOSTIC and separately records tolerance exceedances. A harness PASS is insufficient for full G0 if additional controls fail or cross-prefix validity remains unexplained. README and protocol require stronger coverage than the original runbook auto-pass criterion.

Compute limit: one GPU container, zero retries, worker subprocess timeout 1,650 seconds, function timeout 1,800 seconds. No monetary cap was supplied. Actual invoice cost must be obtained from Modal; runtime is logged. No automatic follow-on job is configured. Evidence volume is retained deliberately.

G1 remains a separate pending independent-annotation gate. Gold labels were not read or used as independent annotation. Confirmatory extraction is forbidden and absent from these scripts.
