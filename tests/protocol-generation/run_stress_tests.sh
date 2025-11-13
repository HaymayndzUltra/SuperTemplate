#!/bin/bash
# Protocol Generation System - Stress Test Runner
# Executes all test scenarios and generates comprehensive report

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Test counters
TESTS_PASSED=0
TESTS_FAILED=0
TESTS_WARNED=0

# Directories
TEST_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$TEST_DIR/../.." && pwd)"
RESULTS_DIR="$TEST_DIR/results"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Create results directory
mkdir -p "$RESULTS_DIR"

echo "=========================================="
echo "PROTOCOL GENERATION STRESS TESTS"
echo "=========================================="
echo "Start Time: $(date)"
echo "Results Dir: $RESULTS_DIR"
echo ""

# Helper functions
log_test() {
    echo -e "${BLUE}[TEST]${NC} $1"
}

log_pass() {
    echo -e "${GREEN}[PASS]${NC} $1"
    ((TESTS_PASSED++))
}

log_fail() {
    echo -e "${RED}[FAIL]${NC} $1"
    ((TESTS_FAILED++))
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
    ((TESTS_WARNED++))
}

# Test Scenario 1: Simple Web App
test_simple_web_app() {
    log_test "Scenario 1: Simple Web App (Happy Path)"
    
    local output_dir="$RESULTS_DIR/scenario1-simple"
    local artifacts_dir="$RESULTS_DIR/scenario1-artifacts"
    
    if python3 "$ROOT_DIR/scripts/orchestration/generate_project_protocols.py" \
        --protocol-ids 06,07,08,09,10 \
        --project-brief "$TEST_DIR/test-project-brief-simple.md" \
        --execution-plan "$ROOT_DIR/PROTOCOL-EXECUTION-PLAN.md" \
        --output-dir "$output_dir" \
        --artifacts-dir "$artifacts_dir" \
        > "$RESULTS_DIR/scenario1.log" 2>&1; then
        
        # Validation checks
        if [ -f "$output_dir/06-create-prd-artisans-corner-dashboard.md" ]; then
            if grep -q "Next.js" "$output_dir/06-create-prd-artisans-corner-dashboard.md"; then
                if grep -q "FastAPI" "$output_dir/06-create-prd-artisans-corner-dashboard.md"; then
                    if ! grep -q "{PROJECT_NAME}" "$output_dir/06-create-prd-artisans-corner-dashboard.md"; then
                        log_pass "Simple Web App - All validations passed"
                        return 0
                    else
                        log_fail "Simple Web App - Placeholders not replaced"
                        return 1
                    fi
                else
                    log_fail "Simple Web App - FastAPI validations missing"
                    return 1
                fi
            else
                log_fail "Simple Web App - Next.js validations missing"
                return 1
            fi
        else
            log_fail "Simple Web App - Protocol 06 not generated"
            return 1
        fi
    else
        log_fail "Simple Web App - Generation failed"
        return 1
    fi
}

# Test Scenario 2: Enterprise App
test_enterprise_app() {
    log_test "Scenario 2: Enterprise App (Complex)"
    
    local output_dir="$RESULTS_DIR/scenario2-enterprise"
    local artifacts_dir="$RESULTS_DIR/scenario2-artifacts"
    
    if python3 "$ROOT_DIR/scripts/orchestration/generate_project_protocols.py" \
        --protocol-ids 06,07,08 \
        --project-brief "$TEST_DIR/test-project-brief-enterprise.md" \
        --execution-plan "$ROOT_DIR/PROTOCOL-EXECUTION-PLAN.md" \
        --output-dir "$output_dir" \
        --artifacts-dir "$artifacts_dir" \
        > "$RESULTS_DIR/scenario2.log" 2>&1; then
        
        # Check for enterprise-specific content
        if [ -f "$output_dir/06-create-prd-global-supply-chain-management-system.md" ]; then
            if grep -q "React" "$output_dir/06-create-prd-global-supply-chain-management-system.md"; then
                log_pass "Enterprise App - Generated successfully"
                return 0
            else
                log_fail "Enterprise App - React validations missing"
                return 1
            fi
        else
            log_fail "Enterprise App - Protocol 06 not generated"
            return 1
        fi
    else
        log_fail "Enterprise App - Generation failed"
        return 1
    fi
}

# Test Scenario 3: Minimal Brief
test_minimal_brief() {
    log_test "Scenario 3: Minimal Brief (Edge Case)"
    
    local output_dir="$RESULTS_DIR/scenario3-minimal"
    local artifacts_dir="$RESULTS_DIR/scenario3-artifacts"
    
    if python3 "$ROOT_DIR/scripts/orchestration/generate_project_protocols.py" \
        --protocol-ids 06,07 \
        --project-brief "$TEST_DIR/test-project-brief-minimal.md" \
        --execution-plan "$ROOT_DIR/PROTOCOL-EXECUTION-PLAN.md" \
        --output-dir "$output_dir" \
        --artifacts-dir "$artifacts_dir" \
        > "$RESULTS_DIR/scenario3.log" 2>&1; then
        
        # Should succeed with defaults
        if [ -f "$output_dir/06-create-prd-my-project.md" ]; then
            log_pass "Minimal Brief - Handled gracefully with defaults"
            return 0
        else
            log_fail "Minimal Brief - Protocol not generated"
            return 1
        fi
    else
        log_fail "Minimal Brief - Should not fail completely"
        return 1
    fi
}

# Test Scenario 4: Missing Templates
test_missing_templates() {
    log_test "Scenario 4: Missing Templates (Error Handling)"
    
    local output_dir="$RESULTS_DIR/scenario4-missing"
    local artifacts_dir="$RESULTS_DIR/scenario4-artifacts"
    
    # This should partially succeed (exit code 2)
    python3 "$ROOT_DIR/scripts/orchestration/generate_project_protocols.py" \
        --protocol-ids 06,99 \
        --project-brief "$TEST_DIR/test-project-brief-simple.md" \
        --execution-plan "$ROOT_DIR/PROTOCOL-EXECUTION-PLAN.md" \
        --output-dir "$output_dir" \
        --artifacts-dir "$artifacts_dir" \
        > "$RESULTS_DIR/scenario4.log" 2>&1
    
    local exit_code=$?
    
    if [ $exit_code -eq 2 ]; then
        # Check that Protocol 06 was generated but 99 was not
        if [ -f "$output_dir/06-create-prd-artisans-corner-dashboard.md" ]; then
            log_warn "Missing Templates - Partial success (expected)"
            ((TESTS_PASSED++))
            return 0
        else
            log_fail "Missing Templates - Should generate valid protocols"
            return 1
        fi
    elif [ $exit_code -eq 0 ]; then
        log_fail "Missing Templates - Should return exit code 2 for partial success"
        return 1
    else
        log_fail "Missing Templates - Unexpected exit code: $exit_code"
        return 1
    fi
}

# Test Scenario 5: Invalid Brief
test_invalid_brief() {
    log_test "Scenario 5: Invalid Brief (Error Handling)"
    
    local output_dir="$RESULTS_DIR/scenario5-invalid"
    local artifacts_dir="$RESULTS_DIR/scenario5-artifacts"
    
    # This should fail gracefully
    if python3 "$ROOT_DIR/scripts/orchestration/generate_project_protocols.py" \
        --protocol-ids 06 \
        --project-brief "/nonexistent/file.md" \
        --execution-plan "$ROOT_DIR/PROTOCOL-EXECUTION-PLAN.md" \
        --output-dir "$output_dir" \
        --artifacts-dir "$artifacts_dir" \
        > "$RESULTS_DIR/scenario5.log" 2>&1; then
        
        log_fail "Invalid Brief - Should fail with error"
        return 1
    else
        # Check for clear error message
        if grep -q "not found" "$RESULTS_DIR/scenario5.log" || grep -q "ERROR" "$RESULTS_DIR/scenario5.log"; then
            log_pass "Invalid Brief - Failed gracefully with clear error"
            return 0
        else
            log_fail "Invalid Brief - Error message unclear"
            return 1
        fi
    fi
}

# Test Scenario 6: Performance Test
test_performance() {
    log_test "Scenario 6: Performance Test (Large Batch)"
    
    local output_dir="$RESULTS_DIR/scenario6-performance"
    local artifacts_dir="$RESULTS_DIR/scenario6-artifacts"
    
    local start_time=$(date +%s)
    
    if python3 "$ROOT_DIR/scripts/orchestration/generate_project_protocols.py" \
        --protocol-ids 06,07,08,09,10,11,12,13 \
        --project-brief "$TEST_DIR/test-project-brief-simple.md" \
        --execution-plan "$ROOT_DIR/PROTOCOL-EXECUTION-PLAN.md" \
        --output-dir "$output_dir" \
        --artifacts-dir "$artifacts_dir" \
        > "$RESULTS_DIR/scenario6.log" 2>&1; then
        
        local end_time=$(date +%s)
        local duration=$((end_time - start_time))
        
        if [ $duration -lt 30 ]; then
            log_pass "Performance Test - Completed in ${duration}s (<30s threshold)"
            return 0
        else
            log_warn "Performance Test - Completed in ${duration}s (>30s threshold)"
            ((TESTS_PASSED++))
            return 0
        fi
    else
        log_fail "Performance Test - Generation failed"
        return 1
    fi
}

# Test Scenario 7: Idempotency
test_idempotency() {
    log_test "Scenario 7: Idempotency Test"
    
    local output_dir="$RESULTS_DIR/scenario7-idempotency"
    local artifacts_dir="$RESULTS_DIR/scenario7-artifacts"
    
    # First run
    python3 "$ROOT_DIR/scripts/orchestration/generate_project_protocols.py" \
        --protocol-ids 06,07 \
        --project-brief "$TEST_DIR/test-project-brief-simple.md" \
        --execution-plan "$ROOT_DIR/PROTOCOL-EXECUTION-PLAN.md" \
        --output-dir "$output_dir" \
        --artifacts-dir "$artifacts_dir" \
        > "$RESULTS_DIR/scenario7-run1.log" 2>&1
    
    local checksum1=$(md5sum "$output_dir/06-create-prd-artisans-corner-dashboard.md" | awk '{print $1}')
    
    # Second run with --force
    python3 "$ROOT_DIR/scripts/orchestration/generate_project_protocols.py" \
        --protocol-ids 06,07 \
        --project-brief "$TEST_DIR/test-project-brief-simple.md" \
        --execution-plan "$ROOT_DIR/PROTOCOL-EXECUTION-PLAN.md" \
        --output-dir "$output_dir" \
        --artifacts-dir "$artifacts_dir" \
        --force \
        > "$RESULTS_DIR/scenario7-run2.log" 2>&1
    
    local checksum2=$(md5sum "$output_dir/06-create-prd-artisans-corner-dashboard.md" | awk '{print $1}')
    
    if [ "$checksum1" == "$checksum2" ]; then
        log_pass "Idempotency Test - Identical output on re-run"
        return 0
    else
        log_fail "Idempotency Test - Output differs between runs"
        return 1
    fi
}

# Run all tests
echo "Running test scenarios..."
echo ""

test_simple_web_app
test_enterprise_app
test_minimal_brief
test_missing_templates
test_invalid_brief
test_performance
test_idempotency

# Generate summary
echo ""
echo "=========================================="
echo "TEST SUMMARY"
echo "=========================================="
echo -e "${GREEN}Passed:${NC} $TESTS_PASSED"
echo -e "${RED}Failed:${NC} $TESTS_FAILED"
echo -e "${YELLOW}Warnings:${NC} $TESTS_WARNED"
echo "Total: $((TESTS_PASSED + TESTS_FAILED))"
echo ""
echo "End Time: $(date)"
echo "Results saved to: $RESULTS_DIR"
echo "=========================================="

# Exit with appropriate code
if [ $TESTS_FAILED -gt 0 ]; then
    exit 1
else
    exit 0
fi
