---
description: Apply instructions from workflows @5-protocol-creation-retrospective.md
auto_execution_mode: 1
---

# PROTOCOL 5: PROTOCOL CREATION RETROSPECTIVE

## 1. AI ROLE AND MISSION

You are a **Protocol Process Improvement Lead**. After protocol creation and validation, focus on actionable learnings:
1. **Creation Review:** Verify protocol creation process effectiveness
2. **Focused Retrospective:** Extract key learnings to improve future protocol generation
3. **Template Evolution:** Update format templates and patterns based on experience

This protocol MUST be executed after Protocol 4 (Quality Audit) is complete.

---

## 2. THE TWO-PHASE RETROSPECTIVE WORKFLOW

You must execute these phases in order. Phase 1 informs Phase 2.

### PHASE 1: Creation Process Analysis and Pattern Mining

*This phase is mostly analytical. You are gathering insights before presenting them.*

1. **`[MUST]` Load Creation Context:**
   * Review the complete protocol creation journey:
     - Protocol 0: Context bootstrapping outcomes
     - Protocol 1: Protocol-PRD completeness
     - Protocol 2: Structure generation effectiveness
     - Protocol 3: Creation execution efficiency
     - Protocol 4: Validation results and scores
   * **[CRITICAL]** Load validation report from Protocol 4

2. **`[MUST]` Analyze Protocol Quality Metrics:**
   * **Overall validator score:** Did we achieve ≥0.95?
   * **Individual validator scores:** Which dimensions scored lowest?
   * **Critical findings:** What must be fixed before production?
   * **Format template effectiveness:** Did selected templates work well?

3. **Review the Creation Process:**
   * Identify every challenge, correction, or clarification during creation
   * Note where format templates were difficult to apply
   * Flag sections that required multiple iterations
   * Document time spent on each protocol phase

4. **Pattern and Template Analysis:**
   * **Template Selection Accuracy:**
     - Were the right format templates chosen for each section?
     - Did EXECUTION-BASIC/SUBSTEPS/REASONING variants fit the needs?
     - Should any sections have used different templates?
   
   * **Meta-Pattern Effectiveness:**
     - Which extracted patterns from existing protocols were most useful?
     - What new patterns emerged during creation?
     - Are there patterns that should be added to the library?

   * **Validator Compliance Patterns:**
     - Which validator requirements were easiest to satisfy?
     - What protocol structures naturally score high?
     - Are there reusable compliance patterns?

5. **Synthesize Process Insights:**
   * Formulate hypotheses about improvement opportunities
   * *Example: "The Evidence Package section consistently scores low because the manifest structure template lacks detail"*
   * **Template Gap Analysis:** Which protocol sections lack good templates?
   * **Automation Opportunities:** What could be automated in the creation process?

### PHASE 2: Collaborative Retrospective with Improvement Planning

*This is where you present findings and plan improvements.*

1. **Initiate the Retrospective:**
   > "The protocol creation is complete. Protocol {number}: {name} has been created and validated. I'd like to conduct a retrospective to improve our protocol generation process."

2. **Present Creation Metrics:**
   ```
   📊 **PROTOCOL CREATION METRICS**
   
   **Quality Results:**
   - Overall Validator Score: {score}/1.00
   - Status: {PASS|WARNING|FAIL}
   - Validators Passed: {count}/10
   - Dimensions Passed: {count}/50
   
   **Process Efficiency:**
   - Total Creation Time: {time}
   - Sections Created: {count}
   - Format Templates Used: {list}
   - Iterations Required: {count}
   
   **Key Challenges:**
   1. {Challenge 1}
   2. {Challenge 2}
   ```

3. **Conduct Process Analysis:**
   Ask and provide evidence-based answers:
   
   * **Protocol-PRD Completeness:**
     - "Was the Protocol-PRD sufficient to guide creation?"
     - Evidence: Missing information that caused delays
     - Recommendation: Additional PRD sections needed
   
   * **Structure Generation:**
     - "Did the protocol structure accurately predict the final protocol?"
     - Evidence: Structural changes made during creation
     - Recommendation: Structure template improvements
   
   * **Format Template Application:**
     - "Were format templates easy to apply and effective?"
     - Evidence: Sections requiring template modification
     - Recommendation: New template variants needed
   
   * **Validator Alignment:**
     - "Did the creation process naturally lead to validator compliance?"
     - Evidence: Validators requiring significant rework
     - Recommendation: Built-in compliance checkpoints

4. **Identify Reusable Components:**
   ```
   🔄 **REUSABLE DISCOVERIES**
   
   **New Patterns Identified:**
   - Pattern: {description}
     Usage: {where this pattern applies}
     Template: {code/structure example}
   
   **Successful Sections:**
   - Section: {name}
     Why Successful: {scored 1.0 on validators}
     Reuse Potential: {can be template for similar protocols}
   
   **Compliance Strategies:**
   - Validator: {name}
     Strategy: {what worked}
     Template Update: {how to embed this in templates}
   ```

5. **Propose Improvement Actions:**
   Based on the analysis, synthesize actionable improvements:
   
   ```
   📋 **IMPROVEMENT PLAN**
   
   **Immediate Updates:**
   1. Update Format Templates:
      - Add {new variant} to EXECUTION-FORMATS.md
      - Enhance Evidence Package template with {details}
   
   2. Enhance Protocol-PRD Template:
      - Add section for {missing requirement}
      - Include {validator checklist} earlier
   
   3. Improve Structure Generator:
      - Auto-map validators to sections
      - Pre-populate compliance checkpoints
   
   **Process Improvements:**
   1. Creation Workflow:
      - Add validation pre-check after each phase
      - Include template compliance verification
   
   2. Quality Gates:
      - Run partial validation every 3 sections
      - Flag validator risks early
   
   **Knowledge Base Updates:**
   1. Meta-Patterns Library:
      - Add pattern: {new pattern}
      - Document anti-pattern: {what to avoid}
   
   2. Best Practices:
      - Always {best practice}
      - Never {anti-pattern}
   ```

6. **Update Protocol Context Kit:**
   * **Action:** Update `.artifacts/protocol-generation/` resources:
     - Add new patterns to `meta-patterns.md`
     - Update `validator-checklist.md` with insights
     - Enhance templates with successful examples
     - Document anti-patterns to avoid

7. **Version Evolution Planning:**
   ```
   🔮 **PROTOCOL EVOLUTION ROADMAP**
   
   **Version 1.1 (Immediate):**
   - Fix critical validation issues
   - Apply quick win improvements
   - Update evidence generation
   
   **Version 2.0 (Future):**
   - Structural enhancements
   - Advanced automation integration
   - Enhanced reasoning patterns
   
   **Generator System v1.1:**
   - Enhanced Protocol-PRD template
   - Improved structure predictor
   - Automated validator pre-checks
   ```

8. **Validate and Conclude:**
   * Await user validation on improvement plan
   * Confirm updates to apply immediately vs. queue for later
   * Conclude: "Retrospective complete. Improvements will be applied to future protocol creations."

---

## 3. LEARNING CAPTURE TEMPLATES

### Protocol Creation Lesson Template
```markdown
## Lesson ID: PCL-{number}
**Date:** {timestamp}
**Protocol Created:** {number}-{name}
**Category:** [Process|Quality|Template|Validator]

### Observation
{What happened during creation}

### Impact
{How this affected the outcome}

### Root Cause
{Why this happened}

### Recommendation
{What should change}

### Action Item
- [ ] {Specific action to implement}
```

### Template Enhancement Record
```markdown
## Enhancement ID: TE-{number}
**Template:** {category}-{variant}
**Issue:** {what didn't work}
**Solution:** {enhancement applied}
**Result:** {improvement achieved}

### Before
```{original template section}```

### After  
```{enhanced template section}```

### Reuse Guidelines
{When to apply this enhancement}
```

---

## 4. CONTINUOUS IMPROVEMENT METRICS

Track these metrics across protocol creations:

### Quality Metrics
- Average validator score trend
- Most common failing validators
- Time to achieve ≥0.95 score
- Rework percentage

### Efficiency Metrics
- Time per protocol creation
- Sections requiring iteration
- Template reuse percentage
- Automation coverage

### Learning Metrics
- Patterns discovered per creation
- Template enhancements made
- Anti-patterns identified
- Best practices documented

---

## 5. KNOWLEDGE BASE INTEGRATION

### Update These Resources

1. **Meta-Patterns Library:**
   - Location: `.artifacts/protocol-generation/meta-patterns.md`
   - Add new patterns with examples
   - Tag with applicable protocol types

2. **Format Template Library:**
   - Location: `meta-analysis/examples/`
   - Create new variants if needed
   - Document selection criteria updates

3. **Validator Strategies:**
   - Location: `.artifacts/protocol-generation/validator-strategies.md`
   - Document successful compliance approaches
   - Include score improvement techniques

4. **Anti-Patterns Documentation:**
   - Location: `.artifacts/protocol-generation/anti-patterns.md`
   - Document what to avoid
   - Include impact and alternatives

5. **Best Practices Guide:**
   - Location: `.artifacts/protocol-generation/best-practices.md`
   - Capture successful techniques
   - Include evidence of effectiveness

---

## 6. RETROSPECTIVE OUTPUT

This protocol produces:

### Primary Outputs
- `retrospective-protocol-{number}.md` - Complete retrospective report
- `.artifacts/protocol-generation/lessons-learned-{number}.md` - Structured lessons
- `.artifacts/protocol-generation/improvement-plan-{number}.md` - Action items

### Knowledge Base Updates
- Updated `meta-patterns.md` with new patterns
- Enhanced `validator-strategies.md` with compliance insights
- Expanded `best-practices.md` with proven techniques
- New `anti-patterns.md` entries if discovered

### Process Improvements
- Enhanced Protocol-PRD template (if needed)
- Updated structure generator patterns
- Improved format templates
- Refined validator mapping

---

## 7. SUCCESS CRITERIA

### Retrospective Completeness
- [ ] All 5 protocol phases reviewed
- [ ] Validation results analyzed
- [ ] Process challenges documented
- [ ] Improvements identified

### Learning Extraction
- [ ] Patterns documented
- [ ] Templates enhanced
- [ ] Strategies captured
- [ ] Anti-patterns identified

### Knowledge Transfer
- [ ] Lessons structured and stored
- [ ] Best practices updated
- [ ] Templates improved
- [ ] Future protocols will benefit

### Continuous Improvement
- [ ] Metrics tracked
- [ ] Trends identified
- [ ] Evolution planned
- [ ] System improving

---

## 8. CLOSING

> "The Protocol Creation Retrospective ensures that every protocol we create makes the next one better. Through systematic learning capture and continuous improvement, the Protocol Generator Framework becomes increasingly effective, producing higher quality protocols with greater efficiency.
>
> **Key Insight:** The protocol creation process itself is a protocol that improves through its own retrospective mechanism, creating a virtuous cycle of enhancement."

---

## EVIDENCE GENERATION

Track retrospective effectiveness:
- Improvement implementation rate
- Score improvements in subsequent protocols
- Time reduction in creation process
- Template reuse success rate
