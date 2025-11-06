# 🚀 HOW TO USE R2 PROMPTS - STEP BY STEP GUIDE

## 📋 Quick Start

### Option 1: Single Session (Complete Batches One by One)

**Step 1:** Copy this prompt for NEW SESSION:

```
I need to continue Phase 5 R2 batch remediation.

CONTEXT:
- Protocol 01 already enhanced (Evidence PASS 1.0, Gates PASS 0.962)
- Pattern established - see Protocol 01 as reference
- Working on Batch 1: Protocols 02-06

TASK:
Enhance Protocols 02-06 following the exact pattern from Protocol 01.
Do BOTH Evidence AND Gates together for each protocol (not separately).

PATTERN GUIDE:
Read .artifacts/phase-5-remediation/CONTINUATION-PROMPT-R2.md

FILES TO ENHANCE:
- 02-client-discovery-initiation.md
- 03-project-brief-creation.md
- 04-project-bootstrap-and-context-engineering.md
- 05-bootstrap-your-project.md
- 06-create-prd.md

VALIDATION AFTER:
python3 validators-system/scripts/validate_protocol_evidence.py --protocol 02 --protocol 03 --protocol 04 --protocol 05 --protocol 06 --report --workspace .
python3 validators-system/scripts/validate_protocol_gates.py --protocol 02 --protocol 03 --protocol 04 --protocol 05 --protocol 06 --report --workspace .
```

**Step 2:** After Batch 1 complete, move to Batch 2:

```
Continue R2 Batch 2: Protocols 07-11
[Same format as above, just change protocol numbers]
```

---

### Option 2: Parallel Sessions (4 Workers Simultaneously)

**Worker 1** - Copy this prompt:
```
I need to continue Phase 5 R2 batch remediation.

CONTEXT:
- Protocol 01 already enhanced (Evidence PASS 1.0, Gates PASS 0.962)
- Pattern established - see Protocol 01 as reference
- Working on Batch 1: Protocols 02-06

TASK:
Enhance Protocols 02-06 following the exact pattern from Protocol 01.
Do BOTH Evidence AND Gates together for each protocol (not separately).

PATTERN GUIDE:
Read .artifacts/phase-5-remediation/CONTINUATION-PROMPT-R2.md

FILES TO ENHANCE:
- 02-client-discovery-initiation.md
- 03-project-brief-creation.md
- 04-project-bootstrap-and-context-engineering.md
- 05-bootstrap-your-project.md
- 06-create-prd.md

VALIDATION AFTER:
python3 validators-system/scripts/validate_protocol_evidence.py --protocol 02 --protocol 03 --protocol 04 --protocol 05 --protocol 06 --report --workspace .
python3 validators-system/scripts/validate_protocol_gates.py --protocol 02 --protocol 03 --protocol 04 --protocol 05 --protocol 06 --report --workspace .
```

**Worker 2** - Copy this prompt:
```
I need to continue Phase 5 R2 batch remediation.

CONTEXT:
- Protocol 01 already enhanced (Evidence PASS 1.0, Gates PASS 0.962)
- Pattern established - see Protocol 01 as reference
- Working on Batch 2: Protocols 07-11

TASK:
Enhance Protocols 07-11 following the exact pattern from Protocol 01.
Do BOTH Evidence AND Gates together for each protocol (not separately).

PATTERN GUIDE:
Read .artifacts/phase-5-remediation/CONTINUATION-PROMPT-R2.md

FILES TO ENHANCE:
- 07-technical-design-architecture.md
- 08-generate-tasks.md
- 09-environment-setup-validation.md
- 10-process-tasks.md
- 11-integration-testing.md

VALIDATION AFTER:
python3 validators-system/scripts/validate_protocol_evidence.py --protocol 07 --protocol 08 --protocol 09 --protocol 10 --protocol 11 --report --workspace .
python3 validators-system/scripts/validate_protocol_gates.py --protocol 07 --protocol 08 --protocol 09 --protocol 10 --protocol 11 --report --workspace .
```

**Worker 3** - Copy this prompt:
```
I need to continue Phase 5 R2 batch remediation.

CONTEXT:
- Protocol 01 already enhanced (Evidence PASS 1.0, Gates PASS 0.962)
- Pattern established - see Protocol 01 as reference
- Working on Batch 3: Protocols 12-17

TASK:
Enhance Protocols 12-17 following the exact pattern from Protocol 01.
Do BOTH Evidence AND Gates together for each protocol (not separately).

PATTERN GUIDE:
Read .artifacts/phase-5-remediation/CONTINUATION-PROMPT-R2.md

FILES TO ENHANCE:
- 12-quality-audit.md
- 13-uat-coordination.md
- 14-pre-deployment-staging.md
- 15-production-deployment.md
- 16-monitoring-observability.md
- 17-incident-response-rollback.md

VALIDATION AFTER:
python3 validators-system/scripts/validate_protocol_evidence.py --protocol 12 --protocol 13 --protocol 14 --protocol 15 --protocol 16 --protocol 17 --report --workspace .
python3 validators-system/scripts/validate_protocol_gates.py --protocol 12 --protocol 13 --protocol 14 --protocol 15 --protocol 16 --protocol 17 --report --workspace .
```

**Worker 4** - Copy this prompt:
```
I need to continue Phase 5 R2 batch remediation.

CONTEXT:
- Protocol 01 already enhanced (Evidence PASS 1.0, Gates PASS 0.962)
- Pattern established - see Protocol 01 as reference
- Working on Batch 4: Protocols 18-23

TASK:
Enhance Protocols 18-23 following the exact pattern from Protocol 01.
Do BOTH Evidence AND Gates together for each protocol (not separately).

PATTERN GUIDE:
Read .artifacts/phase-5-remediation/CONTINUATION-PROMPT-R2.md

FILES TO ENHANCE:
- 18-performance-optimization.md
- 19-documentation-knowledge-transfer.md
- 20-project-closure.md
- 21-maintenance-support.md
- 22-implementation-retrospective.md
- 23-script-governance-protocol.md

VALIDATION AFTER:
python3 validators-system/scripts/validate_protocol_evidence.py --protocol 18 --protocol 19 --protocol 20 --protocol 21 --protocol 22 --protocol 23 --report --workspace .
python3 validators-system/scripts/validate_protocol_gates.py --protocol 18 --protocol 19 --protocol 20 --protocol 21 --protocol 22 --protocol 23 --report --workspace .
```

---

## 📝 What Each Worker Needs to Do

### 1. Read the Pattern Guide
```bash
# Read this first to understand what to add
cat .artifacts/phase-5-remediation/CONTINUATION-PROMPT-R2.md
```

### 2. Check Protocol 01 Example
```bash
# Reference Protocol 01 to see the pattern
grep -A 50 "## EVIDENCE SUMMARY" .cursor/ai-driven-workflow/01-client-proposal-generation.md
grep -A 50 "## QUALITY GATES" .cursor/ai-driven-workflow/01-client-proposal-generation.md
```

### 3. Find Sections in Each Protocol
```bash
# Find EVIDENCE SUMMARY section
grep -n "EVIDENCE SUMMARY\|Evidence Summary" .cursor/ai-driven-workflow/02-client-discovery-initiation.md

# Find QUALITY GATES section
grep -n "QUALITY GATES\|Quality Gates" .cursor/ai-driven-workflow/02-client-discovery-initiation.md
```

### 4. Enhance Each Protocol
For each protocol file:
- **Enhance EVIDENCE SUMMARY section:**
  - Add Artifact Generation Table (if missing or incomplete)
  - Add Storage Structure subsection
  - Add Manifest Completeness subsection
  - Add Traceability subsection (use "Input From" and "Output To" format)
  - Add Archival Strategy subsection

- **Enhance QUALITY GATES section:**
  - Convert gates to heading format (`### Gate 1:`, `### Gate 2:`, etc.)
  - Add Pass Criteria to each gate (thresholds ≥2, metrics ≥3, evidence links ≥3)
  - Add Automation section to each gate (script mentions ≥2, CI integration)
  - Add Failure Handling to each gate (rollback, notification, waiver)
  - Add Compliance Integration section at end

### 5. Validate After Each Protocol
```bash
# Single protocol validation
python3 validators-system/scripts/validate_protocol_evidence.py --protocol 02 --report --workspace .
python3 validators-system/scripts/validate_protocol_gates.py --protocol 02 --report --workspace .

# Check results
cat .artifacts/validation/protocol-02-evidence.json | python3 -m json.tool | grep -A 5 "validation_status"
cat .artifacts/validation/protocol-02-quality-gates.json | python3 -m json.tool | grep -A 5 "validation_status"
```

### 6. Update Tracker
```bash
# Edit this file after each batch
vim .artifacts/phase-5-remediation/02-VALIDATION-TRACKER.md
# Or use your preferred editor
```

---

## 🔍 Key Checklist Per Protocol

### EVIDENCE SUMMARY Must Have:
- [ ] Artifact Generation Table with columns: Artifact Name, Metrics, Location, Evidence Link
- [ ] Storage Structure section (protocol directory, subdirectories, permissions, naming)
- [ ] Manifest Completeness section (metadata, dependencies, coverage)
- [ ] Traceability section (use "Input From" and "Output To" format)
- [ ] Archival Strategy section (compression, retention, retrieval, cleanup)

### QUALITY GATES Must Have:
- [ ] Gate headings in format `### Gate 1:`, `### Gate 2:`, etc.
- [ ] Each gate has Pass Criteria (thresholds ≥2, metrics ≥3, evidence links ≥3)
- [ ] Each gate has Automation section (script mentions ≥2, CI integration)
- [ ] Each gate has Failure Handling (rollback, notification, waiver)
- [ ] Compliance Integration section at end (industry standards, security, regulatory, governance)

---

## ✅ Success Criteria

After enhancement, validator should show:
- **Evidence:** PASS (score ≥ 0.90)
- **Quality Gates:** PASS (score ≥ 0.92)

If FAIL or WARNING:
- Check validator JSON output for specific issues
- Fix issues and re-validate
- Repeat until PASS

---

## 📞 Quick Reference Commands

```bash
# Validate single protocol
python3 validators-system/scripts/validate_protocol_evidence.py --protocol XX --report --workspace .
python3 validators-system/scripts/validate_protocol_gates.py --protocol XX --report --workspace .

# Validate multiple protocols
python3 validators-system/scripts/validate_protocol_evidence.py --protocol 02 --protocol 03 --protocol 04 --report --workspace .
python3 validators-system/scripts/validate_protocol_gates.py --protocol 02 --protocol 03 --protocol 04 --report --workspace .

# Validate all protocols
python3 validators-system/scripts/validate_protocol_evidence.py --all --report --workspace .
python3 validators-system/scripts/validate_protocol_gates.py --all --report --workspace .

# Check validation results
cat .artifacts/validation/protocol_evidence-summary.json | python3 -m json.tool | grep -A 3 "protocol_id"
cat .artifacts/validation/protocol_quality_gates-summary.json | python3 -m json.tool | grep -A 3 "protocol_id"
```

---

## 🚨 Common Issues & Fixes

### Issue: "Evidence summary should include a table of artifacts and outcomes"
**Fix:** Add Artifact Generation Table with proper columns

### Issue: "Traceability gaps: inputs, outputs"
**Fix:** Use "Input From" and "Output To" format (not just "Input" or "Output")

### Issue: "No gate headings defined"
**Fix:** Convert gates to `### Gate 1:`, `### Gate 2:` format (not `Gate 1:` or `## Gate 1:`)

### Issue: "Numeric thresholds missing for gates"
**Fix:** Add thresholds with ≥ or <= symbols in Pass Criteria section

### Issue: "Document executable automation commands for gates"
**Fix:** Add script mentions in format `python3 scripts/script-name.py`

---

## 📚 Reference Files

- **Pattern Guide:** `.artifacts/phase-5-remediation/CONTINUATION-PROMPT-R2.md`
- **Batch Prompts:** `.artifacts/phase-5-remediation/BATCH-ASSIGNMENT-PROMPTS-R2.md`
- **Quick Start:** `.artifacts/phase-5-remediation/QUICK-START-R2.md`
- **Example:** `.cursor/ai-driven-workflow/01-client-proposal-generation.md` (Protocol 01)

---

*Ready to use! Just copy the appropriate prompt above and start a new session.*

