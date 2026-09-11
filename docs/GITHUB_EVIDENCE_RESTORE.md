# GitHub evidence transfer — incomplete

Code, frozen handoff, reports, source, safeguards and provenance are on main. This additional attempt to upload all large raw artifacts is not complete. Do not treat this as a fully restored research environment.

A private draft release named research-state-2026-09-11 was prepared. original_work_and_handoff.zip uploaded with a matching GitHub SHA256. Larger release uploads failed or stalled, and a one-MiB test exceeded a 60-second limit. The complete local ZIP archives remain in the originating task's outputs/github_complete_release directory; their asset/member hashes are in provenance/GITHUB_RELEASE_ASSETS.json.

Previously remote-only v0.5 pipeline files (232 files including 230 tensors and two manifests) were checked against the original manifests inside a bounded CPU-only Modal recovery job. Their ZIP is preserved as pipeline_verified.zip in Modal volume aeb-g0-github-transfer. Transfer to the desktop did not complete; the partial local ZIP must not be treated as valid. No GPU experiment or confirmatory extraction ran.

## Resume the upload

From the original desktop task, authenticate gh for usecommon, then upload each completed ZIP individually to the existing draft release. Inspect existing asset names, sizes and SHA256 first. Never overwrite a verified asset unnecessarily. Recover the pipeline ZIP from the transfer volume or rerun the CPU-only transport helper with verified input hashes. The manifest supplies its required hash and byte length.

After all assets have matching server-side hashes, update uploaded flags and status in provenance/GITHUB_RELEASE_ASSETS.json, publish the draft release, and commit the verified status. Do not mark the release complete based only on a CLI exit code. Keep transfer failures recorded.

## Cloud use now

Codex Cloud can already inspect and edit the checked-in project. Run python3 scripts/verify_import.py. Raw-tensor analysis still needs the original Modal volumes or a completed GitHub asset upload. Runtime credentials do not transfer from Desktop automatically. G1 is pending and confirmatory extraction remains blocked.

scripts/fetch_research_evidence.py is prepared for authenticated GitHub CLI downloads. It verifies archive and member hashes and restores into ignored .local/research-evidence, preserving original paths without overwriting checked-in evidence. It refuses assets marked upload-pending. Draft assets require suitable GitHub access. After transfer completion, use --asset to select archives or omit it for all. Use --verify-only with an existing archives directory for offline archive verification.

Model weights remain pinned upstream/in the existing Modal checkpoint volume. Credentials, environments, Python caches and partial network downloads are not valid research artifacts for ingestion.
