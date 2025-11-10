# Framework Review Process

**Version**: 1.0  
**Created**: 2025-01-10  
**Purpose**: Establish systematic review process for Decision Framework and architectural decisions

---

## 🎯 OVERVIEW

This document defines the review process for:
1. **Decision Framework** (`DECISION-FRAMEWORK.md`) - The evaluation criteria and scoring rubric
2. **Architectural Decisions** (e.g., `architecture-decision.md`) - Specific decisions made using the framework

---

## 📅 REVIEW SCHEDULE

### Framework Review (Quarterly)
**Frequency**: Every 3 months  
**Next Review**: 2025-04-10

**Review Questions**:
1. Are the 6 criteria still relevant?
2. Are the scoring scales appropriate?
3. Are the recommendation thresholds accurate?
4. Have any patterns emerged suggesting framework changes?
5. What is the framework adoption rate?

**Review Process**:
1. Collect metrics (decision quality, speed, consistency, adoption)
2. Gather feedback from team/users
3. Analyze decision outcomes (did they achieve goals?)
4. Identify improvement opportunities
5. Propose framework updates if needed
6. Document review findings

**Output**: Framework review report in `.artifacts/framework-reviews/YYYY-MM-DD-review.md`

---

### Decision Review (Per Decision)
**Frequency**: Based on review triggers (see below)

**Review Triggers**:
- **Time-based**: 3 months after decision acceptance
- **Event-based**: When context changes significantly
- **Metric-based**: When success metrics fall below targets
- **Pattern-based**: When 3+ similar decisions deviate from framework

**Review Questions**:
1. Did the decision achieve intended outcomes?
2. Were the consequences as expected?
3. Has the context changed?
4. Should the decision be revised?
5. What lessons were learned?

**Review Process**:
1. Measure success metrics
2. Compare actual vs expected consequences
3. Evaluate if context has changed
4. Determine if decision should be revised
5. Document lessons learned
6. Update decision status if needed

**Output**: Decision review report appended to original decision document

---

## 🔄 FRAMEWORK UPDATE PROCESS

### When to Update Framework

**Mandatory Updates**:
- Quarterly review identifies critical issues
- 3+ decisions deviate from recommendations
- New architectural patterns emerge
- Team structure changes significantly

**Optional Updates**:
- Minor clarifications needed
- New criteria identified
- Scoring scales need adjustment
- Recommendation thresholds need tuning

### Update Workflow

```
1. IDENTIFY ISSUE
   ↓
   Document limitation or improvement opportunity
   Create issue in `.artifacts/framework-issues/`
   ↓
2. PROPOSE CHANGE
   ↓
   Create proposal document with:
   - Problem statement
   - Proposed change
   - Rationale and evidence
   - Impact analysis (breaking vs non-breaking)
   - Migration plan (if breaking)
   ↓
3. REVIEW
   ↓
   Team reviews proposal
   Provide feedback and suggestions
   Iterate on proposal if needed
   ↓
4. APPROVE
   ↓
   Decision maker approves or rejects
   Document approval decision
   ↓
5. UPDATE
   ↓
   Update DECISION-FRAMEWORK.md
   Increment version number
   Update version history
   ↓
6. COMMUNICATE
   ↓
   Notify team of changes
   Update documentation
   Provide migration guidance (if breaking)
   ↓
7. ARCHIVE
   ↓
   Archive previous version
   Store in `.artifacts/framework-versions/`
```

### Version Numbering

**Major Version (X.0)**: Breaking changes
- Criteria added/removed
- Scoring scales changed significantly
- Recommendation thresholds changed
- **Impact**: Existing decisions may need re-evaluation

**Minor Version (X.Y)**: Non-breaking changes
- New criteria added (optional)
- Clarifications to existing criteria
- New recommendation categories
- **Impact**: Existing decisions remain valid

**Patch Version (X.Y.Z)**: Trivial changes
- Typo fixes
- Formatting improvements
- Documentation clarifications
- **Impact**: No impact on decisions

---

## 📊 METRICS TRACKING

### Framework Metrics

**Decision Quality** (Target: ≥90%)
- **Measurement**: % of decisions that achieve intended outcomes
- **Collection**: Review each decision 3 months after acceptance
- **Formula**: `(Successful Decisions / Total Decisions) × 100`

**Decision Speed** (Target: ≤3 days)
- **Measurement**: Average time from problem identification to decision
- **Collection**: Track timestamps in decision documents
- **Formula**: `Average(Decision Date - Problem Identification Date)`

**Decision Consistency** (Target: ≥85%)
- **Measurement**: % of decisions following framework recommendations
- **Collection**: Compare decision choice vs framework recommendation
- **Formula**: `(Decisions Following Framework / Total Decisions) × 100`

**Framework Adoption** (Target: ≥95%)
- **Measurement**: % of architectural decisions using framework
- **Collection**: Count decisions with vs without framework evaluation
- **Formula**: `(Decisions Using Framework / Total Architectural Decisions) × 100`

### Decision Metrics

**Success Rate** (Target: ≥90%)
- **Measurement**: Did decision achieve intended outcomes?
- **Collection**: Measure at 3-month review
- **Values**: Yes (100%) / Partial (50%) / No (0%)

**Consequence Accuracy** (Target: ≥80%)
- **Measurement**: Were consequences as expected?
- **Collection**: Compare actual vs predicted consequences
- **Formula**: `(Accurate Predictions / Total Predictions) × 100`

**Context Stability** (Target: ≥70%)
- **Measurement**: Has context remained stable?
- **Collection**: Evaluate at review
- **Values**: Stable (100%) / Minor Changes (50%) / Major Changes (0%)

---

## 📝 REVIEW TEMPLATES

### Framework Review Template

```markdown
# Framework Review: [Date]

**Review Date**: YYYY-MM-DD  
**Framework Version**: X.Y.Z  
**Reviewer**: [Name]

## Metrics Summary

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Decision Quality | ≥90% | X% | ✅/⚠️/❌ |
| Decision Speed | ≤3 days | X days | ✅/⚠️/❌ |
| Decision Consistency | ≥85% | X% | ✅/⚠️/❌ |
| Framework Adoption | ≥95% | X% | ✅/⚠️/❌ |

## Decisions Reviewed
- [Decision ID]: [Status] - [Outcome]
- [Decision ID]: [Status] - [Outcome]

## Findings

### What's Working Well
- [Finding 1]
- [Finding 2]

### Issues Identified
- [Issue 1]: [Severity] - [Impact]
- [Issue 2]: [Severity] - [Impact]

### Patterns Observed
- [Pattern 1]: [Description]
- [Pattern 2]: [Description]

## Recommendations

### Framework Updates Needed
- [ ] [Update 1]: [Rationale]
- [ ] [Update 2]: [Rationale]

### Process Improvements
- [ ] [Improvement 1]: [Rationale]
- [ ] [Improvement 2]: [Rationale]

## Action Items
- [ ] [Action 1]: [Owner] - [Due Date]
- [ ] [Action 2]: [Owner] - [Due Date]

## Next Review
**Date**: YYYY-MM-DD  
**Focus Areas**: [Areas to focus on]
```

---

### Decision Review Template

```markdown
# Decision Review: [Decision ID]

**Review Date**: YYYY-MM-DD  
**Decision Date**: YYYY-MM-DD  
**Time Since Decision**: X months  
**Reviewer**: [Name]

## Success Metrics

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| [Metric 1] | [Target] | [Actual] | ✅/⚠️/❌ |
| [Metric 2] | [Target] | [Actual] | ✅/⚠️/❌ |

## Outcome Evaluation

### Intended Outcomes
- [Outcome 1]: ✅ Achieved / ⚠️ Partially / ❌ Not Achieved
- [Outcome 2]: ✅ Achieved / ⚠️ Partially / ❌ Not Achieved

### Actual Consequences

**Positive** (Expected vs Actual):
- [Expected]: [Actual Result]
- [Expected]: [Actual Result]

**Negative** (Expected vs Actual):
- [Expected]: [Actual Result]
- [Expected]: [Actual Result]

**Unexpected**:
- [Unexpected Consequence 1]
- [Unexpected Consequence 2]

## Context Changes

### Original Context
[Summary of context at decision time]

### Current Context
[Summary of current context]

### Significant Changes
- [Change 1]: [Impact]
- [Change 2]: [Impact]

## Lessons Learned

### What Worked Well
- [Lesson 1]
- [Lesson 2]

### What Didn't Work
- [Lesson 1]
- [Lesson 2]

### What Would We Do Differently
- [Improvement 1]
- [Improvement 2]

## Decision Status

**Current Status**: ✅ Accepted / ⚠️ Needs Revision / ❌ Superseded

**Recommendation**:
- [ ] Keep as-is
- [ ] Minor revision needed
- [ ] Major revision needed
- [ ] Supersede with new decision

## Action Items
- [ ] [Action 1]: [Owner] - [Due Date]
- [ ] [Action 2]: [Owner] - [Due Date]

## Next Review
**Date**: YYYY-MM-DD  
**Trigger**: [Time-based / Event-based / Metric-based]
```

---

## 🚨 ESCALATION PROCESS

### When to Escalate

**Critical Issues** (Immediate escalation):
- Framework fundamentally flawed
- Multiple decisions failing
- Major context change affecting all decisions
- Security or compliance risk identified

**High Priority** (Escalate within 1 week):
- Framework metrics below targets for 2+ quarters
- 3+ decisions deviating from framework
- New architectural pattern not covered by framework
- Team feedback indicates framework issues

**Medium Priority** (Escalate at next review):
- Minor framework improvements needed
- Single decision deviation
- Clarifications needed
- Process improvements identified

### Escalation Workflow

```
1. IDENTIFY ISSUE
   ↓
2. ASSESS SEVERITY
   ↓
   Critical → Immediate escalation
   High → Escalate within 1 week
   Medium → Escalate at next review
   ↓
3. DOCUMENT ISSUE
   ↓
   Create issue document in `.artifacts/framework-issues/`
   Include: Description, Impact, Evidence, Proposed Solution
   ↓
4. NOTIFY STAKEHOLDERS
   ↓
   Decision maker
   Team members
   Affected projects
   ↓
5. RESOLVE
   ↓
   Follow framework update process
   Or follow decision revision process
   ↓
6. COMMUNICATE RESOLUTION
   ↓
7. CLOSE ISSUE
```

---

## 📁 ARTIFACT STRUCTURE

```
.artifacts/
├── architecture-decision.md (Current decision)
├── framework-reviews/
│   ├── 2025-04-10-review.md
│   ├── 2025-07-10-review.md
│   └── ...
├── framework-issues/
│   ├── ISSUE-001-criteria-missing.md
│   ├── ISSUE-002-scoring-unclear.md
│   └── ...
├── framework-versions/
│   ├── DECISION-FRAMEWORK-v1.0.md
│   ├── DECISION-FRAMEWORK-v1.1.md
│   └── ...
└── decision-reviews/
    ├── AD-001-review-2025-04-10.md
    ├── AD-002-review-2025-05-15.md
    └── ...
```

---

## ✅ REVIEW CHECKLIST

### Framework Review Checklist
- [ ] Collect metrics (quality, speed, consistency, adoption)
- [ ] Gather team feedback
- [ ] Analyze decision outcomes
- [ ] Identify patterns and issues
- [ ] Evaluate criteria relevance
- [ ] Assess scoring scales
- [ ] Review recommendation thresholds
- [ ] Propose updates if needed
- [ ] Document review findings
- [ ] Schedule next review

### Decision Review Checklist
- [ ] Measure success metrics
- [ ] Evaluate outcome achievement
- [ ] Compare expected vs actual consequences
- [ ] Assess context changes
- [ ] Document lessons learned
- [ ] Determine if revision needed
- [ ] Update decision status
- [ ] Create action items
- [ ] Schedule next review
- [ ] Communicate findings

---

## 🎯 SUCCESS CRITERIA

### Framework Review Success
- ✅ All metrics tracked and documented
- ✅ Review completed within 1 week of scheduled date
- ✅ Findings documented with evidence
- ✅ Action items created and assigned
- ✅ Next review scheduled

### Decision Review Success
- ✅ All success metrics measured
- ✅ Consequences evaluated (expected vs actual)
- ✅ Context changes documented
- ✅ Lessons learned captured
- ✅ Decision status updated
- ✅ Action items created if needed

---

**Process Status**: ✅ Active  
**Next Framework Review**: 2025-04-10  
**Next Decision Review**: 2025-04-10 (AD-001)  
**Maintained By**: System Architect
