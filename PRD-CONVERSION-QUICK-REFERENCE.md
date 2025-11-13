# PRD to Protocol Conversion - Quick Reference

**Quick guide for converting PRD specifications to structured protocol files**

---

## 🎯 Core Process (5 Steps)

### 1. **Extract & Map** (15 min)
- Read PRD section for target protocol
- Map PRD content to 10 standard sections
- Identify gaps vs. Protocol 06 template

### 2. **Create Structure** (10 min)
- Copy Protocol 06 structure as template
- Replace protocol-specific metadata
- Set up all section headers

### 3. **Expand Content** (2-4 hours)
- **PREREQUISITES:** Add validation checkpoints, error codes
- **AI ROLE:** Expand to 4-6 capabilities, constraints, decision authority
- **WORKFLOW:** Transform steps → detailed actions with evidence, validation, error handling
- **QUALITY GATES:** Add automation, CI integration, failure handling
- **AUTOMATION HOOKS:** Add full commands, CI/CD config, manual fallbacks
- **EVIDENCE SUMMARY:** Create artifact table, storage structure
- **INTEGRATION POINTS:** Specify exact formats and validation
- **COMMUNICATION:** Create phase-specific templates
- **HANDOFF:** Add predecessor/successor/knowledge transfer
- **REASONING:** Add patterns, decision logic, learning mechanisms

### 4. **Validate** (30 min)
- Run all 11 validators
- Fix issues (target: all scores ≥ 0.95)
- Cross-reference with Protocol 06

### 5. **Refine** (30 min)
- Review completeness
- Check formatting consistency
- Verify all PRD requirements included

---

## 📋 Section Expansion Cheat Sheet

| PRD Section | Protocol Section | Key Expansions Needed |
|-------------|------------------|----------------------|
| "Required Sections" | PREREQUISITES | Add validation checkpoints, error codes, file format specs |
| "AI acts as" | AI ROLE AND MISSION | Add 4-6 capabilities, behavioral constraints, decision authority |
| "WORKFLOW (STEPS)" | WORKFLOW | Expand each step: actions, evidence, validation, error handling, halt conditions |
| "QUALITY GATES" | QUALITY GATES | Add automation scripts, CI integration, failure handling procedures |
| "AUTOMATION HOOKS" | AUTOMATION HOOKS | Add full command syntax, CI/CD YAML, manual fallbacks |
| "EVIDENCE SUMMARY" | EVIDENCE SUMMARY | Create artifact table, storage structure, manifest requirements |
| "INTEGRATION POINTS" | INTEGRATION POINTS | Specify exact artifact formats, validation requirements |
| "COMMUNICATION PROTOCOLS" | COMMUNICATION PROTOCOLS | Create phase-specific announcement templates |
| "HANDOFF CHECKLIST" | HANDOFF CHECKLIST | Add predecessor/successor/knowledge transfer sections |
| "REASONING & REFLECTION" | REASONING & COGNITIVE PROCESS | Add patterns, decision logic, learning mechanisms, meta-cognition |

---

## 🔑 Key Transformation Patterns

### Pattern 1: Step → Detailed Workflow
```
PRD: "STEP 1: Business Problem Analysis"
↓
Protocol:
1. **`[MUST]` Analyze Business Problem:**
   * **Action:** {Detailed procedure with commands}
   * **Communication:** > "[MASTER RAY™ | PHASE 1 START] - {Message}"
   * **Evidence:** `.artifacts/protocol-{NN}/phase-01/{artifact}.md`
   * **Validation:** {Specific criteria with thresholds}
   * **Validation Checkpoint:** {Embedded checks with error codes}
   * **Error Handling:** {Specific error scenarios}
   * **Halt condition:** {Specific condition}
```

### Pattern 2: Gate → Comprehensive Quality Gate
```
PRD: "Gate 1: Problem-AI Fit Score ≥ 0.8"
↓
Protocol:
### Gate 1: Problem-AI Fit Validation
**Type:** Prerequisite
**Purpose:** {Detailed purpose}
**Pass Criteria:**
- **Threshold:** Problem-AI fit score ≥ 0.8 (numeric: `fit_score >= 0.8`)
- **Boolean Check:** `{file}` field `status` equals "PASS"
- **Metrics:** {Detailed metrics}
- **Evidence Link:** {File references}
**Automation:**
- Script: `python3 scripts/ai/{script}.py --args`
- CI Integration: {CI config}
**Failure Handling:**
- **Rollback:** {Procedure}
- **Notification:** {Procedure}
- **Waiver:** {Conditions}
```

### Pattern 3: Script → Full Automation Hook
```
PRD: "Script: classify_ai_problem_type.py (NEW)"
↓
Protocol:
1. **AI Problem Type Classification:**
   * **Action:** Classify AI problem type using automated analysis
   * **Command:** `python scripts/ai/classify_ai_problem_type.py --brief PROJECT-BRIEF.md --output .artifacts/protocol-{NN}/problem-type.json`
   * **Evidence:** `.artifacts/protocol-{NN}/problem-type.json`
   * **Validation:** Exit code 0, JSON contains `problem_type` field with valid value
```

---

## ✅ Validation Checklist (Per Protocol)

### Structure
- [ ] All 10+ sections present
- [ ] Section order matches Protocol 06
- [ ] HTML comments for category classification
- [ ] Correct markdown header levels

### Content
- [ ] All PRD requirements included
- [ ] All PRD steps expanded
- [ ] All PRD gates expanded
- [ ] All PRD scripts detailed
- [ ] All PRD evidence specified

### Formatting
- [ ] Directive markers consistent ([STRICT], [GUIDELINE], [MUST])
- [ ] Code blocks use language tags
- [ ] Tables formatted consistently
- [ ] Communication templates match style

### Validation
- [ ] Protocol identity metadata complete
- [ ] Workflow steps have validation checkpoints
- [ ] Quality gates have measurable thresholds
- [ ] Automation scripts have full paths
- [ ] Evidence artifacts have metadata

---

## 🚀 Quick Commands

### Create Protocol File
```bash
# Use helper script
./scripts/create-protocol-from-prd.sh {protocol-number} "{protocol-name}" "{phase}"

# Or manually
cp AI-project-workflow/06-ai-use-case-definition-prioritization.md \
   AI-project-workflow/{NN}-{protocol-name}.md
```

### Validate Protocol
```bash
# Individual validators
python scripts/validate_protocol_identity.py --path AI-project-workflow/{NN}-{name}.md
python scripts/validate_protocol_role.py --path AI-project-workflow/{NN}-{name}.md
python scripts/validate_protocol_workflow.py --path AI-project-workflow/{NN}-{name}.md

# All validators
python scripts/validate_all_protocols.py --protocol {NN}
```

### Check Completeness
```bash
# Compare with reference
diff -u <(grep "^##" AI-project-workflow/06-ai-use-case-definition-prioritization.md) \
        <(grep "^##" AI-project-workflow/{NN}-{name}.md)
```

---

## 📊 Conversion Metrics

**Target Metrics:**
- **Time per Protocol:** 3-5 hours
- **Sections Expanded:** 10+ sections
- **Steps Expanded:** 4-8 workflow steps
- **Gates Expanded:** 3-5 quality gates
- **Scripts Detailed:** 2-5 automation scripts
- **Validator Scores:** All ≥ 0.95

**Quality Gates:**
- Structure completeness: 100%
- PRD requirement coverage: 100%
- Formatting consistency: 100%
- Validation readiness: 100%

---

## 🎯 Success Criteria

A successfully converted protocol:
1. ✅ Passes all 11 validators (score ≥ 0.95 each)
2. ✅ Contains all PRD requirements
3. ✅ Matches Protocol 06 structure exactly
4. ✅ Has detailed workflow steps with validation
5. ✅ Includes comprehensive error handling
6. ✅ Specifies all automation scripts with commands
7. ✅ Documents all evidence artifacts with paths
8. ✅ Provides clear integration points
9. ✅ Includes reasoning patterns and decision logic
10. ✅ Ready for production use

---

**For detailed instructions, see:** `PRD-TO-PROTOCOL-CONVERSION-GUIDE.md`

