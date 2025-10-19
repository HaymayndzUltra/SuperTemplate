# Protocol Reference Validation Script Outline

## Objectives
Design an automated validator that ensures every reference affected by the renumbering aligns with the sequential protocol scheme. The outline below assumes the raw reference inventory captured in `documentation/protocol-reference-data.json` and the aggregate counts in `documentation/protocol-reference-summary.json` as the authoritative baseline for comparisons.【F:documentation/protocol-reference-data.json†L1-L354】【F:documentation/protocol-reference-summary.json†L2-L5】

## Recommended Toolchain
- **Language:** Python 3.11+
- **Libraries:** `pathlib`, `json`, `re`, `subprocess`
- **Inputs:**
  - Freshly renumbered repository snapshot
  - Baseline reference inventory (`protocol-reference-data.json`)
  - Sequential mapping table from `protocol-renumbering-prompt.md`

## High-Level Workflow
1. **Load Baseline Data** – Parse `protocol-reference-data.json` to obtain the list of files, expected `@apply` targets, artifact prefixes, and filename references prior to renumbering.【F:documentation/protocol-reference-data.json†L2-L354】
2. **Resolve Sequential Mapping** – Convert legacy filenames to their sequential counterparts using the mapping table in Section 1.1 of the adjustment prompt.【F:protocol-renumbering-prompt.md†L14-L44】
3. **Scan Repository** – Traverse the renumbered tree to build an updated snapshot of `@apply` directives, artifact references, textual “Protocol X” mentions, and `.cursor/ai-driven-workflow/*.md` paths.
4. **Compare References** – Verify that every baseline reference has a renamed counterpart with the new numbering, and ensure no stale legacy identifiers remain.
5. **Report & Exit Codes** – Produce a Markdown or JSON report summarising mismatches, with a non-zero exit code when discrepancies are found.

## Detailed Check List

### 1. File Rename Verification
- Confirm that each legacy filename now exists at the sequential path described in the mapping table.
- Validate that no files retain the old naming pattern (e.g., `01-*`, `0-*`).

### 2. `@apply` Chain Integrity
- Extract every `@apply` directive from protocol and review files.
- Assert that each directive targets the expected new filename (e.g., `01-client-proposal-generation.md` → `02-client-discovery-initiation.md`).【F:protocol-reference-mapping.md†L22-L75】
- Ensure there are no dangling or circular references relative to the sequence documented in `PROTOCOL-INTEGRATION-MAP.md`.【F:.cursor/ai-driven-workflow/PROTOCOL-INTEGRATION-MAP.md†L1-L92】

### 3. Artifact Path Alignment
- Search for `.artifacts/protocol-` strings.
- Confirm every occurrence uses the new numbering (e.g., `.artifacts/protocol-12/` instead of `.artifacts/protocol-4/`).【F:protocol-renumbering-prompt.md†L32-L62】
- Optionally, verify that the referenced directories actually exist on disk after regeneration.

### 4. Textual Protocol Mentions
- Identify any remaining “Protocol X” phrases.
- Cross-check the numbers against the sequential IDs to ensure no legacy values persist.【F:documentation/protocol-reference-summary.json†L2-L5】

### 5. Supporting Documentation Integrity
- Audit `INTEGRATION-GUIDE.md`, `PROTOCOL-INTEGRATION-MAP.md`, `VALIDATION-GUIDE.md`, and `review-protocols/*` for updated filenames and numbering.【F:protocol-renumbering-prompt.md†L74-L90】
- Confirm that navigation links and tables of contents resolve to the new file names.

## Pseudocode Skeleton
```python
from pathlib import Path
import json, re, sys

ROOT = Path('.')
BASELINE = json.loads(Path('documentation/protocol-reference-data.json').read_text())
MAPPING = {...}  # Populate from Section 1.1 of the prompt
errors = []

for old_name, new_name in MAPPING.items():
    if not ROOT.joinpath('.cursor/ai-driven-workflow', new_name).exists():
        errors.append(f"Missing renamed file: {new_name}")
    if ROOT.joinpath('.cursor/ai-driven-workflow', old_name).exists():
        errors.append(f"Legacy file still present: {old_name}")

for rel_path, baseline in BASELINE.items():
    # Skip supporting docs without renumbering requirements as needed
    new_path = resolve_new_path(rel_path, MAPPING)
    content = ROOT.joinpath('.cursor/ai-driven-workflow', new_path).read_text()
    # 1. Verify @apply
    expected = [rewrite_target(t, MAPPING) for t in baseline['apply_targets']]
    actual = re.findall(r'@apply\s+([^\s]+)', content)
    if sorted(actual) != sorted(expected):
        errors.append(f"@apply mismatch in {new_path}: {actual} vs {expected}")
    # 2. Verify artifact paths
    for old_prefix in baseline['artifact_refs']:
        new_prefix = translate_artifact(old_prefix)
        if f".artifacts/protocol-{new_prefix}/" not in content:
            errors.append(f"Artifact prefix missing in {new_path}: protocol-{new_prefix}")
    # Additional checks for textual mentions, etc.

if errors:
    Path('validation-report.md').write_text('\n'.join(errors))
    sys.exit(1)
else:
    print('All protocol references validated successfully.')
```

## Execution Steps
1. Run the validation script after completing all renames: `python scripts/validate_protocol_references.py`.
2. Inspect `validation-report.md` for any discrepancies and resolve them before shipping the branch.
3. Re-run the validator until it exits with code `0` and prints the success banner.

---

**Outcome:** Following this outline ensures the renumbered protocol system preserves its integration flow, evidence chain, and supporting documentation without regression.
