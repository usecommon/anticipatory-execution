# Anticipatory Execution — G0/G1 Execution Status

## G1 Label Validity Pilot — PACKAGE READY / ANNOTATION PENDING
- 50 task utterances
- 200 prefix-action judgment items
- 12 domains
- 148 owner-key useful labels / 52 non-useful labels
- Two blind annotator worksheets
- Separate owner-only gold key
- Automatic adjudication sheet with Cohen's kappa and PASS threshold at kappa >= 0.70
- Annotation rubric rendered and visually QA'd

G1 is **not yet passed** because the protocol requires two independent annotators and third-party adjudication of disagreements. The package is ready for that step.

## G0 Instrumentation — HARNESS READY / EXECUTION BLOCKED IN CURRENT ENVIRONMENT
Current environment:
- CPU-only PyTorch
- no NVIDIA GPU
- no installed Transformers package/model weights

Created a deterministic extraction QA harness for Qwen2.5-7B-Instruct covering:
1. exact repeat equivalence
2. batch-vs-singleton equivalence
3. fixed-shape masked-padding invariance
4. model reload equivalence
5. sequence-length extension diagnostic (informational, not incorrectly treated as a mathematical invariant)

G0 remains blocked until the harness is run in a model-capable environment and produces zero blocking failures.

## Next protocol gate sequence
1. Obtain two independent G1 annotations; adjudicate disagreements; require kappa >= 0.70.
2. Run G0 harness on Modal/RunPod/HF or equivalent GPU environment.
3. If both pass, begin Stage 1 descriptive pilot and B0/B1/B2/M extraction.
