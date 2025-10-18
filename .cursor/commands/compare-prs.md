# `/compare-prs` – Pull Request Comparison Assistant

## Purpose
Generate an at-a-glance comparison for multiple GitHub pull requests so you
can quickly decide review order, spot blockers, and identify merge-ready work.
The command wraps `scripts/compare_prs.py`.

## Usage
```
/compare-prs <pr-number> [additional-pr-numbers]
```

- Automatically targets the repository for the current workspace
- Supports optional arguments via flags:
  - `--format json` to get structured data for automations
  - `--repo owner/name` to compare PRs from another repository

## Examples
```
/compare-prs 12 34 56
/compare-prs 10 14 --format json
```

## Integration Points
- **Workflow Phases**: Review prioritisation during Protocol 10 (Process Tasks)
  and Protocol 11 (Integration Testing)
- **Evidence Collection**: Captures recommended merge order, risk overview, and
  action hints for each PR
- **Quality Gates**: Highlights merge conflicts or failing checks that must be
  resolved before passing quality gates

## Output Highlights
- Summary table with status, risk, and priority labels
- Dependency map inferred from "Depends on" references
- Recommended merge order using dependency-aware sorting
- Detailed notes per PR including metrics, reviewers, and suggested actions

## Environment Notes
- Uses `$GITHUB_TOKEN` or `$GH_TOKEN` if available to extend API limits
- Works with public repositories without authentication (rate limited)
