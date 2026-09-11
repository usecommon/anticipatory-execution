#!/usr/bin/env bash
set -euo pipefail

printf 'Anticipatory Execution — Codex Cloud bootstrap\n'
printf 'Repository: usecommon/anticipatory-execution\n\n'

python3 --version
git rev-parse --show-toplevel
git rev-parse HEAD

# This repository's migration verifier intentionally uses only the Python
# standard library. Running it is safe: it verifies checksums/source parsing
# and recorded gate state; it does not run model inference or GPU jobs.
python3 scripts/verify_import.py

printf '\nBootstrap verification complete.\n'
printf 'Read README.md, AGENTS.md, and docs/CHATGPT_CODEX_CLOUD_HANDOFF.md before substantive work.\n'
printf 'G0 is scoped PASS; G1 is pending; Stage 1 remains blocked.\n'
printf 'No GPU/Modal job is authorized by this setup script.\n'
