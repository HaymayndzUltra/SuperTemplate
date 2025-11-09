# Protocol Creation Workflow

This workflow creates complete, validator-compliant AI workflow protocols based on the validator system requirements.

## Overview

The protocol creation workflow consists of 5 sequential protocols that transform validator requirements into a production-ready protocol document:

1. **1-analyze-validator-requirements.md** (684 lines) - Analyzes all 10 validators to extract requirements
2. **2-generate-protocol-structure.md** (645 lines) - Generates protocol structure template with placeholders
3. **3-create-protocol-content.md** (567 lines) - Populates structure with validator-compliant content
4. **4-validate-protocol.md** (644 lines) - Validates protocol and fixes all issues automatically
5. **5-protocol-retrospective.md** (625 lines) - Reviews process with quantitative scoring and improvement prioritization

## Workflow Flow

```
Protocol 1: Requirements Analysis
    ↓
    Creates: protocol-requirements-spec.md
    ↓
Protocol 2: Structure Generation
    ↓
    Creates: protocol-structure-template.md
    ↓
Protocol 3: Content Creation
    ↓
    Creates: XX-protocol-name.md
    ↓
Protocol 4: Validation
    ↓
    Creates: validation-report-XX.md
    ↓
Protocol 5: Retrospective
    ↓
    Creates: retrospective-XX.md
    ↓
PRODUCTION-READY PROTOCOL
```

## Quick Start

### Step 1: Analyze Validator Requirements
**Purpose**: Extract all validation requirements from 10 validator scripts  
**Output**: `protocol-requirements-spec.md` with complete requirements

```bash
@apply dev-workflow/protocol-creation/1-analyze-validator-requirements.md
```

**Key Features**:
- Systematic parsing of validator code (class definitions, validation methods, thresholds)
- Conflict detection and resolution
- Machine-readable YAML output for automation
- Checkpoint validation at each step

---

### Step 2: Generate Protocol Structure
**Purpose**: Create complete protocol skeleton with typed placeholders  
**Output**: `protocol-structure-template.md` ready for content population

```bash
@apply dev-workflow/protocol-creation/2-generate-protocol-structure.md
```

**Key Features**:
- All 9 required sections with validator mappings
- Typed placeholder system (string, enum, number, path, list)
- Validator requirement comments embedded in template
- Structure validation before handoff

---

### Step 3: Create Protocol Content
**Purpose**: Populate template with validator-compliant content  
**Output**: Complete protocol file in `.cursor/ai-driven-workflow/`

```bash
@apply dev-workflow/protocol-creation/3-create-protocol-content.md
```

**User Input Required**:
- Protocol number (01-28)
- Protocol name and purpose
- Protocol phase (0, 1-2, 3, 4, 5, 6)
- Integration points (input/output protocols)
- Main workflow steps

**Key Features**:
- Pre-validation checks after each section
- Content pattern library with exact validator requirements
- Role validator compliance guide with examples
- Automatic placeholder replacement

---

### Step 4: Validate Protocol
**Purpose**: Run all validators and automatically fix issues  
**Output**: Validated protocol + validation report

```bash
@apply dev-workflow/protocol-creation/4-validate-protocol.md
```

**Key Features**:
- Runs all 10 validators + master validator
- 5 issue classification types (missing content, insufficient count, pattern mismatch, format error, keyword missing)
- Automatic fix application with verification
- Maximum 3 iteration loops with escalation
- Comprehensive validation report generation

---

### Step 5: Retrospective Review
**Purpose**: Quantitative quality assessment and improvement prioritization  
**Output**: Retrospective report + improvement plan

```bash
@apply dev-workflow/protocol-creation/5-protocol-retrospective.md
```

**Key Features**:
- **Quantitative Scoring** (0-100): Clarity, Completeness, Accuracy, Consistency
- **Improvement Prioritization Matrix**: Impact/Effort scoring with Do Now/Next Sprint/Backlog tiers
- **Benchmark Comparison**: Compare against best protocol, average, and target standards
- **Continuous Improvement Tracking**: JSON-based iteration log with lessons learned
- **Automation Scripts**: Quality scorer and improvement prioritizer

## Artifacts

All artifacts are stored in `.artifacts/protocol-creation/`:

### Core Artifacts
- `protocol-requirements-spec.md` - Complete requirements from validators (Protocol 1)
- `protocol-requirements-spec.yaml` - Machine-readable requirements (Protocol 1)
- `protocol-structure-template.md` - Protocol structure template (Protocol 2)
- `XX-protocol-name.md` - Final protocol file in `.cursor/ai-driven-workflow/` (Protocol 3)
- `validation-report-XX.md` - Validation results and fixes (Protocol 4)
- `retrospective-XX.md` - Retrospective review and improvements (Protocol 5)

### Quality & Improvement Artifacts (Protocol 5)
- `quality-score-XX.json` - Quantitative quality scores (0-100)
- `improvement-plan-XX.md` - Prioritized improvement plan with impact/effort matrix
- `improvement-log.json` - Iteration tracking with lessons learned
- `sample-improvements.json` - Example improvements data for testing

### Validation Artifacts (Protocol 4)
- `.artifacts/validation/protocol-XX-master-report.json` - Master validator results
- `.artifacts/validation/protocol-XX-identity.json` - Identity validator results
- `.artifacts/validation/protocol-XX-role.json` - Role validator results
- `.artifacts/validation/protocol-XX-*.json` - All 10 validator results

## Validator Requirements

The workflow ensures protocols meet all requirements from 10 validators:

1. **Identity Validator** - Basic info, prerequisites, integration, compliance, documentation
2. **Role Validator** - AI role, mission, constraints, outputs, behavior
3. **Workflow Validator** - Structure, steps, markers, halt conditions, evidence
4. **Quality Gates Validator** - Gate definitions, criteria, automation, failure handling
5. **Scripts Validator** - Automation hooks, registry alignment, execution context
6. **Communication Validator** - Status announcements, user interaction, error messaging
7. **Evidence Validator** - Artifact generation, storage, manifest, traceability
8. **Handoff Validator** - Checklist, verification, signoff, documentation, next protocol
9. **Reasoning Validator** - Reasoning patterns, decision trees, problem solving
10. **Reflection Validator** - Retrospective, improvement, evolution, knowledge capture

## Required Sections

Every protocol must include these 9 sections:

1. **PREREQUISITES** - Required artifacts, approvals, system state
2. **AI ROLE AND MISSION** - Role definition, mission statement, constraints
3. **WORKFLOW** - Step-by-step execution instructions
4. **INTEGRATION POINTS** - Inputs, outputs, data formats, storage
5. **QUALITY GATES** - Validation criteria and thresholds
6. **COMMUNICATION PROTOCOLS** - Status, interaction, error, progress, evidence
7. **AUTOMATION HOOKS** - Scripts, registry, execution context, error handling
8. **HANDOFF CHECKLIST** - Prerequisites, workflow, quality, evidence, integration
9. **EVIDENCE SUMMARY** - Artifacts, storage, manifest, traceability, archival

## Validation Criteria

Protocols must pass all validators with:

- **Master Validator**: Status = PASS, Score ≥0.90
- **Identity Validator**: Score ≥0.95
- **Role Validator**: Score ≥0.90
- **Workflow Validator**: Score ≥0.90
- **Quality Gates Validator**: Score ≥0.92
- **Scripts Validator**: Score ≥0.90
- **Communication Validator**: Score ≥0.90
- **Evidence Validator**: Score ≥0.90
- **Handoff Validator**: Score ≥0.90
- **Reasoning Validator**: Score ≥0.85
- **Reflection Validator**: Score ≥0.85

## Automation Scripts

The workflow includes automation scripts for quality assessment and improvement management:

### Quality Score Calculator
**Script**: `scripts/calculate_protocol_quality_score.py`  
**Purpose**: Calculate quantitative quality score (0-100) for protocols

```bash
python3 scripts/calculate_protocol_quality_score.py \
  --protocol .cursor/ai-driven-workflow/XX-protocol-name.md \
  --validators .artifacts/validation/protocol-XX-*.json \
  --output quality-score-XX.json \
  --verbose
```

**Scoring Breakdown**:
- **Clarity** (0-25): Readability, sentence length, technical terms, examples
- **Completeness** (0-25): Required sections, no placeholders, no TODOs
- **Accuracy** (0-25): Validator scores, line references, code syntax
- **Consistency** (0-25): Naming conventions, section order, formatting, terminology

**Dependencies**: `pip install textstat numpy nltk`

---

### Improvement Prioritizer
**Script**: `scripts/prioritize_improvements.py`  
**Purpose**: Prioritize improvements using impact/effort matrix

```bash
python3 scripts/prioritize_improvements.py \
  --improvements improvements-XX.json \
  --output prioritized-XX.json \
  --markdown improvement-plan-XX.md \
  --verbose
```

**Priority Formula**: `(Impact×3 + (4-Effort)) / 7`
- **Do Now** (>0.7): High impact improvements
- **Next Sprint** (0.4-0.7): Medium priority
- **Backlog** (<0.4): Low priority

**Output**: Sorted list with estimated time, expected impact, and owner assignment

---

## Best Practices

1. **Follow the Sequence**: Execute protocols 1-5 in order without skipping
2. **Provide Complete Context**: Give detailed protocol information in Protocol 3
3. **Fix All Issues**: Address all validation failures before proceeding to Protocol 5
4. **Document Improvements**: Capture lessons learned in Protocol 5 retrospective
5. **Validate Thoroughly**: Run all validators and achieve PASS status (≥0.90)
6. **Use Automation**: Leverage quality scorer and prioritizer scripts for data-driven decisions
7. **Track Progress**: Maintain improvement log for continuous learning

## Recent Enhancements (Protocol 5)

Protocol 5 was recently upgraded with **data-driven continuous improvement capabilities**:

### 1. Quantitative Scoring System ✅
**Before**: Subjective quality assessment  
**After**: 0-100 point scoring across 4 dimensions

- Replaces vague assessments with measurable metrics
- Enables tracking quality improvements over time
- Provides objective comparison between protocols

### 2. Improvement Prioritization Matrix ✅
**Before**: Simple categorization (Immediate/Short-term/Long-term)  
**After**: Impact/Effort scoring with priority formula

- Calculates priority scores (0-1) using `(Impact×3 + (4-Effort)) / 7`
- Automatically categorizes into Do Now/Next Sprint/Backlog
- Includes estimated time and expected impact for each improvement

### 3. Benchmark Comparison ✅
**Before**: No comparative analysis  
**After**: Compare against best protocol, average, and targets

- Rank protocols by percentile
- Show performance vs best and average
- Track creation efficiency metrics (time, revisions, first-pass success)

### 4. Continuous Improvement Tracking ✅
**Before**: No iteration history  
**After**: JSON-based improvement log with lessons learned

- Track validator scores across iterations
- Document issues and fixes applied
- Capture lessons learned for future protocols
- Analyze trends across all protocols

**Impact**: Protocol quality scores expected to increase **15% per iteration**, creation time to decrease **20%**, and first-pass success rate to improve from **30% to 85%**.

---

## Troubleshooting

### Validator Failures (Protocol 4)
- Read the validator JSON file for specific issues
- Protocol 4 automatically classifies and fixes 5 issue types
- Maximum 3 iteration loops before escalation
- Check validation report for detailed fix history

### Missing Requirements (Protocol 1)
- Review the requirements spec from Protocol 1
- Check for conflicts in requirements
- Verify all 10 validators were analyzed
- Consult validator documentation

### Structure Issues (Protocol 2)
- Verify all 9 sections present
- Check section order matches template
- Validate markdown syntax
- Ensure all placeholders have type specifications

### Content Issues (Protocol 3)
- Use pre-validation checks after each section
- Reference content pattern library for exact requirements
- Check Role Validator compliance guide for "You are a" pattern
- Verify all required keywords present

## Related Documentation

- Validator System: `validators-system/documentation/`
- Example Protocols: `.cursor/ai-driven-workflow/`
- Phase Assignments: `AGENTS.md`

## Support

For issues or questions:
1. Review the validator documentation in `validators-system/documentation/`
2. Check example protocols in `.cursor/ai-driven-workflow/`
3. Review retrospective reports in `.artifacts/protocol-creation/`
4. Consult the requirements specification from Protocol 1
5. Run automation scripts with `--verbose` flag for detailed output

---

## Workflow Statistics

### Protocol Files
- **Total Protocols**: 5
- **Total Lines**: 3,165 lines
- **Average Length**: 633 lines per protocol

| Protocol | Lines | Purpose |
|----------|-------|---------|
| Protocol 1 | 684 | Requirements Analysis |
| Protocol 2 | 645 | Structure Generation |
| Protocol 3 | 567 | Content Creation |
| Protocol 4 | 644 | Validation & Fixing |
| Protocol 5 | 625 | Retrospective & Improvement |

### Validation Coverage
- **Validators**: 10 validators + 1 master validator
- **Required Sections**: 9 sections per protocol
- **Pass Thresholds**: 0.85-0.95 depending on validator
- **Quality Gates**: 2-3 gates per protocol

### Automation
- **Scripts**: 2 automation scripts (quality scorer, improvement prioritizer)
- **Dependencies**: Python 3.8+, textstat, numpy, nltk
- **Artifact Types**: 4 types (core, quality, improvement, validation)

### Success Metrics (Protocol 5 Targets)
- **Quality Score Increase**: +15% per iteration
- **Creation Time Decrease**: -20% over time
- **First-Pass Success**: 30% → 85%
- **Validator Pass Rate**: 100% (all protocols must pass)

---

## Version History

### v1.1 (2025-01-09) - Protocol 5 Enhancement
- ✅ Added quantitative scoring system (0-100 points)
- ✅ Added improvement prioritization matrix
- ✅ Added benchmark comparison framework
- ✅ Added continuous improvement tracking
- ✅ Created automation scripts (quality scorer, prioritizer)
- ✅ Updated README with comprehensive documentation

### v1.0 (Initial Release)
- ✅ Protocol 1: Validator Requirements Analysis
- ✅ Protocol 2: Protocol Structure Generation
- ✅ Protocol 3: Protocol Content Creation
- ✅ Protocol 4: Protocol Validation
- ✅ Protocol 5: Protocol Retrospective (basic)

