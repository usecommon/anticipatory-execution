# Codex Cloud environment setup

Canonical repository: `usecommon/anticipatory-execution`

This document configures Codex Cloud to continue the checked-in local Codex work without changing the scientific gate state.

## Environment

- Repository: `usecommon/anticipatory-execution`
- Base branch: `main`
- Setup command: `bash scripts/codex_cloud_setup.sh`
- Default task behavior: inspect, verify, edit documentation/source, run standard-library migration verification, and prepare reviewed changes.
- Do not infer authorization for GPU jobs, Modal runs, annotation outreach, development extraction, or confirmatory extraction from environment creation.

## Secrets

No secret is required for the default bootstrap.

Only add provider credentials when a separately authorized task requires them. Keep all values in Codex environment secrets, never in Git. Potential future secret names include:

- `MODAL_TOKEN_ID`
- `MODAL_TOKEN_SECRET`
- `HF_TOKEN`
- `RUNPOD_API_KEY`
- `OPENAI_API_KEY`

Do not add a GitHub personal access token merely to make normal Codex pull-request workflow work; use the connected GitHub repository integration unless a specific task explicitly requires a separate GitHub CLI credential.

## Network access

The default repository verification needs no internet access. Keep task-time network access disabled unless a task specifically needs an external provider or dependency download. When enabled, prefer an allowlist limited to the required service.

## First Cloud task

Use this as the first task after creating the environment:

> Continue the Anticipatory Execution project from the checked-in repository state. First read README.md, AGENTS.md, docs/CHATGPT_CODEX_CLOUD_HANDOFF.md, outputs/g0_closure_v0_5/STATUS.json, outputs/g0_closure_v0_5/G0_CLOSURE_REPORT.md, and outputs/g0_closure_v0_5/RESEARCH_SAFEGUARDS.md. Run `python3 scripts/verify_import.py` and report the checkout SHA and verification result. Do not launch GPU/Modal work, do not perform annotation, and do not run development or confirmatory extraction. Confirm the current gate state and identify only the next allowed preparation work.

## Local ↔ Cloud transfer

GitHub is the source of truth.

1. Local Codex commits and pushes work to this repository.
2. Codex Cloud starts from the latest intended Git commit.
3. Cloud work is returned through a branch/pull request or explicit commit.
4. Local work pulls the accepted Git history before continuing.
5. Large raw tensors and external evidence remain outside Git and are tracked by checksummed provenance manifests.

Never use a transient Cloud container as the only copy of research evidence.
