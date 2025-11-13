# Protocol Generation System - Test Scenarios

**Purpose**: Comprehensive stress testing to identify gaps and validate effectiveness  
**Created**: 2025-01-10  
**Status**: Ready for Execution

---

## 🎯 TEST OBJECTIVES

1. **Completeness**: Verify all scripts work end-to-end
2. **Robustness**: Test error handling and edge cases
3. **Accuracy**: Validate transformations are correct
4. **Performance**: Ensure acceptable execution time
5. **Quality**: Confirm validation catches issues

---

## 📋 TEST SCENARIOS

### **Scenario 1: Happy Path - Simple Web App**

**Project Type**: Simple Web Application  
**Tech Stack**: Next.js + FastAPI + PostgreSQL  
**Complexity**: Standard  
**Team Size**: Solo Developer

**Test Data** (`test-project-brief-simple.md`):
```markdown
# Artisan's Corner Dashboard

## Project Overview
A simple e-commerce analytics dashboard for artisan marketplace vendors.

## Tech Stack
- Frontend: Next.js 14 with TypeScript
- Backend: FastAPI with Python 3.11
- Database: PostgreSQL 15

## Objectives
Build a dashboard to track sales, inventory, and customer analytics.

## Timeline
8 weeks

## Team
Solo developer
```

**Expected Outcomes**:
- ✅ All 10 protocols generated (06-15)
- ✅ Next.js validations injected in Protocol 06
- ✅ FastAPI validations injected in Protocol 06
- ✅ PostgreSQL schema validation in Protocol 09
- ✅ Solo developer workflow (simplified approvals)
- ✅ All validation scores ≥0.95
- ✅ Project name: `artisans-corner-dashboard`

**Validation Checks**:
1. Check `06-create-prd-artisans-corner-dashboard.md` contains "Next.js"
2. Check artifact paths: `.artifacts/artisans-corner-dashboard/protocol-06/`
3. Check no placeholders remain: `{PROJECT_NAME}`, `{FRONTEND}`, etc.
4. Check README.md lists all 10 protocols
5. Check manifest has correct project name and tech stack

---

### **Scenario 2: Complex Enterprise App**

**Project Type**: Enterprise Application  
**Tech Stack**: React + Django + MongoDB + Redis  
**Complexity**: Complex  
**Team Size**: Large (20+ developers)

**Test Data** (`test-project-brief-enterprise.md`):
```markdown
# Global Supply Chain Management System

## Project Overview
Enterprise-grade supply chain management platform with real-time tracking,
multi-tenant architecture, and compliance requirements (SOC2, GDPR).

## Tech Stack
- Frontend: React 18 with TypeScript, Redux
- Backend: Django 4.2 with Django REST Framework
- Database: MongoDB Atlas, Redis for caching
- Infrastructure: Kubernetes, AWS ECS

## Objectives
Build a scalable, compliant supply chain platform supporting 10,000+ concurrent users.

## Timeline
24 weeks

## Team
- 5 Frontend developers
- 5 Backend developers
- 2 DevOps engineers
- 3 QA engineers
- 2 Security specialists

## Compliance
- SOC2 Type II
- GDPR
- ISO 27001
```

**Expected Outcomes**:
- ✅ All protocols generated with enterprise complexity
- ✅ React validations (not Next.js)
- ✅ Django-specific validations
- ✅ MongoDB schema validation
- ✅ Redis caching validation
- ✅ Enterprise workflow (multiple approval gates)
- ✅ Compliance checks injected (SOC2, GDPR)
- ✅ Large team coordination steps added

**Validation Checks**:
1. Check for "Architecture Review Board" step (enterprise)
2. Check for "Security Review" step (compliance)
3. Check for "Legal/Compliance Review" step
4. Check artifact paths use project name
5. Check validation includes compliance requirements

---

### **Scenario 3: AI/ML Application**

**Project Type**: AI/ML Application  
**Tech Stack**: Python + TensorFlow + FastAPI + PostgreSQL  
**Complexity**: Complex  
**Team Size**: Medium (8 developers)

**Test Data** (`test-project-brief-aiml.md`):
```markdown
# Predictive Maintenance AI System

## Project Overview
AI-powered predictive maintenance system for industrial equipment using
machine learning models to predict failures before they occur.

## Tech Stack
- Frontend: Vue.js 3 with TypeScript
- Backend: FastAPI with Python 3.11
- AI/ML: TensorFlow 2.x, scikit-learn, MLflow
- Database: PostgreSQL 15, TimescaleDB
- Infrastructure: Docker, AWS SageMaker

## Objectives
Build ML pipeline for predictive maintenance with 95% accuracy.

## Timeline
16 weeks

## Team
- 2 ML Engineers
- 2 Backend developers
- 2 Frontend developers
- 1 DevOps engineer
- 1 Data Scientist
```

**Expected Outcomes**:
- ✅ AI/ML-specific protocols generated (if templates exist)
- ✅ Model training validation steps
- ✅ Data pipeline validation
- ✅ MLflow integration checks
- ✅ TensorFlow-specific validations
- ✅ TimescaleDB time-series validation

**Validation Checks**:
1. Check for ML-specific validation steps
2. Check for model evaluation metrics
3. Check for data quality validation
4. Check for experiment tracking (MLflow)
5. Check for model deployment steps

---

### **Scenario 4: Edge Case - Minimal Brief**

**Project Type**: Unknown  
**Tech Stack**: Minimal information  
**Complexity**: Unknown  
**Team Size**: Not specified

**Test Data** (`test-project-brief-minimal.md`):
```markdown
# My Project

Build a web app.
```

**Expected Outcomes**:
- ✅ System handles minimal input gracefully
- ✅ Uses default values for missing info
- ✅ Project name: `my-project`
- ✅ Tech stack: "unknown" for all fields
- ✅ Standard complexity workflow
- ⚠️ Validation warnings for missing information
- ✅ Still generates valid protocols

**Validation Checks**:
1. Check system doesn't crash
2. Check default values used
3. Check validation warnings logged
4. Check protocols still structurally valid
5. Check manifest shows "unknown" tech stack

---

### **Scenario 5: Edge Case - Missing Templates**

**Project Type**: Web Application  
**Protocol IDs**: Include non-existent protocol (99)  
**Expected Behavior**: Graceful handling

**Test Command**:
```bash
python scripts/orchestration/generate_project_protocols.py \
  --protocol-ids 06,07,99 \
  --project-brief PROJECT-BRIEF.md \
  --execution-plan PROTOCOL-EXECUTION-PLAN.md
```

**Expected Outcomes**:
- ✅ Protocols 06, 07 generated successfully
- ⚠️ Warning logged for missing Protocol 99
- ✅ Exit code 2 (partial success)
- ✅ Manifest shows 2 protocols generated
- ✅ Report shows missing template warning

---

### **Scenario 6: Edge Case - Invalid PROJECT-BRIEF.md**

**Test Data**: Corrupted or invalid brief file

**Test Cases**:
1. **Empty file**: `PROJECT-BRIEF.md` is empty
2. **Invalid encoding**: File with binary data
3. **Missing file**: File doesn't exist
4. **Malformed markdown**: Broken syntax

**Expected Outcomes**:
- ❌ System fails gracefully with clear error message
- ❌ Exit code 1 (error)
- ✅ Error message indicates specific problem
- ✅ No partial files written
- ✅ No corrupt manifest created

---

### **Scenario 7: Validation Failure Recovery**

**Test Data**: Intentionally create protocols with issues

**Setup**:
1. Generate protocols normally
2. Manually corrupt one protocol (remove required section)
3. Run validation

**Expected Outcomes**:
- ❌ Validation fails for corrupted protocol
- ✅ Auto-fix attempts to repair (if enabled)
- ⚠️ If auto-fix fails, clear error message
- ✅ Validation report shows specific issues
- ✅ Other protocols still pass

---

### **Scenario 8: Performance Test - Large Batch**

**Test Data**: Generate many protocols at once

**Test Command**:
```bash
python scripts/orchestration/generate_project_protocols.py \
  --protocol-ids 06,07,08,09,10,11,12,13,14,15,16,17,18 \
  --project-brief PROJECT-BRIEF.md \
  --execution-plan PROTOCOL-EXECUTION-PLAN.md
```

**Expected Outcomes**:
- ✅ All 13 protocols generated
- ✅ Execution time <30 seconds
- ✅ Memory usage reasonable (<500MB)
- ✅ All validations pass
- ✅ Manifest accurate for all protocols

**Performance Metrics**:
- Generation time per protocol: <2 seconds
- Validation time per protocol: <1 second
- Total pipeline time: <30 seconds

---

### **Scenario 9: Idempotency Test**

**Test**: Run generation twice with same inputs

**Test Commands**:
```bash
# First run
python scripts/orchestration/generate_project_protocols.py \
  --protocol-ids 06,07,08 \
  --project-brief PROJECT-BRIEF.md \
  --execution-plan PROTOCOL-EXECUTION-PLAN.md

# Second run (with --force)
python scripts/orchestration/generate_project_protocols.py \
  --protocol-ids 06,07,08 \
  --project-brief PROJECT-BRIEF.md \
  --execution-plan PROTOCOL-EXECUTION-PLAN.md \
  --force
```

**Expected Outcomes**:
- ✅ First run succeeds
- ✅ Second run overwrites files (with --force)
- ✅ Generated files identical (same checksums)
- ✅ Manifest updated with new timestamp
- ✅ No duplicate entries

---

### **Scenario 10: Integration Test - Full Workflow**

**Test**: Complete Protocol 01-05b → Generation → Execution

**Steps**:
1. Create PROJECT-BRIEF.md (Protocol 03 output)
2. Run Protocol 05b PHASE 7 (calls generation)
3. Verify generated protocols
4. Execute Protocol 06 (generated version)

**Expected Outcomes**:
- ✅ Protocol 05b PHASE 7 completes successfully
- ✅ Generated protocols available
- ✅ Protocol 06 (generated) executes without errors
- ✅ Artifacts created in project-specific paths
- ✅ Integration points work correctly

---

## 🧪 TEST EXECUTION PLAN

### **Phase 1: Unit Tests** (Individual Scripts)

Test each script independently:

```bash
# Test 1: Template Loading
python scripts/orchestration/load_protocol_templates.py \
  --protocol-ids 06,07,08 \
  --output /tmp/test-loaded.json \
  --verbose

# Test 2: Transformation
python scripts/orchestration/transform_protocols.py \
  --templates /tmp/test-loaded.json \
  --project-brief tests/test-project-brief-simple.md \
  --execution-plan PROTOCOL-EXECUTION-PLAN.md \
  --output /tmp/test-transformed.json \
  --verbose

# Test 3: Writing
python scripts/orchestration/write_generated_protocols.py \
  --transformed /tmp/test-transformed.json \
  --output-dir /tmp/test-protocols \
  --force \
  --verbose

# Test 4: Validation
python scripts/orchestration/validate_generated_protocols.py \
  --protocols-dir /tmp/test-protocols \
  --output /tmp/test-validation.json \
  --auto-fix \
  --verbose

# Test 5: Reporting
python scripts/orchestration/generate_protocol_report.py \
  --manifest /tmp/test-protocols/.protocol-manifest.json \
  --validation /tmp/test-validation.json \
  --output /tmp/test-report.md \
  --verbose
```

---

### **Phase 2: Integration Tests** (Full Pipeline)

Test complete pipeline:

```bash
# Scenario 1: Simple Web App
python scripts/orchestration/generate_project_protocols.py \
  --protocol-ids 06,07,08,09,10 \
  --project-brief tests/test-project-brief-simple.md \
  --execution-plan PROTOCOL-EXECUTION-PLAN.md \
  --output-dir /tmp/test-simple \
  --artifacts-dir /tmp/artifacts-simple \
  --verbose

# Scenario 2: Enterprise App
python scripts/orchestration/generate_project_protocols.py \
  --protocol-ids 06,07,08,09,10,11,12,13,14,15 \
  --project-brief tests/test-project-brief-enterprise.md \
  --execution-plan PROTOCOL-EXECUTION-PLAN.md \
  --output-dir /tmp/test-enterprise \
  --artifacts-dir /tmp/artifacts-enterprise \
  --verbose

# Scenario 3: AI/ML App
python scripts/orchestration/generate_project_protocols.py \
  --protocol-ids 06,07,08,09,10 \
  --project-brief tests/test-project-brief-aiml.md \
  --execution-plan PROTOCOL-EXECUTION-PLAN.md \
  --output-dir /tmp/test-aiml \
  --artifacts-dir /tmp/artifacts-aiml \
  --verbose
```

---

### **Phase 3: Edge Case Tests**

Test error handling:

```bash
# Test missing templates
python scripts/orchestration/generate_project_protocols.py \
  --protocol-ids 06,99 \
  --project-brief tests/test-project-brief-simple.md \
  --execution-plan PROTOCOL-EXECUTION-PLAN.md \
  --output-dir /tmp/test-missing

# Test minimal brief
python scripts/orchestration/generate_project_protocols.py \
  --protocol-ids 06,07 \
  --project-brief tests/test-project-brief-minimal.md \
  --execution-plan PROTOCOL-EXECUTION-PLAN.md \
  --output-dir /tmp/test-minimal

# Test invalid brief (should fail gracefully)
python scripts/orchestration/generate_project_protocols.py \
  --protocol-ids 06 \
  --project-brief /nonexistent/file.md \
  --execution-plan PROTOCOL-EXECUTION-PLAN.md \
  --output-dir /tmp/test-invalid
```

---

## ✅ SUCCESS CRITERIA

### **Must Pass**:
1. ✅ All happy path scenarios succeed (1, 2, 3)
2. ✅ Edge cases handled gracefully (4, 5, 6, 7)
3. ✅ Performance acceptable (8)
4. ✅ Idempotency maintained (9)
5. ✅ Integration works end-to-end (10)

### **Validation Requirements**:
- ✅ All generated protocols score ≥0.95
- ✅ No placeholders remain in output
- ✅ Artifact paths customized correctly
- ✅ Tech stack validations injected
- ✅ Project name used consistently

### **Error Handling**:
- ✅ Clear error messages for failures
- ✅ No corrupt files on error
- ✅ Proper exit codes (0=success, 1=error, 2=partial)
- ✅ Logs provide debugging information

---

## 📊 TEST RESULTS TEMPLATE

```markdown
# Test Execution Results

**Date**: YYYY-MM-DD  
**Tester**: [Name]

## Scenario Results

| Scenario | Status | Duration | Issues |
|----------|--------|----------|--------|
| 1. Simple Web App | ✅ PASS | 5.2s | None |
| 2. Enterprise App | ✅ PASS | 8.7s | None |
| 3. AI/ML App | ✅ PASS | 6.1s | None |
| 4. Minimal Brief | ✅ PASS | 3.8s | Warnings logged |
| 5. Missing Templates | ⚠️ PARTIAL | 2.1s | Protocol 99 missing |
| 6. Invalid Brief | ❌ FAIL | 0.5s | Clear error message |
| 7. Validation Recovery | ✅ PASS | 4.3s | Auto-fix worked |
| 8. Performance Test | ✅ PASS | 18.9s | Within limits |
| 9. Idempotency | ✅ PASS | 10.4s | Identical output |
| 10. Full Workflow | ✅ PASS | 25.3s | End-to-end success |

## Issues Found

[List any bugs, gaps, or improvements needed]

## Recommendations

[Suggestions for fixes or enhancements]
```

---

**Status**: Ready for Execution  
**Next Step**: Create test data files and run scenarios
