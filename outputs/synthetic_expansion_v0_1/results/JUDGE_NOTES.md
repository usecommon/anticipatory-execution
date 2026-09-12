# Synthetic expansion AI adjudication notes

This is an AI adjudication of all 200 JUDGE_INPUT items after access to both frozen AI ratings. It is neither an independent third annotation nor human G1 validation. No scientific accuracy, agreement-threshold success, or G1 pass is claimed.

Only RUBRIC.txt and review/JUDGE_INPUT.jsonl were read as task inputs. Each item was reviewed using its own prefix, action, stipulated work product, full instruction, and both ratings. Related rows were not used to supply absent log formats, sensor readings, provenance, or conditional state. All scenario tools, records, outputs, and actions are fictional and unexecuted; no scenario actions or browsing occurred.

The explicit row-level decisions were serialized with the frozen A rationale retained where adjudication agreed with its reasoning. Differences and uncertain cases received specific explanations. Agreement was not a requirement: J136, J172, J177, J182, and J184 remain binary-null. J100 is definitively invalid because its target is wrong regardless of the unknown conditional branch, but its fractional utility is null. Fractions are qualitative estimates of surviving artifact content, not measured effort or expected utility, and no unstated probability was assigned to conditional branches. Null fractional values mean unquantifiable rather than zero utility.

Materiality is evaluated semantically: wrong times, public interfaces, predicates, priority orderings, or command targets require material revision even when editing them is cheap. Empty layouts and generic formulas can remain useful without being complete deliverables. Ancillary access notes and optional weight sorting remain ambiguous positive judgments. Independent lab scores in J158 are accepted under the ordinary independent-evaluation reading, with replication protocol detail absent. These judgments expose limits of the rubric rather than eliminate them.

J172 does not establish company-stated provenance, operand units, or year mapping within its own item. J184 includes the old timeout value but does not supply file/line metadata. Partial extraction versus material reexecution remains unresolved in these two cases. J136 lacks a severity-format contract, J177 lacks the required prior sensor check, and J182 lacks current thermostat state.

Validation checked exactly 200 unique sequential IDs J001–J200, exact field names, allowed binary/null and fractional/null values, confidence range, ambiguity values, and nonempty explanations. Counts: {"0": 59, "1": 136, "None": 5}. Ambiguity Y: 19.

SHA-256 of JUDGE.jsonl: 03169903552e4c8dfd5a24b5d332654f1bfb11be9ccba204df08cfce30702d52.
