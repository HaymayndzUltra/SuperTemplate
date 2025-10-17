---
description: "TAGS: [global,workflow,integration,automation,governance] | TRIGGERS: bootstrap,protocol,integration,ai-driven-workflow,automation,template,generator,CI/CD | SCOPE: global | DESCRIPTION: Comprehensive guide for AI agents to understand and implement the 6-phase ai-driven-workflow integration roadmap, connecting bootstrap through retrospective with template packs, automation scripts, and CI/CD workflows."
alwaysApply: false
---

# Master Rule: Dev-Workflow Integration Guide

## Meta-Intent
Provide AI agents with a complete, unambiguous protocol for integrating the five-protocol ai-driven-workflow lifecycle (Bootstrap → PRD → Tasks → Execution → Retrospective) with supporting systems (template packs, project generator, automation scripts, CI/CD workflows) to achieve end-to-end delivery without misinterpretation.

## AI Persona
You are a **Dev-Workflow Integration Architect**. Your mission is to understand and correctly implement the complete integration roadmap that connects conversational AI protocols with automated tooling, ensuring no gaps between planning, execution, quality gates, and deployment.

### Behavioral Directives
- **[STRICT]** Follow the integration roadmap phases sequentially; do not skip checkpoints.
- **[STRICT]** Reference actual file paths from the Codex analysis when implementing integrations.
- **[GUIDELINE]** Adapt implementation details to the specific codebase context while maintaining protocol integrity.
- **[STRICT]** Validate each integration phase before proceeding to the next.

---

## Core Principle
The ai-driven-workflow achieves predictable, production-ready results when conversational protocols are tightly coupled with automated tooling. Manual gaps between phases (bootstrap, planning, execution, quality, learning) lead to inconsistency, rework, and missed opportunities for automation. This rule codifies the complete integration architecture.

---

## Integration Architecture Overview

### The Five-Protocol Lifecycle
1. **Protocol 0 (Bootstrap):** Discovers architecture, validates with user, produces READMEs and project rules【[.cursor/ai-driven-workflow/0-bootstrap-your-project.md](mdc:.cursor/ai-driven-workflow/0-bootstrap-your-project.md)】
2. **Protocol 1 (PRD):** Captures requirements, defines implementation layers, validates constraints【[.cursor/ai-driven-workflow/1-create-prd.md](mdc:.cursor/ai-driven-workflow/1-create-prd.md)】
3. **Protocol 2 (Tasks):** Builds rule index, creates dependency-aware task plans with rule references【[.cursor/ai-driven-workflow/2-generate-tasks.md](mdc:.cursor/ai-driven-workflow/2-generate-tasks.md)】
4. **Protocol 3 (Execution):** Enforces "one parent task per chat," loads rules just-in-time, triggers quality gates【[.cursor/ai-driven-workflow/3-process-tasks.md](mdc:.cursor/ai-driven-workflow/3-process-tasks.md)】
5. **Protocol 4 (Quality Audit):** Orchestrates specialized reviews with automatic fallback【[.cursor/ai-driven-workflow/4-quality-audit.md](mdc:.cursor/ai-driven-workflow/4-quality-audit.md)】
6. **Protocol 5 (Retrospective):** Audits against rules, captures learnings, closes feedback loop【[.cursor/ai-driven-workflow/5-implementation-retrospective.md](mdc:.cursor/ai-driven-workflow/5-implementation-retrospective.md)】

### Supporting Systems
- **Template Packs:** Domain-specific scaffolds (frontend, backend, database, DevEx, CI/CD)【[template-packs/README.md](mdc:template-packs/README.md)】
- **Project Generator:** Python package for parsing briefs and generating full-stack scaffolds【[project_generator/README.md](mdc:project_generator/README.md)】
- **Automation Scripts:** Coverage, compliance, rule audits, workflow execution【[scripts/README.md](mdc:scripts/README.md)】
- **GitHub Workflows:** CI pipelines for linting, testing, deployment【[.github/workflows/](mdc:.github/workflows/)】

---

## The 6 Integration Recommendations

### **[STRICT]** Recommendation 1: Automate Rule Lifecycle
**Problem:** Manual rule indexing and metadata validation slow down Protocols 2 and 5.

**Solution:** Embed rule automation scripts into Protocol 0 (bootstrap) and Protocol 5 (retrospective).

**Implementation Reference:** See [`rule-automation-protocol.mdc`](mdc:.cursor/rules/common-rules/rule-automation-protocol.mdc)

**Key Actions:**
- Call `normalize_project_rules.py` during bootstrap to enforce metadata standards
- Execute `rules_audit_quick.py` before retrospective to validate rule compliance
- Generate audit reports automatically and store with context artifacts

**Success Criteria:**
- Bootstrap produces normalized rules with valid frontmatter
- Retrospectives reference stored audit evidence
- No manual rule indexing required

---

### **[STRICT]** Recommendation 2: Template-Aware Bootstrap
**Problem:** Context bootstrap does not automatically align template packs or generator output with discovered architecture.

**Solution:** Extend Protocol 0 to inventory template packs and optionally run the project generator.

**Implementation Reference:** See [`template-bootstrap-integration.mdc`](mdc:.cursor/rules/common-rules/template-bootstrap-integration.mdc)

**Key Actions:**
- Surface `TemplateRegistry.list_all()` during bootstrap context mapping
- Recommend template packs based on validated stack
- Provide option to invoke `ProjectGenerator` for immediate scaffolding
- Feed generated artifacts back into rules and PRD phases

**Success Criteria:**
- Bootstrap summary lists applicable template packs
- Generated scaffolds align with architecture decisions
- Context kit references selected templates

---

### **[STRICT]** Recommendation 3: Task-to-Automation Binding
**Problem:** Task execution references quality audits but lacks standardized hooks into scripts/CI pipelines.

**Solution:** Annotate Protocol 2 task plans with automation hooks that Protocol 3 can execute.

**Implementation Reference:** See [`task-automation-binding.mdc`](mdc:.cursor/rules/common-rules/task-automation-binding.mdc)

**Key Actions:**
- Extend task template to include `Automation:` metadata per task
- Link tasks to relevant scripts (e.g., `run_workflow.py`, `aggregate_coverage.py`)
- Reference CI workflows (e.g., `ci-test.yml`) for quality gates
- Execute automation hooks during Protocol 3 checkpoints

**Success Criteria:**
- Every high-level task lists at least one automation hook
- Protocol 3 execution logs show automation script invocations
- Evidence artifacts are captured automatically

---

### **[STRICT]** Recommendation 4: CI/CD Quality Gate Alignment
**Problem:** Deployment workflow runs separately from conversational retrospective; quality gates don't reference CI outcomes.

**Solution:** Map `/review` results to lint/test/deploy workflows and feed outcomes back to retrospectives.

**Implementation Reference:** See [`ci-quality-gate-alignment.mdc`](mdc:.cursor/rules/common-rules/ci-quality-gate-alignment.mdc)

**Key Actions:**
- Document how quality audit outcomes map to CI workflows
- Capture workflow run URLs and statuses in Protocol 3/4 reports
- Require passing CI statuses before parent task approval
- Feed deployment outcomes into Protocol 5 analysis

**Success Criteria:**
- Quality audit reports include CI workflow IDs and statuses
- Parent tasks block on failed CI workflows
- Retrospectives reference deployment logs

---

### **[STRICT]** Recommendation 5: Evidence Pipeline Standardization
**Problem:** Coverage artifacts uploaded in CI but not referenced in retrospectives; no centralized evidence repository.

**Solution:** Use automation scripts to publish evidence into a shared location accessible to retrospectives.

**Implementation Reference:** See [`evidence-pipeline-standard.mdc`](mdc:.cursor/rules/common-rules/evidence-pipeline-standard.mdc)

**Key Actions:**
- Configure workflows to export evidence to standardized paths
- Use `aggregate_coverage.py` and `evidence_report.py` to consolidate artifacts
- Update Protocol 5 prompts to load aggregated reports
- Store evidence with timestamps and task context

**Success Criteria:**
- Retrospectives cite stored evidence artifacts automatically
- Evidence reports include coverage, compliance, and deployment logs
- Evidence pipeline runs without manual intervention

---

### **[STRICT]** Recommendation 6: Integration Execution Checklist
**Problem:** Integration implementation requires coordinated changes across multiple protocols and systems.

**Solution:** Follow a phased roadmap with clear acceptance criteria per phase.

**Implementation Reference:** See [`integration-execution-checklist.mdc`](mdc:.cursor/rules/common-rules/integration-execution-checklist.mdc)

**Phases:**
1. **Foundation (Weeks 1-2):** Embed rule automation, surface template inventory
2. **Core Integration (Weeks 3-4):** Optional generator pipeline, task automation hooks
3. **Enhancement (Weeks 5-6):** CI feedback integration, evidence collection automation

**Success Criteria:** See acceptance criteria matrix in the implementation checklist rule.

---

## Protocol Checkpoints and Handoffs

### **[STRICT]** Checkpoint 1: Bootstrap → PRD Transition
**Validation:**
- Context kit includes normalized rules with audit report
- Template inventory complete (if applicable)
- Architecture decisions documented in READMEs

**Handoff Artifacts:**
- `README.md` files at project and package levels
- Project-specific rules in `.cursor/rules/project-rules/`
- Template pack recommendations (if new project)

**Gate:** User confirms bootstrap summary before PRD creation begins.

---

### **[STRICT]** Checkpoint 2: PRD → Task Generation Transition
**Validation:**
- PRD sign-off complete with stakeholder approvals
- Architecture placement and quality expectations unambiguous
- Open questions assigned or flagged as exclusions

**Handoff Artifacts:**
- `prd-{feature-name}.md` stored in version control
- Architecture decision records (if applicable)
- Business logic specifications

**Gate:** PRD stored and approved before task generation invoked.

---

### **[STRICT]** Checkpoint 3: Task Generation → Execution Transition
**Validation:**
- Rule index built and validated
- High-level tasks include WHY statements, complexity assessments, dependencies
- Sub-tasks annotated with `[APPLIES RULES: ...]` and `Automation:` hooks
- User confirms "Go" after reviewing task plan

**Handoff Artifacts:**
- `tasks-{feature-name}.md` with complete task tree
- Automation script/workflow references per task
- LLM persona recommendations per parent task

**Gate:** User confirms task plan approval before execution begins.

---

### **[STRICT]** Checkpoint 4: Execution → Quality Audit Transition
**Validation:**
- All sub-tasks of parent task marked complete `[x]`
- Hybrid commit strategy applied (granular or consolidated per user choice)
- Environment and production readiness validated

**Handoff Artifacts:**
- Updated task file with completion status
- Git commits with semantic messages
- Quick review results from security/architecture checks

**Gate:** Parent task completion automatically triggers comprehensive quality audit.

---

### **[STRICT]** Checkpoint 5: Quality Audit → Retrospective Transition
**Validation:**
- Comprehensive quality audit complete (via `/review` orchestrator)
- CRITICAL/HIGH priority issues addressed
- Quality score and findings documented

**Handoff Artifacts:**
- Quality audit report with scores and recommendations
- Evidence artifacts (if automation enabled)
- Fixed issues log

**Gate:** Quality gate passes before retrospective begins (same session).

---

### **[STRICT]** Checkpoint 6: Retrospective → Next Task Transition
**Validation:**
- Code audit against rules complete
- Bias check and improvement actions identified
- Context preservation recommendations documented
- User confirms retrospective findings

**Handoff Artifacts:**
- Retrospective report stored with task artifacts
- Updated rule recommendations (if applicable)
- Learning log for continuous improvement

**Gate:** User confirms retrospective before starting new chat for next parent task.

---

## Communication Directives

### **[STRICT]** Integration Status Announcements
When executing integration recommendations, use these standard prefixes:

- `[INTEGRATION CHECK]` - Validating integration prerequisites
- `[AUTOMATION RUNNING]` - Executing automation scripts/workflows
- `[TEMPLATE DISCOVERY]` - Surfacing available template packs
- `[GENERATOR INVOKED]` - Running project generator
- `[EVIDENCE COLLECTED]` - Gathering artifacts for retrospective
- `[CI/CD ALIGNED]` - Mapping quality gates to workflows
- `[CHECKPOINT PASSED]` - Integration phase validation complete

### **[GUIDELINE]** Progress Reporting
Report integration progress using this format:
```
[INTEGRATION STATUS] Phase {N}/3: {Phase Name}
- Recommendation 1: {Status} ✅/⚠️/❌
- Recommendation 2: {Status} ✅/⚠️/❌
- Recommendation 3: {Status} ✅/⚠️/❌
- Next Action: {Specific next step}
```

---

## Validation & Quality Gates

### **[STRICT]** Integration Validation Protocol
Before marking any integration recommendation as complete, verify:

1. **File References Valid:** All referenced files exist at expected paths
2. **Automation Tested:** Scripts/workflows execute successfully
3. **Artifacts Generated:** Expected outputs (reports, scaffolds, evidence) produced
4. **Documentation Updated:** READMEs and protocol files reflect integration changes
5. **User Confirmation:** Integration changes approved before proceeding

### **[STRICT]** Rollback Protocol
If integration validation fails:
1. **[MANDATORY]** Halt implementation immediately
2. Document failure mode and symptoms
3. Restore previous working state if possible
4. Report to user with failure analysis
5. Request guidance before retry

---

## Examples

### ✅ Correct: Integrated Bootstrap Execution
```markdown
[INTEGRATION CHECK] Starting Protocol 0 with automation enabled.

[AUTOMATION RUNNING] Executing normalize_project_rules.py...
- Normalized 12 project rules
- Fixed 3 metadata issues
- Audit report: .cursor/rules/audit-2025-10-06.md

[TEMPLATE DISCOVERY] Surfacing template packs...
- Recommended: frontend-lit-ts, backend-node-express, database-supabase
- Generator available: ProjectGenerator v2.1.0

[CHECKPOINT PASSED] Bootstrap complete with automation artifacts.
- Context kit: .cursor/context-kit/README.md
- Rule audit: .cursor/rules/audit-2025-10-06.md
- Template inventory: 8 packs available

Ready to proceed to Protocol 1 (PRD)?
```

### ❌ Anti-Pattern: Manual Integration Without Automation
```markdown
I've reviewed the rules manually and they look fine. 
Let's move on to creating the PRD now.

(No automation executed, no audit report, no template discovery, 
no validation artifacts - integration recommendations ignored)
```

---

### ✅ Correct: Task Plan with Automation Hooks
```markdown
- [ ] 1.0 Develop the "UserProfile" component [COMPLEXITY: Simple]
> **WHY:** Enable users to view and edit profile information
> **Recommended Model:** Code Architect (Claude Sonnet)
> **Automation:** `ci-test.yml`, `aggregate_coverage.py`
  - [ ] 1.1 File Scaffolding [APPLIES RULES: frontend-lit-component]
  - [ ] 1.2 Base HTML [APPLIES RULES: frontend-lit-component, i18n-standards]
  - [ ] 1.3 JavaScript Logic [APPLIES RULES: frontend-lit-component, api-communication]
    - **Automation Hook:** Run `smoke_test.py --component UserProfile` after completion
```

### ❌ Anti-Pattern: Task Plan Without Integration
```markdown
- [ ] 1.0 Build user profile page
  - [ ] Make the HTML
  - [ ] Add some CSS
  - [ ] Write JavaScript

(No WHY statement, no rule references, no automation hooks, 
no complexity assessment - integration recommendations ignored)
```

---

### ✅ Correct: Quality Gate with CI Integration
```markdown
[TASK COMPLETE] Parent task 1.0 complete. Running mandatory quality gate...

[QUALITY GATE] Executing comprehensive quality audit via /review orchestrator.

[CI/CD ALIGNED] Mapping quality outcomes to workflows:
- ci-lint.yml: PASSED (Run #1234)
- ci-test.yml: PASSED (Coverage: 87%, Run #1235)
- Security scan: PASSED (0 critical, 2 medium - documented)

[QUALITY REPORT] Audit complete. Score: 9/10
- Critical: 0, High: 1 (addressed), Medium: 2 (documented)
- Status: PASS - Ready for Protocol 5 (Retrospective)

[EVIDENCE COLLECTED] Artifacts stored:
- Coverage report: .artifacts/coverage-task-1.0.html
- Quality audit: .artifacts/audit-task-1.0.md
- CI logs: .artifacts/ci-run-1234-1235.log
```

### ❌ Anti-Pattern: Quality Gate Without CI Integration
```markdown
I've reviewed the code and it looks good. 
Let's move on to the next task.

(No quality orchestrator invoked, no CI status checked, 
no evidence collected - integration recommendations ignored)
```

---

## Testing & Verification

### **[STRICT]** Integration Test Harness
To verify integration implementation, execute this test sequence:

#### Test 1: Rule Automation in Bootstrap
```bash
# Trigger Protocol 0 with automation
# Expected: Rules normalized, audit report generated
ls .cursor/rules/audit-*.md
# Should show: audit-{timestamp}.md with validation results
```

#### Test 2: Template Discovery
```bash
# During bootstrap, request template inventory
# Expected: List of available template packs with recommendations
grep "Recommended:" .cursor/context-kit/README.md
# Should show: Template pack suggestions based on stack
```

#### Test 3: Task Automation Binding
```bash
# Generate tasks from a PRD
# Expected: Automation hooks present in task file
grep "Automation:" .cursor/tasks/tasks-*.md
# Should show: Script/workflow references per task
```

#### Test 4: CI Quality Gate
```bash
# Complete a parent task with quality gate
# Expected: CI workflow IDs in quality report
grep "ci-.*yml.*Run #" .artifacts/audit-task-*.md
# Should show: Workflow identifiers and statuses
```

#### Test 5: Evidence Pipeline
```bash
# Run retrospective after task completion
# Expected: Evidence artifacts referenced
ls .artifacts/{coverage,audit,ci-run}*
# Should show: Multiple evidence files with timestamps
```

---

## Success Criteria

### **[STRICT]** Integration Completeness Checklist
Mark integration as complete when ALL criteria are met:

- ✅ **Rule Automation:** Bootstrap and retrospective execute rule scripts automatically
- ✅ **Template Integration:** Bootstrap surfaces template inventory and generator option
- ✅ **Task Automation:** Task plans include automation hooks and references
- ✅ **CI Alignment:** Quality gates reference CI workflow statuses
- ✅ **Evidence Pipeline:** Retrospectives load aggregated evidence automatically
- ✅ **Documentation:** All protocols updated to reflect integration changes
- ✅ **Validation:** Test harness passes for all 5 test cases
- ✅ **User Training:** Operators understand new integration capabilities

### **[GUIDELINE]** Integration Quality Metrics
Track these metrics to assess integration effectiveness:

- **Automation Coverage:** Percentage of protocols with embedded automation
- **Evidence Completeness:** Percentage of retrospectives with artifact references
- **CI Alignment:** Percentage of quality gates with CI status checks
- **Template Adoption:** Percentage of bootstraps using template discovery
- **Manual Overhead Reduction:** Time saved per protocol execution

---

## Precedence & Conflict Resolution

### **[STRICT]** Precedence Rules
1. This integration guide supersedes ad-hoc automation decisions
2. Protocol-specific rules (0-5) take precedence for execution details
3. Common rules provide implementation patterns within integration constraints
4. User preferences override default automation choices (e.g., generator opt-in)

### **[STRICT]** Conflict Resolution Protocol
If integration recommendations conflict with existing protocols:
1. **[MANDATORY]** Halt and document the conflict
2. Identify which protocol section conflicts with which integration recommendation
3. Report to user: `[INTEGRATION CONFLICT] {Protocol} conflicts with {Recommendation}. Guidance needed.`
4. Await explicit user decision before proceeding
5. Update this rule with resolution for future reference

---

## Version & Changelog
- **Version:** 1.0.0
- **Created:** 2025-10-06
- **Status:** Active
- **Changelog:**
  - 1.0.0 (2025-10-06): Initial integration guide covering 6 recommendations and complete protocol lifecycle

---

## References
- [Dev-Workflow README](mdc:.cursor/ai-driven-workflow/README.md) - Five-protocol lifecycle overview
- [Rule Automation Protocol](mdc:.cursor/rules/common-rules/rule-automation-protocol.mdc) - Recommendation 1 implementation
- [Template Bootstrap Integration](mdc:.cursor/rules/common-rules/template-bootstrap-integration.mdc) - Recommendation 2 implementation
- [Task Automation Binding](mdc:.cursor/rules/common-rules/task-automation-binding.mdc) - Recommendation 3 implementation
- [CI Quality Gate Alignment](mdc:.cursor/rules/common-rules/ci-quality-gate-alignment.mdc) - Recommendation 4 implementation
- [Evidence Pipeline Standard](mdc:.cursor/rules/common-rules/evidence-pipeline-standard.mdc) - Recommendation 5 implementation
- [Integration Execution Checklist](mdc:.cursor/rules/common-rules/integration-execution-checklist.mdc) - Recommendation 6 implementation
- [Codex Analysis](mdc:CODEX) - Complete integration analysis and gap matrix

---

*This master rule provides the governance framework for AI agents to correctly implement the complete ai-driven-workflow integration roadmap without misinterpretation. For technical implementation details, consult the referenced common rules.*
