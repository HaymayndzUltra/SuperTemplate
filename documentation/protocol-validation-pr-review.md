# Protocol Validation PR Review Template

Use this template when producing validation comparisons for external pull requests. Every submission **must** include:

1. A protocol inventory covering Protocols 01-23 with explicit presence/absence markers
2. A dependency matrix summarising all claimed dependency findings and their supporting evidence
3. A remediation plan that tags each action with an explicit effort estimate (hours or story points)

Run `python scripts/check_evidence_citations.py` before publishing to ensure all citations resolve to repository files.

---

## 0. Metadata
- **Reviewer:** <!-- your name -->
- **Date:** <!-- ISO-8601 date -->
- **Source PRs:** <!-- e.g., #60, #61 -->
- **Artifacts:** <!-- Link to supporting archives/logs -->

---

## 1. Completeness & Coverage

### 1.1 Protocol Inventory (01-23)
Provide a single table that enumerates every mainline protocol. Do not omit any IDs.

| Protocol | Title | Present in Report? (✓/✗) | Notes |
|----------|-------|---------------------------|-------|
| 01 | Client Proposal Generation | <!-- ✓/✗ --> | <!-- rationale --> |
| 02 | Client Discovery Initiation | <!-- ✓/✗ --> | <!-- rationale --> |
| … | … | … | … |
| 23 | Script Governance | <!-- ✓/✗ --> | <!-- rationale --> |

### 1.2 Dependency Matrix Extract
Document each dependency the report validates, disputes, or flags as missing. Cite the exact protocol lines (`F:.cursor/...†Lx-Ly`).

| Dependency | Report Claim | Evidence | Reviewer Conclusion |
|------------|--------------|----------|---------------------|
| P14 → P20 | <!-- e.g., Missing --> | <!-- citation --> | <!-- pass/fail --> |
| … | … | … | … |

### 1.3 Gap & Severity Summary
Summarise completeness outcomes alongside severity tallies.

| PR | Completeness (components delivered / 6) | Evidence Validity (%) | Gap Totals (Critical/High/Medium/Low) |
|----|----------------------------------------|-----------------------|---------------------------------------|
| <!-- # --> | <!-- value --> | <!-- value --> | <!-- value --> |

---

## 2. Evidence Quality Audit
Explain your sampling method and highlight invalid citations. All references must pass `check_evidence_citations`.

- **Sample Size per PR:** <!-- number -->
- **Invalid Citation Examples:** <!-- cite specific failures -->
- **Observations:** <!-- narrative -->

---

## 3. Gap Math Verification
Describe how reported gap counts compare with ground truth artefacts.

| PR | Reported Total | Observed Total | Variance | Notes |
|----|----------------|----------------|----------|-------|

---

## 4. Dependency Logic Review
Summarise each disputed dependency along with supporting evidence and judgement.

| Dependency | Reported By | Evidence | Reviewer Verdict |
|------------|-------------|----------|------------------|

---

## 5. Internal Consistency Checks
Highlight contradictions or alignment within each report (tables vs narrative).

- **PR #**: <!-- notes -->
- **PR #**: <!-- notes -->

---

## 6. Remediation Plan (Include Effort Estimates)
List concrete follow-up actions. Every row must include an effort estimate (hours or points) and severity.

| Action | Severity | Effort Estimate | Owner | Status | Evidence |
|--------|----------|-----------------|-------|--------|----------|
| <!-- e.g., Add citation linting --> | Critical | 6h | <!-- team --> | Planned | <!-- citation --> |

---

## 7. Recommendation & Confidence
Provide final ranking, recommendation, and confidence statement referencing evidence citations.

- **Recommended PR:** <!-- # -->
- **Score Summary:** <!-- table or text -->
- **Confidence Level:** <!-- Low/Medium/High with rationale -->

---

## 8. Appendices
Include quoted excerpts or additional tables as needed. Ensure every block retains file citations.
