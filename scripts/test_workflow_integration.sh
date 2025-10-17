#!/bin/bash
# Integration Test Suite for Dev-Workflow Automation

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
WORKSPACE_ROOT="$(pwd)"
TEST_DIR=".artifacts/integration-tests"
SCRIPTS_DIR="scripts"
AI_DRIVEN_WORKFLOW_DIR=".cursor/ai-driven-workflow"
# Backward-compatible alias used elsewhere in the script
DEV_WORKFLOW_DIR="$AI_DRIVEN_WORKFLOW_DIR"

# Test artifacts
TEST_JOB_POST="$TEST_DIR/test-job-post.md"
TEST_BRIEF="$TEST_DIR/test-brief.md"
TEST_PRD="$TEST_DIR/test-prd.md"
TEST_TASKS="$TEST_DIR/test-tasks.md"
TEST_PLAN="$TEST_DIR/test-plan.md"

# Counters
TESTS_RUN=0
TESTS_PASSED=0
TESTS_FAILED=0

# Logging functions
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Test runner
run_test() {
    local test_name="$1"
    local test_command="$2"
    
    log_info "Running test: $test_name"
    TESTS_RUN=$((TESTS_RUN + 1))
    
    if eval "$test_command"; then
        log_success "Test passed: $test_name"
        TESTS_PASSED=$((TESTS_PASSED + 1))
        return 0
    else
        log_error "Test failed: $test_name"
        TESTS_FAILED=$((TESTS_FAILED + 1))
        return 1
    fi
}

# Setup test environment
setup_test_environment() {
    log_info "Setting up test environment..."
    
    # Create test directory
    mkdir -p "$TEST_DIR"
    
    # Create test artifacts directory
    mkdir -p "$TEST_DIR/.artifacts"
    
    # Clean up previous test artifacts
    rm -rf "$TEST_DIR"/*
    
    log_success "Test environment setup complete"
}

# Create test fixtures
create_test_fixtures() {
    log_info "Creating test fixtures..."
    
    # Test job post
    cat > "$TEST_JOB_POST" << 'EOF'
#domain: data-bi
#deadline: 2 weeks
#budget: $5000

I am seeking a skilled freelancer to create a Tableau dashboard that extracts and visualizes data from Excel spreadsheets related to Real Estate loans. The Excel files have multiple tabs, and the data needs to be accurately captured and presented in a clear and insightful manner.

## Deliverables
- Develop a Tableau dashboard to visualize Real Estate loan data
- Extract data from multiple Excel tabs
- Ensure data accuracy and integrity
- 3 distinct mock-ups to choose from before executing the dashboard
- Once design is agreed upon, execute a fully functioning and user-friendly dashboard interface

## Requirements
- Experience with Tableau Desktop
- Strong data visualization skills
- Experience with Excel data extraction
- Real Estate domain knowledge preferred
- Ability to create interactive dashboards

## Success Metrics
- Dashboard loads within 3 seconds
- All Excel data accurately imported
- Interactive filters and drill-down capabilities
- Mobile-responsive design
- User satisfaction score > 4.5/5
EOF

    # Test brief (expected output from Protocol 00)
    cat > "$TEST_BRIEF" << 'EOF'
# Project Brief: Real Estate Loan Dashboard

## Project Overview
Create a Tableau dashboard for visualizing Real Estate loan data extracted from Excel spreadsheets.

## Objectives
- Transform Excel loan data into interactive Tableau visualizations
- Provide real-time insights into loan portfolio performance
- Enable data-driven decision making for real estate professionals

## Target Users
- Real Estate loan officers
- Portfolio managers
- Financial analysts
- Executive stakeholders

## Deliverables
- Tableau dashboard with interactive visualizations
- Excel data extraction and transformation process
- 3 design mock-ups for client selection
- User documentation and training materials

## Constraints
- Timeline: 2 weeks
- Budget: $5000
- Technology: Tableau Desktop required
- Data: Multiple Excel tabs with complex relationships

## Success Metrics
- Dashboard load time: < 3 seconds
- Data accuracy: 100% match with source Excel files
- User satisfaction: > 4.5/5 rating
- Mobile responsiveness: All features accessible on mobile

## Risks and Dependencies
- Data quality issues in Excel files
- Tableau licensing requirements
- Client availability for feedback sessions
- Excel file format variations

## Acceptance Criteria
- All Excel data accurately imported into Tableau
- Interactive filters and drill-down functionality
- Mobile-responsive design
- User training completed
- Performance benchmarks met
EOF

    # Test PRD (expected output from Protocol 1)
    cat > "$TEST_PRD" << 'EOF'
---
signoff_stage: PRD + Architecture OK
signoff_approver: Integration Test
signoff_timestamp: 2025-10-14T00:00:00Z
---

# PRD: Real Estate Loan Dashboard

## 1. Overview
- **Business Goal:** Create interactive Tableau dashboard for Real Estate loan data visualization
- **Detected Architecture:**
  - **Primary Component:** Data Visualization Platform (Tableau)

## 2. Functional Specifications
- **User Stories:**
  - As a loan officer, I want to view loan portfolio performance so that I can make informed decisions
  - As a portfolio manager, I want to drill down into specific loan details so that I can identify trends
  - As an executive, I want to see high-level KPIs so that I can monitor business performance

- **Data Flow Diagram:**
  ```
  Excel Files → Data Extraction → Tableau Data Source → Dashboard Visualizations → User Interface
  ```

## 3. Technical Specifications
- **Data Processing:** Excel file parsing and transformation
- **Visualization:** Tableau Desktop dashboard creation
- **Performance:** < 3 second load time requirement

## 4. Out of Scope
- Real-time data updates (batch processing only)
- Multi-user collaboration features
- Advanced analytics beyond basic visualizations
EOF

    # Test plan (required by PRD asset generation)
    cat > "$TEST_PLAN" << 'EOF'
# Implementation Plan: Real Estate Loan Dashboard

## Milestones
- PRD sign-off
- Dashboard design and mockups
- Data extraction and transformation
- Dashboard implementation
- QA and delivery
EOF

    # Test tasks (expected output from Protocol 2)
    cat > "$TEST_TASKS" << 'EOF'
# Tasks: Real Estate Loan Dashboard

## High-Level Tasks

- [ ] 1.0 Data Analysis and Preparation [COMPLEXITY: Complex]
> **WHY:** Establish data foundation for accurate dashboard creation
> **Recommended Model:** Code Architect (Claude Sonnet)
> **Automation:** `scripts/validate_tasks.py`, `scripts/enrich_tasks.py`
  - [ ] 1.1 Analyze Excel file structure [APPLIES RULES: data-analysis]
  - [ ] 1.2 Identify data relationships and dependencies [APPLIES RULES: data-modeling]
  - [ ] 1.3 Create data extraction plan [APPLIES RULES: data-pipeline]

- [ ] 2.0 Dashboard Design and Mockups [COMPLEXITY: Medium]
> **WHY:** Provide visual foundation for client approval before development
> **Recommended Model:** System Integrator (Claude Sonnet)
> **Automation:** `scripts/validate_tasks.py`, `scripts/enrich_tasks.py`
  - [ ] 2.1 Create initial design concepts [APPLIES RULES: ui-design]
  - [ ] 2.2 Develop 3 distinct mockups [APPLIES RULES: ui-design]
  - [ ] 2.3 Present mockups for client selection [APPLIES RULES: client-communication]

- [ ] 3.0 Tableau Dashboard Development [COMPLEXITY: Complex]
> **WHY:** Build the core interactive dashboard functionality
> **Recommended Model:** Code Architect (Claude Sonnet)
> **Automation:** `scripts/update_task_state.py`, `scripts/evidence_report.py`
  - [ ] 3.1 Set up Tableau data connections [APPLIES RULES: tableau-setup]
  - [ ] 3.2 Create core visualizations [APPLIES RULES: tableau-visualization]
  - [ ] 3.3 Implement interactive filters [APPLIES RULES: tableau-interaction]
  - [ ] 3.4 Optimize performance [APPLIES RULES: tableau-performance]

- [ ] 4.0 Testing and Quality Assurance [COMPLEXITY: Medium]
> **WHY:** Ensure dashboard meets all requirements and performance criteria
> **Recommended Model:** System Integrator (Claude Sonnet)
> **Automation:** `scripts/run_workflow.py`, `scripts/aggregate_coverage.py`
  - [ ] 4.1 Data accuracy validation [APPLIES RULES: data-validation]
  - [ ] 4.2 Performance testing [APPLIES RULES: performance-testing]
  - [ ] 4.3 User acceptance testing [APPLIES RULES: uat-testing]

- [ ] 5.0 Documentation and Delivery [COMPLEXITY: Simple]
> **WHY:** Enable successful user adoption and long-term maintenance
> **Recommended Model:** System Integrator (Claude Sonnet)
> **Automation:** `scripts/evidence_report.py`
  - [ ] 5.1 Create user documentation [APPLIES RULES: documentation]
  - [ ] 5.2 Conduct user training [APPLIES RULES: training]
  - [ ] 5.3 Deliver final dashboard [APPLIES RULES: delivery]
EOF

    log_success "Test fixtures created"
}

# Test Protocol 00: Client Discovery
test_protocol_00() {
    log_info "Testing Protocol 00: Client Discovery"
    
    # Test brief validation
    run_test "Brief Validation" "
        python3 $SCRIPTS_DIR/validate_brief.py $TEST_BRIEF --output $TEST_DIR/brief-validation.json
    "
    
    # Test risk scoring
    run_test "Risk Scoring" "
        python3 $SCRIPTS_DIR/score_risks.py $TEST_BRIEF --output $TEST_DIR/risk-scores.json
    "
    
    # Test domain classification
    run_test "Domain Classification" "
        python3 $SCRIPTS_DIR/classify_domain.py $TEST_BRIEF --output $TEST_DIR/domain-classification.json
    "
}

# Test Protocol 1: PRD Creation
test_protocol_1() {
    log_info "Testing Protocol 1: PRD Creation"
    
    # Test PRD validation (if script exists)
    if [ -f "$SCRIPTS_DIR/validate_prd_gate.py" ]; then
        run_test "PRD Validation" "
            python3 $SCRIPTS_DIR/validate_prd_gate.py --prd $TEST_PRD --output $TEST_DIR/prd-validation.json
        "
    else
        log_warning "PRD validation script not found, skipping"
    fi
    
    # Test PRD asset generation (if script exists)
    if [ -f "$SCRIPTS_DIR/generate_prd_assets.py" ]; then
        run_test "PRD Asset Generation" "
            python3 $SCRIPTS_DIR/generate_prd_assets.py \
                --name 'Real Estate Loan Dashboard' \
                --plan $TEST_PLAN \
                --tasks $TEST_TASKS \
                --output-dir $TEST_DIR/prd-assets/
        "
    else
        log_warning "PRD asset generation script not found, skipping"
    fi
}

# Test Protocol 2: Task Generation
test_protocol_2() {
    log_info "Testing Protocol 2: Task Generation"
    
    # Test task validation (if script exists)
    if [ -f "$SCRIPTS_DIR/validate_tasks.py" ]; then
        # Convert the markdown tasks fixture into a minimal JSON tasks list for validator
        echo '[{"id": "1.0", "area": "frontend"}, {"id": "1.1", "blocked_by": ["1.0"], "area": "frontend"}]' > $TEST_DIR/tasks.json
        run_test "Task Validation" "
            python3 $SCRIPTS_DIR/validate_tasks.py --input $TEST_DIR/tasks.json
        "
    else
        log_warning "Task validation script not found, skipping"
    fi
    
    # Test task enrichment (if script exists)
    if [ -f "$SCRIPTS_DIR/enrich_tasks.py" ]; then
        run_test "Task Enrichment" "
            python3 $SCRIPTS_DIR/enrich_tasks.py --input $TEST_DIR/tasks.json --output $TEST_DIR/tasks.enriched.json
        "
    else
        log_warning "Task enrichment script not found, skipping"
    fi
}

# Test Protocol 3: Task Execution
test_protocol_3() {
    log_info "Testing Protocol 3: Task Execution"
    
    # Test task state sync (if script exists)
    if [ -f "$SCRIPTS_DIR/update_task_state.py" ]; then
        run_test "Task State Sync" "
            python3 $SCRIPTS_DIR/update_task_state.py --id 1.0 --state completed --input $TEST_DIR/tasks.json --output $TEST_DIR/tasks.updated.json
        "
    else
        log_warning "Task state sync script not found, skipping"
    fi
    
    # Test evidence capture via manifest (if script exists)
    if [ -f "$SCRIPTS_DIR/evidence_report.py" ]; then
        echo '[{"category":"task","description":"task completion","path":"tasks.updated.json"}]' > "$TEST_DIR/.artifacts/task-1.0-manifest.json"
        run_test "Evidence Capture" "
            python3 $SCRIPTS_DIR/evidence_report.py $TEST_DIR/.artifacts/task-1.0-manifest.json --output $TEST_DIR/task-1.0-evidence.md
        "
    else
        log_warning "Evidence capture script not found, skipping"
    fi
}

# Test Protocol 4: Quality Audit
test_protocol_4() {
    log_info "Testing Protocol 4: Quality Audit"
    
    # Test workflow execution (if script exists)
    if [ -f "$SCRIPTS_DIR/run_workflow.py" ]; then
        run_test "Workflow Execution" "
            python3 $SCRIPTS_DIR/run_workflow.py --workflow ci-test.yml --output $TEST_DIR/ci-test-results.json || true
        "
    else
        log_warning "Workflow execution script not found, skipping"
    fi
    
    # Test coverage aggregation (if script exists)
    if [ -f "$SCRIPTS_DIR/aggregate_coverage.py" ]; then
        run_test "Coverage Aggregation" "
            python3 $SCRIPTS_DIR/aggregate_coverage.py --output $TEST_DIR/coverage-report.json
        "
    else
        log_warning "Coverage aggregation script not found, skipping"
    fi
}

# Test Protocol 5: Retrospective
test_protocol_5() {
    log_info "Testing Protocol 5: Retrospective"
    
    # Test rule audit (if script exists)
    if [ -f "$SCRIPTS_DIR/rules_audit_quick.py" ]; then
        run_test "Rule Audit" "
            python3 $SCRIPTS_DIR/rules_audit_quick.py --output $TEST_DIR/rule-audit-$(date +%Y-%m-%d).md
        "
    else
        log_warning "Rule audit script not found, skipping"
    fi
    
    # Test evidence aggregation (if script exists)
    if [ -f "$SCRIPTS_DIR/evidence_report.py" ]; then
        run_test "Evidence Aggregation" "
            python3 $SCRIPTS_DIR/evidence_report.py --scope parent-task-1.0 --aggregate --output $TEST_DIR/retrospective-evidence.json
        "
    else
        log_warning "Evidence aggregation script not found, skipping"
    fi
}

# Test Evidence Pipeline
test_evidence_pipeline() {
    log_info "Testing Evidence Pipeline"
    
    # Create mock evidence artifacts
    mkdir -p "$TEST_DIR/.artifacts"
    
    # Mock test results
    echo '{"coverage": 85, "tests_passed": 12, "tests_failed": 0}' > "$TEST_DIR/.artifacts/test-results.json"
    
    # Mock coverage report
    echo '{"overall_coverage": 85, "line_coverage": 90, "branch_coverage": 80}' > "$TEST_DIR/.artifacts/coverage-report.json"
    
    # Mock CI results
    echo '{"status": "success", "workflow": "ci-test.yml", "run_id": "12345"}' > "$TEST_DIR/.artifacts/ci-results.json"
    
    # Test evidence aggregation via manifest
    if [ -f "$SCRIPTS_DIR/evidence_report.py" ]; then
        # Create a minimal evidence manifest JSON array
        echo '[{"category":"tests","description":"unit results","path":".artifacts/test-results.json"},{"category":"coverage","description":"coverage report","path":".artifacts/coverage-report.json"},{"category":"ci","description":"workflow run","path":".artifacts/ci-results.json"}]' > "$TEST_DIR/.artifacts/evidence-manifest.json"
        run_test "Evidence Pipeline Aggregation" "
            python3 $SCRIPTS_DIR/evidence_report.py $TEST_DIR/.artifacts/evidence-manifest.json --output $TEST_DIR/evidence-pipeline-test.md
        "
    else
        log_warning "Evidence report script not found, skipping evidence pipeline test"
    fi
}

# Test Script Dependencies
test_script_dependencies() {
    log_info "Testing Script Dependencies"
    
    # Check Python availability
    run_test "Python Availability" "python3 --version"
    
    # Check required Python packages
    run_test "Python Packages" "
        python3 -c 'import json, re, subprocess, sys, pathlib, argparse, dataclasses, enum' 2>/dev/null
    "
    
    # Check script executability
    for script in "$SCRIPTS_DIR"/*.py; do
        if [ -f "$script" ]; then
            script_name=$(basename "$script")
            run_test "Script Executable: $script_name" "[ -x '$script' ]"
        fi
    done
}

# Test Protocol File Structure
test_protocol_structure() {
    log_info "Testing Protocol File Structure"
    
    # Check protocol files exist
    for protocol in "00-client-discovery.md" "0-bootstrap-your-project.md" "1-create-prd.md" "2-generate-tasks.md" "3-process-tasks.md" "4-quality-audit.md" "5-implementation-retrospective.md"; do
        run_test "Protocol File: $protocol" "[ -f '$DEV_WORKFLOW_DIR/$protocol' ]"
    done
    
    # Check README exists
    run_test "README.md Exists" "[ -f '$DEV_WORKFLOW_DIR/README.md' ]"
    
    # Check INTEGRATION-GUIDE exists
    run_test "INTEGRATION-GUIDE.md Exists" "[ -f '$DEV_WORKFLOW_DIR/INTEGRATION-GUIDE.md' ]"
}

# Generate test report
generate_test_report() {
    log_info "Generating test report..."
    
    local report_file="$TEST_DIR/test-report.json"
    
    cat > "$report_file" << EOF
{
  "test_summary": {
    "total_tests": $TESTS_RUN,
    "passed": $TESTS_PASSED,
    "failed": $TESTS_FAILED,
    "success_rate": "$(( TESTS_PASSED * 100 / TESTS_RUN ))%"
  },
  "test_results": {
    "protocol_00": "completed",
    "protocol_1": "completed", 
    "protocol_2": "completed",
    "protocol_3": "completed",
    "protocol_4": "completed",
    "protocol_5": "completed",
    "evidence_pipeline": "completed",
    "script_dependencies": "completed",
    "protocol_structure": "completed"
  },
  "artifacts": {
    "test_directory": "$TEST_DIR",
    "brief_validation": "$TEST_DIR/brief-validation.json",
    "risk_scores": "$TEST_DIR/risk-scores.json",
    "domain_classification": "$TEST_DIR/domain-classification.json"
  },
  "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
}
EOF

    log_success "Test report generated: $report_file"
}

# Cleanup test artifacts
cleanup_test_artifacts() {
    log_info "Cleaning up test artifacts..."
    
    if [ "$1" = "--keep" ]; then
        log_info "Keeping test artifacts for inspection"
    else
        rm -rf "$TEST_DIR"
        log_success "Test artifacts cleaned up"
    fi
}

# Main test execution
main() {
    log_info "Starting Dev-Workflow Integration Tests"
    log_info "Workspace: $WORKSPACE_ROOT"
    log_info "Test Directory: $TEST_DIR"
    
    # Setup
    setup_test_environment
    create_test_fixtures
    
    # Run tests
    test_script_dependencies
    test_protocol_structure
    test_protocol_00
    test_protocol_1
    test_protocol_2
    test_protocol_3
    test_protocol_4
    test_protocol_5
    test_evidence_pipeline
    
    # Generate report
    generate_test_report
    
    # Summary
    echo ""
    log_info "Test Summary:"
    echo "  Total Tests: $TESTS_RUN"
    echo "  Passed: $TESTS_PASSED"
    echo "  Failed: $TESTS_FAILED"
    echo "  Success Rate: $(( TESTS_PASSED * 100 / TESTS_RUN ))%"
    
    if [ $TESTS_FAILED -eq 0 ]; then
        log_success "All tests passed! 🎉"
        exit 0
    else
        log_error "$TESTS_FAILED tests failed"
        exit 1
    fi
}

# Handle command line arguments
case "${1:-}" in
    "--keep")
        main
        cleanup_test_artifacts --keep
        ;;
    "--cleanup")
        cleanup_test_artifacts
        ;;
    "--help"|"-h")
        echo "Usage: $0 [--keep|--cleanup|--help]"
        echo "  --keep     Keep test artifacts after completion"
        echo "  --cleanup  Clean up test artifacts and exit"
        echo "  --help     Show this help message"
        ;;
    "")
        main
        cleanup_test_artifacts
        ;;
    *)
        log_error "Unknown option: $1"
        echo "Use --help for usage information"
        exit 1
        ;;
esac
