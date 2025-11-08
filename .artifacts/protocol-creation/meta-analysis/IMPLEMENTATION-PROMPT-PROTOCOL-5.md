# IMPLEMENTATION PROMPT: PROTOCOL 5 IMPROVEMENTS

Copy this entire prompt to implement Protocol 5 improvements.

---

## TASK

Improve `/home/haymayndz/SuperTemplate/dev-workflow/protocol-creation/5-protocol-retrospective.md`

**Goal**: Add quantitative scoring system + improvement prioritization

---

## KEY IMPROVEMENTS

### 1. Replace Subjective Assessment with Quantitative Scoring (CRITICAL)

**Location**: STEP 2, replace lines 68-84

**Current**:
```markdown
1. **Content Quality**
   - **Clarity**: Is the protocol clear and understandable?
   - **Completeness**: Are all sections complete?
```

**Replace With**:
```markdown
### STEP 2: Protocol Quality Assessment (QUANTITATIVE)

#### 2.1 Content Quality Score (0-100 points)

**Clarity Score** (0-25 points):
```python
def calculate_clarity_score(protocol_content):
    score = 0
    
    # Readability (Flesch-Kincaid grade level)
    import textstat
    fk_grade = textstat.flesch_kincaid_grade(protocol_content)
    if 8 <= fk_grade <= 12:
        score += 10
    elif 6 <= fk_grade <= 14:
        score += 5
    
    # Average sentence length
    sentences = sent_tokenize(protocol_content)
    avg_words = np.mean([len(s.split()) for s in sentences])
    if 15 <= avg_words <= 25:
        score += 5
    
    # Technical term definitions
    tech_terms = find_technical_terms(protocol_content)
    defined_terms = [t for t in tech_terms if has_definition(protocol_content, t)]
    if len(defined_terms) == len(tech_terms):
        score += 5
    
    # Examples provided
    example_count = protocol_content.lower().count("example")
    sections = count_sections(protocol_content)
    if example_count >= sections * 2:
        score += 5
    
    return score
```

**Completeness Score** (0-25 points):
```python
def calculate_completeness_score(protocol_content):
    score = 0
    
    # Required sections present
    required = ["PREREQUISITES", "AI ROLE", "WORKFLOW", "INTEGRATION",
                "QUALITY GATES", "COMMUNICATION", "AUTOMATION", "HANDOFF", "EVIDENCE"]
    present = sum(1 for section in required if section in protocol_content.upper())
    score += (present / len(required)) * 15
    
    # All placeholders filled
    placeholders = re.findall(r'\[([A-Z_]+)\]', protocol_content)
    if len(placeholders) == 0:
        score += 5
    
    # No TODOs
    todos = protocol_content.upper().count("TODO") + protocol_content.upper().count("TBD")
    if todos == 0:
        score += 5
    
    return score
```

**Accuracy Score** (0-25 points):
```python
def calculate_accuracy_score(validator_results):
    score = 0
    
    # Validator score average
    avg_score = np.mean([v['score'] for v in validator_results.values()])
    if avg_score >= 0.95:
        score += 15
    elif avg_score >= 0.90:
        score += 10
    elif avg_score >= 0.85:
        score += 5
    
    # Line number references accurate
    line_refs = extract_line_references(protocol_content)
    accurate_refs = verify_line_references(line_refs)
    score += (accurate_refs / len(line_refs)) * 5 if line_refs else 0
    
    # Code examples syntax valid
    code_blocks = extract_code_blocks(protocol_content)
    valid_blocks = [b for b in code_blocks if validate_syntax(b)]
    score += (len(valid_blocks) / len(code_blocks)) * 5 if code_blocks else 5
    
    return score
```

**Consistency Score** (0-25 points):
```python
def calculate_consistency_score(protocol_content, existing_protocols):
    score = 0
    
    # Naming conventions match
    if naming_conventions_match(protocol_content, existing_protocols):
        score += 10
    
    # Section order matches template
    if section_order_correct(protocol_content):
        score += 5
    
    # Formatting matches style guide
    if formatting_correct(protocol_content):
        score += 5
    
    # Terminology consistent
    if terminology_consistent(protocol_content, existing_protocols):
        score += 5
    
    return score
```

**Total Quality Score**: Sum of all subscores (0-100)
- 90-100: Excellent ✅
- 80-89: Good ✓
- 70-79: Acceptable ⚠️
- <70: Needs Improvement ❌

**Usage**:
```python
quality_score = (
    calculate_clarity_score(protocol_content) +
    calculate_completeness_score(protocol_content) +
    calculate_accuracy_score(validator_results) +
    calculate_consistency_score(protocol_content, existing_protocols)
)

print(f"Protocol Quality Score: {quality_score}/100")
```
```

---

### 2. Add Improvement Prioritization Matrix (HIGH)

**Location**: STEP 5, replace lines 120-133

**Replace**:
```markdown
1. **Immediate Improvements** (Do now)
2. **Short-term Improvements** (Next protocol)
3. **Long-term Improvements** (Process enhancement)
```

**With**:
```markdown
### STEP 5: Create Prioritized Improvement Plan

**Prioritization Matrix**:

| Improvement | Impact | Effort | Priority Score | Action |
|-------------|--------|--------|----------------|--------|
| Add content pattern library | High | High | 0.71 | Do Now |
| Fix typo in line 45 | Low | Low | 0.43 | Backlog |

**Priority Calculation**:
```python
def calculate_priority(impact, effort):
    """
    Calculate priority score (0-1)
    
    Impact: High=3, Medium=2, Low=1
    Effort: High=3, Medium=2, Low=1
    
    Formula: (Impact×3 + (4-Effort)) / 7
    """
    impact_value = {'High': 3, 'Medium': 2, 'Low': 1}[impact]
    effort_value = {'High': 3, 'Medium': 2, 'Low': 1}[effort]
    
    score = (impact_value * 3 + (4 - effort_value)) / 7
    
    if score > 0.7:
        return score, "Do Now"
    elif score > 0.4:
        return score, "Next Sprint"
    else:
        return score, "Backlog"

# Example usage
improvements = [
    {"item": "Add content pattern library", "impact": "High", "effort": "High"},
    {"item": "Fix typo in line 45", "impact": "Low", "effort": "Low"},
    {"item": "Add pre-validation", "impact": "High", "effort": "Medium"},
]

for imp in improvements:
    score, action = calculate_priority(imp["impact"], imp["effort"])
    imp["priority_score"] = score
    imp["action"] = action
    print(f"{imp['item']}: {score:.2f} → {action}")
```

**Output Format**:
```markdown
## IMPROVEMENT PLAN

### Do Now (Priority >0.7)
1. **Add content pattern library** (Impact: High, Effort: High, Score: 0.71)
   - Estimated time: 8 hours
   - Expected impact: 50% reduction in validation failures
   - Owner: [Assign]

2. **Add pre-validation framework** (Impact: High, Effort: Medium, Score: 0.86)
   - Estimated time: 6 hours
   - Expected impact: Catch 80% of issues before validation
   - Owner: [Assign]

### Next Sprint (Priority 0.4-0.7)
3. **Improve error messages** (Impact: Medium, Effort: Low, Score: 0.57)
   - Estimated time: 2 hours
   - Expected impact: Faster debugging
   - Owner: [Assign]

### Backlog (Priority <0.4)
4. **Fix typo in line 45** (Impact: Low, Effort: Low, Score: 0.43)
   - Estimated time: 5 minutes
   - Expected impact: Minimal
   - Owner: [Assign]
```
```

---

### 3. Add Benchmark Comparison (MEDIUM)

**Location**: New section after STEP 2

**Add**:
```markdown
### STEP 2.5: Benchmark Comparison

**Compare this protocol against**:
1. Best protocol in workflow (highest validator scores)
2. Average protocol performance
3. Target standards (industry best practices)

```python
def benchmark_protocol(protocol_id, all_protocols):
    """Benchmark protocol against others"""
    
    metrics = {
        "validator_score": get_validator_score(protocol_id),
        "creation_time": get_creation_time(protocol_id),
        "revision_count": get_revision_count(protocol_id),
    }
    
    # Compare to best
    best_protocol = max(all_protocols, key=lambda p: p['validator_score'])
    metrics["vs_best"] = {
        "validator_score_diff": metrics["validator_score"] - best_protocol['validator_score'],
        "percentile": calculate_percentile(protocol_id, all_protocols)
    }
    
    # Compare to average
    avg_score = np.mean([p['validator_score'] for p in all_protocols])
    metrics["vs_average"] = {
        "validator_score_diff": metrics["validator_score"] - avg_score,
        "above_average": metrics["validator_score"] > avg_score
    }
    
    return metrics
```

**Benchmark Report Format**:
```markdown
## BENCHMARK COMPARISON

### Validator Score: 0.92
- **Rank**: 8/28 protocols (71st percentile)
- **vs Best** (Protocol 15: 0.97): -0.05 (5% below)
- **vs Average** (0.88): +0.04 (4.5% above) ✓

### Creation Efficiency
- **Time to Complete**: 4.5 hours
- **vs Average**: 5.2 hours (13% faster) ✓
- **Revisions Required**: 2
- **vs Average**: 3.1 (35% fewer) ✓

### Quality Indicators
- **First-Pass Success**: 8/10 validators (80%)
- **vs Average**: 6.2/10 (62%) - **29% better** ✓
```
```

---

### 4. Add Continuous Improvement Tracking (MEDIUM)

**Location**: New APPENDIX at end

**Add**:
```markdown
## APPENDIX: Continuous Improvement Tracking

### Improvement Log
`.artifacts/protocol-creation/improvement-log.json`

```json
{
  "protocol_id": "06",
  "creation_date": "2025-01-09",
  "iterations": [
    {
      "iteration": 1,
      "timestamp": "2025-01-09T10:00:00Z",
      "validator_score": 0.78,
      "issues": ["Missing mission keyword", "Only 1 gate defined"],
      "fixes_applied": ["Added mission statement", "Added Gate 2"]
    },
    {
      "iteration": 2,
      "timestamp": "2025-01-09T11:30:00Z",
      "validator_score": 0.92,
      "issues": ["Insufficient evidence mentions"],
      "fixes_applied": ["Added evidence links to gates"]
    }
  ],
  "final_score": 0.92,
  "total_time_hours": 4.5,
  "lessons_learned": [
    "Content pattern library reduced fixing time by 40%",
    "Pre-validation caught 80% of issues before formal validation"
  ],
  "improvements_for_next_protocol": [
    "Use mission template from start",
    "Add evidence links proactively"
  ]
}
```

**Usage**:
```python
# Log iteration
log_iteration(protocol_id, iteration_num, validator_score, issues, fixes)

# Analyze trends
trends = analyze_improvement_trends(all_protocols)
print(f"Average improvement per iteration: {trends['avg_improvement']}")
print(f"Most common issues: {trends['common_issues']}")
print(f"Most effective fixes: {trends['effective_fixes']}")
```
```

---

## VALIDATION

```bash
# Test quantitative scoring
python3 scripts/calculate_protocol_quality_score.py \
  --protocol .cursor/ai-driven-workflow/06-create-prd.md

# Expected output: Score breakdown with total

# Test prioritization
python3 scripts/prioritize_improvements.py \
  --improvements improvements.json

# Expected output: Sorted list with priority scores
```

---

## EXPECTED OUTCOME

**Before**: Subjective retrospective, no tracking  
**After**: Data-driven continuous improvement with measurable progress

**Key Metrics**:
- Protocol quality scores increase 15% per iteration
- Time to create protocols decreases 20% over time
- First-pass success rate improves from 30% to 85%
