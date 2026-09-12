# Public data and dataset sensitivity requirement

## Authority and scope

The owner requires experimental data to be publicly available so others can verify the experiment and assess whether changing the data changes the result. This is an additional data eligibility and reporting requirement. It does not change the frozen thesis, hypotheses, endpoints, numerical tolerances or human G1 gate. Earlier artifacts retain their historical status; this document does not certify their compliance.

Use public, versioned sources for future thesis experiments. Public availability alone is insufficient: document applicable licensing and the ability to obtain the exact version. A private repository or a source name without an accessible snapshot is not public availability. Author-created or synthetic data must also be publicly released with generation provenance before supporting a publicly verifiable result; describe it separately from independently sourced benchmarks.

## Required evidence before admitting data

For each source, record its public URL, exact revision, retrieval date, source record IDs, content hashes, license/redistribution terms and acquisition instructions. Preserve a lawful snapshot or a durable public route to the exact bytes. Do not assume repository code licensing covers all dataset content. If access or rights cannot be established, keep the source pending rather than silently substituting it.

Publish the construction code and manifests linking source records to adapted instructions, prefixes, actions, concrete outputs, labels and task-level splits. Include generation/model configurations, seeds, annotation rubric and anonymized judgments/adjudication, filtering decisions, unresolved cases and failure counts. Publish necessary tool fixtures or simulator versions so a changing live service does not become an undocumented data change. If a component cannot be publicly reproduced, disclose the limitation and do not mark the complete experiment publicly verifiable.

Annotation answers and final instructions must remain hidden from prefix-time models and independent raters as required by the protocol. Public release of evaluation labels should occur after blind submissions and the applicable evaluation are frozen. Use separate public release artifacts; do not make the existing private repository public wholesale, because it contains the owner-only gold key and historical private material. This requirement does not authorize exposing that key or identifying annotators.

## Dataset changes are experimental interventions

Never overwrite a dataset release or transfer labels automatically to changed prefix–action pairs. Preserve the old release and record the new version, reason, source mix, transformations, affected IDs and label provenance. Making prefixes literal, switching public sources, changing candidate actions or using executable labels can change the task being measured, its difficulty and the apparent internal-state advantage.

Before evaluating a new version, specify the comparison and keep B1/B2/M on the same examples, splits, action policy, labels and validated numerical contract. Where possible, compare dataset versions with other factors fixed and use paired analysis on genuinely matched units. If data and implementation must change together, report the confounding rather than attribute the difference solely to either one. Do not average incompatible releases into one score.

Report source/domain composition, task and prefix counts, action coverage, non-reuse prevalence, ambiguity, exclusions/failures, token lengths and late-revision patterns for each version. Preserve aggregate and source/domain-level results, the frozen H2/H3 comparisons and uncertainty estimates. Sensitivity analyses supplement the frozen primary endpoints; they do not replace them after outcomes are known. Report loss or reversal of the internal-state advantage as a valid outcome, not a reason to select a more favorable dataset.

Public sources can overlap model training data. Group related tasks/templates before prefix expansion, document exposure and contamination uncertainty, and do not claim that public availability proves unseen generalization. Inspecting a development sample does not make it an untouched holdout.

## Current disposition and next step

- The existing 200-item pilot and owner decisions are preserved as diagnostic history.
- The 50-task, 703-observation literal-prefix candidate is structural preparation only. Its public source provenance and redistribution eligibility have not been established. It is not eligible for thesis efficacy evidence under this requirement.
- The earlier public-dataset audit is a starting inventory, not a completed source-admission check or an action-reusability label oracle.
- Next, prepare a source-admission manifest and reproducible adapter for a pinned public development source, with source rights and exact bytes verified before adopting its records. Do not further label the unverified pilot candidate as though it were the thesis benchmark.
- G0 remains scoped; G1 remains pending. No development or confirmatory extraction is authorized by this document. Any required protocol amendment must be explicit and prospective.
