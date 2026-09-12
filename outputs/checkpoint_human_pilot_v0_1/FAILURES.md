# Preserved issues and limitations

- Initial protocol-file search used a zsh glob that matched no docs; zsh reported no matches. No file changed. Repository-relative reads then used explicit paths and `rg --files`.
- Real browser QA could not launch: the sandbox denied Chromium's MachPort rendezvous and it exited before page load. `software_qa/BROWSER_BLOCKED.json` records this. No approval escalation was attempted because the available permission categories do not provide a process/IPC override. JavaScript behavior passed a minimal DOM harness, which does not verify rendering or native browser behavior.
- The collector initially crashed after parsing a top-level JSON list/null when its identity check assumed an object. Raw originals had been copied first. The previous code and hash-based fix record are preserved under software_qa; the corrected version rejects the malformed submission and writes a report.
- The next collector version could overflow when calling math.isfinite on a huge out-of-range JSON integer. Range checking now precedes finiteness conversion. The previous version and fix hashes remain under software_qa.
- Checkpoints already complete or unreached remain explicit in the schedule. They are not negative reuse labels, policy abstentions, silently dropped cases or forced earlier prefixes.
- No genuine human submissions exist. Software QA drafts and synthetic checker fixtures are not annotation evidence and must never be included in G1 or research scores.
