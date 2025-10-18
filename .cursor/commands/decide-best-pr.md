# decide-best-pr

**Objective**  
Pick the single most logical PR to merge among exactly four PRs that are alternative solutions. Use ONLY the actual PR content (bodies + diffs). No heuristic scoring. No assumptions.

**How to run**
1) Open an integrated terminal.
2) Run: `./scripts/pr-bundle.sh <PR1> <PR2> <PR3> <PR4>` (GH_SUPERTEMPLATE is already set).
3) Read these files per PR:
   - `pr_bundle/PR_<n>/title.txt`
   - `pr_bundle/PR_<n>/body.md`
   - `pr_bundle/PR_<n>/files.json`
   - `pr_bundle/PR_<n>/diff.patch`

**Decision rules (strict, content-only)**
- **Task fit first**: Does the code/docs implement EXACTLY the requested deliverable?
  - Look for concrete evidence in `body.md` and `diff.patch` (filenames changed, artifacts added).
- **Correctness/logic**: Is the approach technically sound and coherent end-to-end?
  - Read critical hunks in `diff.patch`; confirm no missing pieces or contradictions.
- **Scope discipline**: No unnecessary churn unrelated to the task.
- **Merge cleanliness**: Prefer straightforward diffs (few, focused files; clean structure) if both solve the task equally well.

**What to output (Markdown)**
### 🏆 Executive Pick
- **PR**: #<n> — <title from title.txt>
- **Why it's the most logical**: cite exact files/hunks (paths + brief references) that prove task completion and correctness.
- **What it delivers**: list the artifacts it adds/changes that match the request.
- **Side-effects avoided**: note any risky or irrelevant changes the other PRs attempted.

### Quick Contrast
- **vs #A**: one-liner grounded in specific diff/body evidence.
- **vs #B**: …
- **vs #C**: …

### Minimal Merge Checklist
- Files to glance after merge (if any).
- Follow-ups (if any).

**Constraints**
- Do NOT invent content. Only reference what appears in `body.md` and `diff.patch`.
- Keep it concise and decision-ready.
