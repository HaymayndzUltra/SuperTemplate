# Validation Script Outline

Use this outline to implement automated checks (Python or Bash) verifying that the renumbering completed without regressions.

## 1. Directory and Filename Validation
- Walk `.cursor/ai-driven-workflow/` and confirm every protocol file matches the `NN-name.md` pattern (01–27).
- Ensure legacy filenames are absent (e.g., `00a-client-proposal-generation.md`).
- Verify supporting docs renamed (`25-protocol-integration-map.md`, `26-integration-guide.md`, `27-validation-guide.md`).

### Pseudocode
```python
from pathlib import Path
EXPECTED = {
    '01-client-proposal-generation.md',
    '02-client-discovery-initiation.md',
    # ... continue through 27
}
root = Path('.cursor/ai-driven-workflow')
found = {p.name for p in root.glob('*.md') if p.name[:2].isdigit()}
assert EXPECTED <= found
assert not any(name.startswith(('00a', '00B', '0-')) for name in found)
```

## 2. `@apply` Integrity Check
- Use `rg` or Python regex to extract every `@apply` target.
- Confirm each target filename exists post-renumbering.
- Flag lingering references to legacy names or missing files.

### Bash Snippet
```bash
rg '@apply' .cursor/ai-driven-workflow -o -r '$0' \
  | sed 's/.*@apply \(.*\)/\1/' \
  | while read target; do
      if [ ! -f "$target" ]; then
        echo "Missing target: $target"
      fi
    done
```

## 3. Protocol Number Text Replacement
- Search for `Protocol [0-9A-Za-z]+` occurrences and ensure numbers align with new sequence.
- Implement mapping dictionary to detect old IDs (00a, 00B, 4, 15, etc.).
- Produce report listing offending files and line numbers.

### Pseudocode
```python
OLD_TOKENS = {'Protocol 00a', 'Protocol 0', 'Protocol 15', ...}
for path in Path('.').rglob('*.md'):
    for i, line in enumerate(path.read_text().splitlines(), 1):
        for token in OLD_TOKENS:
            if token in line:
                print(f"Legacy token {token} in {path}:{i}")
```

## 4. Artifact Path Consistency
- Confirm `.artifacts/protocol-XX/` directories align with new IDs.
- Search automation snippets for outdated directory names.
- Optionally, rename directories using a mapping list and verify success.

### Bash Snippet
```bash
rg '\.artifacts/protocol-' -n \
  | rg 'protocol-(0[0AB]|[1-9])' && echo "Legacy artifact paths detected"
```

## 5. Supporting Documentation Integrity
- Re-parse PROTOCOL-INTEGRATION-MAP, INTEGRATION-GUIDE, AGENTS docs to ensure sequences follow 01→27 without gaps.
- Validate that scenario descriptions reference updated protocol IDs.

## 6. Reporting
- Aggregate results into a CSV or Markdown summary highlighting:
  - Missing files
  - Invalid `@apply` targets
  - Legacy protocol mentions
  - Artifact path mismatches
- Exit with non-zero status if any violations detected to support CI/CD enforcement.

## 7. Optional Enhancements
- Integrate with pre-commit hook to block merges with stale references.
- Provide auto-fix suggestions (search/replace) when feasible.
- Generate HTML report summarizing remapped references for audit trail.
