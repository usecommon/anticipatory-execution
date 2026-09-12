"""Reconstruct and verify the complete word-boundary inventory without inference."""
import json
import re
from pathlib import Path
p = Path(__file__).resolve().parent
rows = [json.loads(x) for x in (p / "ALL_CANDIDATES.jsonl").read_text().splitlines()]
tasks = {}
for row in rows:
    key = row["task_id"]
    assert key not in tasks or tasks[key] == row["full_instruction"]
    tasks[key] = row["full_instruction"]
expected = []
for task, instruction in tasks.items():
    for i, match in enumerate(re.finditer(r"\S+", instruction), 1):
        expected.append({"observation_id": f"{task}-w{i:03d}", "task_id": task, "prefix": instruction[:match.end()]})
actual = [json.loads(x) for x in (p / "ALL_WORD_PREFIXES.jsonl").read_text().splitlines()]
assert expected == actual
print(f"PASS: {len(actual)} word prefixes reconstructed across {len(tasks)} task variants")
