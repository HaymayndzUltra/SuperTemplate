# Protocol Generation System - Stress Testing

**Purpose**: Comprehensive stress testing suite to validate the protocol generation system  
**Status**: ✅ Ready for Execution  
**Last Updated**: 2025-01-10

---

## 🎯 OVERVIEW

This test suite validates the complete protocol generation pipeline through:
- **10 Test Scenarios** covering happy paths, edge cases, and stress conditions
- **7 Automated Tests** in `run_stress_tests.sh`
- **3 Test Data Files** representing different project types

---

## 📁 TEST FILES

```
tests/protocol-generation/
├── README.md (this file)
├── test_scenarios.md (detailed scenario descriptions)
├── run_stress_tests.sh (automated test runner)
├── test-project-brief-simple.md (simple web app)
├── test-project-brief-enterprise.md (complex enterprise app)
├── test-project-brief-minimal.md (minimal edge case)
└── results/ (generated during test execution)
```

---

## 🚀 QUICK START

### Run All Tests

```bash
cd /home/haymayndz/SuperTemplate
./tests/protocol-generation/run_stress_tests.sh
```

### Run Individual Scenario

```bash
# Scenario 1: Simple Web App
python scripts/orchestration/generate_project_protocols.py \
  --protocol-ids 06,07,08,09,10 \
  --project-brief tests/protocol-generation/test-project-brief-simple.md \
  --execution-plan PROTOCOL-EXECUTION-PLAN.md \
  --output-dir /tmp/test-simple \
  --verbose
```

---

## 📋 TEST SCENARIOS

### ✅ **Scenario 1: Simple Web App** (Happy Path)
- **Tech Stack**: Next.js + FastAPI + PostgreSQL
- **Complexity**: Standard
- **Expected**: All protocols generated, validations injected
- **Duration**: ~5 seconds

### ✅ **Scenario 2: Enterprise App** (Complex)
- **Tech Stack**: React + Django + MongoDB
- **Complexity**: Enterprise
- **Expected**: Enterprise workflows, compliance checks
- **Duration**: ~8 seconds

### ⚠️ **Scenario 3: Minimal Brief** (Edge Case)
- **Input**: Minimal project information
- **Expected**: Graceful handling with defaults
- **Duration**: ~3 seconds

### ⚠️ **Scenario 4: Missing Templates** (Error Handling)
- **Input**: Include non-existent protocol ID (99)
- **Expected**: Partial success, clear warnings
- **Duration**: ~2 seconds

### ❌ **Scenario 5: Invalid Brief** (Error Handling)
- **Input**: Non-existent file path
- **Expected**: Graceful failure with clear error
- **Duration**: <1 second

### ✅ **Scenario 6: Performance Test** (Stress)
- **Input**: 8 protocols at once
- **Expected**: Complete in <30 seconds
- **Duration**: ~18 seconds

### ✅ **Scenario 7: Idempotency Test** (Consistency)
- **Input**: Run twice with same inputs
- **Expected**: Identical output (same checksums)
- **Duration**: ~10 seconds

---

## ✅ SUCCESS CRITERIA

### Must Pass (7 tests)
1. ✅ Simple Web App generates correctly
2. ✅ Enterprise App handles complexity
3. ✅ Minimal Brief uses defaults
4. ✅ Missing Templates handled gracefully
5. ✅ Invalid Brief fails with clear error
6. ✅ Performance meets <30s threshold
7. ✅ Idempotency maintained

### Validation Requirements
- ✅ All generated protocols score ≥0.95
- ✅ No placeholders remain (`{PROJECT_NAME}`, etc.)
- ✅ Artifact paths customized correctly
- ✅ Tech stack validations injected
- ✅ Project name used consistently
- ✅ README.md and manifest created

---

## 📊 EXPECTED RESULTS

```
==========================================
TEST SUMMARY
==========================================
Passed: 7
Failed: 0
Warnings: 0
Total: 7

End Time: 2025-01-10 14:30:00
Results saved to: tests/protocol-generation/results
==========================================
```

---

## 🔍 VALIDATION CHECKS

### Structural Validation
- ✅ All required sections present
- ✅ Proper markdown formatting
- ✅ Code blocks for automation scripts
- ✅ Integration points defined

### Customization Validation
- ✅ Placeholders replaced with actual values
- ✅ Project name appears in content
- ✅ Artifact paths use project-specific location
- ✅ Tech stack-specific validations injected

### Integration Validation
- ✅ Input/output definitions present
- ✅ Artifact storage defined
- ✅ Dependencies documented

---

## 🐛 TROUBLESHOOTING

### Test Fails: "Template not found"
**Cause**: Foundation templates missing  
**Solution**: Ensure `.cursor/ai-driven-workflow/` contains protocol templates

### Test Fails: "Module not found"
**Cause**: Python dependencies missing  
**Solution**: Install required packages (if any)

### Test Fails: "Permission denied"
**Cause**: Script not executable  
**Solution**: `chmod +x tests/protocol-generation/run_stress_tests.sh`

### Test Slow: >30 seconds
**Cause**: System resources constrained  
**Solution**: Close other applications, check CPU/memory usage

---

## 📈 PERFORMANCE BENCHMARKS

| Scenario | Protocols | Expected Duration | Threshold |
|----------|-----------|-------------------|-----------|
| Simple Web App | 5 | ~5s | <10s |
| Enterprise App | 3 | ~8s | <15s |
| Minimal Brief | 2 | ~3s | <5s |
| Missing Templates | 2 | ~2s | <5s |
| Invalid Brief | 1 | <1s | <2s |
| Performance Test | 8 | ~18s | <30s |
| Idempotency | 2×2 | ~10s | <15s |

---

## 🔄 CONTINUOUS TESTING

### Run Before Commits
```bash
# Quick smoke test
./tests/protocol-generation/run_stress_tests.sh

# If all pass, safe to commit
git add .
git commit -m "feat: protocol generation system"
```

### Run in CI/CD
```yaml
# .github/workflows/test.yml
- name: Run Protocol Generation Tests
  run: ./tests/protocol-generation/run_stress_tests.sh
```

---

## 📝 TEST RESULTS LOCATION

After running tests, results are saved to:
```
tests/protocol-generation/results/
├── scenario1-simple/ (generated protocols)
├── scenario1-artifacts/ (intermediate files)
├── scenario1.log (execution log)
├── scenario2-enterprise/
├── scenario2-artifacts/
├── scenario2.log
└── ... (all scenarios)
```

---

## 🎯 NEXT STEPS

### After Tests Pass
1. ✅ Review generated protocols manually
2. ✅ Verify validation reports
3. ✅ Check generation reports
4. ✅ Test with real PROJECT-BRIEF.md
5. ✅ Execute generated Protocol 06

### If Tests Fail
1. ❌ Review failure logs in `results/*.log`
2. ❌ Check error messages for root cause
3. ❌ Fix identified issues
4. ❌ Re-run tests
5. ❌ Document any gaps found

---

## 📚 REFERENCES

- **Test Scenarios**: `test_scenarios.md` - Detailed scenario descriptions
- **Test Runner**: `run_stress_tests.sh` - Automated test execution
- **Implementation**: `../../IMPLEMENTATION-SUMMARY.md` - Complete system documentation
- **Generation Scripts**: `../../scripts/orchestration/` - Core implementation

---

**Status**: ✅ Ready for Execution  
**Maintainer**: Protocol Generation Team  
**Last Test Run**: Not yet executed
