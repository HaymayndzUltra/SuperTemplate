# Protocol Reference Validation Script Outline

## 1. Objectives
Design automated checks that confirm the renumbered workflow retains intact handoffs, artifact paths, and documentation references. The outline below pairs a Python validation module with optional Bash wrappers for CI execution.

## 2. Python Validation Module (`scripts/validate_protocol_references.py`)
```python
from pathlib import Path
import re

EXPECTED_HANDOFFS = {
    "01-client-proposal-generation.md": "02-client-discovery-initiation.md",
    "02-client-discovery-initiation.md": "03-project-brief-creation.md",
    # ... populate from Section 1.1 of the renumbering prompt
}

ARTIFACT_MAP = {
    "01": "protocol-01",
    "02": "protocol-02",
    # ... include every renumbered protocol id
}

PROTOCOL_PATTERN = re.compile(r"Protocol\s+(\d{2})")
APPLY_PATTERN = re.compile(r"@apply\s+\.cursor/ai-driven-workflow/(.+?)\s")
ARTIFACT_PATTERN = re.compile(r"\.artifacts/protocol-([0-9A-Za-z]+)/")

class ValidationError(Exception):
    pass

class ProtocolValidator:
    def __init__(self, root: Path):
        self.root = root / ".cursor" / "ai-driven-workflow"

    def iter_protocol_files(self):
        yield from sorted(self.root.glob("*.md"))
        yield from sorted((self.root / "review-protocols").rglob("*.md"))

    def check_apply_targets(self, path: Path, content: str):
        for match in APPLY_PATTERN.finditer(content + " "):
            target = match.group(1).split()[0]
            expected = EXPECTED_HANDOFFS.get(path.name)
            if expected and not target.endswith(expected):
                raise ValidationError(f"{path.name}: expected @apply → {expected}, found {target}")

    def check_artifact_paths(self, path: Path, content: str):
        for folder in ARTIFACT_PATTERN.findall(content):
            if folder not in ARTIFACT_MAP.values():
                raise ValidationError(f"{path.name}: unexpected artifact folder '{folder}'")

    def run(self):
        for file in self.iter_protocol_files():
            text = file.read_text(encoding="utf-8", errors="ignore")
            self.check_apply_targets(file, text)
            self.check_artifact_paths(file, text)
        print("All protocol references validated.")

if __name__ == "__main__":
    ProtocolValidator(Path.cwd()).run()
```

### Extension Hooks
- Add a `check_protocol_mentions` method that verifies `Protocol XX` strings match expected numbering for each file.
- Emit a JSON report summarizing validations per file to assist reviewers.

## 3. Bash Wrapper (`scripts/check_protocol_references.sh`)
```bash
#!/usr/bin/env bash
set -euo pipefail

python scripts/validate_protocol_references.py
rg "Protocol [0-9]" . | sort > .artifacts/reference-audit/protocol-mentions.txt
rg "@apply" .cursor/ai-driven-workflow -n > .artifacts/reference-audit/apply-targets.txt
```
- Store audit outputs under `.artifacts/reference-audit/` so they can be attached to PRs.
- Optionally add `pytest`/`tox` invocation if validation integrates with an existing test suite.

## 4. Reporting & CI Integration
- Configure CI to run the Bash wrapper after file renames and before deployment jobs.
- Fail the pipeline if the Python validator raises a `ValidationError` or if Git detects untracked changes after the script runs (guarding against missing renames).
- Publish the generated audit artifacts as build outputs for reviewer download.

## 5. Manual Verification Checklist
- [ ] Spot-check the audit files for representative protocols in each phase (foundation, planning, development, quality, deployment, closure).
- [ ] Confirm supporting docs (AGENTS, integration guides) appear in the audit lists with updated identifiers.
- [ ] Re-run the script after any follow-up edits to ensure the report stays current.
