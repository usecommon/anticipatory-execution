# Action response prompt/tokenizer preflight — v0.1

**PASS: all 27 frozen directory-context prompts fit the canonical width; maximum length is 61/128 tokens.** No text was truncated. Tokenizer file hashes and backend identity match the pinned G0 tokenizer.

Appending each exact response string leaves the prompt IDs unchanged and adds one distinct token in every context:

| Declared event | Response string | Token ID |
|---|---|---:|
| list current directory, hidden included | leading space + A | 362 |
| list current directory, hidden excluded | leading space + B | 425 |
| wait/abstain | leading space + C | 356 |

This fixes an operational next-token event for the probability interface. It does not establish calibrated action usefulness, semantic completeness, general task coverage or model efficacy. Future measurements must retain raw support mass alongside code-conditional probabilities.

The CPU-only Modal preflight loaded tokenizer files, not model weights. Worker tokenization time was approximately 0.85 seconds, excluding infrastructure overhead. No GPU/model forward or action-output extraction occurred. Prompt/data/source freeze and the complete ID checks are retained in the run directory; VERIFICATION.json checks all 27 payload hashes, lengths and shared mapping. No unexpected preflight failure occurred.

The prompts derive only from the previously frozen prefix/cwd payloads; full instructions, source IDs, directory contents and usefulness judgments are not prompt fields. These are already-exposed selected development cases, not a new independent dataset. Only three instruction groups currently have supported final-task reuse witnesses.

Next: validate a separately versioned entrypoint/manifest for these exact prompted inputs, including sidecar-to-tensor joins and response-code coverage, before bounded exploratory capture. Do not edit the old allowlist or mix old plain-prefix states with these contextual observables. Full B1, semantic argument completeness and human G1 remain incomplete. No confirmatory extraction.
