#!/usr/bin/env python3
import json
import tarfile
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
BACKUPS_DIR = REPO_ROOT / "backups"
ARCHIVE = BACKUPS_DIR / "workflows_backup.tar.gz"
INCLUDE_PATHS = [
    REPO_ROOT / "docs" / "workflows",
    REPO_ROOT / ".cursor" / "rules" / "trigger-commands",
]
PROOF = BACKUPS_DIR / "last_success.json"


def ensure_dirs():
    BACKUPS_DIR.mkdir(parents=True, exist_ok=True)


def create_archive() -> list[str]:
    archived: list[str] = []
    with tarfile.open(ARCHIVE, "w:gz") as tar:
        for p in INCLUDE_PATHS:
            if p.exists():
                tar.add(p, arcname=str(p.relative_to(REPO_ROOT)))
                archived.append(str(p.relative_to(REPO_ROOT)))
    return archived


def write_proof(archived: list[str]):
    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "archive": str(ARCHIVE.relative_to(REPO_ROOT)),
        "archived_paths": archived,
        "size_bytes": ARCHIVE.stat().st_size if ARCHIVE.exists() else 0,
    }
    PROOF.write_text(json.dumps(payload, indent=2))


def main():
    ensure_dirs()
    archived = create_archive()
    if not ARCHIVE.exists() or not archived:
        print("ERROR: archive not created or nothing archived")
        raise SystemExit(2)
    write_proof(archived)
    print(f"Backup OK → {ARCHIVE}")
    print(f"Proof → {PROOF}")


if __name__ == "__main__":
    main()