# Pull Request Comparison Workflow

This guide explains how to generate a consolidated review summary for multiple GitHub pull requests using the `compare_prs.py` script.

## Prerequisites

1. **Python 3.9+**
2. **Dependencies**: Install the Python dependencies listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

3. **GitHub Token**: Create a personal access token with at least the `repo` scope and export it as `GITHUB_TOKEN`:

   ```bash
   export GITHUB_TOKEN=ghp_your_token_here
   ```

## Usage

Run the script from the repository root and provide the repository slug (`owner/name`) along with the pull request numbers you want to compare:

```bash
python scripts/compare_prs.py --repo HaymayndzUltra/SuperTemplate 1 3 4 8
```

### Example Output

```
## Pull Request Comparison Summary

| PR | Title | State | Risk | Action |
|----|-------|-------|------|--------|
| #1 | Batch 1 design-to-operations protocols | Open | Medium | ⚠️ Needs final checks |
| #3 | Architecture and environment protocols | Open | Low | ⚠️ Needs final checks |
| #4 | Critical deployment protocols | Open | High | 🚧 Resolve merge blockers |
| #8 | Protocol reference mapping | Open | Low | ⚠️ Needs final checks |

### Recommended Merge Order
1. PR #1 — Batch 1 design-to-operations protocols (Risk: Medium)
2. PR #3 — Architecture and environment protocols (Risk: Low)
3. PR #4 — Critical deployment protocols (Risk: High)
4. PR #8 — Protocol reference mapping (Risk: Low)

### PR #1: Batch 1 design-to-operations protocols
- **URL**: https://github.com/HaymayndzUltra/SuperTemplate/pull/1
- **State**: Open | **Draft**: No
- **Branches**: feature/batch-1 → main
- **Reviews**: 0 approvals, 0 change requests, 0 comments
- **Files Changed**: 12 | **Total Changes**: 842
- **Labels**: operations
- **Risk Level**: Medium
- **Action**: ⚠️ Needs final checks
- **Risk Factors**: no approvals yet, 12 files changed, 842 total changes
- **Dependencies**: #3
```

## Tips

- Add `--token` to explicitly pass a token if you do not want to rely on the `GITHUB_TOKEN` environment variable.
- The script detects dependencies mentioned in pull request descriptions using phrases like `Depends on #123` or `Blocked by #123` and uses them to recommend a merge order.
- Reviewers can paste the Markdown output directly into check-in notes or status updates.
