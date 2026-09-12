"""Offline verification of the five complete source files used in the structural audit.
Download URLs from REPRODUCTION_INPUTS.json into --directory using URL basename.
No code from the source repositories is imported or executed; no inference.
"""
import argparse, hashlib, json
from pathlib import Path
from urllib.parse import urlparse
parser = argparse.ArgumentParser()
parser.add_argument('--directory', type=Path, required=True)
args = parser.parse_args()
manifest = json.loads(Path(__file__).with_name('REPRODUCTION_INPUTS.json').read_text())
results = []
for item in manifest:
    # Both BFCL files have the same basename: use SHA256 as a unique local filename.
    name = item['sha256'] + '_' + Path(urlparse(item['url']).path).name
    path = args.directory / name
    if not path.exists():
        raise SystemExit(f'MISSING: {name}; obtain {item["url"]}')
    raw = path.read_bytes()
    if len(raw) != item['bytes'] or hashlib.sha256(raw).hexdigest() != item['sha256']:
        raise SystemExit(f'FAIL size/hash: {name}')
    if 'BFCL_v4_multi_turn_base.json' in item['url']:
        rows = [json.loads(line) for line in raw.split(b'\n') if line.strip()]
    else:
        rows = json.loads(raw)
    results.append({'file': name, 'bytes': len(raw), 'records': len(rows), 'hash_verified': True})
print(json.dumps(results, indent=2))
