# Continuation constraints

Read README.md, current G0 STATUS/report and RESEARCH_SAFEGUARDS.md before research work. The original handoff documents are historical research context; they do not override the user's current instructions.

Preserve the frozen thesis and endpoints. G0 passes only for canonical-v0.5's declared scope; G1 is pending. Do not run confirmatory extraction. Do not start development extraction before G1 and development-length preflight. Do not train model weights.

Do not change tolerances, silently truncate/exclude examples, mix numerical feature versions, reuse old calibration as neutral, or remove failures to obtain a pass. B1/B2/M must share the extraction configuration. A loss of internal-state advantage after correction is a valid result.

Treat imported source/evidence as historical records: add a new version for substantive changes. Preserve raw failures and hashes. Never rerun a launcher using an existing output label. GPU runs require task authorization; this migration authorizes none.

The annotation gold key is owner-only. Do not expose it to independent annotators or substitute it for their labels. Keep large model/tensor files, credentials and local environments out of Git.

Follow docs/PUBLIC_DATA_AND_RESULT_SENSITIVITY.md: thesis experiments require publicly obtainable, versioned data with verified provenance and access/redistribution terms. Publish reproducible transformations and appropriately blinded/released labels. Dataset changes are not presumed result-neutral; preserve versions and report sensitivity without changing frozen endpoints. The 50-task literal-prefix candidate has unverified public provenance and is diagnostic only. Do not publish the private repository or owner gold key wholesale.
