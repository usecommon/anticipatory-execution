# Coordinator: independent-human collection

Only share the assigned reviewer ZIP. Do not share this file, source mappings, boundary identities, AI reports, or repository access. The private repository contains an owner-only key; it must remain inaccessible to annotators. No invitations or messages were sent by this task.

Each package contains 220 cases. The same 200 main cases are presented to both reviewers, plus 20 separately tracked sufficiency-boundary checks. The original rubric's200-item reliability criterion pertains to the main set. Package START_HERE and on-page instructions specify that all 220 should be completed. Boundary diagnostics never count as additional main/G1 items. No expected labels are given to reviewers.

1. Arrange two actual distinct human reviewers who have not seen prior item-level AI labels for the assigned work. Record identity/pseudonym and independence/exposure evidence outside the packages. Software cannot establish that a declared name belongs to an independent person.
2. Have them work separately and return their exported JSON. Preserve both returned originals before parsing, discussing disagreements or requesting changes. The form labels incomplete exports DRAFT; its submitted status is not validation.
3. Run the checker with a new output directory, using only genuine returned files:

```sh
python3 outputs/checkpoint_human_pilot_v0_1/collect_humans.py \
  --a /absolute/path/to/Annotator_A_SUBMITTED_FOR_REVIEW.json \
  --b /absolute/path/to/Annotator_B_SUBMITTED_FOR_REVIEW.json \
  --out /absolute/path/to/new_collection_directory
```

The checker copies originals and hashes them before validation. It refuses to overwrite an existing collection. It checks package/role bindings, exact item coverage, required fields, declarations, types, null rules and main/control separation. Rejected readable submissions remain preserved with a report. Software_qa files are test fixtures and must never be passed off as human submissions.

4. Review main sufficiency/disposition agreement, all missing or unresolved fields, label prevalence, and kappa with its exact denominator before adjudication. A kappa on fewer than 200 complete substantive binary main pairs does not satisfy the original 200-item gate. Do not recode insufficient work or unknowns into zeros. Boundary diagnostics are reported separately and need substantive interpretation; no automated control-pass threshold was invented.
5. Record a distinct third human adjudicator and resolve disagreements with both originals, final sufficiency/reuse judgment and reasons. The checker prepares an ADJUDICATION_PENDING file for disagreements and ambiguity flags, but generates no final judgments. Discuss findings only after both originals are frozen.
6. Produce a separate evidence-backed process report. If reliability is below 0.70, prevalence is degenerate, completeness fails or materiality remains unsettled, preserve that result and follow the frozen revision/new-pilot procedure. Do not edit original answers or redefine the denominator to obtain a pass. Check boundary-control behavior when deciding whether the clarification is understood.

The numerical criterion is intentionally not a G1 closure function. The clarified rubric and new sample also require explicit process review; high agreement alone does not establish data validity, public reproducibility or scientific efficacy. G0 remains scoped. No extraction is enabled by receiving or validating forms.

When publishing any later release, anonymize reviewer identities and respect source rights and blinding. Do not publish the private repository wholesale. No human submissions or identifying reviewer information exist in this newly created package.
