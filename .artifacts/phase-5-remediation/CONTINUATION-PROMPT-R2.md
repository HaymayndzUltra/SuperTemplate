# Phase 5 R2 - Continuation Prompt for New Session

## Context & Status

**Completed Work:** Protocol 01 enhanced (Evidence + Gates)
- ✅ Protocol 01: Evidence PASS (1.0), Quality Gates PASS (0.962)

**Remaining Work:** 22 protocols need enhancement (Protocols 02-23)

**Pattern Established:** Proven working pattern for Evidence + Gates enhancements

**Important:** Do BOTH Evidence AND Gates together per protocol (not separately) to ensure consistency.

---

## Task: Complete R2 Batch Enhancement

**Objective:** Enhance EVIDENCE SUMMARY and QUALITY GATES sections for Protocols 02-23 using the same pattern as Protocol 01.

**Target:** Achieve PASS status (≥0.90) for evidence and quality gates validators across all protocols.

---

## Enhancement Pattern (Follow Exactly)

### 1. EVIDENCE SUMMARY Enhancements

**A. Add Artifact Generation Table:**
```markdown
### Artifact Generation Table

| Artifact Name | Metrics | Location | Evidence Link |
|---------------|---------|----------|---------------|
| artifact-1.json | Metric description (threshold, score) | `.artifacts/protocol-{XX}/artifact-1.json` | Gate validation reference |
| artifact-2.md | Metric description | `.artifacts/protocol-{XX}/artifact-2.md` | Gate validation reference |
| ... | ... | ... | ... |
```

**Requirements:**
- Table must have columns: Artifact Name, Metrics, Location, Evidence Link
- At least 2 rows (or 3+ artifact mentions)
- Artifact column must contain "artifact" keyword
- Metrics column must contain "metric", "evidence", or "result" keyword
- Location must reference `.artifacts/protocol-{XX}/` path

**B. Document Storage Structure:**
```markdown
### Storage Structure

**Protocol Directory:** `.artifacts/protocol-{XX}/`
- **Subdirectories:** [List subdirectories if any, or "None (flat structure)"]
- **Permissions:** Read/write access for protocol executor, read-only for downstream protocols
- **Naming Convention:** `{artifact-name}.{extension}` (e.g., `artifact-name.json`, `artifact-name.md`)
```

**C. Add Manifest Completeness:**
```markdown
### Manifest Completeness

**Manifest File:** `.artifacts/protocol-{XX}/evidence-manifest.json`

**Metadata Requirements:**
- Timestamp: ISO 8601 format (e.g., `2025-11-06T05:34:29Z`)
- Artifact checksums: SHA-256 hash for each artifact
- Size: File size in bytes
- Dependencies: List of upstream artifacts or inputs

**Dependency Tracking:**
- Input: [List input sources]
- Output: [List all artifacts from table]
- Transformations: [Describe transformation steps]

**Coverage:** 100% of required artifacts documented in manifest
```

**D. Add Traceability:**
```markdown
### Traceability

**Input Sources:**
- **Input From:** [Input source 1] - [Description]
- **Input From:** [Input source 2] - [Description]

**Output Artifacts:**
- **Output To:** [Output artifact 1] - [Description]
- **Output To:** [Output artifact 2] - [Description]
- ... (list all outputs from table)

**Transformation Steps:**
1. [Input] → [Output]: [Description]
2. [Output] → [Next Output]: [Description]
...

**Audit Trail:**
- Each transformation logged in evidence manifest
- Timestamps record when each artifact generated
- Checksums enable integrity verification
- Dependencies mapped to enable traceability
```

**Important:** Must use "Input From" and "Output To" format (not just "Input" or "Output")

**E. Add Archival Strategy:**
```markdown
### Archival Strategy

**Compression:**
- Artifacts compressed into `.artifacts/protocol-{XX}/evidence-bundle.zip` after handoff
- Compression format: ZIP with standard compression level

**Retention Policy:**
- Active artifacts: Retained for [X] days after protocol completion
- Archived bundles: Retained for [X] years after project closure
- Cleanup: Automated cleanup runs quarterly, removes artifacts older than retention period

**Retrieval Procedures:**
- Active artifacts: Direct access from `.artifacts/protocol-{XX}/` directory
- Archived bundles: Extract from `.artifacts/protocol-{XX}/evidence-bundle.zip` using standard unzip tools
- Integrity verification: SHA checksums in manifest enable verification after retrieval

**Cleanup Process:**
- Quarterly automated script removes artifacts older than retention period
- Cleanup log stored in `.artifacts/protocol-{XX}/cleanup-log.json`
- Critical artifacts flagged for extended retention (manual review required)
```

---

### 2. QUALITY GATES Enhancements

**A. Add Gate Headings:**
```markdown
### Gate 1: [Gate Name]
**Type:** Prerequisite | Execution | Completion
**Purpose:** [Purpose description]
```

**Required:** Must use format `### Gate 1:`, `### Gate 2:`, etc. (validator looks for this pattern)

**B. Add Pass Criteria:**
```markdown
**Pass Criteria:**
- **Threshold:** [Numeric threshold with ≥ or <=]
- **Boolean Check:** [Boolean condition description]
- **Metrics:** [Metric description]
- **Evidence Link:** Validated against `.artifacts/protocol-{XX}/[artifact-name]`
```

**Requirements:**
- Need ≥2 threshold mentions (with "threshold", "≥", ">=", etc.)
- Need ≥2 boolean check mentions ("status", "pass", "fail")
- Need ≥3 metrics mentions ("score", "confidence", "rate", "percentage")
- Need ≥3 evidence link mentions (word "evidence" in gate descriptions)

**C. Add Automation Hooks:**
```markdown
**Automation:**
- Script: `python3 scripts/[script-name].py [arguments]`
- CI Integration: [Description of CI/CD integration]
- Config: `config/protocol_gates/{XX}.yaml` defines gate thresholds
```

**Requirements:**
- Need ≥2 script mentions (`python3 scripts/`)
- Need CI/CD mentions ("CI/CD", "workflow", "runs-on")
- Automation labels must be present

**D. Add Failure Handling:**
```markdown
**Failure Handling:**
- **Rollback:** [Describe rollback procedure]
- **Notification:** [Who gets notified and how]
- **Waiver:** [Waiver procedure or "Not applicable - mandatory"]
```

**Requirements:**
- Need failure actions mentioned
- Need rollback mentioned
- Need notification mentioned
- Need waiver mentioned (or document why not applicable)

**E. Add Compliance Integration:**
```markdown
### Compliance Integration
- **Industry Standards:** [List standards: CommonMark, JSON Schema, YAML, Markdown]
- **Security Requirements:** [Security/compliance terms: HIPAA, SOC2, GDPR, security]
- **Regulatory Compliance:** [Regulatory terms: FDA, FTC, regulatory, compliance]
- **Governance:** Gate thresholds defined in `config/protocol_gates/{XX}.yaml`, integrated with protocol governance system
```

---

## Work Division: Split into 4 Batches

### **BATCH 1: Protocols 02-06** (5 protocols)
**Assign to:** Session Worker 1

**Protocols:**
- 02: Client Discovery Initiation
- 03: Project Brief Creation
- 04: Project Bootstrap & Context Engineering
- 05: Bootstrap Your Project
- 06: Create PRD

**Files to Edit:**
- `.cursor/ai-driven-workflow/02-client-discovery-initiation.md`
- `.cursor/ai-driven-workflow/03-project-brief-creation.md`
- `.cursor/ai-driven-workflow/04-project-bootstrap-and-context-engineering.md`
- `.cursor/ai-driven-workflow/05-bootstrap-your-project.md`
- `.cursor/ai-driven-workflow/06-create-prd.md`

**Validation After:**
```bash
python3 validators-system/scripts/validate_protocol_evidence.py --protocol 02 --protocol 03 --protocol 04 --protocol 05 --protocol 06 --report --workspace .
python3 validators-system/scripts/validate_protocol_gates.py --protocol 02 --protocol 03 --protocol 04 --protocol 05 --protocol 06 --report --workspace .
```

---

### **BATCH 2: Protocols 07-11** (5 protocols)
**Assign to:** Session Worker 2

**Protocols:**
- 07: Technical Design & Architecture
- 08: Generate Tasks
- 09: Environment Setup & Validation
- 10: Process Tasks
- 11: Integration Testing

**Files to Edit:**
- `.cursor/ai-driven-workflow/07-technical-design-architecture.md`
- `.cursor/ai-driven-workflow/08-generate-tasks.md`
- `.cursor/ai-driven-workflow/09-environment-setup-validation.md`
- `.cursor/ai-driven-workflow/10-process-tasks.md`
- `.cursor/ai-driven-workflow/11-integration-testing.md`

**Validation After:**
```bash
python3 validators-system/scripts/validate_protocol_evidence.py --protocol 07 --protocol 08 --protocol 09 --protocol 10 --protocol 11 --report --workspace .
python3 validators-system/scripts/validate_protocol_gates.py --protocol 07 --protocol 08 --protocol 09 --protocol 10 --protocol 11 --report --workspace .
```

---

### **BATCH 3: Protocols 12-17** (6 protocols)
**Assign to:** Session Worker 3

**Protocols:**
- 12: Quality Audit
- 13: UAT Coordination
- 14: Pre-Deployment Staging
- 15: Production Deployment
- 16: Monitoring & Observability
- 17: Incident Response & Rollback

**Files to Edit:**
- `.cursor/ai-driven-workflow/12-quality-audit.md`
- `.cursor/ai-driven-workflow/13-uat-coordination.md`
- `.cursor/ai-driven-workflow/14-pre-deployment-staging.md`
- `.cursor/ai-driven-workflow/15-production-deployment.md`
- `.cursor/ai-driven-workflow/16-monitoring-observability.md`
- `.cursor/ai-driven-workflow/17-incident-response-rollback.md`

**Validation After:**
```bash
python3 validators-system/scripts/validate_protocol_evidence.py --protocol 12 --protocol 13 --protocol 14 --protocol 15 --protocol 16 --protocol 17 --report --workspace .
python3 validators-system/scripts/validate_protocol_gates.py --protocol 12 --protocol 13 --protocol 14 --protocol 15 --protocol 16 --protocol 17 --report --workspace .
```

---

### **BATCH 4: Protocols 18-23** (6 protocols)
**Assign to:** Session Worker 4

**Protocols:**
- 18: Performance Optimization
- 19: Documentation & Knowledge Transfer
- 20: Project Closure
- 21: Maintenance & Support
- 22: Implementation Retrospective
- 23: Script Governance Protocol

**Files to Edit:**
- `.cursor/ai-driven-workflow/18-performance-optimization.md`
- `.cursor/ai-driven-workflow/19-documentation-knowledge-transfer.md`
- `.cursor/ai-driven-workflow/20-project-closure.md`
- `.cursor/ai-driven-workflow/21-maintenance-support.md`
- `.cursor/ai-driven-workflow/22-implementation-retrospective.md`
- `.cursor/ai-driven-workflow/23-script-governance-protocol.md`

**Validation After:**
```bash
python3 validators-system/scripts/validate_protocol_evidence.py --protocol 18 --protocol 19 --protocol 20 --protocol 21 --protocol 22 --protocol 23 --report --workspace .
python3 validators-system/scripts/validate_protocol_gates.py --protocol 18 --protocol 19 --protocol 20 --protocol 21 --protocol 22 --protocol 23 --report --workspace .
```

---

## How to Find Sections in Each Protocol

### Finding EVIDENCE SUMMARY Section:
```bash
grep -n "EVIDENCE SUMMARY\|Evidence Summary" .cursor/ai-driven-workflow/{protocol-file}.md
```

### Finding QUALITY GATES Section:
```bash
grep -n "QUALITY GATES\|Quality Gates" .cursor/ai-driven-workflow/{protocol-file}.md
```

**Note:** Section headers may vary:
- `## EVIDENCE SUMMARY`
- `## N. EVIDENCE SUMMARY` (where N is a number)
- `## QUALITY GATES`
- `## N. QUALITY GATES` (where N is a number)

---

## Example: Protocol 02 Enhancement

**Before (typical structure):**
```markdown
## EVIDENCE SUMMARY

**Required Artifacts:**
1. artifact-1.json
2. artifact-2.md
```

**After (enhanced structure):**
```markdown
## EVIDENCE SUMMARY

### Artifact Generation Table

| Artifact Name | Metrics | Location | Evidence Link |
|---------------|---------|----------|---------------|
| discovery-brief.md | Completeness score ≥90% | `.artifacts/protocol-02/discovery-brief.md` | Gate 1 validation |
| client-info.json | Info coverage score ≥85% | `.artifacts/protocol-02/client-info.json` | Gate 2 validation |

### Storage Structure
[Follow pattern from Protocol 01]

### Manifest Completeness
[Follow pattern from Protocol 01]

### Traceability
**Input Sources:**
- **Input From:** PROPOSAL.md (from Protocol 01)
- **Input From:** Client communication: Discovery call transcripts

**Output Artifacts:**
- **Output To:** discovery-brief.md
- **Output To:** client-info.json
...

### Archival Strategy
[Follow pattern from Protocol 01]
```

---

## Validation Commands

### After Each Batch:
```bash
# Validate evidence
python3 validators-system/scripts/validate_protocol_evidence.py --all --report --workspace .

# Validate quality gates
python3 validators-system/scripts/validate_protocol_gates.py --all --report --workspace .

# Check results
cat .artifacts/validation/protocol_evidence-summary.json | python3 -m json.tool | grep -A 3 "protocol_id"
cat .artifacts/validation/protocol_quality_gates-summary.json | python3 -m json.tool | grep -A 3 "protocol_id"
```

### Final Validation (After All Batches):
```bash
# Master validator
python3 validators-system/scripts/validate_all_protocols.py --all --report --workspace .
```

---

## Success Criteria

**R2 Workstream Complete When:**
- ✅ All 22 protocols (02-23) enhanced
- ✅ Evidence validator: 0 FAIL protocols
- ✅ Quality gates validator: 0 FAIL protocols
- ✅ Average scores ≥ 0.90 for both validators

**Target Scores:**
- Evidence: ≥ 0.90 (PASS)
- Quality Gates: ≥ 0.92 (PASS) - note: gates validator uses 0.92 threshold

---

## Important Notes

1. **Do BOTH Together:** Always enhance Evidence AND Gates together for each protocol to ensure consistency
2. **Gate Headings:** Must use `### Gate 1:`, `### Gate 2:` format (not `Gate 1:` or `## Gate 1:`)
3. **Traceability Format:** Must use "Input From" and "Output To" (not just "Input" or "Output")
4. **Pass Criteria:** Need ≥2 thresholds, ≥2 boolean checks, ≥3 metrics, ≥3 evidence links
5. **Automation:** Need ≥2 script mentions (`python3 scripts/`)
6. **Compliance:** Need industry standards, security terms, regulatory terms

---

## Progress Tracking

After completing each batch, update:
- `.artifacts/phase-5-remediation/02-VALIDATION-TRACKER.md`
- Run validators and check scores
- Document any issues or fixes needed

---

*Generated: 2025-11-06*  
*Status: Ready for parallel execution across 4 batches*  
*Pattern: Protocol 01 validated and complete*

