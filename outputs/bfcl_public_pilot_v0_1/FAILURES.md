# Preserved failures and limitations

- Initial file inspection used the task root rather than the nested repository: AGENTS.md, study plan and source directory reads failed with no modifications. Correct repository path was then used.
- A guessed prior rubric path `synthetic_expansion_v0_1/review/RUBRIC.txt` was absent. The frozen rubric was recovered from `synthetic_curation_1000_v0_1/RUBRIC.txt` without changing its contents.
- The six-word checkpoint was selected after observing source length coverage; it is not preregistered. Very early prefixes may yield abstentions or low-value scaffolds; retain those outcomes.
