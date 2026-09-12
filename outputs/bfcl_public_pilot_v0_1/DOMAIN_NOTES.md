# Descriptive first-turn domain annotations

`DOMAIN_TAGS.jsonl` contains 200 evaluator-only AI classifications of the retained full first-user instructions. These are new descriptive annotations, not official BFCL domains, source metadata, reuse ratings, inferred hidden user intents, or human-validated judgments. They must not be supplied as per-task hints to prefix-only proposers.

The vocabulary is the 12 domain names obtained from the earlier synthetic dataset's `domain` fields, plus `Other/Unclear`. No synthetic reuse labels, current pilot reuse ratings, or owner gold were consulted. All 200 evaluator IDs are represented exactly once, with only `item_id`, `domain`, `secondary_domains`, and `rationale` fields. Primary and secondary labels were validated against this vocabulary; no primary label repeats as a secondary label.

## Classification conventions

Primary domain follows the requested work, not an incidental profession, filename extension, or motivation. A Python filename lookup is Information Retrieval, a financial-text storage request is Document Work, and creating a directory with a web-development name is General Productivity. File-content manipulation and document management are Document Work; file discovery and directory inventories are Information Retrieval. Local Search is reserved here for nearby physical services. Vehicle control and vehicle-state inspection are Device/Home Control; route-distance and navigation planning are Travel. Fuel unit conversion alone is General Productivity.

The available finance label explicitly says **Read-only Analysis**. Accordingly, stock orders and stock-watchlist mutations use Other/Unclear; a separately explicit financial-information request can receive a finance secondary label. This avoids silently recasting financial writes as read-only. Item 160 also uses Other/Unclear because it changes an account allowance without clearly requesting travel work. Explicit travel-account authentication, travel budgets, identity checks, booking and insurance remain Travel. These are ontology conventions, not claims that stock mutations lack a recognizable real-world domain.

Secondary domains mark explicit additional work useful for descriptive coverage. They are not exhaustive metadata and do not count as additional observations. Generic information retrieval implicit in a travel or financial lookup is not redundantly tagged. Primary choices for mixed requests are judgment calls, and rationale text makes those choices reviewable.

## Coverage comparison

| Domain | BFCL primary conversation rows | Synthetic candidate-review rows |
|---|---:|---:|
| Coding | 0 | 16 |
| Communication | 3 | 16 |
| Device/Home Control | 30 | 16 |
| Document Work | 25 | 16 |
| Finance-like Read-only Analysis | 24 | 16 |
| General Productivity | 11 | 16 |
| Information Retrieval | 18 | 20 |
| Local Search | 0 | 16 |
| Media | 0 | 16 |
| Scheduling | 0 | 16 |
| Shopping/Research | 0 | 20 |
| Travel | 63 | 16 |
| Other/Unclear | 26 | 0 |
| Total | 200 | 200 |

BFCL has eight nonzero primary categories under these conventions. Local Search appears only as a secondary label on two tire-service requests. Secondary totals are Communication 3, Device/Home Control 1, Document Work 4, Finance-like Read-only Analysis 12, General Productivity 4, Information Retrieval 8, Local Search 2, and Travel 3; these overlap primary observations and must not be added to the 200-row denominator.

The two columns measure different units: BFCL has 200 conversation records, while the synthetic set has 200 candidate-review rows from 100 variants in 50 related families. Domain count differences are descriptive composition differences, not evidence of increased breadth, representativeness, performance or harder/easier evaluation. The synthetic comparison uses only its existing domain-field counts and the previously read README; no outcome labels enter this classification.

## Source patterns and dependence

Direct inspection of the retained text shows strong contiguous thematic blocks: source IDs 0–49 concern local files and directories (with an occasional forwarding request), 50–99 mostly vehicle operations and travel distances, 100–149 stock information or account actions, and 150–199 mostly travel booking and account workflows. These observations are about text ordering, not independently verified source-generation templates.

Repeated instruction patterns include hidden-file listings, document lookup or creation, vehicle locking/refueling/startup, routes among a small recurring set of cities, stock prices/watchlist changes/orders, and flight fares/bookings with payment fixtures. The exact duplicated first instruction in IDs 40 and 43 is documented in `ADAPTER_AUDIT.md`. Conversation-only grouping does not resolve these observed or possible template dependencies. This source should not be presented as 200 independent intent families or a broad substitute for the synthetic set's 12-category coverage.

Many instructions state concrete commands, numerical constraints, conditional state checks, and multi-step sequences. Some preserve awkward wording or conflicting intent, including item 198's booking, subsequent cancellation and social-post request within the same first turn. These features remain source text; classification does not repair them or infer an unstated final outcome. A literal six-word boundary can expose different amounts of actionable information across requests, so the fixed checkpoint is not a semantic-complexity match to the earlier synthetic anchors.

Travel first-turn instructions contain credential-like and payment/identity fixture strings. Exclusion of initial-state credentials does **not** mean all credential-like strings are absent from evaluator full instructions or the all-word inventory. No values are reproduced in these domain annotations, and no authenticity assessment is made. These evaluator-side files must remain outside prefix-only proposer context.

No task execution, domain-specific factual advice, reuse adjudication, model extraction or human G1 evaluation was performed for these annotations.
