# External PR Suggestion Comparison

This report cross-references the locally implemented `scripts/compare_pull_requests.py` tool with the three open-source proposals referenced in PRs #17, #19, and #20 of the upstream repository. The goal is to understand how each suggestion aligns with or diverges from the current workflow so future refinements can borrow the strongest ideas.

Since the initial comparison, the local tool has been upgraded to incorporate the
most actionable ideas from those PRs:

- **Review signal ingestion** – approvals, change requests, and mergeability now
  influence risk, priority, and recommended actions.
- **Conflict hotspot detection** – overlapping files across PRs are surfaced in a
  dedicated report section.
- **JSON export & enriched Markdown** – output includes review tables and can be
  exported as structured JSON for downstream automation.

## Capability Matrix

| Capability | Local tool (`compare_pull_requests.py`) | PR #17 (`compare_prs.py`) | PR #19 (`compare_prs.py`) | PR #20 (`compare_prs.py`) |
| --- | --- | --- | --- | --- |
| Data sources | GitHub live fetch or offline JSON snapshots | GitHub live fetch only | GitHub live fetch only | GitHub live fetch only |
| Dependency handling | Parses body for `depends on` phrases and renders a merge order section | Parses body for dependencies and produces topological order list | Extracts dependencies and factors them into readiness scoring | Parses dependencies, shows map, and uses topo sort with fallbacks |
| Risk evaluation | Labels plus change requests/mergeable state elevate risk tiers | Heuristic scoring from draft status, review state, size, and labels | Priority + risk heuristics using label keywords, change size, and test coverage | Label prefix parsing for risk/priority and mergeability-based action hints |
| Priority assessment | Labels, outstanding change requests, and clean + approved PRs | No dedicated priority scoring | Multi-tier priority detection from labels with critical/high emphasis | Priority classification via label prefixes and keywords |
| Action guidance | Contextual next step (update branch, fix reviews, resolve conflicts, merge) | Suggests actions like addressing changes, resolving blockers, or ready to merge | Computes readiness buckets (ready, draft, changes requested) and adds scoring weight | Provides user-facing action hints (awaiting review, resolve conflicts, ready to merge) |
| Conflict analysis | Highlights overlapping files with per-PR breakdown | None | Conflict matrix via file list traversal | Summarizes conflicts in narrative output |
| Output formats | Markdown (tables, review signals, dependency map, conflict hotspots), TSV text, JSON | Markdown summary table + merge order + detailed sections | Plain-text tables plus conflict matrix and scoring summary | Text report or JSON export including summary, dependencies, risk buckets |
| Additional insights | Review signal table, test detection, dependency-aware ordering | Pulls review counts (approvals/changes) and mergeability to influence risk | Detects overlapping files across PRs to highlight conflict hotspots | Groups PRs by risk bucket and exposes reviewer queues |

## Observations by Proposal

### PR #17 — Focus on Review Signals and Merge Blocking
- Strengthens review-awareness by pulling review summaries (approvals vs. change requests) and including them in risk calculations—capabilities now mirrored in the local tool's review signal table.
- Risk scoring emphasizes draft status, lack of approvals, change volume, and "high-risk" labels, leaning toward conservative merge readiness decisions; the local heuristics now elevate risk when change requests or merge blockers appear.
- Output mirrors the local Markdown format but adds explicit merge blocker messaging when `mergeable_state` is problematic, aligning closely with the updated recommended-action copy.

### PR #19 — Scoring, Conflict Analysis, and Auto-Detection
- Introduces an auto-detected repository fallback using the local Git configuration alongside a urllib-based GitHub client, reducing the number of required flags for common workflows.
- Calculates readiness, risk, and priority scores that roll into a numeric ranking, rewarding PRs that touch tests or remain small while penalizing items with overlapping file conflicts.
- Builds a conflict matrix by traversing file lists, flagging hotspots where multiple PRs touch the same files—an idea adopted by the upgraded conflict hotspot section.

### PR #20 — Action-Oriented Narrative with JSON Export
- Provides rich action hints derived from mergeable state, reviewer assignments, and draft reasons so stakeholders can triage follow-up work without digging into GitHub directly.
- Normalizes label prefixes (`risk:` and `priority:`) to bucket PRs, producing risk overviews and priority-aware merge ordering with topo-sort fallbacks when dependency graphs cycle.
- Offers dual output modes (structured JSON and text narrative) for downstream automation—paralleling the local script's Markdown, TSV, and JSON renderers.

## Takeaways for Local Evolution
- ✅ Review signals and mergeability now inform risk, priority, and recommended actions, reducing false "ready" states when change requests or conflicts exist.
- ✅ Conflict hotspots highlight overlapping files, making PR #19's coordination insight available directly in the Markdown report.
- ✅ JSON export plus Markdown review tables capture PR #20's automation and communication focus.
- 🔄 Future enhancement: incorporate automatic repository detection and scoring weights from PR #19 for richer prioritization when test coverage or file types change.
- 🔄 Future enhancement: expose reviewer queue summaries similar to PR #20 for teams that triage by reviewer workload.
