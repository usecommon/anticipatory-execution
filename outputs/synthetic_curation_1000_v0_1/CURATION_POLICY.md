# Curation policy for 1,000 synthetic candidates

The task requests 1,000 new items, judging, and removal of non-reusable items. This batch contains 1,000 new request-framing variants built from the earlier 200 concrete fixture items. They remain 50 substantive scenario templates, 250 scenario variants and 500 task variants. They are not 1,000 independent tasks or 1,000 new semantic situations. No existing label is inherited. Original datasets and labels remain unchanged.

Three AI judging sessions each receive a disjoint, shuffled portion and the frozen rubric. Every item receives a fresh explicit judgment: binary 1, binary 0, or unresolved; ambiguity flag; specific rationale. Reviewers do not receive old labels or mappings. This is one AI judgment per item, not three independent ratings per item. There is no paired inter-rater kappa and no human G1 pass. AI judgment is not ground truth.

The active collection contains only clearly reusable items. Non-reusable items are discarded from the active collection and preserved in an exclusion archive with rationale and provenance. Unresolved or ambiguity-flagged judgments are quarantined rather than recoded as negatives. Because the five variants of a parent item preserve its artifact semantics, conflicting labels or any ambiguity within that parent group quarantine its otherwise-positive variants pending review. Negative judgments remain negative in the archive; no majority vote changes a raw decision. This conservative grouping check is a consistency screen, not an additional independent judge.

All 1,000 original candidates, reviewer inputs, raw submissions, mapping files and exclusion decisions are retained. Counts must sum to 1,000 and active/archive/quarantine sets must be disjoint. No repeated generation to achieve a chosen positive count is allowed. The resulting active collection is expected to contain fewer than 1,000 records.

The public-plus-synthetic plan remains as previously documented. This private synthetic collection does not satisfy public release eligibility, replace public-source adapters or become an untouched holdout. Families must remain grouped in later splits. Existing model parameters, G0 scope, tolerances and H2/H3 endpoints are unchanged. No research-model feature extraction or confirmatory extraction is performed.

A positive-only collection supports demonstrations and example curation. It cannot by itself test revision prediction, false-speculation rate, specificity or usefulness at matched risk. Preserve the complete candidate distribution for any future separately authorized, properly labeled research design. This collection must not be used to claim a favorable internal-state result by removing negative cases.

This is an expansion of wording coverage, not a diversity expansion sufficient for the full 3,000-task benchmark. Templates include synthetic explicit exclusions and stipulated unexecuted outputs. Fractions, confidence, execution time and predictive efficacy are not measured in this curation pass.

Reviewer dispatch preceded this written policy/hash inventory; the input files and assignments existed before dispatch, and no completed submission was inspected before this policy was written. This is a documented curation workflow, not preregistration.
