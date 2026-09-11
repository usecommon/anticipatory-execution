# Raw artifact storage

Imported source and reports are byte-preserved; imported-file hashes are in IMPORTED_FILES.json. EXTERNAL_ARTIFACTS.json inventories large locally present tensors and tar archives excluded from Git by path, byte length and SHA256. Existing bundle manifests may reference these absent files; that is intentional and is not a claim of a complete raw-data clone.

Modal evidence volumes and run roots:

| Version | Volume | Run directory |
|---|---|---|
| v0.1 | aeb-g0-evidence-v0-1 | run_20260911T163140Z |
| v0.2 | aeb-g0-rca-v0-2 | rca_20260911T165054Z |
| v0.3 | aeb-g0-fix-v0-3 | fix_20260911T171625Z |
| v0.5 | aeb-g0-closure-v0-5 | closure_a_20260911T175740Z; closure_b_20260911T180521Z; closure_c_20260911T180932Z |

Pinned checkpoint volume: aeb-qwen-pinned-model-v0-2. Model/tokenizer commit: a09a35458c702b33eeacc393d103063234e8bc28. The original task's sibling evidence directories retain downloaded raw tensors and archives. Check the preserved launcher/report for exact remote paths before retrieval. Use the authenticated Modal CLI's volume get command, download to a scratch location, then verify hashes before analysis. Do not assume compressed local archives also exist remotely.

Additional remote-only pipeline tensors are listed in each completed v0.5 run's final_manifest.json and pipeline_job/manifest.json; they were verified inside the worker but were not downloaded during closure or this migration. This Git repository therefore requires Modal volume access or the original local evidence archive to repeat raw-tensor audits. No new storage service, public artifact upload or deletion was performed.
