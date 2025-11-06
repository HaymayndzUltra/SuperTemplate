# Phase 5 R1 - Batch Assignment Prompts

## PROMPT FOR SESSION WORKER 1 (Batch 1: Protocols 07-10)

**Task:** Enhance HANDOFF CHECKLIST and COMMUNICATION PROTOCOLS sections for Protocols 07-10.

**Instructions:**
1. Read `.artifacts/phase-5-remediation/CONTINUATION-PROMPT-R1.md` for full pattern details
2. Enhance these 4 protocols:
   - 07: `07-technical-design-architecture.md`
   - 08: `08-generate-tasks.md`
   - 09: `09-environment-setup-validation.md`
   - 10: `10-process-tasks.md`
3. Apply the exact pattern from Protocols 01-06
4. Run validators after completion
5. Update `.artifacts/phase-5-remediation/02-VALIDATION-TRACKER.md`

**Validation:**
```bash
python3 validators-system/scripts/validate_protocol_handoff.py --protocol 07 --protocol 08 --protocol 09 --protocol 10 --report --workspace .
python3 validators-system/scripts/validate_protocol_communication.py --protocol 07 --protocol 08 --protocol 09 --protocol 10 --report --workspace .
```

**Expected Output:** All 4 protocols should show PASS (≥0.90) for handoff and communication validators.

---

## PROMPT FOR SESSION WORKER 2 (Batch 2: Protocols 11-14)

**Task:** Enhance HANDOFF CHECKLIST and COMMUNICATION PROTOCOLS sections for Protocols 11-14.

**Instructions:**
1. Read `.artifacts/phase-5-remediation/CONTINUATION-PROMPT-R1.md` for full pattern details
2. Enhance these 4 protocols:
   - 11: `11-integration-testing.md`
   - 12: `12-quality-audit.md`
   - 13: `13-uat-coordination.md`
   - 14: `14-pre-deployment-staging.md`
3. Apply the exact pattern from Protocols 01-06
4. Run validators after completion
5. Update `.artifacts/phase-5-remediation/02-VALIDATION-TRACKER.md`

**Validation:**
```bash
python3 validators-system/scripts/validate_protocol_handoff.py --protocol 11 --protocol 12 --protocol 13 --protocol 14 --report --workspace .
python3 validators-system/scripts/validate_protocol_communication.py --protocol 11 --protocol 12 --protocol 13 --protocol 14 --report --workspace .
```

**Expected Output:** All 4 protocols should show PASS (≥0.90) for handoff and communication validators.

---

## PROMPT FOR SESSION WORKER 3 (Batch 3: Protocols 15-18)

**Task:** Enhance HANDOFF CHECKLIST and COMMUNICATION PROTOCOLS sections for Protocols 15-18.

**Instructions:**
1. Read `.artifacts/phase-5-remediation/CONTINUATION-PROMPT-R1.md` for full pattern details
2. Enhance these 4 protocols:
   - 15: `15-production-deployment.md`
   - 16: `16-monitoring-observability.md`
   - 17: `17-incident-response-rollback.md`
   - 18: `18-performance-optimization.md`
3. Apply the exact pattern from Protocols 01-06
4. Run validators after completion
5. Update `.artifacts/phase-5-remediation/02-VALIDATION-TRACKER.md`

**Validation:**
```bash
python3 validators-system/scripts/validate_protocol_handoff.py --protocol 15 --protocol 16 --protocol 17 --protocol 18 --report --workspace .
python3 validators-system/scripts/validate_protocol_communication.py --protocol 15 --protocol 16 --protocol 17 --protocol 18 --report --workspace .
```

**Expected Output:** All 4 protocols should show PASS (≥0.90) for handoff and communication validators.

---

## PROMPT FOR SESSION WORKER 4 (Batch 4: Protocols 19-23)

**Task:** Enhance HANDOFF CHECKLIST and COMMUNICATION PROTOCOLS sections for Protocols 19-23.

**Instructions:**
1. Read `.artifacts/phase-5-remediation/CONTINUATION-PROMPT-R1.md` for full pattern details
2. Enhance these 5 protocols:
   - 19: `19-documentation-knowledge-transfer.md`
   - 20: `20-project-closure.md`
   - 21: `21-maintenance-support.md`
   - 22: `22-implementation-retrospective.md`
   - 23: `23-script-governance-protocol.md`
3. Apply the exact pattern from Protocols 01-06
4. Run validators after completion
5. Update `.artifacts/phase-5-remediation/02-VALIDATION-TRACKER.md`

**Note:** Protocol 23 is the final protocol - adjust "Ready-for-Next-Protocol Statement" accordingly (no next protocol).

**Validation:**
```bash
python3 validators-system/scripts/validate_protocol_handoff.py --protocol 19 --protocol 20 --protocol 21 --protocol 22 --protocol 23 --report --workspace .
python3 validators-system/scripts/validate_protocol_communication.py --protocol 19 --protocol 20 --protocol 21 --protocol 22 --protocol 23 --report --workspace .
```

**Expected Output:** All 5 protocols should show PASS (≥0.90) for handoff and communication validators.

---

## After All Batches Complete

**Final Validation:**
```bash
# Run all validators
python3 validators-system/scripts/validate_protocol_handoff.py --all --report --workspace .
python3 validators-system/scripts/validate_protocol_communication.py --all --report --workspace .
python3 validators-system/scripts/validate_all_protocols.py --all --report --workspace .

# Generate final summary
echo "✅ R1 Workstream Complete!" > .artifacts/phase-5-remediation/R1-COMPLETE.md
```

**Success Criteria:**
- ✅ All 23 protocols enhanced
- ✅ Handoff validator: 0 FAIL protocols
- ✅ Communication validator: 0 FAIL protocols
- ✅ Average scores ≥ 0.90 for both validators

---

*Generated: 2025-11-06*  
*Ready for parallel execution*

