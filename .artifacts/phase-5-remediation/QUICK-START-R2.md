# 🔄 QUICK START: Phase 5 R2 Continuation

## Copy This Prompt for New Session:

```
I need to continue Phase 5 R2 batch remediation work. 

CONTEXT:
- Protocol 01 is already enhanced (pattern established)
- Remaining: Protocols 02-23 need Evidence + Gates enhancements
- Pattern: See .artifacts/phase-5-remediation/CONTINUATION-PROMPT-R2.md

IMPORTANT: Do BOTH Evidence AND Gates together per protocol (not separately).

TASK:
Enhance Protocols [BATCH NUMBER] ([PROTOCOL NUMBERS]) following the exact pattern from Protocol 01.

PATTERN GUIDE:
Read .artifacts/phase-5-remediation/CONTINUATION-PROMPT-R2.md for complete pattern details.

VALIDATION:
Run validators after completion and update tracker.

BATCH ASSIGNMENT:
See .artifacts/phase-5-remediation/BATCH-ASSIGNMENT-PROMPTS-R2.md for batch details.
```

---

## Batch Quick Reference

### Batch 1: Protocols 02-06 (5 protocols)
```
Work on: 02, 03, 04, 05, 06
Target: PASS (≥0.90) for evidence + gates
```

### Batch 2: Protocols 07-11 (5 protocols)
```
Work on: 07, 08, 09, 10, 11
Target: PASS (≥0.90) for evidence + gates
```

### Batch 3: Protocols 12-17 (6 protocols)
```
Work on: 12, 13, 14, 15, 16, 17
Target: PASS (≥0.90) for evidence + gates
```

### Batch 4: Protocols 18-23 (6 protocols)
```
Work on: 18, 19, 20, 21, 22, 23
Target: PASS (≥0.90) for evidence + gates
```

---

## Pattern Checklist (Apply to Each Protocol)

**EVIDENCE SUMMARY:**
- [ ] Add Artifact Generation Table (Artifact Name, Metrics, Location columns)
- [ ] Add Storage Structure section
- [ ] Add Manifest Completeness section
- [ ] Add Traceability section (use "Input From" and "Output To" format)
- [ ] Add Archival Strategy section (compression, retention, retrieval, cleanup)

**QUALITY GATES:**
- [ ] Convert gates to headings format (`### Gate 1:`, `### Gate 2:`, etc.)
- [ ] Add Pass Criteria to each gate (thresholds ≥2, metrics ≥3, evidence links ≥3)
- [ ] Add Automation section to each gate (script mentions ≥2, CI integration)
- [ ] Add Failure Handling to each gate (rollback, notification, waiver)
- [ ] Add Compliance Integration section (industry standards, security, regulatory, governance)

---

## Files You Need

**Pattern Reference:**
- `.artifacts/phase-5-remediation/CONTINUATION-PROMPT-R2.md` - Full pattern guide

**Example Pattern:**
- `.cursor/ai-driven-workflow/01-client-proposal-generation.md` - Enhanced example (Evidence PASS 1.0, Gates PASS 0.962)

**Tracker:**
- `.artifacts/phase-5-remediation/02-VALIDATION-TRACKER.md` - Update after each batch

---

## Critical Points

1. **Do BOTH Together:** Always enhance Evidence AND Gates together for each protocol
2. **Gate Headings:** Must use `### Gate 1:` format (not `Gate 1:` or `## Gate 1:`)
3. **Traceability:** Must use "Input From" and "Output To" format
4. **Evidence Links:** Gates must reference evidence artifacts from Evidence Summary table

---

*Ready for parallel execution across 4 batches*

