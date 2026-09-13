# Proposed observable freshness interface — v0.1

This specifies requirements for a future provider adapter. The challenge harness supplies a mocked version service; it does not add that service to BFCL or establish a production implementation. Original BFCL and public-case results remain unchanged.

At execution, preserve a provider-issued directory identity/incarnation, a listing-dependency revision, the request's coverage and the result. Reuse-time metadata must be obtained through an actually available interface and counted as work. The reuse gate sees this metadata and the now-complete task requirements; it does not inspect the evaluator's full environment or expected answer. The pre-execution candidate still sees only its declared prefix-time context, never these future requirements or receipts.

A valid provider contract must establish:

- Target identity and incarnation remain distinct from path spelling. Same path/revision after replacement cannot authorize stale reuse.
- Revisions cover the query's dependencies: names, relevant types, visibility and scope for listing; content changes matter only if the requested output depends on content. Identity/access-context differences cannot silently share a receipt.
- Metadata and listing belong to a defined coherent observation. Specify the time at which correctness is guaranteed and handle concurrent changes between validation and consumption, for example through a provider-supported consistent snapshot or revalidation protocol. This harness does not test those races or implement such mechanisms.
- Missing or untrusted metadata fails closed to fresh work or unresolved evidence. This is an execution choice, not a judgment that earlier work could never be useful.
- Hidden-inclusive coverage may support filtering to a visible-only result; visible-only coverage does not generally certify completeness of an inclusive task. A lack of hidden entries in four sampled public directories does not remove this requirement.
- Byte digests detect accidental modification but do not authenticate a provider, establish truthful revisions or prove semantic correctness. Actual provider provenance and integrity guarantees must be validated separately.

The deliberately broken-provider case demonstrates the boundary: stale output passes the metadata-based gate when the provider fails to revise its token, and the independent evaluator rejects the task output. No threshold change fixes that violated premise. Preserve and report it; do not call the guard validated against dishonest or buggy revision providers.

Acceptance work still needed: a real provider with documented dependency/version semantics, explicit race behavior, failure cases and measured metadata/validation cost. If checking freshness costs as much as redoing the listing, this mechanism may have no latency or compute value. Count early work, metadata, fallback, validation and discarded work in any later matched-budget S1 study; keep offline oracle checks separately identified.

The directory challenge set now exercises the intended mechanical distinctions. Do not expand it merely to accumulate passing tests. Next resolve the actual provider/measurement scope and complete observable-baseline capture/feature interfaces before further model comparisons. Preparation/draft materiality and human G1 require their own rubric/process review; these software cases cannot close them. Confirmatory extraction remains prohibited.
