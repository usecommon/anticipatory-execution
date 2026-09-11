# Launcher correction v0.5.1

Attempt 01 stopped in CPU-only identity verification with ModuleNotFoundError for the staged extractor module. No GPU run or numerical test occurred. Added /src to the verifier function import path. Extractor, pipeline, worker, fixtures, thresholds and gate criteria are unchanged. Original launcher and failure log retained. Attempt 02 is separately logged.

## Attempt 03 — allocation logging and bounded replacement repeat

Attempt 02 closure_a passed all 8427 checks; closure_b rejected an unvalidated GPU before model loading. Its exact device was not logged and remains unknown. Preserve both runs. Attempt 03 runs only closure_c in a new single-use container, with the same A100-40GB request and unchanged extractor, worker, fixtures, tolerance and contract. Capture nvidia-smi allocation metadata before the worker, including on rejection. Reuse the upstream-verified checkpoint manifest; the extractor still hashes cached files on every load. No hardware guard relaxation. A repeat rejected by hardware is not a numerical trial. Modal documentation specifies A100-40GB but does not distinguish SXM from PCIe: https://modal.com/docs/guide/gpu .
