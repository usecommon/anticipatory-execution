# Original-context directory adapter — v0.1

**Four first-turn directory tasks replay successfully with original source filesystem states and independently specified requirements.** All nine fixed selected records remain recorded; five are outside the current flat-directory checker. This is final-task adapter validation, not speculative usefulness prediction, official BFCL scoring, human G1 or thesis evidence.

## What was restored and checked

The cached complete BFCL source exactly matched the pinned dataset SHA-256. The projection restores the original GorillaFileSystem configuration and retains full source dialogue for all nine selected records. Other API classes' initial states are explicitly omitted. No authored environment was substituted. See [restoration](restoration_attempt_01/RESTORATION.json), [projection](restoration_attempt_01/SOURCE_PROJECTION.jsonl) and [attribution](NOTICE.md).

The pinned [upstream filesystem implementation](https://github.com/ShishirPatil/gorilla/blob/6ea57973c7a6097fd7c5915698c54c17c5b1b6c8/berkeley-function-call-leaderboard/bfcl_eval/eval_checker/multi_turn_eval/func_source_code/gorilla_file_system.py#L145) initializes cwd from the first root key; it does not treat the outer JSON root as a Unix directory. Its ls operation lists cwd, with hidden-entry inclusion controlled by `a`. We preserved source bytes and inspected the initialization/listing paths before running them. Other external/mutating methods were not called.

The evaluator's [four task specifications](restoration_attempt_01/TASK_SPECS.jsonl) were frozen before replay. Expected targets/entry sets come directly from those requirements and source JSON, independently of the runtime result. Structural snapshots verify initialization and no mutation, excluding constructor timestamps. Exact answer prose, unrelated API behavior and later dialogue are outside the checker.

| Source task | Initial/target directory | Expected inclusive listing | Final-task result |
|---|---|---|---|
| multi_turn_base_4 | /tmp | report.txt | PASS |
| multi_turn_base_40 | /alex | Documents | PASS |
| multi_turn_base_43 | /alex | Documents, Reports | PASS |
| multi_turn_base_49 | /temp | file1.txt, file2.txt, file3.txt | PASS |

The identical instructions in records 40 and 43 have different source environments and correct listings. They remain in one instruction group but retain separate environment identities. Do not deduplicate their environments or treat them as independent linguistic tasks.

The other five selected cases (1,26,33,47,48) retain restored source context but were not executed: identity verification, navigation, file filtering/search or conditional recursion exceeds this checker. They were not replaced or labeled negative. Source record 33 also has multiple outer root entries; the pinned loader uses the first, so a later extension must preserve that behavior rather than silently reinterpret the JSON.

## Evidence and limits

[Replay results](replay_attempt_01/RESULTS.jsonl) retain outputs, environment/task hashes, receipts, snapshots, checks and all skipped cases. Four replays passed, with six counterchecks per executed record: wrong target, omitted entry, invented entry and mutation detection, plus visible-only filtering and no-mutation checks. No attempt failed in this package. [Verification](VERIFICATION.json) independently checks sources, frozen inputs, replay summaries and expected entry sets.

**All four original target directories lack hidden entries.** The visible-only query produces the same result as the inclusive query in every case. That is observational equivalence, not empirical evidence that the hidden constraint was tested successfully. The output mutations are checker controls, not non-reusable public actions or additional independent research cases. Existing authored hidden-entry tests remain separately labeled software fixtures.

The executed ls(a=True) was chosen by the evaluator from the full instruction. It is not a prefix-generated candidate. There are **zero new usefulness labels, zero model forwards and zero speculative-reuse measurements**. The independent task mapping is authored and needs rubric/source alignment review; a replay pass is not public dataset admission. Full G1, full B1 and confirmatory restrictions remain unchanged. Numerical feature versions and the old negative comparison were untouched.

## Reproduce and continue

Obtain the exact source JSON from the URL in SOURCE_MANIFEST.json and verify its hash. Run with new output directories, never overwrite a prior attempt:

```sh
python3 outputs/public_directory_adapter_v0_1/restore.py --source /path/to/BFCL_v4_multi_turn_base.json --out /tmp/aeb-directory-restore-new
python3 outputs/public_directory_adapter_v0_1/replay.py --out /tmp/aeb-directory-replay-new
```

The replay uses the frozen checked-in restoration, specifications and vendored modules. Restore independently reproduces the selected source projection/specifications. No dependency installation, host-filesystem enumeration, network execution or GPU is needed by replay. Full raw dataset storage is unnecessary in Git.

Next: construct a separate prefix-only candidate/context interface for these fixed source contexts, using the accepted before_execution contract. Freeze what environment metadata is available, then measure early-result reuse separately from final-task correctness. Any authored contrast cases stay separate from original public tasks; do not fabricate natural negatives. Keep all unsupported selections. New context-conditioned model inputs require their own preflight/bridge before feature capture. No confirmatory extraction.
