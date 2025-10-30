   
   ```bash
   # Validate timeline, budget, and collaboration agreements
   python scripts/validate_discovery_expectations.py \
     --recap .artifacts/protocol-02/discovery-recap.md \
     --timeline .artifacts/protocol-02/timeline-discussion.md \
     --comms .artifacts/protocol-02/communication-plan.md \
     --output .artifacts/protocol-02/gate3-validation.json
   
   # Exit codes: 0=pass (client approved), 1=fail (missing approval), 3=escalation required
   # Logs: .artifacts/protocol-02/gate3-validation.log
   # Output: JSON with approval_status, pending_items, escalation_recommendations
   # Owner: account management team
   # CI Integration: manual trigger only (requires client input)
   ```

#### Evidence Aggregation
1. **`[MUST]` Aggregate evidence artifacts:**
   * **Action:** Execute script to collect and validate all discovery artifacts
   * **Evidence:** `.artifacts/protocol-02/evidence-manifest.json`
   * **Validation:** Exit code 0 and all required artifacts present
   
   ```bash
   # Aggregate all discovery artifacts into evidence package
   python scripts/aggregate_evidence_02.py \
     --input-dir .artifacts/protocol-02/ \
     --output .artifacts/protocol-02/evidence-manifest.json \
     --include-transcripts \
     --validate-integrity
   
   # Exit codes: 0=success, 1=missing artifacts, 2=integrity check failed
   # Logs: .artifacts/protocol-02/evidence-aggregation.log
   # Output: JSON manifest with artifact_list, checksums, timestamps, completeness_score
   # Owner: protocol orchestration team
   # Registry: scripts/script-registry.json → protocol-gates.evidence-aggregation
   ```

#### Prerequisite Validation
1. **`[MUST]` Validate prerequisites:**
   * **Action:** Execute script to check all prerequisites before starting discovery
   * **Evidence:** `.artifacts/protocol-02/prereq-validation.json`
   * **Validation:** Exit code 0 and all prerequisites met
   
   ```bash
   # Validate all prerequisites before starting discovery
   python scripts/validate_prerequisites_02.py \
     --check-artifacts \
     --check-approvals \
     --check-system-state \
     --output .artifacts/protocol-02/prereq-validation.json
   
   # Exit codes: 0=all met, 1=missing prerequisites, 2=partial (can proceed with warnings)
   # Logs: .artifacts/protocol-02/prereq-validation.log
   # Output: JSON with prerequisites_status, missing_items, blocking_issues
   # Owner: protocol orchestration team
   # Note: Must run BEFORE any workflow steps
   ```

### CI/CD Integration:
```yaml
name: Protocol 02 Validation Pipeline
on:
  push:
    paths:
      - '.artifacts/protocol-02/**'
  pull_request:
    paths:
      - '.cursor/ai-driven-workflow/02-*.md'

jobs:
  validate-gates:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      
      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Run Protocol 02 Quality Gates
        run: |
          python3 scripts/run_protocol_gates.py \
            --protocol 02 \
            --fail-on-gate-failure \
            --output .artifacts/protocol-02/ci-gate-results.json
        continue-on-error: false
      
      - name: Upload gate results
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: protocol-02-gate-results
          path: .artifacts/protocol-02/*-validation.json
      
      - name: Comment on PR
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v6
        with:
          script: |
            const fs = require('fs');
            const results = JSON.parse(fs.readFileSync('.artifacts/protocol-02/ci-gate-results.json'));
            const comment = `## Protocol 02 Validation Results\n\n${results.summary}`;
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: comment
            });
```

### Script Execution Context

**Environment Requirements:**
- Python 3.9+
- Dependencies: `pyyaml`, `jsonschema`, `pydantic` (see `requirements.txt`)
- Environment variables: `PROJECT_ROOT`, `ARTIFACTS_DIR` (optional, defaults to `.artifacts/`)

**Permissions:**
- Read access: `.artifacts/protocol-01/`, `.artifacts/protocol-02/`
- Write access: `.artifacts/protocol-02/`
- No external API credentials required

**Output Capture:**
All validation scripts write structured JSON to `--output` path and human-readable logs to `.log` file with same basename:
```bash
# Example: Both files created
.artifacts/protocol-02/gate1-validation.json  # Machine-readable
.artifacts/protocol-02/gate1-validation.log   # Human-readable
```

### Manual Fallbacks:

**When automation is unavailable:**

1. **Manual Discovery Review:**
   - Conduct live review session with client
   - Document in `.artifacts/protocol-02/manual-discovery-review.md`
   - Use checklist from `.templates/discovery/manual-review-checklist.md`
   - Record session: `.artifacts/protocol-02/transcripts/YYYY-MM-DD-review-session.txt`

2. **Manual Gate Validation:**
   - For each gate, complete manual checklist:
     ```markdown
     ## Gate 1 Manual Validation
     - [ ] Business objectives documented (min 3)
     - [ ] User personas identified (min 2)
     - [ ] Success metrics defined (min 3 KPIs)
     - [ ] Client approval obtained (email/signature)
     ```
   - Store completed checklists: `.artifacts/protocol-02/manual-gate-[N]-checklist.md`

3. **Evidence Collection:**
   - Obtain written confirmation via email → save as `.artifacts/protocol-02/transcripts/client-approval-YYYY-MM-DD.eml`
   - Scan signed documents → save as `.artifacts/protocol-02/transcripts/signed-discovery-recap-YYYY-MM-DD.pdf`
   - Log all manual validations: `.artifacts/protocol-02/manual-validation-log.md`

4. **Manual Evidence Aggregation:**
   - Create evidence manifest manually: `.artifacts/protocol-02/manual-evidence-manifest.json`
   - Use template from `.templates/discovery/evidence-manifest-template.json`
   - Include checksums (SHA-256) of all artifacts for integrity verification

---

## 10. HANDOFF CHECKLIST
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple checklist execution for protocol completion -->

### Pre-Handoff Validation:

1. **`[MUST]` Validate protocol completion:**
   * **Action:** Verify all prerequisites were met and workflow steps completed
   * **Evidence:** Completed checklist in protocol execution log
   * **Validation:** All items checked
   
   **Checklist:**
   - [ ] All prerequisites were met
   - [ ] All workflow steps completed successfully
   - [ ] All quality gates passed (or waivers documented)
   - [ ] All evidence artifacts captured and stored
   - [ ] All integration outputs generated
   - [ ] All automation hooks executed successfully
   - [ ] Communication log complete

### Handoff to Protocol 03:

1. **`[MUST]` Execute protocol handoff:**
   * **Action:** Package evidence and trigger Protocol 03
   * **Evidence:** Handoff confirmation in execution log
   * **Validation:** Protocol 03 acknowledges receipt
   
   **[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 03: Project Brief Creation
   
   **Evidence Package:**
   - `client-discovery-form.md` - Validated functional requirements
   - `discovery-recap.md` - Client-approved discovery summary
   
   **Execution:**
   ```bash
   # Trigger next protocol
   @apply .cursor/ai-driven-workflow/03-project-brief-creation.md
   ```

---

## 11. EVIDENCE SUMMARY
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Defining standards for evidence collection and quality metrics -->

### Learning and Improvement Mechanisms

**[STRICT]** All artifacts must generate feedback for continuous improvement:

**Feedback Collection:** All artifacts generate feedback for continuous improvement. Quality gate outcomes tracked in historical logs for pattern analysis and threshold calibration.

**Improvement Tracking:** Protocol execution metrics monitored quarterly. Template evolution logged with before/after comparisons. Knowledge base updated after every 5 executions.

**Knowledge Integration:** Execution patterns cataloged in institutional knowledge base. Best practices documented and shared across teams. Common blockers maintained with proven resolutions.

**Adaptation:** Protocol adapts based on project context (complexity, domain, constraints). Quality gate thresholds adjust dynamically based on risk tolerance. Workflow optimizations applied based on historical efficiency data.

### Generated Artifacts:

**[STRICT]** The following artifacts must be generated and validated:

| Artifact | Location | Purpose | Consumer | Verification Owner |
|----------|----------|---------|----------|-------------------|
| `client-context-notes.md` | `.artifacts/protocol-02/` | Business objectives and goals | Protocol 03 | Solutions Architect |
| `client-discovery-form.md` | `.artifacts/protocol-02/` | Structured feature list | Protocol 03 | Product Owner |
| `scope-clarification.md` | `.artifacts/protocol-02/` | Technical preferences and constraints | Protocol 03, 07 | Technical Lead |
| `timeline-discussion.md` | `.artifacts/protocol-02/` | Delivery expectations | Protocol 03, 08 | Account Manager |
| `communication-plan.md` | `.artifacts/protocol-02/` | Collaboration blueprint | Protocol 04 | Delivery Manager |
| `governance-map.md` | `.artifacts/protocol-02/` | Decision authority matrix | Protocol 04, 20 | Account Manager |
| `risk-log.md` | `.artifacts/protocol-02/` | Identified risks and mitigation | Protocol 03, 08, 17 | Risk Manager |
| `discovery-recap.md` | `.artifacts/protocol-02/` | Client-approved summary | Protocol 03 | Account Manager |
| `gate1-validation.json` | `.artifacts/protocol-02/` | Gate 1 validation results | Protocol 04, CI/CD | Automation |
| `gate2-validation.json` | `.artifacts/protocol-02/` | Gate 2 validation results | Protocol 04, CI/CD | Automation |
| `gate3-validation.json` | `.artifacts/protocol-02/` | Gate 3 validation results | Protocol 04, CI/CD | Automation |
| `evidence-manifest.json` | `.artifacts/protocol-02/` | Complete evidence package | Protocol 03, 20, 22 | Protocol Orchestrator |

### Traceability Matrix

**Upstream Dependencies:**
- Input artifacts inherit from: Protocol 01, Protocol 04
- Configuration dependencies: `.templates/discovery/`, `scripts/script-registry.json`
- External dependencies: Client communication channel

**Downstream Consumers:**
- Output artifacts consumed by: Protocol 03, Protocol 04, Protocol 07, Protocol 08, Protocol 17, Protocol 20, Protocol 22
- Shared artifacts: `communication-plan.md`, `governance-map.md`, `risk-log.md`
- Archive requirements: 7-year retention per compliance

**Verification Chain:**
- Each artifact includes: SHA-256 checksum, timestamp, verified_by field
- Verification procedure: Run `scripts/validate_protocol_handoffs.py`
- Audit trail: All artifact modifications logged in protocol execution log

### Archival and Traceability

**Evidence Manifest Schema:**
```json
{
  "protocol_id": "02",
  "execution_timestamp": "2024-05-10T14:30:00Z",
  "artifacts": [
    {
      "name": "client-discovery-form.md",
      "path": ".artifacts/protocol-02/client-discovery-form.md",
      "sha256": "abc123...",
      "created": "2024-05-10T14:15:00Z",
      "verified_by": "product-owner@example.com",
      "verification_timestamp": "2024-05-10T14:20:00Z"
    }
  ],
  "quality_gates": [
    {"gate_id": "gate1", "status": "pass", "score": 0.97, "timestamp": "2024-05-10T14:25:00Z"},
    {"gate_id": "gate2", "status": "pass", "score": 0.92, "timestamp": "2024-05-10T14:28:00Z"}
  ],
  "traceability_links": {
    "upstream_protocols": ["01"],
    "downstream_protocols": ["03", "04"],
    "related_artifacts": [".artifacts/protocol-01/PROPOSAL.md"]
  }
}
```

**Archival Procedure:**
1. Generate evidence manifest: `python scripts/aggregate_evidence_02.py --validate-integrity`
2. Create archive bundle: `.artifacts/protocol-02/archive/protocol-02-YYYY-MM-DD-HHmm.tar.gz`
3. Upload to long-term storage: `s3://project-archives/protocol-02/[project-id]/[timestamp]/`
4. Record archive location in project ledger: `.artifacts/project-ledger.json`

**Retention Policy:**
- Active project artifacts: Retain in `.artifacts/protocol-02/` until project closure
- Archived artifacts: Retain for 7 years per compliance requirements
- PII-containing artifacts: Purge after 30 days post-project completion (per GDPR)

### Quality Metrics:

**[STRICT]** Track and maintain the following quality metrics:

| Metric | Target | Baseline | Current | Status | Trend |
|--------|--------|----------|---------|--------|-------|
| Gate 1 Pass Rate | ≥ 95% | 0.88 | 0.92 | ⚠️ Warning | ↗️ +4% |
| Gate 2 Pass Rate | ≥ 90% | 0.83 | 0.87 | ⚠️ Warning | ↗️ +5% |
| Gate 3 Pass Rate | ≥ 95% | 0.88 | 0.91 | ⚠️ Warning | ↗️ +3% |
| Gate 4 Pass Rate | ≥ 95% | 0.95 | 0.96 | ✅ Pass | ↗️ +1% |
| Evidence Completeness | 100% | 0.94 | 0.98 | ⚠️ Warning | ↗️ +4% |
| Integration Integrity | 100% | 0.97 | 0.99 | ⚠️ Warning | ↗️ +2% |
| Client Satisfaction | ≥ 4.5/5 | 4.2 | 4.6 | ✅ Pass | ↗️ +0.4 |
| Discovery Duration (days) | ≤ 5 | 6.5 | 4.2 | ✅ Pass | ↗️ -2.3 |

**Quality Gate History:** `.artifacts/protocol-02/gate-history.json`

### Downstream Handoff Verification

**Verification Checklist for Protocol 03:**
- [ ] `client-discovery-form.md` contains ≥5 MVP features with acceptance criteria
- [ ] `scope-clarification.md` includes tech stack preferences and constraints
- [ ] `discovery-recap.md` has client approval timestamp and signature
- [ ] All quality gates passed or have documented waivers
- [ ] Evidence manifest generated and archived

**Verification Procedure:**
```bash
# Run downstream handoff verification
python scripts/validate_protocol_handoffs.py \
  --from-protocol 02 \
  --to-protocol 03 \
  --output .artifacts/protocol-02/handoff-verification.json

# Exit code 0 = ready for handoff, 1 = missing artifacts, 2 = quality gate failures
```

**Verification Owner:** Protocol Orchestrator (automated) + Account Manager (final approval)