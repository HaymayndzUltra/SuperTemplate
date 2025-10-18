# Validation Script Outline

## Purpose
Design an automated checker that guarantees every renamed protocol and artifact reference stays synchronized after the renumbering pass. The outline below assumes the script will run inside the repository root and can leverage Python plus `rg` or `git` tooling for verification.【F:documentation/reference-alignment/REFERENCE-MATRIX.md†L6-L79】

## Core Checks
1. **File rename verification**
   - Confirm every expected new filename exists (01–23 plus supporting docs) and the legacy names no longer appear in the tree.【F:protocol-renumbering-prompt.md†L50-L119】
2. **`@apply` continuity audit**
   - Parse each protocol for `@apply` directives and ensure targets map to valid renamed files without loops or missing hops, matching the intended linear flow documented in the integration map.【F:documentation/reference-alignment/REFERENCE-MATRIX.md†L6-L37】【F:.cursor/ai-driven-workflow/PROTOCOL-INTEGRATION-MAP.md†L8-L40】
3. **Artifact directory mapping**
   - Grep for `.artifacts/protocol-` usages and assert they match the new numbering table (e.g., `protocol-05`, `protocol-10`).【F:documentation/reference-alignment/REFERENCE-MATRIX.md†L39-L68】【F:protocol-renumbering-prompt.md†L62-L83】
4. **Documentation alignment**
   - Scan supporting docs (`INTEGRATION-GUIDE.md`, `VALIDATION-GUIDE.md`, `AGENTS.md`, review protocols) for textual protocol numbers and verify they reference the new identifiers only.【F:.cursor/ai-driven-workflow/INTEGRATION-GUIDE.md†L12-L80】【F:.cursor/ai-driven-workflow/VALIDATION-GUIDE.md†L12-L86】【F:.cursor/ai-driven-workflow/AGENTS.md†L20-L231】【F:.cursor/ai-driven-workflow/review-protocols/README.md†L63-L79】
5. **Scenario chain validation**
   - Reconstruct the workflow graph from `@apply` data and assert it matches the documented Phase sequence (no dead ends, 14 flows into 16, 18 into 22, etc.).【F:documentation/reference-alignment/REFERENCE-MATRIX.md†L74-L79】

## Implementation Sketch (Python)
```python
from pathlib import Path
import re
import sys

ROOT = Path('.')
PROTOCOL_DIR = ROOT / '.cursor' / 'ai-driven-workflow'
EXPECTED_FILES = {
    '01-client-proposal-generation.md',
    # ... populate from renumbering map ...
}
ARTIFACT_MAP = {
    'protocol-0': 'protocol-05',
    # ... populate from renumbering prompt ...
}

errors = []

# 1. File rename verification
present = {p.name for p in PROTOCOL_DIR.glob('*.md')}
missing = EXPECTED_FILES - present
legacy = {name for name in present if re.match(r'^[0-9A-Za-z-]+$', name) and name[:2] in {'00', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'} and name not in EXPECTED_FILES}
if missing or legacy:
    errors.append(f"File mismatch: missing={sorted(missing)}, legacy={sorted(legacy)}")

# 2. `@apply` continuity audit
apply_edges = {}
for path in PROTOCOL_DIR.rglob('*.md'):
    for idx, line in enumerate(path.read_text().splitlines(), 1):
        match = re.search(r'@apply\s+([^\s]+)', line)
        if match:
            apply_edges.setdefault(path.name, []).append((idx, match.group(1)))
# Validate edges point to renamed files, detect loops as needed

# 3. Artifact directory mapping
for path in PROTOCOL_DIR.rglob('*.md'):
    for old, new in ARTIFACT_MAP.items():
        if f'.artifacts/{old}/' in path.read_text():
            errors.append(f"Stale artifact path {old} found in {path}")

# 4. Documentation alignment (search across repo)
for doc in ['INTEGRATION-GUIDE.md', 'PROTOCOL-INTEGRATION-MAP.md', 'VALIDATION-GUIDE.md', 'AGENTS.md']:
    doc_path = PROTOCOL_DIR / doc
    text = doc_path.read_text()
    if re.search(r'Protocol\s+(0|00[a-zA-Z]|[1-9])\b', text):
        errors.append(f"Legacy protocol numbering found in {doc_path}")

if errors:
    for issue in errors:
        print(f"ERROR: {issue}")
    sys.exit(1)
print('✅ Reference validation passed')
```

## Optional Enhancements
- Export a DOT graph of the protocol network before and after renumbering for visual inspection.
- Integrate with CI (e.g., GitHub Actions) to block merges when validation fails, mirroring existing validation guidance.【F:.cursor/ai-driven-workflow/VALIDATION-GUIDE.md†L12-L86】
