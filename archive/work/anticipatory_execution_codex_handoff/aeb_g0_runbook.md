# Anticipatory Execution — G0 Instrumentation Runbook

## Gate objective
G0 passes only when deterministic extraction is stable enough that Stage 1 feature differences cannot plausibly be attributed to batching, reload, masking, or extraction bugs.

## Recommended environment
- GPU with enough memory for Qwen2.5-7B-Instruct in BF16 (24 GB+ is comfortable for this QA run).
- Python 3.11+
- Frozen model: `Qwen/Qwen2.5-7B-Instruct`
- Record exact Hugging Face model revision / commit SHA before protocol freeze.

## Run
```bash
pip install -r aeb_g0_requirements.txt
python aeb_g0_qwen_qa_harness.py \
  --model-id Qwen/Qwen2.5-7B-Instruct \
  --dtype bfloat16 \
  --output g0_qwen_qa_report.json
```

## Blocking tests
1. Exact-repeat equivalence.
2. Batch-vs-singleton equivalence.
3. Fixed-shape masked-padding invariance.
4. Model-reload equivalence.

All must pass at the prespecified numerical tolerance. If they do not, do not extract research features.

## Diagnostic only
Sequence-length extension is recorded separately because different tensor shapes can legitimately select different kernels and numerical paths. The prior pilot's length-extension sensitivity should therefore be characterized, not mislabeled as a mathematical suffix-invariance requirement.

## Evidence to persist
- model and tokenizer revisions
- torch / transformers versions
- hardware + precision
- seed and deterministic flags
- full JSON QA report
- checksums for the QA dataset and extraction code

## Exit criteria
`g0_qwen_qa_report.json` reports `status: PASS` with zero blocking failures. Anything else leaves G0 blocked.
