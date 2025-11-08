# IMPLEMENTATION PROMPT: PROTOCOL 1 IMPROVEMENTS

Copy this entire prompt and use it to implement improvements to Protocol 1.

---

## TASK

Improve `/home/haymayndz/SuperTemplate/dev-workflow/protocol-creation/1-analyze-validator-requirements.md` based on meta-analysis findings.

**Goal**: Transform vague "extract requirements" instructions into exact, executable validator parsing algorithm with specific line numbers, patterns, and validation checkpoints.

---

## CONTEXT

**Meta-Analysis Findings**:
- **Specificity Score**: 3/10 (CRITICAL)
- **Main Issues**: 
  1. Says "Read Each Validator Script" without HOW to parse Python code
  2. No conflict resolution process
  3. No validation checkpoints between steps
  4. Requirements spec format not machine-readable

**Reference Documents**:
- Meta-analysis: `.artifacts/protocol-creation/meta-analysis/01-PROTOCOL-1-ANALYSIS.md`
- Gap filling: `.artifacts/protocol-creation/meta-analysis/06-GAP-FILLING-REQUIREMENTS.md`

---

## IMPROVEMENTS TO IMPLEMENT

### IMPROVEMENT 1: Replace STEP 1 Lines 65-69 (CRITICAL)

**Current** (Lines 65-69):
```markdown
3. **Read Each Validator Script**
   - Extract validation dimensions
   - Extract pass/fail criteria
   - Extract required patterns
   - Extract expected content
```

**Replace With**:
```markdown
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
```

---

### IMPROVEMENT 2: Add Validation Checkpoints (HIGH)

**Location**: After each STEP

**Add After STEP 1**:
```markdown
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
```

**Add After STEP 2**:
```markdown
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
```

**Add After STEP 4**:
```markdown
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
```

---

### IMPROVEMENT 3: Add Conflict Resolution Process (HIGH)

**Location**: STEP 4, replace lines 250-254

**Current**:
```markdown
1. **Check Coverage**: Ensure all 10 validators are represented
2. **Check Conflicts**: Identify any conflicting requirements
3. **Check Gaps**: Identify missing requirements
4. **Prioritize**: Mark critical vs. optional requirements
```

**Replace With**:
```markdown
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
```

---

### IMPROVEMENT 4: Add YAML Output Format (MEDIUM)

**Location**: STEP 5, after line 261

**Add**:
```markdown
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
```

---

### IMPROVEMENT 5: Add Quantifiable Success Criteria (HIGH)

**Location**: Lines 40-41

**Current**:
```markdown
**Success Criteria**: Complete requirements document that enables Protocol 2 to generate a valid protocol structure.
```

**Replace With**:
```markdown
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
```

---

## VALIDATION AFTER IMPLEMENTATION

Run these checks to verify improvements work:

```bash
# 1. Test validator parser
python3 scripts/extract_validator_requirements.py validators-system/scripts/

# 2. Verify checkpoints work
bash -x dev-workflow/protocol-creation/1-analyze-validator-requirements.md

# 3. Check YAML output
yamllint .artifacts/protocol-creation/protocol-requirements-spec.yaml

# 4. Verify success criteria measurable
python3 scripts/measure_protocol_1_success.py
```

---

## EXPECTED OUTCOME

**Before**: AI guesses at requirements, 30% accuracy  
**After**: AI extracts exact requirements, 95% accuracy

**Key Improvement**: Validator parsing algorithm provides exact blueprint for requirements extraction
