"""Download private GitHub release evidence and verify hashes; no inference."""
import argparse, hashlib, json, subprocess, zipfile
from pathlib import Path

def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(8 * 1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()

def main():
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / 'provenance/GITHUB_RELEASE_ASSETS.json').read_text())
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--asset', action='append', help='Asset filename; repeat to select. Default: all.')
    p.add_argument('--destination', type=Path, default=root / '.local/research-evidence')
    p.add_argument('--verify-only', action='store_true', help='Verify already downloaded ZIPs without network or extraction.')
    args = p.parse_args()
    known = {a['asset']: a for a in manifest['assets']}
    if args.asset and set(args.asset) - known.keys():
        p.error('Unknown asset: ' + ', '.join(set(args.asset) - known.keys()))
    selected = args.asset or list(known)
    archive_dir = args.destination / 'archives'
    archive_dir.mkdir(parents=True, exist_ok=True)
    for name in selected:
        record = known[name]
        if not record.get('uploaded', False) and not args.verify_only:
            raise RuntimeError('Asset upload is pending: ' + name + '. See docs/GITHUB_EVIDENCE_RESTORE.md')
        archive = archive_dir / name
        if not archive.exists() and not args.verify_only:
            subprocess.run(['gh', 'release', 'download', manifest['release'], '--repo',
                            'usecommon/anticipatory-execution', '--pattern', name,
                            '--dir', str(archive_dir)], check=True)
        if not archive.is_file() or archive.stat().st_size != record['bytes'] or sha(archive) != record['sha256']:
            raise RuntimeError('Missing or mismatched archive: ' + str(archive))
        with zipfile.ZipFile(archive) as z:
            members = z.namelist()
            expected = {f['path']: f for f in record['files']}
            if len(members) != len(set(members)) or set(members) != set(expected):
                raise RuntimeError('Archive member mismatch: ' + name)
            for member in members:
                rel = Path(member)
                if rel.is_absolute() or '..' in rel.parts:
                    raise RuntimeError('Unsafe archive path')
                if args.verify_only:
                    continue  # Archive hash already binds every member byte.
                target = args.destination / 'restored' / rel
                row = expected[member]
                if target.exists():
                    if not target.is_file() or sha(target) != row['sha256']:
                        raise RuntimeError('Refusing to overwrite: ' + str(target))
                else:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    with z.open(member) as source, target.open('xb') as dest:
                        for chunk in iter(lambda: source.read(8 * 1024 * 1024), b''):
                            dest.write(chunk)
                if target.stat().st_size != row['bytes'] or sha(target) != row['sha256']:
                    raise RuntimeError('Restored member mismatch: ' + str(target))
        print('VERIFIED', name, flush=True)

if __name__ == '__main__':
    main()
