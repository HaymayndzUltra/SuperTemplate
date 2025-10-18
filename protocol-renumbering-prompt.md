# Comprehensive Protocol Renumbering Adjustment Prompt

## Overview
This prompt provides systematic instructions for renumbering all 28 AI-driven workflow protocols from inconsistent numbering (00a, 00B, 01, 0, 1-18) to sequential numbering (01-27), excluding `00-generate-rules.md` as requested.

## Critical Reference Updates Required

### 1. Direct @apply Handoffs (32 references)
### 2. Artifact Path References (365 references)  
### 3. Protocol Number Mentions (602 references)
### 4. Supporting Documentation Updates
### 5. Review Protocol References

---

## SECTION 1: Reference Mapping Matrix

### Complete Old → New Filename Mappings

```bash
# Phase 0: Foundation & Discovery (01-05)
00a-client-proposal-generation.md → 01-client-proposal-generation.md
00B-client-discovery-initiation.md → 02-client-discovery-initiation.md
01-project-brief-creation.md → 03-project-brief-creation.md
00-project-bootstrap-and-context-engineering.md → 04-project-bootstrap-and-context-engineering.md
0-bootstrap-your-project.md → 05-bootstrap-your-project.md

# Phase 1-2: Planning & Design (06-09)
1-create-prd.md → 06-create-prd.md
6-technical-design-architecture.md → 07-technical-design-architecture.md
2-generate-tasks.md → 08-generate-tasks.md
7-environment-setup-validation.md → 09-environment-setup-validation.md

# Phase 3: Development (10-11)
3-process-tasks.md → 10-process-tasks.md
9-integration-testing.md → 11-integration-testing.md

# Phase 4: Quality & Testing (12-14)
4-quality-audit.md → 12-quality-audit.md
15-uat-coordination.md → 13-uat-coordination.md
10-pre-deployment-staging.md → 14-pre-deployment-staging.md

# Phase 5: Deployment & Operations (15-18)
11-production-deployment.md → 15-production-deployment.md
12-monitoring-observability.md → 16-monitoring-observability.md
13-incident-response-rollback.md → 17-incident-response-rollback.md
14-performance-optimization.md → 18-performance-optimization.md

# Phase 6: Closure & Maintenance (19-23)
16-documentation-knowledge-transfer.md → 19-documentation-knowledge-transfer.md
17-project-closure.md → 20-project-closure.md
18-maintenance-support.md → 21-maintenance-support.md
5-implementation-retrospective.md → 22-implementation-retrospective.md
8-script-governance-protocol.md → 23-script-governance-protocol.md

# Supporting Protocols (24-27)
00-client-discovery.md → 24-client-discovery.md
INTEGRATION-GUIDE.md → 26-integration-guide.md
VALIDATION-GUIDE.md → 27-validation-guide.md
```

### Artifact Path Transformations

```bash
# Protocol artifact paths
.artifacts/protocol-0/ → .artifacts/protocol-05/
.artifacts/protocol-3/ → .artifacts/protocol-10/
.artifacts/protocol-4/ → .artifacts/protocol-12/
.artifacts/protocol-5/ → .artifacts/protocol-22/
.artifacts/protocol-6/ → .artifacts/protocol-07/
.artifacts/protocol-7/ → .artifacts/protocol-09/
.artifacts/protocol-8/ → .artifacts/protocol-23/
.artifacts/protocol-9/ → .artifacts/protocol-11/
.artifacts/protocol-10/ → .artifacts/protocol-14/
.artifacts/protocol-11/ → .artifacts/protocol-15/
.artifacts/protocol-12/ → .artifacts/protocol-16/
.artifacts/protocol-13/ → .artifacts/protocol-17/
.artifacts/protocol-14/ → .artifacts/protocol-18/
.artifacts/protocol-15/ → .artifacts/protocol-13/
.artifacts/protocol-16/ → .artifacts/protocol-19/
.artifacts/protocol-17/ → .artifacts/protocol-20/
.artifacts/protocol-18/ → .artifacts/protocol-21/
```

---

## SECTION 2: File-by-File Update Instructions

### Step 1: Rename Protocol Files

```bash
# Phase 0: Foundation & Discovery
mv 00a-client-proposal-generation.md 01-client-proposal-generation.md
mv 00B-client-discovery-initiation.md 02-client-discovery-initiation.md
mv 01-project-brief-creation.md 03-project-brief-creation.md
mv 00-project-bootstrap-and-context-engineering.md 04-project-bootstrap-and-context-engineering.md
mv 0-bootstrap-your-project.md 05-bootstrap-your-project.md

# Phase 1-2: Planning & Design
mv 1-create-prd.md 06-create-prd.md
mv 6-technical-design-architecture.md 07-technical-design-architecture.md
mv 2-generate-tasks.md 08-generate-tasks.md
mv 7-environment-setup-validation.md 09-environment-setup-validation.md

# Phase 3: Development
mv 3-process-tasks.md 10-process-tasks.md
mv 9-integration-testing.md 11-integration-testing.md

# Phase 4: Quality & Testing
mv 4-quality-audit.md 12-quality-audit.md
mv 15-uat-coordination.md 13-uat-coordination.md
mv 10-pre-deployment-staging.md 14-pre-deployment-staging.md

# Phase 5: Deployment & Operations
mv 11-production-deployment.md 15-production-deployment.md
mv 12-monitoring-observability.md 16-monitoring-observability.md
mv 13-incident-response-rollback.md 17-incident-response-rollback.md
mv 14-performance-optimization.md 18-performance-optimization.md

# Phase 6: Closure & Maintenance
mv 16-documentation-knowledge-transfer.md 19-documentation-knowledge-transfer.md
mv 17-project-closure.md 20-project-closure.md
mv 18-maintenance-support.md 21-maintenance-support.md
mv 5-implementation-retrospective.md 22-implementation-retrospective.md
mv 8-script-governance-protocol.md 23-script-governance-protocol.md

# Supporting Protocols
mv 00-client-discovery.md 24-client-discovery.md
mv INTEGRATION-GUIDE.md 26-integration-guide.md
mv VALIDATION-GUIDE.md 27-validation-guide.md
```

### Step 2: Update @apply Handoff References

#### Update each protocol file's @apply handoff at the bottom:

```bash
# 01-client-proposal-generation.md
sed -i 's/@apply \.cursor\/ai-driven-workflow\/00B-client-discovery-initiation\.md/@apply .cursor\/ai-driven-workflow\/02-client-discovery-initiation.md/' 01-client-proposal-generation.md

# 02-client-discovery-initiation.md
sed -i 's/@apply \.cursor\/ai-driven-workflow\/01-project-brief-creation\.md/@apply .cursor\/ai-driven-workflow\/03-project-brief-creation.md/' 02-client-discovery-initiation.md

# 03-project-brief-creation.md
sed -i 's/@apply \.cursor\/ai-driven-workflow\/00-project-bootstrap-and-context-engineering\.md/@apply .cursor\/ai-driven-workflow\/04-project-bootstrap-and-context-engineering.md/' 03-project-brief-creation.md

# 04-project-bootstrap-and-context-engineering.md
sed -i 's/@apply \.cursor\/ai-driven-workflow\/0-bootstrap-your-project\.md/@apply .cursor\/ai-driven-workflow\/05-bootstrap-your-project.md/' 04-project-bootstrap-and-context-engineering.md

# 05-bootstrap-your-project.md
sed -i 's/@apply \.cursor\/ai-driven-workflow\/00-client-discovery\.md/@apply .cursor\/ai-driven-workflow\/24-client-discovery.md/' 05-bootstrap-your-project.md

# 06-create-prd.md
sed -i 's/@apply \.cursor\/ai-driven-workflow\/6-technical-design-architecture\.md/@apply .cursor\/ai-driven-workflow\/07-technical-design-architecture.md/' 06-create-prd.md

# 07-technical-design-architecture.md
sed -i 's/@apply \.cursor\/ai-driven-workflow\/2-generate-tasks\.md/@apply .cursor\/ai-driven-workflow\/08-generate-tasks.md/' 07-technical-design-architecture.md

# 08-generate-tasks.md
sed -i 's/@apply \.cursor\/ai-driven-workflow\/7-environment-setup-validation\.md/@apply .cursor\/ai-driven-workflow\/09-environment-setup-validation.md/' 08-generate-tasks.md

# 09-environment-setup-validation.md
sed -i 's/@apply \.cursor\/ai-driven-workflow\/3-process-tasks\.md/@apply .cursor\/ai-driven-workflow\/10-process-tasks.md/' 09-environment-setup-validation.md

# 10-process-tasks.md
sed -i 's/@apply \.cursor\/ai-driven-workflow\/9-integration-testing\.md/@apply .cursor\/ai-driven-workflow\/11-integration-testing.md/' 10-process-tasks.md

# 11-integration-testing.md
sed -i 's/@apply \.cursor\/ai-driven-workflow\/4-quality-audit\.md/@apply .cursor\/ai-driven-workflow\/12-quality-audit.md/' 11-integration-testing.md

# 12-quality-audit.md
sed -i 's/@apply \.cursor\/ai-driven-workflow\/15-uat-coordination\.md/@apply .cursor\/ai-driven-workflow\/13-uat-coordination.md/' 12-quality-audit.md

# 13-uat-coordination.md
sed -i 's/@apply \.cursor\/ai-driven-workflow\/10-pre-deployment-staging\.md/@apply .cursor\/ai-driven-workflow\/14-pre-deployment-staging.md/' 13-uat-coordination.md

# 14-pre-deployment-staging.md
sed -i 's/@apply \.cursor\/ai-driven-workflow\/11-production-deployment\.md/@apply .cursor\/ai-driven-workflow\/15-production-deployment.md/' 14-pre-deployment-staging.md

# 15-production-deployment.md
sed -i 's/@apply \.cursor\/ai-driven-workflow\/12-monitoring-observability\.md/@apply .cursor\/ai-driven-workflow\/16-monitoring-observability.md/' 15-production-deployment.md

# 16-monitoring-observability.md
sed -i 's/@apply \.cursor\/ai-driven-workflow\/13-incident-response-rollback\.md/@apply .cursor\/ai-driven-workflow\/17-incident-response-rollback.md/' 16-monitoring-observability.md

# 17-incident-response-rollback.md
sed -i 's/@apply \.cursor\/ai-driven-workflow\/14-performance-optimization\.md/@apply .cursor\/ai-driven-workflow\/18-performance-optimization.md/' 17-incident-response-rollback.md

# 18-performance-optimization.md
sed -i 's/@apply \.cursor\/ai-driven-workflow\/5-implementation-retrospective\.md/@apply .cursor\/ai-driven-workflow\/22-implementation-retrospective.md/' 18-performance-optimization.md

# 19-documentation-knowledge-transfer.md
sed -i 's/@apply \.cursor\/ai-driven-workflow\/17-project-closure\.md/@apply .cursor\/ai-driven-workflow\/20-project-closure.md/' 19-documentation-knowledge-transfer.md

# 20-project-closure.md
sed -i 's/@apply \.cursor\/ai-driven-workflow\/18-maintenance-support\.md/@apply .cursor\/ai-driven-workflow\/21-maintenance-support.md/' 20-project-closure.md

# 21-maintenance-support.md
sed -i 's/@apply \.cursor\/ai-driven-workflow\/5-implementation-retrospective\.md/@apply .cursor\/ai-driven-workflow\/22-implementation-retrospective.md/' 21-maintenance-support.md

# 22-implementation-retrospective.md
sed -i 's/@apply \.cursor\/ai-driven-workflow\/8-script-governance-protocol\.md/@apply .cursor\/ai-driven-workflow\/23-script-governance-protocol.md/' 22-implementation-retrospective.md

# 23-script-governance-protocol.md
sed -i 's/@apply \.cursor\/ai-driven-workflow\/4-quality-audit\.md/@apply .cursor\/ai-driven-workflow\/12-quality-audit.md/' 23-script-governance-protocol.md

# 24-client-discovery.md
sed -i 's/@apply \.cursor\/ai-driven-workflow\/01-project-brief-creation\.md/@apply .cursor\/ai-driven-workflow\/03-project-brief-creation.md/' 24-client-discovery.md
```

### Step 3: Update Artifact Path References

```bash
# Update all artifact path references across all files
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/\.artifacts\/protocol-0\//.artifacts\/protocol-05\//g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/\.artifacts\/protocol-3\//.artifacts\/protocol-10\//g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/\.artifacts\/protocol-4\//.artifacts\/protocol-12\//g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/\.artifacts\/protocol-5\//.artifacts\/protocol-22\//g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/\.artifacts\/protocol-6\//.artifacts\/protocol-07\//g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/\.artifacts\/protocol-7\//.artifacts\/protocol-09\//g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/\.artifacts\/protocol-8\//.artifacts\/protocol-23\//g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/\.artifacts\/protocol-9\//.artifacts\/protocol-11\//g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/\.artifacts\/protocol-10\//.artifacts\/protocol-14\//g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/\.artifacts\/protocol-11\//.artifacts\/protocol-15\//g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/\.artifacts\/protocol-12\//.artifacts\/protocol-16\//g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/\.artifacts\/protocol-13\//.artifacts\/protocol-17\//g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/\.artifacts\/protocol-14\//.artifacts\/protocol-18\//g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/\.artifacts\/protocol-15\//.artifacts\/protocol-13\//g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/\.artifacts\/protocol-16\//.artifacts\/protocol-19\//g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/\.artifacts\/protocol-17\//.artifacts\/protocol-20\//g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/\.artifacts\/protocol-18\//.artifacts\/protocol-21\//g' {} \;
```

### Step 4: Update Protocol Number Text References

```bash
# Update "Protocol X" mentions
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/Protocol 0\b/Protocol 05/g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/Protocol 1\b/Protocol 06/g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/Protocol 2\b/Protocol 08/g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/Protocol 3\b/Protocol 10/g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/Protocol 4\b/Protocol 12/g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/Protocol 5\b/Protocol 22/g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/Protocol 6\b/Protocol 07/g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/Protocol 7\b/Protocol 09/g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/Protocol 8\b/Protocol 23/g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/Protocol 9\b/Protocol 11/g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/Protocol 10\b/Protocol 14/g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/Protocol 11\b/Protocol 15/g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/Protocol 12\b/Protocol 16/g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/Protocol 13\b/Protocol 17/g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/Protocol 14\b/Protocol 18/g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/Protocol 15\b/Protocol 13/g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/Protocol 16\b/Protocol 19/g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/Protocol 17\b/Protocol 20/g' {} \;
find .cursor/ai-driven-workflow -name "*.md" -exec sed -i 's/Protocol 18\b/Protocol 21/g' {} \;
```

---

## SECTION 3: Supporting Documentation Updates

### Update PROTOCOL-INTEGRATION-MAP.md

```bash
# Update the complete handoff chain (lines 9-39)
sed -i 's/00a-client-proposal-generation\.md/01-client-proposal-generation.md/g' PROTOCOL-INTEGRATION-MAP.md
sed -i 's/00B-client-discovery-initiation\.md/02-client-discovery-initiation.md/g' PROTOCOL-INTEGRATION-MAP.md
sed -i 's/01-project-brief-creation\.md/03-project-brief-creation.md/g' PROTOCOL-INTEGRATION-MAP.md
sed -i 's/00-project-bootstrap-and-context-engineering\.md/04-project-bootstrap-and-context-engineering.md/g' PROTOCOL-INTEGRATION-MAP.md
sed -i 's/0-bootstrap-your-project\.md/05-bootstrap-your-project.md/g' PROTOCOL-INTEGRATION-MAP.md
sed -i 's/1-create-prd\.md/06-create-prd.md/g' PROTOCOL-INTEGRATION-MAP.md
sed -i 's/6-technical-design-architecture\.md/07-technical-design-architecture.md/g' PROTOCOL-INTEGRATION-MAP.md
sed -i 's/2-generate-tasks\.md/08-generate-tasks.md/g' PROTOCOL-INTEGRATION-MAP.md
sed -i 's/7-environment-setup-validation\.md/09-environment-setup-validation.md/g' PROTOCOL-INTEGRATION-MAP.md
sed -i 's/3-process-tasks\.md/10-process-tasks.md/g' PROTOCOL-INTEGRATION-MAP.md
sed -i 's/9-integration-testing\.md/11-integration-testing.md/g' PROTOCOL-INTEGRATION-MAP.md
sed -i 's/4-quality-audit\.md/12-quality-audit.md/g' PROTOCOL-INTEGRATION-MAP.md
sed -i 's/15-uat-coordination\.md/13-uat-coordination.md/g' PROTOCOL-INTEGRATION-MAP.md
sed -i 's/10-pre-deployment-staging\.md/14-pre-deployment-staging.md/g' PROTOCOL-INTEGRATION-MAP.md
sed -i 's/11-production-deployment\.md/15-production-deployment.md/g' PROTOCOL-INTEGRATION-MAP.md
sed -i 's/12-monitoring-observability\.md/16-monitoring-observability.md/g' PROTOCOL-INTEGRATION-MAP.md
sed -i 's/13-incident-response-rollback\.md/17-incident-response-rollback.md/g' PROTOCOL-INTEGRATION-MAP.md
sed -i 's/14-performance-optimization\.md/18-performance-optimization.md/g' PROTOCOL-INTEGRATION-MAP.md
sed -i 's/16-documentation-knowledge-transfer\.md/19-documentation-knowledge-transfer.md/g' PROTOCOL-INTEGRATION-MAP.md
sed -i 's/17-project-closure\.md/20-project-closure.md/g' PROTOCOL-INTEGRATION-MAP.md
sed -i 's/18-maintenance-support\.md/21-maintenance-support.md/g' PROTOCOL-INTEGRATION-MAP.md
sed -i 's/5-implementation-retrospective\.md/22-implementation-retrospective.md/g' PROTOCOL-INTEGRATION-MAP.md
sed -i 's/8-script-governance-protocol\.md/23-script-governance-protocol.md/g' PROTOCOL-INTEGRATION-MAP.md
```

### Update INTEGRATION-GUIDE.md

```bash
# Update protocol automation flow map (lines 12-24)
sed -i 's/Protocol 00/Protocol 24/g' INTEGRATION-GUIDE.md
sed -i 's/Protocol 0/Protocol 05/g' INTEGRATION-GUIDE.md
sed -i 's/Protocol 1/Protocol 06/g' INTEGRATION-GUIDE.md
sed -i 's/Protocol 2/Protocol 08/g' INTEGRATION-GUIDE.md
sed -i 's/Protocol 3/Protocol 10/g' INTEGRATION-GUIDE.md
sed -i 's/Protocol 4/Protocol 12/g' INTEGRATION-GUIDE.md
sed -i 's/Protocol 5/Protocol 22/g' INTEGRATION-GUIDE.md

# Update file location references
sed -i 's/00-client-discovery\.md/24-client-discovery.md/g' INTEGRATION-GUIDE.md
sed -i 's/0-bootstrap-your-project\.md/05-bootstrap-your-project.md/g' INTEGRATION-GUIDE.md
sed -i 's/1-create-prd\.md/06-create-prd.md/g' INTEGRATION-GUIDE.md
sed -i 's/2-generate-tasks\.md/08-generate-tasks.md/g' INTEGRATION-GUIDE.md
sed -i 's/3-process-tasks\.md/10-process-tasks.md/g' INTEGRATION-GUIDE.md
sed -i 's/4-quality-audit\.md/12-quality-audit.md/g' INTEGRATION-GUIDE.md
sed -i 's/5-implementation-retrospective\.md/22-implementation-retrospective.md/g' INTEGRATION-GUIDE.md
```

### Update AGENTS.md

```bash
# Update file organization structure (lines 22-26)
sed -i 's/0-bootstrap-your-project\.md/05-bootstrap-your-project.md/g' AGENTS.md
sed -i 's/1-create-prd\.md/06-create-prd.md/g' AGENTS.md
sed -i 's/2-generate-tasks\.md/08-generate-tasks.md/g' AGENTS.md
sed -i 's/3-process-tasks\.md/10-process-tasks.md/g' AGENTS.md
sed -i 's/4-quality-audit\.md/12-quality-audit.md/g' AGENTS.md
sed -i 's/5-implementation-retrospective\.md/22-implementation-retrospective.md/g' AGENTS.md

# Update Cursor commands integration examples (lines 225-231)
sed -i 's/1-create-prd\.md/06-create-prd.md/g' AGENTS.md
sed -i 's/3-process-tasks\.md/10-process-tasks.md/g' AGENTS.md
sed -i 's/4-quality-audit\.md/12-quality-audit.md/g' AGENTS.md
```

---

## SECTION 4: Review Protocol Updates

### Update review-protocols/ directory files

```bash
# Update security-check.md
sed -i 's/11-production-deployment\.md/15-production-deployment.md/g' review-protocols/security-check.md

# Update architecture-review.md  
sed -i 's/6-technical-design-architecture\.md/07-technical-design-architecture.md/g' review-protocols/architecture-review.md

# Update code-review.md
sed -i 's/3-process-tasks\.md/10-process-tasks.md/g' review-protocols/code-review.md

# Update README.md
sed -i 's/4-quality-audit\.md/12-quality-audit.md/g' review-protocols/README.md

# Update _review-router.md
sed -i 's/4-quality-audit\.md/12-quality-audit.md/g' review-protocols/utils/_review-router.md
```

---

## SECTION 5: Validation Checklist

### Pre-Execution Validation
- [ ] All 27 protocol files identified and ready for renaming
- [ ] Backup created of entire `.cursor/ai-driven-workflow/` directory
- [ ] All @apply handoffs documented (32 found)
- [ ] All artifact paths catalogued (365 found)
- [ ] All text references identified (602 found)
- [ ] Supporting documentation analyzed
- [ ] Review protocols checked

### Post-Execution Validation
- [ ] All protocol files renamed to 01-27 sequence
- [ ] All @apply handoffs point to correct new filenames
- [ ] All artifact paths updated to new numbering
- [ ] All "Protocol X" text references updated
- [ ] PROTOCOL-INTEGRATION-MAP.md updated
- [ ] INTEGRATION-GUIDE.md updated
- [ ] AGENTS.md updated
- [ ] All review protocol references updated
- [ ] No broken references remain
- [ ] Integration map reflects new sequence
- [ ] Quality gates reference correct protocols

### Automated Validation Commands

```bash
# Check for remaining old references
grep -r "00a-client-proposal-generation" .cursor/ai-driven-workflow/
grep -r "00B-client-discovery-initiation" .cursor/ai-driven-workflow/
grep -r "01-project-brief-creation" .cursor/ai-driven-workflow/
grep -r "00-project-bootstrap-and-context-engineering" .cursor/ai-driven-workflow/
grep -r "0-bootstrap-your-project" .cursor/ai-driven-workflow/
grep -r "1-create-prd" .cursor/ai-driven-workflow/
grep -r "6-technical-design-architecture" .cursor/ai-driven-workflow/
grep -r "2-generate-tasks" .cursor/ai-driven-workflow/
grep -r "7-environment-setup-validation" .cursor/ai-driven-workflow/
grep -r "3-process-tasks" .cursor/ai-driven-workflow/
grep -r "9-integration-testing" .cursor/ai-driven-workflow/
grep -r "4-quality-audit" .cursor/ai-driven-workflow/
grep -r "15-uat-coordination" .cursor/ai-driven-workflow/
grep -r "10-pre-deployment-staging" .cursor/ai-driven-workflow/
grep -r "11-production-deployment" .cursor/ai-driven-workflow/
grep -r "12-monitoring-observability" .cursor/ai-driven-workflow/
grep -r "13-incident-response-rollback" .cursor/ai-driven-workflow/
grep -r "14-performance-optimization" .cursor/ai-driven-workflow/
grep -r "16-documentation-knowledge-transfer" .cursor/ai-driven-workflow/
grep -r "17-project-closure" .cursor/ai-driven-workflow/
grep -r "18-maintenance-support" .cursor/ai-driven-workflow/
grep -r "5-implementation-retrospective" .cursor/ai-driven-workflow/
grep -r "8-script-governance-protocol" .cursor/ai-driven-workflow/
grep -r "00-client-discovery" .cursor/ai-driven-workflow/

# Check for remaining old artifact paths
grep -r "protocol-0/" .cursor/ai-driven-workflow/
grep -r "protocol-3/" .cursor/ai-driven-workflow/
grep -r "protocol-4/" .cursor/ai-driven-workflow/
grep -r "protocol-5/" .cursor/ai-driven-workflow/
grep -r "protocol-6/" .cursor/ai-driven-workflow/
grep -r "protocol-7/" .cursor/ai-driven-workflow/
grep -r "protocol-8/" .cursor/ai-driven-workflow/
grep -r "protocol-9/" .cursor/ai-driven-workflow/
grep -r "protocol-10/" .cursor/ai-driven-workflow/
grep -r "protocol-11/" .cursor/ai-driven-workflow/
grep -r "protocol-12/" .cursor/ai-driven-workflow/
grep -r "protocol-13/" .cursor/ai-driven-workflow/
grep -r "protocol-14/" .cursor/ai-driven-workflow/
grep -r "protocol-15/" .cursor/ai-driven-workflow/
grep -r "protocol-16/" .cursor/ai-driven-workflow/
grep -r "protocol-17/" .cursor/ai-driven-workflow/
grep -r "protocol-18/" .cursor/ai-driven-workflow/

# Verify new sequence is correct
ls -la .cursor/ai-driven-workflow/ | grep -E "^-.*[0-9]{2}-.*\.md$"
```

---

## SECTION 6: Risk Mitigation

### High-Risk Operations
1. **File Renaming**: Risk of breaking references
   - **Mitigation**: Complete all reference updates before renaming
   - **Rollback**: Restore from backup if issues occur

2. **Artifact Path Updates**: Risk of breaking automation
   - **Mitigation**: Update all paths systematically
   - **Validation**: Test automation scripts after updates

3. **Integration Map Updates**: Risk of breaking workflow
   - **Mitigation**: Update integration map last
   - **Validation**: Verify all handoffs work correctly

### Medium-Risk Operations
1. **Text Reference Updates**: Risk of missing references
   - **Mitigation**: Use comprehensive grep searches
   - **Validation**: Automated validation commands

2. **Supporting Documentation**: Risk of inconsistency
   - **Mitigation**: Update all supporting docs together
   - **Validation**: Cross-reference all documentation

### Low-Risk Operations
1. **Review Protocol Updates**: Limited impact
   - **Mitigation**: Update review protocols last
   - **Validation**: Test review protocol execution

---

## SECTION 7: Execution Timeline

### Phase 1: Preparation (30 minutes)
- [ ] Create backup of entire directory
- [ ] Verify all files present
- [ ] Run pre-execution validation

### Phase 2: File Renaming (15 minutes)
- [ ] Execute file rename commands
- [ ] Verify all files renamed correctly
- [ ] Check for any missing files

### Phase 3: Reference Updates (45 minutes)
- [ ] Update @apply handoffs
- [ ] Update artifact paths
- [ ] Update protocol number mentions
- [ ] Update supporting documentation
- [ ] Update review protocols

### Phase 4: Validation (30 minutes)
- [ ] Run automated validation commands
- [ ] Manual verification of critical references
- [ ] Test workflow integration
- [ ] Document any issues found

### Phase 5: Cleanup (15 minutes)
- [ ] Remove backup if successful
- [ ] Update any remaining references
- [ ] Final validation pass

**Total Estimated Time**: 2.5 hours

---

## SECTION 8: Success Criteria

### Primary Success Criteria
- [ ] All 27 protocols renamed to 01-27 sequence
- [ ] All 32 @apply handoffs updated correctly
- [ ] All 365 artifact path references updated
- [ ] All 602 protocol number mentions updated
- [ ] All supporting documentation updated
- [ ] All review protocol references updated
- [ ] No broken references remain
- [ ] Workflow integration verified

### Secondary Success Criteria
- [ ] Automated validation passes
- [ ] Manual verification confirms correctness
- [ ] Documentation consistency maintained
- [ ] Workflow execution tested successfully

---

**CRITICAL NOTE**: This renumbering affects **999 total references** across the entire workflow system. Execute systematically and validate thoroughly at each step to ensure workflow continuity.
