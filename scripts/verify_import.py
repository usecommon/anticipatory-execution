"""Read-only standard-library integrity check; never imports model/GPU code."""
from pathlib import Path
import ast, hashlib, json
root = Path(__file__).resolve().parents[1]
records = json.loads((root / "provenance/IMPORTED_FILES.json").read_text())
for record in records:
    p = root / record["path"]
    assert p.stat().st_size == record["bytes"], p
    assert hashlib.sha256(p.read_bytes()).hexdigest() == record["sha256"], p
for p in root.rglob("*.py"):
    ast.parse(p.read_text(), filename=str(p))
s = json.loads((root / "outputs/g0_closure_v0_5/STATUS.json").read_text())
assert s["G0"] == "PASS_SCOPED" and s["G1"] == "PENDING"
assert not s["confirmatory_extraction"] and not s["development_extraction"]
print(f"PASS: {len(records)} imported files verified; source syntax and gate constraints checked.")
