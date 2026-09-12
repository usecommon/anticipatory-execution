# Public dataset suitability research

Read [REPORT.md](REPORT.md) for the detailed recommendation, ranked comparison, source-specific caveats and proposed construction path. This is research and source QA only. G1 remains pending; no development or confirmatory extraction ran.

The recommended first adapter uses pinned BFCL data; SGD supplies complementary breadth and inCLINC supplies an ambiguity diagnostic. No source is yet validated for the new action-reusability target.

## Evidence

- `FILE_AUDIT.json`: final structural checks and incomplete-transfer adjudication.
- `SOURCE_FETCH_MANIFEST.json`: fetched URLs, pinned revisions, sizes, hashes and failures. A successful fetch record alone does not certify a complete or valid dataset; consult FILE_AUDIT.
- `COMPLEX_PUBLISHER_FILE_METADATA.json` and `TINY_PUBLISHER_FILE_METADATA.json`: publisher file sizes and LFS hashes confirming incomplete local transfers.
- `FETCH_FAILURES.json`: preserved acquisition and analysis failures, including later-resolved issues.
- `REPRODUCTION_INPUTS.json`: the five complete input files underlying the BFCL, SGD and Lost in Conversation structural results.
- `historical_scripts/`: original audit scripts, including failed analysis versions. These retain the original work-area layout and are historical evidence, not launchers to run in place.

Raw downloads are preserved locally in the task's `work/public_dataset_research_v0_2` directory. They are not bundled in Git. The manifest hashes of incomplete files identify the received bytes, not the full upstream release. No dataset has been published by this research task.

## Reproduce the complete-file checks

Fetch each exact public URL in REPRODUCTION_INPUTS.json into a new directory. Name each file `<sha256>_<URL-basename>` to distinguish the two BFCL files. Then run:

```sh
python3 verify_source_files.py --directory /path/to/downloads
```

The verifier uses the standard library, checks byte counts and SHA256, and parses record counts without importing external dataset code. It does not validate the action-reuse oracle, annotation quality or inference implementation. Preserve any download or verification failure instead of editing source bytes.

All content-inspected example IDs are recorded in FILE_AUDIT.json. Broader file parsing is structural inspection, not representative semantic review. Keep inspected cases in development and establish future split rules prospectively.
