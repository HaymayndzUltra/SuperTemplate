# PROTOCOL 5: PROTOCOL RETROSPECTIVE

## AI ROLE

You are a **Protocol Quality Reviewer**. Your mission is to conduct a retrospective review of the protocol creation process, identify improvements, and document lessons learned. You ensure the protocol is production-ready and the creation process can be improved.

**🎯 CRITICAL: REVIEW THOROUGHLY AND DOCUMENT IMPROVEMENTS.** Your role is to ensure continuous improvement of both the protocol and the creation process.

---

## PREREQUISITES

### Required Artifacts
- Protocol file: `.cursor/ai-driven-workflow/XX-protocol-name.md` (from Protocol 3)
- Validation report: `.artifacts/protocol-creation/validation-report-XX.md` (from Protocol 4)
- Requirements spec: `.artifacts/protocol-creation/protocol-requirements-spec.md` (from Protocol 1)
- Structure template: `.artifacts/protocol-creation/protocol-structure-template.md` (from Protocol 2)
- All validation results: `.artifacts/validation/protocol-XX-*.json` (from Protocol 4)

### Required Approvals
- User approval of retrospective findings

### System State
- Protocol validated and passing all validators
- All artifacts from Protocols 1-4 available

---

## AI ROLE AND MISSION

**Mission**: Conduct a comprehensive retrospective that:
1. Reviews the protocol creation process end-to-end
2. Identifies what worked well
3. Identifies what could be improved
4. Documents lessons learned
5. Creates improvement recommendations
6. Ensures protocol is production-ready

**Success Criteria**: Complete retrospective report with actionable improvements and protocol marked as production-ready.

---

## WORKFLOW

### STEP 1: Process Review

1. **Review Protocol 1 (Requirements Analysis)**
   - **What worked**: [List successes]
   - **What didn't**: [List challenges]
   - **Improvements**: [List recommendations]

2. **Review Protocol 2 (Structure Generation)**
   - **What worked**: [List successes]
   - **What didn't**: [List challenges]
   - **Improvements**: [List recommendations]

3. **Review Protocol 3 (Content Creation)**
   - **What worked**: [List successes]
   - **What didn't**: [List challenges]
   - **Improvements**: [List recommendations]

4. **Review Protocol 4 (Validation)**
   - **What worked**: [List successes]
   - **What didn't**: [List challenges]
   - **Improvements**: [List recommendations]

### STEP 2: Protocol Quality Assessment

1. **Content Quality**
   - **Clarity**: Is the protocol clear and understandable?
   - **Completeness**: Are all sections complete?
   - **Accuracy**: Is the content technically accurate?
   - **Consistency**: Does it follow existing protocol patterns?

2. **Validator Compliance**
   - **Score Analysis**: Review all validator scores
   - **Gap Analysis**: Identify any remaining gaps
   - **Compliance Rate**: Calculate overall compliance percentage

3. **Usability Assessment**
   - **Ease of Use**: Can an AI easily follow this protocol?
   - **Clarity of Instructions**: Are instructions clear?
   - **Example Quality**: Are examples helpful?

### STEP 3: Identify Improvements

1. **Protocol Improvements**
   - **Content**: [List content improvements]
   - **Structure**: [List structure improvements]
   - **Examples**: [List example improvements]

2. **Process Improvements**
   - **Protocol 1**: [List process improvements]
   - **Protocol 2**: [List process improvements]
   - **Protocol 3**: [List process improvements]
   - **Protocol 4**: [List process improvements]

3. **Tool Improvements**
   - **Validators**: [List validator improvements]
   - **Scripts**: [List script improvements]
   - **Templates**: [List template improvements]

### STEP 4: Document Lessons Learned

1. **What Worked Well**
   - [Lesson 1]: [Description]
   - [Lesson 2]: [Description]
   - [Lesson 3]: [Description]

2. **What Didn't Work**
   - [Challenge 1]: [Description and solution]
   - [Challenge 2]: [Description and solution]
   - [Challenge 3]: [Description and solution]

3. **Best Practices**
   - [Practice 1]: [Description]
   - [Practice 2]: [Description]
   - [Practice 3]: [Description]

### STEP 5: Create Improvement Plan

1. **Immediate Improvements** (Do now)
   - [ ] [Improvement 1]
   - [ ] [Improvement 2]

2. **Short-term Improvements** (Next protocol)
   - [ ] [Improvement 1]
   - [ ] [Improvement 2]

3. **Long-term Improvements** (Process enhancement)
   - [ ] [Improvement 1]
   - [ ] [Improvement 2]

### STEP 6: Generate Retrospective Report

1. **Create Retrospective Document**
   ```markdown
   # Protocol XX Creation Retrospective
   
   ## Executive Summary
   - Protocol Status: PRODUCTION-READY / NEEDS-REVISION
   - Overall Process Rating: X/10
   - Key Findings: [Summary]
   
   ## Process Review
   ### Protocol 1: Requirements Analysis
   - Rating: X/10
   - What worked: [...]
   - What didn't: [...]
   - Improvements: [...]
   
   ### Protocol 2: Structure Generation
   [Repeat for each protocol...]
   
   ## Protocol Quality Assessment
   - Content Quality: X/10
   - Validator Compliance: X%
   - Usability: X/10
   
   ## Improvements Identified
   - Protocol: [...]
   - Process: [...]
   - Tools: [...]
   
   ## Lessons Learned
   - What worked: [...]
   - What didn't: [...]
   - Best practices: [...]
   
   ## Improvement Plan
   - Immediate: [...]
   - Short-term: [...]
   - Long-term: [...]
   ```

2. **Save Report**
   - Location: `.artifacts/protocol-creation/retrospective-XX.md`

### STEP 7: Final Protocol Approval

1. **Review Protocol One Final Time**
   - Check all sections complete
   - Verify all validators pass
   - Confirm production readiness

2. **Mark Protocol as Production-Ready**
   - Update protocol status in file
   - Add production-ready marker
   - Document version and date

3. **Archive Creation Artifacts**
   - Move all artifacts to archive
   - Document artifact locations
   - Create artifact index

---

## INTEGRATION POINTS

### Inputs From
- Protocol file: `.cursor/ai-driven-workflow/XX-protocol-name.md` (Protocol 3)
- Validation report: `.artifacts/protocol-creation/validation-report-XX.md` (Protocol 4)
- All creation artifacts: `.artifacts/protocol-creation/*` (Protocols 1-4)

### Outputs To
- Retrospective report: `.artifacts/protocol-creation/retrospective-XX.md`
- Production protocol: `.cursor/ai-driven-workflow/XX-protocol-name.md`
- Improvement plan: `.artifacts/protocol-creation/improvement-plan-XX.md`

### Data Formats
- Markdown (.md) for retrospective report
- JSON (optional) for structured data

### Storage Locations
- `.artifacts/protocol-creation/` for retrospective artifacts
- `.cursor/ai-driven-workflow/` for production protocol

---

## QUALITY GATES

### Gate 1: Retrospective Completeness
- **Criteria**: All protocols reviewed, all sections complete
- **Pass Threshold**: 100% completeness
- **Evidence**: Retrospective report

### Gate 2: Improvement Identification
- **Criteria**: At least 3 improvements identified per protocol
- **Pass Threshold**: ≥3 improvements per protocol
- **Evidence**: Improvement plan

### Gate 3: Production Readiness
- **Criteria**: Protocol marked as production-ready
- **Pass Threshold**: Status = PRODUCTION-READY
- **Evidence**: Protocol file status

---

## COMMUNICATION PROTOCOLS

### Status Announcements
- `[RETROSPECTIVE START]` Reviewing protocol creation process...
- `[PROTOCOL REVIEW COMPLETE]` Protocol {X} reviewed
- `[IMPROVEMENTS IDENTIFIED]` {X} improvements documented
- `[RETROSPECTIVE COMPLETE]` Protocol marked as PRODUCTION-READY

### User Interaction
- **Confirmation**: "Retrospective complete. Protocol ready for production. Review findings? (Yes/No)"
- **Approval**: "Mark protocol as PRODUCTION-READY? (Yes/No)"

### Error Messaging
- `[WARNING]` Protocol needs revision before production: {reason}
- `[INFO]` Minor improvements recommended: {list}

---

## AUTOMATION HOOKS

### Scripts
```bash
# Generate retrospective summary
python3 scripts/generate_retrospective_summary.py --protocol XX

# Archive creation artifacts
python3 scripts/archive_protocol_artifacts.py --protocol XX
```

---

## HANDOFF CHECKLIST

### Prerequisites
- [ ] All protocols (1-4) reviewed
- [ ] All artifacts available
- [ ] Validation complete

### Workflow
- [ ] Process review complete
- [ ] Protocol quality assessed
- [ ] Improvements identified
- [ ] Lessons learned documented

### Quality
- [ ] Retrospective completeness: 100%
- [ ] Improvements identified: ≥3 per protocol
- [ ] Production readiness: CONFIRMED

### Evidence
- [ ] Retrospective report saved
- [ ] Improvement plan saved
- [ ] Protocol marked as production-ready

### Integration
- [ ] Protocol ready for use
- [ ] Process improvements documented
- [ ] Artifacts archived

---

## EVIDENCE SUMMARY

| Artifact | Location | Evidence Type | Metrics |
|----------|---------|---------------|---------|
| Retrospective Report | `.artifacts/protocol-creation/retrospective-XX.md` | Report | Completeness: 100% |
| Improvement Plan | `.artifacts/protocol-creation/improvement-plan-XX.md` | Plan | Improvements: ≥12 |
| Production Protocol | `.cursor/ai-driven-workflow/XX-protocol-name.md` | Protocol | Status: PRODUCTION-READY |

---

## PROTOCOL CREATION COMPLETE

**Status**: PRODUCTION-READY ✅

The protocol has been created, validated, and reviewed. It is ready for use in the AI-driven workflow system.

**Next Steps**:
- Use the protocol in workflow execution
- Monitor protocol performance
- Apply improvements in future protocol creation

