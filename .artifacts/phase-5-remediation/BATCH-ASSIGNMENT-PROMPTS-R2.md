# Phase 5 R2 - Batch Assignment Prompts

## PROMPT FOR SESSION WORKER 1 (Batch 1: Protocols 02-06)

**Task:** Enhance EVIDENCE SUMMARY and QUALITY GATES sections for Protocols 02-06.

**IMPORTANT:** Do BOTH Evidence AND Gates together for each protocol (not separately).

**Instructions:**
1. Read `.artifacts/phase-5-remediation/CONTINUATION-PROMPT-R2.md` for full pattern details
2. Enhance these 5 protocols:
   - 02: `02-client-discovery-initiation.md`
   - 03: `03-project-brief-creation.md`
   - 04: `04-project-bootstrap-and-context-engineering.md`
   - 05: `05-bootstrap-your-project.md`
   - 06: `06-create-prd.md`
3. Apply the exact pattern from Protocol 01
4. For each protocol:
   - First enhance EVIDENCE SUMMARY section
   - Then enhance QUALITY GATES section (gates reference evidence artifacts)
   - Ensure consistency between Evidence and Gates
5. Run validators after completion
6. Update `.artifacts/phase-5-remediation/02-VALIDATION-TRACKER.md`

**Validation:**
```bash
python3 validators-system/scripts/validate_protocol_evidence.py --protocol 02 --protocol 03 --protocol 04 --protocol 05 --protocol 06 --report --workspace .
python3 validators-system/scripts/validate_protocol_gates.py --protocol 02 --protocol 03 --protocol 04 --protocol 05 --protocol 06 --report --workspace .
```

**Expected Output:** All 5 protocols should show PASS (≥0.90) for evidence and quality gates validators.

---

## PROMPT FOR SESSION WORKER 2 (Batch 2: Protocols 07-11)

**Task:** Enhance EVIDENCE SUMMARY and QUALITY GATES sections for Protocols 07-11.

**IMPORTANT:** Do BOTH Evidence AND Gates together for each protocol (not separately).

**Instructions:**
1. Read `.artifacts/phase-5-remediation/CONTINUATION-PROMPT-R2.md` for full pattern details
2. Enhance these 5 protocols:
   - 07: `07-technical-design-architecture.md`
   - 08: `08-generate-tasks.md`
   - 09: `09-environment-setup-validation.md`
   - 10: `10-process-tasks.md`
   - 11: `11-integration-testing.md`
3. Apply the exact pattern from Protocol 01
4. For each protocol:
   - First enhance EVIDENCE SUMMARY section
   - Then enhance QUALITY GATES section (gates reference evidence artifacts)
   - Ensure consistency between Evidence and Gates
5. Run validators after completion
6. Update `.artifacts/phase-5-remediation/02-VALIDATION-TRACKER.md`

**Validation:**
```bash
python3 validators-system/scripts/validate_protocol_evidence.py --protocol 07 --protocol 08 --protocol 09 --protocol 10 --protocol 11 --report --workspace .
python3 validators-system/scripts/validate_protocol_gates.py --protocol 07 --protocol 08 --protocol 09 --protocol 10 --protocol 11 --report --workspace .
```

**Expected Output:** All 5 protocols should show PASS (≥0.90) for evidence and quality gates validators.

---

## PROMPT FOR SESSION WORKER 3 (Batch 3: Protocols 12-17)

**Task:** Enhance EVIDENCE SUMMARY and QUALITY GATES sections for Protocols 12-17.

**IMPORTANT:** Do BOTH Evidence AND Gates together for each protocol (not separately).

**Instructions:**
1. Read `.artifacts/phase-5-remediation/CONTINUATION-PROMPT-R2.md` for full pattern details
2. Enhance these 6 protocols:
   - 12: `12-quality-audit.md`
   - 13: `13-uat-coordination.md`
   - 14: `14-pre-deployment-staging.md`
   - 15: `15-production-deployment.md`
   - 16: `16-monitoring-observability.md`
   - 17: `17-incident-response-rollback.md`
3. Apply the exact pattern from Protocol 01
4. For each protocol:
   - First enhance EVIDENCE SUMMARY section
   - Then enhance QUALITY GATES section (gates reference evidence artifacts)
   - Ensure consistency between Evidence and Gates
5. Run validators after completion
6. Update `.artifacts/phase-5-remediation/02-VALIDATION-TRACKER.md`

**Validation:**
```bash
python3 validators-system/scripts/validate_protocol_evidence.py --protocol 12 --protocol 13 --protocol 14 --protocol 15 --protocol 16 --protocol 17 --report --workspace .
python3 validators-system/scripts/validate_protocol_gates.py --protocol 12 --protocol 13 --protocol 14 --protocol 15 --protocol 16 --protocol 17 --report --workspace .
```

**Expected Output:** All 6 protocols should show PASS (≥0.90) for evidence and quality gates validators.

---

## PROMPT FOR SESSION WORKER 4 (Batch 4: Protocols 18-23)

**Task:** Enhance EVIDENCE SUMMARY and QUALITY GATES sections for Protocols 18-23.

**IMPORTANT:** Do BOTH Evidence AND Gates together for each protocol (not separately).

**Instructions:**
1. Read `.artifacts/phase-5-remediation/CONTINUATION-PROMPT-R2.md` for full pattern details
2. Enhance these 6 protocols:
   - 18: `18-performance-optimization.md`
   - 19: `19-documentation-knowledge-transfer.md`
   - 20: `20-project-closure.md`
   - 21: `21-maintenance-support.md`
   - 22: `22-implementation-retrospective.md`
   - 23: `23-script-governance-protocol.md`
3. Apply the exact pattern from Protocol 01
4. For each protocol:
   - First enhance EVIDENCE SUMMARY section
   - Then enhance QUALITY GATES section (gates reference evidence artifacts)
   - Ensure consistency between Evidence and Gates
5. Run validators after completion
6. Update `.artifacts/phase-5-remediation/02-VALIDATION-TRACKER.md`

**Validation:**
```bash
python3 validators-system/scripts/validate_protocol_evidence.py --protocol 18 --protocol 19 --protocol 20 --protocol 21 --protocol 22 --protocol 23 --report --workspace .
python3 validators-system/scripts/validate_protocol_gates.py --protocol 18 --protocol 19 --protocol 20 --protocol 21 --protocol 22 --protocol 23 --report --workspace .
```

**Expected Output:** All 6 protocols should show PASS (≥0.90) for evidence and quality gates validators.

---

## After All Batches Complete

**Final Validation:**
```bash
# Run all validators
python3 validators-system/scripts/validate_protocol_evidence.py --all --report --workspace .
python3 validators-system/scripts/validate_protocol_gates.py --all --report --workspace .
python3 validators-system/scripts/validate_all_protocols.py --all --report --workspace .

# Generate final summary
echo "✅ R2 Workstream Complete!" > .artifacts/phase-5-remediation/R2-COMPLETE.md
```

**Success Criteria:**
- ✅ All 23 protocols enhanced
- ✅ Evidence validator: 0 FAIL protocols
- ✅ Quality gates validator: 0 FAIL protocols
- ✅ Average scores ≥ 0.90 for both validators

---

*Generated: 2025-11-06*  
*Ready for parallel execution*

