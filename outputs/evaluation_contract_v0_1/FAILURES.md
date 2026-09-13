# Preserved software failure and recovery

software_attempt_01: 24 PASS, 1 FAIL. The context-isolation test showed that predictor_payload returned a shared reference to nested environment_metadata. Changing the source decision later also changed the previously captured payload. This was a real software snapshot defect, not an evaluation result or label failure.

The complete check report, traceback and original contract/test/screen source are retained in software_attempt_01. PRE_CHECK_FREEZE.json pins that initial contract and the unchanged prospective specifications. Recovery adds a deep copy at the payload boundary; no test expectation, source screening rule, task requirement, research label, model feature or numerical tolerance is changed. software_attempt_02 records the rerun separately. The original failed attempt remains FAIL_PRESERVED.
