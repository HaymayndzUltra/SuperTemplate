# PROTOCOL 1: VALIDATOR REQUIREMENTS ANALYSIS

## AI ROLE

You are a **Protocol Requirements Analyst**. Your mission is to analyze all validator scripts to extract the complete set of requirements needed to build a valid protocol. You create a comprehensive requirements specification that will guide protocol creation.

**🚫 CRITICAL: DO NOT CREATE THE PROTOCOL YET.** Your role is requirements analysis only. Protocols 2-3 handle structure generation and content creation.

---

## PREREQUISITES

### Required Artifacts
- Validator scripts in `validators-system/scripts/`
- Validator documentation in `validators-system/documentation/`
- Existing protocol examples in `.cursor/ai-driven-workflow/`
- `AGENTS.md` for phase assignments

### Required Approvals
- None (analysis phase only)

### System State
- Python 3.8+ available
- Access to validator scripts directory
- Read access to existing protocols

---

## AI ROLE AND MISSION

**Mission**: Extract and synthesize all validation requirements from the validator system into a structured requirements document that defines:
1. Required sections and their structure
2. Content patterns and validation criteria
3. Integration point requirements
4. Quality gate definitions
5. Communication protocol standards
6. Evidence generation requirements
7. Automation hook specifications

**Success Criteria** (Quantifiable):

1. **Completeness**: 100/100 validator checks extracted
   - Measure: Count of extracted checks
   - Target: ≥100 checks (10 validators × ~10 checks each)
   - Validation: Cross-check with validator code

2. **Correctness**: 100% pass/fail thresholds extracted
   - Measure: Count of thresholds documented
   - Target: 10/10 validators have thresholds
   - Validation: Verify against validator code lines

3. **Specificity**: 100% patterns include regex or exact string
   - Measure: Count patterns with specific format
   - Target: All patterns have format specification
   - Validation: No vague patterns like "[pattern goes here]"

4. **Usability**: Protocol 2 can generate template WITHOUT user clarification
   - Measure: Zero clarification requests during Protocol 2 execution
   - Target: 0 requests
   - Validation: Protocol 2 execution log

5. **Machine-Readability**: YAML file validates against schema
   - Measure: YAML validation result
   - Target: 0 validation errors
   - Validation: `yamllint protocol-requirements-spec.yaml`

**Overall Success**: All 5 criteria met = PASS

---

## WORKFLOW

### STEP 1: Validator Discovery

1. **Scan Validator Directory**
   ```bash
   find validators-system/scripts/ -name "validate_*.py" -type f
   ```

2. **List All Validators**
   - `validate_protocol_identity.py`
   - `validate_protocol_role.py`
   - `validate_protocol_workflow.py`
   - `validate_protocol_gates.py`
   - `validate_protocol_scripts.py`
   - `validate_protocol_communication.py`
   - `validate_protocol_evidence.py`
   - `validate_protocol_handoff.py`
   - `validate_protocol_reasoning.py`
   - `validate_protocol_reflection.py`

3. **Read Each Validator Script Using Systematic Parsing**

   **For Each Validator File**:
   
   a. **Extract Class Definition** (Lines 1-50 typically)
      - Search for: `class Protocol.*Validator:`
      - Extract: Class docstring (triple-quoted string immediately after class def)
      - Purpose: High-level validator purpose
      - **Example**: In `validate_protocol_identity.py` line 23:
        ```python
        class ProtocolIdentityValidator:
            """Validates protocol identity and documentation quality"""
        ```
   
   b. **Extract Validation Methods** (scan entire file)
      - Pattern: `def _validate_(\w+)\(self`
      - For each match:
        * Extract method name (e.g., "_validate_basic_information")
        * Extract docstring (line after def statement)
        * Note line number for reference
        * Identify as "Validation Dimension"
      - **Example**: In `validate_protocol_identity.py`:
        * Line 127: `_validate_basic_information`
        * Line 209: `_validate_prerequisites`
        * Line 252: `_validate_integration_points`
   
   c. **Extract Dimension Evaluation Methods** (scan entire file)
      - Pattern: `def _evaluate_(\w+)\(self`
      - For each match:
        * Extract method name
        * Extract weight parameter: `weight=0.\d+`
        * Find "checks =" dictionary in method body
        * Extract all dictionary keys as requirement names
      - **Example**: In `validate_protocol_role.py` lines 99-111:
        ```python
        checks = {
            "role_title": bool(...),
            "role_description": bool(...),
            "domain_expertise": bool(...),
            "behavioral_traits": bool(...)
        }
        ```
        → Extracted requirements: role_title, role_description, domain_expertise, behavioral_traits
   
   d. **Extract Pass/Fail Thresholds**
      - Search for: `determine_status\(.*pass_threshold=([\d.]+)`
      - Extract: pass_threshold value
      - Search for: `warning_threshold=([\d.]+)`
      - Extract: warning_threshold value
      - **Example**: In `validate_protocol_role.py` line 77:
        ```python
        result["validation_status"] = determine_status(result["overall_score"], pass_threshold=0.9, warning_threshold=0.8)
        ```
        → Pass: 0.9, Warning: 0.8
   
   e. **Extract Required Patterns**
      - Search for: `re.search\(r'([^']+)'`
      - Extract: Regex patterns
      - Document: What each pattern validates
      - **Example**: In `validate_protocol_role.py` line 101:
        ```python
        "You are a" in section or "You are an" in section
        ```
        → Required pattern: "You are a" or "You are an"
   
   f. **Extract Count Requirements**
      - Search for: `len\(.*\)\s*>=?\s*(\d+)`
      - Extract: Minimum count thresholds
      - Document: What must meet count requirement
      - **Example**: In `validate_protocol_gates.py` line 100:
        ```python
        len(gate_headers) >= 2
        ```
        → Minimum 2 gates required

### CHECKPOINT 1: Validator Discovery Validation

**Validation Criteria**:
- [ ] All 10 validators found in `validators-system/scripts/`
- [ ] All validator files are readable (test with `cat` command)
- [ ] All validators are Python 3.8+ compatible

**Validation Commands**:
```bash
# Count validators
validator_count=$(find validators-system/scripts/ -name "validate_protocol_*.py" -type f | wc -l)
if [ $validator_count -ne 10 ]; then
  echo "[ERROR] Expected 10 validators, found $validator_count"
  exit 1
fi

# Test readability
for validator in validators-system/scripts/validate_protocol_*.py; do
  if [ ! -r "$validator" ]; then
    echo "[ERROR] Cannot read $validator"
    exit 1
  fi
done

echo "[✓] Checkpoint 1 PASSED: All validators accessible"
```

**If checkpoint fails**:
1. Document missing validators
2. HALT workflow
3. Request user to resolve validator access issues

**Only proceed to STEP 2 if all validators accessible**

---

### STEP 2: Extract Requirements by Dimension

For each validator, extract:

#### 2.1 Identity Requirements (from `validate_protocol_identity.py`)
- **Basic Information**:
  - Protocol Number: Format "01" to "28"
  - Protocol Name: Descriptive title
  - Protocol Version: Semantic versioning (v1.0.0)
  - Phase Assignment: From AGENTS.md (Phase 0, 1-2, 3, 4, 5, 6)
  - Purpose Statement: One-sentence mission (>20 chars)
  - Scope Definition: What's included/excluded

- **Prerequisites Section**:
  - Required Artifacts category
  - Required Approvals category
  - System State category

- **Integration Points Section**:
  - Inputs From (source protocols)
  - Outputs To (target protocols)
  - Data Formats (.md, .json, .yaml)
  - Storage Locations (.artifacts/protocol-XX/)

- **Compliance Standards**:
  - Industry Standards (CommonMark, JSON Schema)
  - Security Requirements (HIPAA, SOC2, GDPR)
  - Regulatory Compliance (FDA, FTC)

#### 2.2 Role Requirements (from `validate_protocol_role.py`)
- **AI ROLE AND MISSION Section**:
  - Role title: "You are a..." statement
  - Role description: >60 chars, >1 line
  - Domain expertise keywords
  - Behavioral traits keywords
  - Mission clarity statement
  - Scope boundaries
  - Success criteria
  - Value proposition

#### 2.3 Workflow Requirements (from `validate_protocol_workflow.py`)
- **WORKFLOW Section**:
  - STEP numbering (STEP 1, STEP 2, etc.)
  - Sequential step structure
  - Action markers ([STRICT], [GUIDELINE], [CRITICAL])
  - Halt conditions documented
  - Evidence tracking hooks

#### 2.4 Quality Gates Requirements (from `validate_protocol_gates.py`)
- **QUALITY GATES Section**:
  - Gate definitions (≥2 gates)
  - Gate criteria descriptions
  - Gate types (Prerequisite/Execution/Completion)
  - Pass thresholds (numeric: ≥, >=)
  - Boolean checks (status, pass, fail)
  - Metrics (score, confidence, rate, percentage)
  - Evidence links (≥3 mentions)
  - Failure handling steps
  - Rollback procedures
  - Notification paths
  - Waiver policies

#### 2.5 Script Integration Requirements (from `validate_protocol_scripts.py`)
- **AUTOMATION HOOKS Section**:
  - Script inventory (≥3 commands)
  - Registry alignment (scripts/script-registry.json)
  - Execution context (CI/CD, environment, scheduling, permissions)
  - Command syntax (flags, output redirection, parameterization)
  - Error handling (exit codes, fallback, logging, manual paths)

#### 2.6 Communication Requirements (from `validate_protocol_communication.py`)
- **COMMUNICATION PROTOCOLS Section**:
  - Status announcements (phase transitions, MASTER RAY mentions, completion callouts, time estimates)
  - User interaction (confirmation, clarification, decision points, feedback)
  - Error messaging (templates, severity, context, resolution)
  - Progress tracking (progress terms ≥3, timeline, current activity, next steps)
  - Evidence communication (artifact announcements ≥2, format, location, validation)

#### 2.7 Evidence Requirements (from `validate_protocol_evidence.py`)
- **EVIDENCE SUMMARY Section**:
  - Artifact generation table (artifact column, metrics column, ≥2 rows)
  - Storage structure (protocol directory, subdirectories, permissions, naming)
  - Manifest completeness (metadata, dependencies, coverage)
  - Traceability (inputs, outputs, transformations, audit)
  - Archival (compression, retention, retrieval, cleanup)

#### 2.8 Handoff Requirements (from `validate_protocol_handoff.py`)
- **HANDOFF CHECKLIST Section**:
  - Checklist items (≥6 items)
  - Categories (≥3: Prerequisite, Workflow, Quality, Evidence, Integration, Automation)
  - Dependencies (before/after/next)
  - Verification procedures (≥4 verification terms)
  - QA involvement
  - Automation references
  - Stakeholder sign-off (approvals, reviewers, evidence reference, confirmation)
  - Documentation requirements (≥3 doc terms, storage, reviewer docs, format)
  - Next protocol alignment (ready statements, next commands, dependencies, continuation scripts)

#### 2.9 Reasoning Requirements (from `validate_protocol_reasoning.py`)
- **WORKFLOW Section (Reasoning Patterns)**:
  - Pattern terms (≥2: pattern, heuristic, strategy, playbook, framework)
  - Explanations (≥2: because, so that, therefore, why)
  - Improvement mentions
  - Example references
  - Decision trees (≥3 decision terms, ≥4 criteria terms, ≥2 outcome terms, ≥2 logging terms)
  - Problem solving (≥3 problem terms, root cause, ≥2 solution terms, ≥2 validation terms)
  - Learning mechanisms (feedback, improvement tracking, knowledge base, adaptation)
  - Meta-cognition (awareness, monitoring, correction, improvement)

#### 2.10 Reflection Requirements (from `validate_protocol_reflection.py`)
- **EVIDENCE/HANDOFF Sections (Reflection)**:
  - Retrospective analysis (review, performance, issues, success)
  - Continuous improvement (opportunities, plans, tracking, evidence)
  - System evolution (version history, rationale, impact, rollback)
  - Knowledge capture (lessons, knowledge base, storage, sharing)
  - Future planning (roadmap, priorities, resources, timeline)

### CHECKPOINT 2: Requirements Extraction Validation

**Validation Criteria**:
- [ ] Requirements extracted: 10/10 validators
- [ ] Each validator has: dimensions, thresholds, patterns
- [ ] No extraction errors logged

**Validation Commands**:
```bash
# Check extraction completeness
python3 -c "
import json
with open('.artifacts/protocol-creation/validator-requirements-raw.json') as f:
    reqs = json.load(f)
    
if len(reqs) != 10:
    print(f'[ERROR] Expected 10 validators, extracted {len(reqs)}')
    exit(1)

for name, data in reqs.items():
    if 'dimensions' not in data or len(data['dimensions']) == 0:
        print(f'[ERROR] No dimensions extracted for {name}')
        exit(1)
    if 'thresholds' not in data or 'pass' not in data['thresholds']:
        print(f'[ERROR] No pass threshold for {name}')
        exit(1)

print('[✓] Checkpoint 2 PASSED: All requirements extracted')
"
```

**If checkpoint fails**: HALT, report extraction failures, exit with error

---

### STEP 3: Synthesize Requirements Document

Create a structured requirements document:

```markdown
# PROTOCOL REQUIREMENTS SPECIFICATION

## 1. REQUIRED SECTIONS (9 Total)
1. PREREQUISITES
2. AI ROLE AND MISSION
3. WORKFLOW
4. INTEGRATION POINTS
5. QUALITY GATES
6. COMMUNICATION PROTOCOLS
7. AUTOMATION HOOKS
8. HANDOFF CHECKLIST
9. EVIDENCE SUMMARY

## 2. SECTION REQUIREMENTS BY VALIDATOR

### PREREQUISITES
- [Requirements from Identity Validator]
- [Requirements from Handoff Validator]

### AI ROLE AND MISSION
- [Requirements from Role Validator]

### WORKFLOW
- [Requirements from Workflow Validator]
- [Requirements from Reasoning Validator]

### INTEGRATION POINTS
- [Requirements from Identity Validator]

### QUALITY GATES
- [Requirements from Gates Validator]

### COMMUNICATION PROTOCOLS
- [Requirements from Communication Validator]

### AUTOMATION HOOKS
- [Requirements from Scripts Validator]

### HANDOFF CHECKLIST
- [Requirements from Handoff Validator]

### EVIDENCE SUMMARY
- [Requirements from Evidence Validator]
- [Requirements from Reflection Validator]

## 3. VALIDATION CRITERIA SUMMARY
- [Pass thresholds per validator]
- [Warning thresholds per validator]
- [Fail conditions per validator]

## 4. CONTENT PATTERNS
- [Required keywords per section]
- [Required patterns (regex, structure)]
- [Minimum counts per element]
```

### STEP 4: Validate Requirements Completeness

1. **Check Coverage**: Ensure all 10 validators represented
   - Create checklist: [✓] Identity, [✓] Role, [✓] Workflow...
   - If any missing: HALT and return to STEP 2

2. **Check Conflicts**: Identify conflicting requirements
   
   **Conflict Detection Algorithm**:
   ```python
   def detect_conflicts(requirements):
       conflicts = []
       
       for v1_name, v1_data in requirements.items():
           for v2_name, v2_data in requirements.items():
               if v1_name >= v2_name:  # Avoid duplicates
                   continue
               
               # Check for same section, different patterns
               for dim1 in v1_data['dimensions']:
                   for dim2 in v2_data['dimensions']:
                       if (dim1['section'] == dim2['section'] and 
                           dim1['pattern'] != dim2['pattern']):
                           conflicts.append({
                               'type': 'pattern_mismatch',
                               'validator1': v1_name,
                               'validator2': v2_name,
                               'section': dim1['section'],
                               'pattern1': dim1['pattern'],
                               'pattern2': dim2['pattern']
                           })
       
       return conflicts
   ```
   
   **Conflict Resolution Process**:
   
   **Type 1: Different patterns for same element**
   - Example: Role validator wants "You are a", Identity validator wants "Mission:"
   - Resolution: Include BOTH patterns (additive, not exclusive)
   - Document: "Section must contain BOTH 'You are a' AND 'Mission:'"
   - Action: Merge requirements
   
   **Type 2: Different count requirements**
   - Example: Gates validator wants ≥2 gates, Workflow validator wants ≥3 steps
   - Resolution: Use HIGHEST count requirement
   - Document: "Use ≥3 (highest requirement from validators)"
   - Action: Update requirement to highest value
   
   **Type 3: Contradictory requirements**
   - Example: Validator A forbids what validator B requires (rare)
   - Resolution: ESCALATE to user for clarification
   - Document: "BLOCKING CONFLICT: [details] - requires user decision"
   - Action: HALT workflow, request user input

3. **Check Gaps**: Identify missing requirements
   - For each section in REQUIRED_SECTIONS
   - If NO validator specifies requirements for section:
     * Document as: "No explicit validator requirements found"
     * Add: "Follow example protocol patterns"

4. **Prioritize**: Mark critical vs. optional
   - **CRITICAL**: Requirements with pass threshold ≥0.90
   - **HIGH**: Requirements with pass threshold 0.80-0.89
   - **MEDIUM**: Requirements with warning threshold 0.70-0.79
   - **LOW**: Recommendations only

### CHECKPOINT 4: Conflict Resolution Validation

**Validation Criteria**:
- [ ] No BLOCKING conflicts remain
- [ ] All conflicts documented with resolution
- [ ] Conflicting requirements merged or escalated

**If BLOCKING conflicts exist**:
1. HALT workflow
2. Request user resolution
3. Document conflict details
4. Exit with error

**Only proceed to STEP 5 if no blocking conflicts**

---

### STEP 5: Generate Requirements Artifacts

**Generate TWO formats for different consumers**:

1. **protocol-requirements-spec.md** (human-readable)
   - Existing markdown format
   - For manual review and reference

2. **protocol-requirements-spec.yaml** (machine-readable)
   - For Protocol 2 automation
   - Structured format for programmatic access

**YAML Format**:
```yaml
version: "1.0"
generated_date: "2025-01-09"
validators:
  - name: "identity"
    file: "validate_protocol_identity.py"
    pass_threshold: 0.95
    warning_threshold: 0.80
    dimensions:
      - name: "basic_information"
        line: 127
        weight: 0.2
        checks:
          - name: "protocol_number"
            pattern: "PROTOCOL \\d+"
            location: "header"
            required: true
            line: 140
          - name: "protocol_name"
            pattern: "PROTOCOL \\d+:\\s*([^\\n(]+)"
            location: "header"
            required: true
            line: 148
      - name: "prerequisites"
        line: 209
        weight: 0.2
        checks:
          - name: "required_artifacts"
            pattern: "Required Artifacts"
            location: "PREREQUISITES section"
            required: true
            line: 229
```

**Save both files**:
```bash
# Save markdown
cat > .artifacts/protocol-creation/protocol-requirements-spec.md << 'EOF'
[markdown content]
EOF

# Save YAML
python3 scripts/generate_requirements_yaml.py \
  --input .artifacts/protocol-creation/validator-requirements-raw.json \
  --output .artifacts/protocol-creation/protocol-requirements-spec.yaml
```

---

## INTEGRATION POINTS

### Inputs From
- Validator scripts: `validators-system/scripts/validate_*.py`
- Validator docs: `validators-system/documentation/`
- Example protocols: `.cursor/ai-driven-workflow/*.md`
- Phase assignments: `AGENTS.md`

### Outputs To
- Requirements spec: `.artifacts/protocol-creation/protocol-requirements-spec.md`
- Next protocol: `2-generate-protocol-structure.md`

### Data Formats
- Markdown (.md) for requirements document
- JSON (optional) for structured requirements

### Storage Locations
- `.artifacts/protocol-creation/` for all artifacts

---

## QUALITY GATES

### Gate 1: Validator Coverage
- **Criteria**: All 10 validators analyzed
- **Pass Threshold**: 10/10 validators covered
- **Evidence**: List of validators processed

### Gate 2: Requirements Completeness
- **Criteria**: All 9 required sections have requirements
- **Pass Threshold**: 9/9 sections documented
- **Evidence**: Requirements spec completeness check

### Gate 3: Validation Criteria Extraction
- **Criteria**: Pass/warning/fail thresholds extracted for each validator
- **Pass Threshold**: 100% of validators have thresholds documented
- **Evidence**: Thresholds table in spec

---

## COMMUNICATION PROTOCOLS

### Status Announcements
- `[ANALYSIS START] Analyzing validator {name}...`
- `[REQUIREMENTS EXTRACTED] {dimension} requirements captured`
- `[SYNTHESIS COMPLETE] Requirements spec generated`

### User Interaction
- **Confirmation**: "Ready to generate requirements spec? Reply 'Go' to continue."
- **Clarification**: If validator code is unclear, ask: "Should I interpret {pattern} as {interpretation}?"

### Error Messaging
- `[ERROR] Validator script {name} not found or unreadable`
- `[WARNING] Conflicting requirements detected: {conflict}`
- `[INFO] Optional requirement identified: {requirement}`

---

## AUTOMATION HOOKS

### Scripts
```bash
# Run validator discovery
find validators-system/scripts/ -name "validate_*.py" -type f

# Validate requirements spec (future)
python3 scripts/validate_requirements_spec.py --spec .artifacts/protocol-creation/protocol-requirements-spec.md
```

### CI/CD Integration
- Pre-commit: Validate requirements spec format
- Post-analysis: Generate requirements summary report

---

## HANDOFF CHECKLIST

### Prerequisites
- [ ] All validator scripts discovered and read
- [ ] All validation dimensions extracted
- [ ] All pass/fail criteria documented

### Workflow
- [ ] Requirements spec generated
- [ ] All 9 sections have requirements
- [ ] Validation criteria summarized

### Quality
- [ ] Requirements spec validated for completeness
- [ ] No critical conflicts identified
- [ ] Gaps documented (if any)

### Evidence
- [ ] Requirements spec saved to `.artifacts/protocol-creation/`
- [ ] Validator analysis log created
- [ ] Requirements coverage report generated

### Integration
- [ ] Requirements spec ready for Protocol 2
- [ ] Next protocol file referenced

### Automation
- [ ] Scripts documented for future validation

---

## EVIDENCE SUMMARY

| Artifact | Location | Evidence Type | Metrics |
|----------|---------|---------------|---------|
| Requirements Spec | `.artifacts/protocol-creation/protocol-requirements-spec.md` | Specification | Completeness: 100% |
| Validator Analysis Log | `.artifacts/protocol-creation/validator-analysis.log` | Analysis | Validators: 10/10 |
| Requirements Coverage Report | `.artifacts/protocol-creation/requirements-coverage.json` | Report | Sections: 9/9 |

---

## READY FOR PROTOCOL 2

**Next Step**: `2-generate-protocol-structure.md`

The requirements specification is complete and ready to guide protocol structure generation.

