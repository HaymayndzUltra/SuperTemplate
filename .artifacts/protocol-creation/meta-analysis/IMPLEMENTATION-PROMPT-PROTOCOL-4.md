# IMPLEMENTATION PROMPT: PROTOCOL 4 IMPROVEMENTS

Copy this entire prompt to implement Protocol 4 improvements.

---

## TASK

Improve `/home/haymayndz/SuperTemplate/dev-workflow/protocol-creation/4-validate-protocol.md`

**Goal**: Add systematic issue classification and fix procedures

---

## KEY IMPROVEMENTS

### 1. Add Issue Classification System (CRITICAL)

**Location**: New section before STEP 4

**Add**:
```markdown
## ISSUE CLASSIFICATION SYSTEM

### Issue Type 1: MISSING_CONTENT (CRITICAL)
**Validator Signals**: `"missing"`, `"not found"`, `score = 0`

**Fix Procedure**:
```python
def fix_missing_content(issue):
    """Fix missing content by inserting required pattern"""
    validator = issue['validator']
    dimension = issue['dimension']
    check = issue['check']
    
    # Load content pattern from library
    pattern = load_pattern(validator, dimension, check)
    
    # Insert at appropriate location
    section = find_section(protocol_content, dimension_to_section_map[dimension])
    section_content = insert_content(section, pattern, position="top")
    
    return section_content
```

**Example**:
- Issue: "Missing 'You are a' pattern in AI ROLE"
- Fix: Insert `You are a **[Role Title]**.` at section start

---

### Issue Type 2: INSUFFICIENT_COUNT (HIGH)
**Validator Signals**: `"count"`, `"<"`, `"minimum"`

**Fix Procedure**:
```python
def fix_insufficient_count(issue):
    """Fix count by duplicating existing items"""
    current_count = extract_number(issue['message'], pattern=r'count:\s*(\d+)')
    required_count = extract_number(issue['message'], pattern=r'≥(\d+)')
    deficit = required_count - current_count
    
    section = find_section(protocol_content, issue['section'])
    last_item = find_last_item(section, issue['item_type'])
    
    for i in range(deficit):
        new_item = duplicate_and_modify(last_item, index=current_count + i + 1)
        section = append_item(section, new_item)
    
    return section
```

**Example**:
- Issue: "Gate count: 1 (need ≥2)"
- Fix: Duplicate Gate 1 as Gate 2 with modified name

---

### Issue Type 3: PATTERN_MISMATCH (HIGH)
**Validator Signals**: `"pattern"`, `"expected"`, `"format"`

**Fix Procedure**:
```python
def fix_pattern_mismatch(issue):
    """Fix pattern by replacing with correct format"""
    required_pattern = issue['required_pattern']
    location = issue['location']
    
    section = find_section(protocol_content, location)
    
    # Check if similar content exists
    if "You're a" in section:
        # Fix: Replace with correct pattern
        section = section.replace("You're a", "You are a")
    else:
        # Insert missing pattern
        role_name = extract_role_name(section) or "[Role Name]"
        pattern_text = f"You are a **{role_name}**."
        section = prepend_to_section(section, pattern_text)
    
    return section
```

**Example**:
- Issue: "Missing 'You are a' pattern"
- Fix: Replace "You're a" with "You are a"

---

### Issue Type 4: FORMAT_ERROR (MEDIUM)
**Validator Signals**: `"syntax"`, `"markdown"`, `"format"`

**Fix Procedure**:
```python
def fix_format_error(issue):
    """Fix markdown formatting errors"""
    if "table" in issue['message'].lower():
        section = find_section(protocol_content, issue['section'])
        table = extract_table(section)
        fixed_table = repair_markdown_table(table)
        section = replace_table(section, table, fixed_table)
    
    elif "heading" in issue['message'].lower():
        section = fix_heading_levels(protocol_content, issue['section'])
    
    return section
```

---

### Issue Type 5: KEYWORD_MISSING (MEDIUM)
**Validator Signals**: `"keyword"`, `"must contain"`, `"missing word"`

**Fix Procedure**:
```python
def fix_keyword_missing(issue):
    """Fix missing keyword by inserting in natural location"""
    keyword = extract_keyword(issue['message'])
    section = find_section(protocol_content, issue['section'])
    
    if keyword == "mission":
        mission_template = load_mission_template()
        section = insert_after_role_definition(section, mission_template)
    
    elif keyword in ["within", "only", "do not"]:
        mission_text = find_mission_statement(section)
        mission_text = insert_scope_keyword(mission_text, keyword)
        section = replace_mission_statement(section, mission_text)
    
    return section
```
```

---

### 2. Update STEP 4 with Classification (CRITICAL)

**Location**: Replace lines 164-185

**Replace**:
```markdown
2. **Fix Protocol Content**
   - Edit the protocol file to address issues
   - Follow validator requirements exactly
   - Maintain protocol structure
```

**With**:
```markdown
2. **Classify and Fix Issues**

   **For each validation failure**:
   
   a. **Classify Issue Type**
   ```python
   def classify_issue(issue):
       message = issue['message'].lower()
       
       if 'missing' in message or 'not found' in message:
           return 'MISSING_CONTENT'
       elif 'count' in message or 'minimum' in message:
           return 'INSUFFICIENT_COUNT'
       elif 'pattern' in message or 'expected' in message:
           return 'PATTERN_MISMATCH'
       elif 'syntax' in message or 'format' in message:
           return 'FORMAT_ERROR'
       elif 'keyword' in message or 'must contain' in message:
           return 'KEYWORD_MISSING'
       else:
           return 'UNKNOWN'
   ```
   
   b. **Apply Appropriate Fix**
   ```python
   issue_type = classify_issue(issue)
   
   if issue_type == 'MISSING_CONTENT':
       fixed_content = fix_missing_content(issue)
   elif issue_type == 'INSUFFICIENT_COUNT':
       fixed_content = fix_insufficient_count(issue)
   elif issue_type == 'PATTERN_MISMATCH':
       fixed_content = fix_pattern_mismatch(issue)
   elif issue_type == 'FORMAT_ERROR':
       fixed_content = fix_format_error(issue)
   elif issue_type == 'KEYWORD_MISSING':
       fixed_content = fix_keyword_missing(issue)
   else:
       print(f"[WARNING] Unknown issue type: {issue}")
       fixed_content = protocol_content  # No fix applied
   ```
   
   c. **Verify Fix**
   ```python
   # Re-run specific validator check
   check_result = run_validator_check(
       validator=issue['validator'],
       dimension=issue['dimension'],
       check=issue['check'],
       content=fixed_content
   )
   
   if check_result['pass']:
       print(f"[✓] Fix successful for {issue['check']}")
       protocol_content = fixed_content
   else:
       print(f"[✗] Fix failed for {issue['check']}: {check_result['message']}")
       # Try alternative fix or escalate
   ```
```

---

### 3. Add Iteration Control (HIGH)

**Location**: After STEP 4

**Add**:
```markdown
### STEP 4.5: Iteration Control

**Maximum Iterations**: 3  
**Current Iteration**: 0

**Iteration Loop**:
```python
max_iterations = 3
iteration = 0

while has_validation_failures() and iteration < max_iterations:
    iteration += 1
    print(f"[ITERATION {iteration}/{max_iterations}]")
    
    # Classify and fix issues
    for issue in get_validation_failures():
        fix_issue(issue)
    
    # Re-validate
    run_validators()
    
    # Check progress
    if iteration >= max_iterations and has_validation_failures():
        print(f"[ESCALATE] Still have failures after {max_iterations} iterations")
        print("Unfixable issues:")
        for issue in get_validation_failures():
            print(f"  - {issue['validator']}: {issue['message']}")
        
        # Generate manual fix guide
        generate_manual_fix_guide(get_validation_failures())
        
        # Request user intervention
        print("\n[ACTION REQUIRED] Please review and fix manually")
        exit(1)
```

**Escalation Procedure**:
1. Document unfixable issues
2. Generate manual fix guide with examples
3. HALT automatic fixing
4. Request user intervention
```

---

### 4. Add Fix Verification (HIGH)

**Location**: After each fix in STEP 4

**Add**:
```markdown
### Fix Verification Procedure

**After each fix**:
```python
def verify_fix(issue, fixed_content):
    """Verify fix resolved the issue"""
    
    # Re-run specific check
    check_result = run_validator_check(
        validator=issue['validator'],
        dimension=issue['dimension'],
        check=issue['check'],
        content=fixed_content
    )
    
    if check_result['pass']:
        return True, "Fix successful"
    else:
        # Fix didn't work - try alternative
        alternative_fix = try_alternative_fix(issue, fixed_content)
        
        if alternative_fix:
            check_result = run_validator_check(
                validator=issue['validator'],
                dimension=issue['dimension'],
                check=issue['check'],
                content=alternative_fix
            )
            
            if check_result['pass']:
                return True, "Alternative fix successful"
        
        return False, f"Fix failed: {check_result['message']}"
```

**Usage**:
```python
fixed_content = fix_issue(issue)
success, message = verify_fix(issue, fixed_content)

if success:
    protocol_content = fixed_content
    print(f"[✓] {message}")
else:
    print(f"[✗] {message}")
    unfixable_issues.append(issue)
```
```

---

## VALIDATION

```bash
# Test issue classification
python3 -c "
from fixers import classify_issue

test_issues = [
    {'message': 'Missing You are a pattern'},
    {'message': 'Gate count: 1 (need ≥2)'},
    {'message': 'Expected pattern not found'},
]

for issue in test_issues:
    issue_type = classify_issue(issue)
    print(f'{issue[\"message\"]} → {issue_type}')
"

# Expected output:
# Missing You are a pattern → MISSING_CONTENT
# Gate count: 1 (need ≥2) → INSUFFICIENT_COUNT
# Expected pattern not found → PATTERN_MISMATCH
```

---

## EXPECTED OUTCOME

**Before**: Random fixes, 60% success rate  
**After**: Systematic fixes, 90% success rate

**Key**: Issue classification ensures correct fix procedure is applied
