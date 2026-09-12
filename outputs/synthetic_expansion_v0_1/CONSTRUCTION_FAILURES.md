# Preserved construction failures and timing limitations

An initial hand-authored scenario specification contained an invalid JSON string in the malformed-input test fixture. Parsing failed before dataset creation. The failed specification is retained locally at work/synthetic_expansion_v0_1/specs_invalid_json_attempt.json. The syntax was corrected without dropping the case.

The first built version attached semicolons directly to the shared prefix in revision continuations. Although the reviewed text was a literal prefix, that anchor did not coincide with the builder's punctuation-inclusive completed-word boundary. The pre-fix dataset is preserved locally at work/synthetic_expansion_v0_1/dataset_pre_boundary_fix. Before dispatching annotators, continuations were changed to begin with a whitespace-separated conjunction and a new dataset was built. The final version has 1,677 word observations, versus 1,627 in that draft. This is a documented text/prefix-construction change, not numerical neutrality or evidence of a model fix.

Rater input files and author expectations were generated before reviewer dispatch. The INPUT_FREEZE hash inventory and written STUDY_PLAN were recorded after reviewer dispatch, before their completed submissions were consumed. No rating-informed input edits were made. This ordering is less strong than a timestamped preregistration before any rater access and must not be described as such. The frozen input inventory is checked again during final scoring.

Input isolation uses separate files, random orders and instructions on a shared filesystem. It is not enforced filesystem isolation. AI agreement and AI adjudication are not independent human reliability evidence.
