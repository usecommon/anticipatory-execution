# Source attribution and adaptation notice

Upstream: ShishirPatil/gorilla, Berkeley Function Calling Leaderboard, commit `6ea57973c7a6097fd7c5915698c54c17c5b1b6c8`. Original repository license is preserved in SOURCE_LICENSE.txt. SOURCE_MANIFEST.json pins the exact dataset, Python source and license identities.

The two files under vendor/ are byte-preserved upstream Python files. They are used only for the inspected in-memory initialization and directory-listing paths. No implication of upstream endorsement or official BFCL benchmark scores is made.

SOURCE_PROJECTION.jsonl is a transformation of nine selected original records: it retains source filesystem configurations and all their dialogue, while omitting every other class's initial state. It adds coordinator IDs, grouping and scope metadata. TASK_SPECS.jsonl contains authored first-turn evaluation mappings, not official upstream labels. Exact transformation code is restore.py. No source file contents or dialogue are interpreted as commands.

Repository license preservation is not blanket admission of all adaptations/annotations for public release. The research repository remains private. No unrelated credential-bearing state is redistributed in this projection. Raw full source can be obtained separately using the pinned URL and hash; it is not committed here.
