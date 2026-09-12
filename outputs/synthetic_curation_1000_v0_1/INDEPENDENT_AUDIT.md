# Independent curation audit

Result: PASS — no mechanical or policy-partition errors found.

This audit independently recomputed the partitions from `ALL_CANDIDATES.jsonl`, `ALL_JUDGMENTS.jsonl` and the prose in `CURATION_POLICY.md`; it did not run the builder or curator, modify ratings, execute fictional fixtures, or read owner gold. The auditor previously authored one disjoint judging submission, so this is an independent implementation check, not a second independent rating of every item.

- Candidates: 1000 unique; prior parents: 200; exactly five framing variants per parent.
- Reviewer assignments: [334, 333, 333]; exact disjoint coverage and one raw AI judgment per candidate.
- Raw labels: 680 positive, 305 negative, 15 unresolved; 39 ambiguity flags.
- Recomputed active: 665; excluded: 305; quarantine: 30; exact disjoint union of all 1,000 candidates.
- Active coverage: 133 parent items and 50 source templates.
- Verified all 13 frozen input hashes, all three saved raw-submission hashes, and the prior-source hash against BUILD_QA.
- Verified every archived/active/quarantined artifact and attached judgment is unchanged from the candidate and aggregate judgment; mappings and disposition ledger agree.
- Prefix schedules: 9585 unique observations across 500 tasks; every literal word-boundary prefix appears exactly once in order, including the full instruction. Designated candidate prefixes are also literal prefixes.
- Semantic lineage: domain, action, execution class, work product, fixture contract, and final-instruction suffix remain identical to each parent; variation is limited to the five request framings.

The 1,000 distinct rows are not 1,000 independent substantive tasks: there are 50 source scenario templates, 250 framed scenario variants, 500 framed task variants, and 12 domains. The prior source has 200 parent action items. Repeated wording variants must stay grouped in any later split. The positive-only active collection cannot alone measure revision prediction, specificity, false speculation, or usefulness at matched risk. One AI rating per item supplies neither inter-rater kappa nor human G1 validation, and no timing or predictive-efficacy claim is established by this audit.

Methodological limitations: matching recorded hashes verifies present byte integrity against the inventory, not an independently timestamped preregistration. The policy explicitly records that reviewer dispatch preceded the written policy/hash inventory. Prefix schedule generation is not present in `build.py`, so this audit verifies the frozen schedule file directly rather than claiming the builder alone regenerates every artifact. Source-template count describes lineage; it does not establish statistical independence among templates.

Checks passed: 5540. Errors: 0.
