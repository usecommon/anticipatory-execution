# Coverage of the frozen comparison hierarchy

This is a prospective availability audit, not a fitted comparison or an amendment to the frozen endpoints. It was written while extraction was running, without inspecting any label-prediction result. The original protocol's signal-family and B0/B1/B2/M definitions remain authoritative.

| Required signal | What this extraction supplies | Remaining work before a defensible comparison |
|---|---|---|
| B0 prefix text, length, embedding, completeness | Exact prefix and token/word counts via coordinator mappings | Freeze a prefix-only embedding/completeness implementation shared across nested models. Do not use actual final instruction length to compute fraction observed; that leaks future input. |
| B1 final-layer probability, entropy, margins | Complete final next-token logits for every observed completed-word prefix | Vocabulary entropy/margins can be computed; they are not automatically calibrated intent/action probabilities. Define and validate the mapping without suffix access. |
| B1 token surprisal | Last-position logits only | This does not recover all per-token observed-prefix surprisal, especially when appending a word retokenizes a boundary. Define a supported observable baseline and identify any separately needed extraction before claiming H2. |
| B1 persistence and argument completeness | Prefix sequence and next-token distributions | Freeze persistence semantics and argument-completeness computation. Full instructions and utility labels may not generate predictor features. |
| B2 single hidden state | 29 last-position entries per prefix, including embedding and layer outputs | Preserve layer indexing; select layer and dimension reduction using fit/development-only procedures. B2 inherits exactly the same B1 inputs. |
| M temporal dynamics | Dense completed-word histories up to eligible 6/12/18 checkpoints | Join by task and order using coordinator mappings. Define time step, boundary cases and displacement/velocity/curvature/stability formulas in advance. |
| M cross-layer/action projections | Layer states at each observed prefix | Fitted action projections/prototypes must use fit labels only. Raw hidden-state similarity is not the same as the protocol's agreement of projected action distributions. |
| Lens features | Layer states, but no lens projections or head parameters in returned tensors | Freeze a valid lens implementation if used; do not substitute an unvalidated lens or claim the whole family was tested. |
| Attention/KV | None | Remain exploratory and unvalidated under this no-cache contract. |

Any prefix-known candidate/action features must be made available consistently to the nested baselines rather than being introduced only for M. Opaque IDs, source labels, final instructions, human/AI rationales and partition membership are not predictor features. Group and task metadata are for splitting, joining and clustered evaluation only.

A smaller diagnostic comparison can be useful, but it must be named according to the features actually implemented; it cannot be reported as the full H2/H3 test if the strong baseline is incomplete. No feature choice may be made to recover an internal-state advantage. All current observations are development-exposed; the exploratory check partition is not confirmatory data. The original minimum effect, bootstrap and confirmatory endpoints are unchanged and are not evaluated by this extraction.
