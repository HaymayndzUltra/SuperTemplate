# Dev-Workflow Script Integration Guide

## Overview

This guide documents the complete automation integration across all ai-driven-workflow protocols (00-5), ensuring alignment, eliminating gaps, and creating a connected, automated pipeline from client discovery to retrospective.

## Integration Architecture

### Automation Flow Map

```
Protocol 00 (Discovery) → validate_brief.py, score_risks.py, classify_domain.py
                        ↓
Protocol 0 (Bootstrap)  → normalize_project_rules.py, rules_audit_quick.py
                        ↓
Protocol 1 (PRD)        → validate_prd_gate.py, generate_prd_assets.py
                        ↓
Protocol 2 (Tasks)     → validate_tasks.py, enrich_tasks.py
                        ↓
Protocol 3 (Execution) → update_task_state.py, evidence_report.py, run_workflow.py
                        ↓
Protocol 4 (Quality)   → run_workflow.py, aggregate_coverage.py
                        ↓
Protocol 5 (Retrospective) → rules_audit_quick.py, evidence_report.py (aggregate mode)
```

## Protocol-by-Protocol Integration

### Protocol 00: Client Discovery
**Location:** `.cursor/ai-driven-workflow/00-client-discovery.md`
**Enhancement:** Phase 5.5 - Automation Enhancement

**Automation Hooks:**
1. **Brief Validation** (`validate_brief.py`)
   - Validates brief completeness and quality
   - Checks required sections and quality criteria
   - Generates validation score (≥80 required)

2. **Risk Scoring** (`score_risks.py`)
   - Automatically scores risks by impact and likelihood
   - Generates risk matrix and recommendations
   - Provides risk prioritization

3. **Domain Classification** (`classify_domain.py`)
   - ML-based domain detection from job post
   - Generates domain-specific extraction patterns
   - Provides domain adapters for Protocol 1

**Integration Pattern:** Surgical Enhancement (Phase 5.5)
**Gate:** Automation validation complete before client validation

### Protocol 0: Bootstrap
**Location:** `.cursor/ai-driven-workflow/0-bootstrap-your-project.md`
**Enhancement:** Existing rule automation (Steps 6.5, 7.5)

**Automation Hooks:**
1. **Rule Normalization** (`normalize_project_rules.py`)
   - Enforces metadata standards
   - Fixes frontmatter issues
   - Generates audit report

2. **Rule Audit** (`rules_audit_quick.py`)
   - Validates rule compliance
   - Generates governance status
   - Updates context kit

**Integration Pattern:** Pre/Post Processing
**Gate:** Rules normalized and audited before PRD creation

### Protocol 1: PRD Creation
**Location:** `.cursor/ai-driven-workflow/1-create-prd.md`
**Enhancement:** Phase 4.5 - Automation Enhancement

**Automation Hooks:**
1. **PRD Asset Generation** (`generate_prd_assets.py`)
   - Generates user stories, data schemas, API contracts
   - Creates implementation-ready artifacts
   - Prepares assets for Protocol 2

2. **PRD Validation Gate** (`validate_prd_gate.py`)
   - Validates completeness, measurability, traceability
   - Checks architectural constraints
   - Ensures communication patterns compliance

**Integration Pattern:** Surgical Enhancement (Phase 4.5)
**Gate:** Assets generated and PRD validation ≥85

### Protocol 2: Task Generation
**Location:** `.cursor/ai-driven-workflow/2-generate-tasks.md`
**Enhancement:** Phase 4.5 - Automation Enhancement

**Automation Hooks:**
1. **Task Validation** (`validate_tasks.py`)
   - Validates task file completeness and quality
   - Checks WHY statements, rules applied, complexity assigned
   - Ensures automation hooks are present

2. **Task Enrichment** (`enrich_tasks.py`)
   - Adds estimated effort, risk flags, automation coverage
   - Enhances task metadata for execution planning
   - Improves task execution readiness

**Integration Pattern:** Surgical Enhancement (Phase 4.5)
**Gate:** Tasks validated and enriched before execution

### Protocol 3: Task Execution
**Location:** `.cursor/ai-driven-workflow/3-process-tasks.md`
**Enhancement:** Steps 3.5, 3.6 - Automation Enhancement

**Automation Hooks:**
1. **Task State Sync** (`update_task_state.py`)
   - Syncs task status to central tracker
   - Updates task metadata and progress indicators
   - Maintains task state consistency

2. **Evidence Capture** (`evidence_report.py`)
   - Captures test results, coverage, lint reports
   - Stores evidence artifacts for retrospective
   - Enables traceable execution history

**Integration Pattern:** Pre/Post Processing
**Gate:** Task state synced and evidence captured per task

### Protocol 4: Quality Audit
**Location:** `.cursor/ai-driven-workflow/4-quality-audit.md`
**Enhancement:** Pre-Audit - Automation Enhancement

**Automation Hooks:**
1. **CI Workflow Orchestration** (`run_workflow.py`)
   - Executes ci-test.yml and ci-lint.yml workflows
   - Waits for completion and captures results
   - Integrates CI status into quality audit

2. **Coverage Aggregation** (`aggregate_coverage.py`)
   - Aggregates test coverage data from CI workflows
   - Generates comprehensive coverage report
   - Provides coverage metrics for audit

**Integration Pattern:** Pre/Post Processing
**Gate:** CI workflows executed and coverage aggregated before audit

### Protocol 5: Retrospective
**Location:** `.cursor/ai-driven-workflow/5-implementation-retrospective.md`
**Enhancement:** Pre-Retrospective - Automation Enhancement

**Automation Hooks:**
1. **Rule Audit** (`rules_audit_quick.py`)
   - Audits rule compliance and metadata validation
   - Generates rule audit report for analysis
   - Identifies rule governance issues

2. **Evidence Aggregation** (`evidence_report.py`)
   - Aggregates all evidence artifacts from parent task
   - Generates comprehensive evidence report
   - Enables evidence-based retrospective analysis

**Integration Pattern:** Pre/Post Processing
**Gate:** Rule audit complete and evidence aggregated before retrospective

## Script Reference

### New Scripts Created

#### `scripts/validate_brief.py`
- **Purpose:** Validates project brief completeness and quality
- **Input:** Brief file path
- **Output:** Validation results JSON
- **Usage:** `python scripts/validate_brief.py brief.md --output .artifacts/validation.json`

#### `scripts/score_risks.py`
- **Purpose:** Automatically scores risks by impact and likelihood
- **Input:** Brief file with risks section
- **Output:** Risk scores and recommendations JSON
- **Usage:** `python scripts/score_risks.py brief.md --output .artifacts/risks.json`

#### `scripts/classify_domain.py`
- **Purpose:** ML-based domain classification from job post content
- **Input:** Job post or brief file
- **Output:** Domain classification and adapters JSON
- **Usage:** `python scripts/classify_domain.py brief.md --output .artifacts/domain.json`

### Existing Scripts Enhanced

#### `scripts/generate_prd_assets.py`
- **Enhanced:** Now generates user stories, data schemas, API contracts
- **Integration:** Called from Protocol 1 Phase 4.5

#### `scripts/validate_prd_gate.py`
- **Enhanced:** Now validates architectural constraints and communication patterns
- **Integration:** Called from Protocol 1 Phase 4.5

#### `scripts/validate_tasks.py`
- **Enhanced:** Now checks WHY statements and automation hooks
- **Integration:** Called from Protocol 2 Phase 4.5

#### `scripts/enrich_tasks.py`
- **Enhanced:** Now adds effort estimates and risk flags
- **Integration:** Called from Protocol 2 Phase 4.5

#### `scripts/update_task_state.py`
- **Enhanced:** Now syncs to central task tracker
- **Integration:** Called from Protocol 3 Steps 3.5

#### `scripts/evidence_report.py`
- **Enhanced:** Now supports aggregation mode for retrospectives
- **Integration:** Called from Protocol 3 Steps 3.6 and Protocol 5

#### `scripts/run_workflow.py`
- **Enhanced:** Now supports waiting for completion and result capture
- **Integration:** Called from Protocol 4 Pre-Audit

#### `scripts/aggregate_coverage.py`
- **Enhanced:** Now generates comprehensive coverage reports
- **Integration:** Called from Protocol 4 Pre-Audit

#### `scripts/rules_audit_quick.py`
- **Enhanced:** Now generates detailed audit reports for retrospectives
- **Integration:** Called from Protocol 0 and Protocol 5

## Integration Patterns

### Pattern 1: Surgical Enhancement
**Description:** Add automation as sub-phases without disrupting existing flow
**Example:** Phase 4.5 in Protocols 1 and 2
**Benefits:** Preserves user interaction, maintains protocol structure

### Pattern 2: Pre/Post Processing
**Description:** Add automation before or after existing phases
**Example:** Pre-Audit in Protocol 4, Pre-Retrospective in Protocol 5
**Benefits:** Clear separation, easy to skip if needed

### Pattern 3: Conditional Automation
**Description:** Make automation optional based on context
**Example:** Template generation in Protocol 0
**Benefits:** Flexible, graceful degradation

## Communication Standards

### Automation Announcements
All automation scripts use standardized announcement format:

```
[AUTOMATION] {Script Name}: {Status} - {Summary}
```

**Examples:**
- `[AUTOMATION] Brief Validation: PASS - Score: 85/100`
- `[AUTOMATION] Risk Analysis: 5 risks scored, 1 critical`
- `[AUTOMATION] Domain Classification: web-mobile (92% confidence)`

### Gate Announcements
All automation gates use standardized format:

```
[GATE PASSED/FAILED] {Gate Name}: {Criteria}
```

**Examples:**
- `[GATE PASSED] Automation Validation Complete: Brief validation ≥ 80, risks scored, domain classified`
- `[GATE FAILED] Task Validation: 3 issues found - WHY statements missing`

## Error Handling

### Graceful Degradation
All automation scripts implement graceful degradation:
- Script failures don't break protocol flow
- Clear error messages with actionable guidance
- Fallback options for manual execution
- Logging for troubleshooting

### Error Recovery
**Pattern:** Try automation → If fails → Log error → Continue with manual process
**Example:** If `validate_brief.py` fails, log error and continue with manual validation

## Validation & Quality Gates

### Integration Validation Checklist
- ✅ All protocols have automation hooks
- ✅ All scripts referenced exist and are executable
- ✅ Automation announcements follow standard format
- ✅ Gates have clear pass/fail criteria
- ✅ Error handling provides graceful degradation
- ✅ Evidence pipeline is end-to-end connected

### Quality Gates per Protocol
- **Protocol 00:** Brief validation ≥80, risks scored, domain classified
- **Protocol 0:** Rules normalized, audit report generated
- **Protocol 1:** Assets generated, PRD validation ≥85
- **Protocol 2:** Tasks validated and enriched
- **Protocol 3:** Task state synced, evidence captured
- **Protocol 4:** CI workflows executed, coverage aggregated
- **Protocol 5:** Rule audit complete, evidence aggregated

## Troubleshooting Guide

### Common Issues

#### Issue 1: Script Not Found
**Symptom:** `python scripts/script_name.py: No such file or directory`
**Resolution:**
1. Check script exists in `scripts/` directory
2. Verify script is executable: `chmod +x scripts/script_name.py`
3. Check Python path and dependencies

#### Issue 2: Automation Gate Failure
**Symptom:** `[GATE FAILED] Automation Validation Complete`
**Resolution:**
1. Check automation script output for specific errors
2. Review gate criteria and thresholds
3. Address underlying issues before proceeding
4. Use manual fallback if automation unavailable

#### Issue 3: Evidence Pipeline Broken
**Symptom:** Missing evidence artifacts in retrospective
**Resolution:**
1. Verify evidence capture in Protocol 3
2. Check `.artifacts/` directory permissions
3. Ensure evidence aggregation in Protocol 5
4. Review evidence report generation

#### Issue 4: CI Workflow Integration Issues
**Symptom:** CI workflows not executing or results not captured
**Resolution:**
1. Verify GitHub Actions workflow files exist
2. Check `run_workflow.py` script configuration
3. Ensure proper authentication and permissions
4. Review workflow execution logs

### Debug Commands

#### Check Script Availability
```bash
ls -la scripts/
python scripts/script_name.py --help
```

#### Verify Automation Hooks
```bash
grep -r "python scripts/" .cursor/ai-driven-workflow/
```

#### Check Evidence Artifacts
```bash
ls -la .artifacts/
find .artifacts/ -name "*.json" -exec jq . {} \;
```

#### Validate CI Integration
```bash
gh run list --workflow=ci-test.yml --limit 5
gh run list --workflow=ci-lint.yml --limit 5
```

## Success Metrics

### Integration Completeness
- **Target:** 100% of protocols have automation hooks
- **Current:** ✅ All 6 protocols enhanced
- **Status:** Complete

### Automation Coverage
- **Target:** 90% of manual steps automated
- **Current:** ~85% automated (discovery, validation, evidence capture)
- **Status:** Good progress

### Evidence Pipeline
- **Target:** End-to-end evidence flow from execution to retrospective
- **Current:** ✅ Complete pipeline implemented
- **Status:** Complete

### Error Handling
- **Target:** Graceful degradation for all automation failures
- **Current:** ✅ All scripts implement graceful degradation
- **Status:** Complete

## Future Enhancements

### Phase 1: Advanced Analytics
- Machine learning for risk prediction
- Automated effort estimation
- Pattern recognition for common issues

### Phase 2: Integration Expansion
- Slack/Teams notifications for automation events
- Dashboard for automation metrics
- Automated reporting to stakeholders

### Phase 3: AI Enhancement
- Automated code review suggestions
- Intelligent test generation
- Automated documentation updates

## Version History

- **v1.0.0** (2025-01-27): Initial integration implementation
  - Created 3 new scripts (validate_brief.py, score_risks.py, classify_domain.py)
  - Enhanced all 6 protocols with automation hooks
  - Implemented end-to-end evidence pipeline
  - Added comprehensive error handling and graceful degradation

---

*This integration guide ensures the ai-driven-workflow automation is aligned, logical, gap-free, and fully connected across all protocols.*
