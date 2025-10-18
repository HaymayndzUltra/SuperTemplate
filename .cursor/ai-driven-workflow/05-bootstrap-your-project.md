---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 0: BOOTSTRAP YOUR PROJECT (LEGACY ALIGNMENT COMPLIANT)

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `.cursor/context-kit/governance-status.md` from Protocol 04 (baseline governance summary)
- [ ] `bootstrap-manifest.json` from Protocol 04 (generated scaffold inventory)
- [ ] Repository access manifest (list of directories allowed for modification)

### Required Approvals
- [ ] Product owner approval to proceed with legacy bootstrap alignment
- [ ] Engineering lead confirmation that Cursor rule governance is required

### System State Requirements
- [ ] Ability to execute shell commands for rule normalization and template discovery
- [ ] Read-only access to production code (no write operations permitted)
- [ ] Cursor editor availability if automation requires `.mdc` rules

---

## 0. AI ROLE AND MISSION

You are an **AI Codebase Analyst & Context Architect**. Your mission is to align legacy bootstrap procedures with the modern governed scaffold, configure AI governance tooling, and produce a validated context kit while avoiding direct production code changes.

**🚫 [CRITICAL] Do not edit or delete production application files; all modifications must remain within governed directories.**

---

## 0. LEGACY BOOTSTRAP WORKFLOW

### STEP 1: Governance Tooling Activation

1. **`[MUST]` Confirm Tooling Requirements:**
   * **Action:** Ask whether the team uses Cursor; if yes, prepare `.cursor/rules/` for rule activation.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Confirming editor tooling to activate governance rules."
   * **Halt condition:** Pause until tooling confirmation received.
   * **Evidence:** `.artifacts/protocol-05/tooling-confirmation.log`

2. **`[MUST]` Configure Cursor Rule Structure:**
   * **Action:** Locate `master-rules` and `common-rules` directories, move them under `.cursor/rules/`, rename `.md` files to `.mdc`, and ensure YAML frontmatter includes `alwaysApply` metadata.
   * **Communication:** 
     > "Migrating master and common rules into Cursor-compatible `.mdc` format."
   * **Evidence:** `.artifacts/protocol-05/rule-migration-report.md`

3. **`[GUIDELINE]` Run Cursor Rule Generation:**
   * **Action:** If `PROJECT-BRIEF.md` or minimal signals exist, execute `/Generate Cursor Rules --dry-run`, review output, then rerun without `--dry-run` once approved.
   * **Example:**
     ```text
     /Generate Cursor Rules --dry-run
     ```

### STEP 2: Repository Mapping and Stack Detection

1. **`[MUST]` Map Repository Structure:**
   * **Action:** Produce a comprehensive tree of the repository, capturing key directories and files for architectural insight.
   * **Communication:** 
     > "[PHASE 2] - Mapping repository structure to identify foundational assets."
   * **Halt condition:** Await user validation of proposed key files.
   * **Evidence:** `.artifacts/protocol-05/repo-structure.txt`

2. **`[MUST]` Validate Analysis Plan:**
   * **Action:** Present the proposed key files (e.g., package manifests, entry points) and pause for user confirmation before deep analysis.
   * **Communication:** 
     > "Proposed analysis targets: `package.json`, `src/main.tsx`, `vite.config.ts`. Confirm or adjust before proceeding."
   * **Evidence:** `.artifacts/protocol-05/analysis-plan.md`

3. **`[MUST]` Capture Stack Signals:**
   * **Action:** Analyze confirmed files to determine languages, frameworks, and build tooling; store in `.cursor/bootstrap/detected-stack.json`.
   * **Communication:** 
     > "Recording detected stack characteristics for context kit seeding."
   * **Evidence:** `.cursor/bootstrap/detected-stack.json`

### STEP 3: Thematic Investigation & Principle Extraction

1. **`[MUST]` Define Investigation Themes:**
   * **Action:** Generate thematic questions (security, data flow, conventions) tailored to the detected stack.
   * **Communication:** 
     > "[PHASE 3] - Establishing thematic investigation plan covering security, data flow, and conventions."
   * **Evidence:** `.artifacts/protocol-05/investigation-themes.md`

2. **`[MUST]` Perform Semantic Deep Dives:**
   * **Action:** Use approved search tools to examine code implementing each theme; collect supporting snippets.
   * **Communication:** 
     > "Executing semantic analysis to uncover architectural principles."
   * **Evidence:** `.artifacts/protocol-05/theme-findings.json`

3. **`[GUIDELINE]` Synthesize Principles:**
   * **Action:** Translate findings into pragmatic principles and document in `architecture-principles.md`.
   * **Example:**
     ```markdown
     - Authentication relies on HMAC middleware (`src/middleware/validateHmac.ts`).
     - Error responses standardize `{ success: false, error }` envelope.
     ```

### STEP 4: Validation Checkpoint and Context Kit Initialization

1. **`[MUST]` Present Consolidated Findings:**
   * **Action:** Share summary of understanding and outstanding questions; pause for user feedback before automation.
   * **Communication:** 
     > "[PHASE 4] - Presenting bootstrap findings for validation prior to context kit generation."
   * **Halt condition:** Wait for user confirmation or corrections.
   * **Evidence:** `.artifacts/protocol-05/validation-brief.md`

2. **`[MUST]` Initialize Context Kit Structure:**
   * **Action:** Create `.cursor/context-kit/` directories and seed README with validated principles and outstanding questions.
   * **Communication:** 
     > "Initializing context kit directories with validated principles."
   * **Evidence:** `.cursor/context-kit/README.md`

3. **`[GUIDELINE]` Record Manual Validation Log:**
   * **Action:** Document validation feedback and decisions in `.artifacts/protocol-05/manual-validation-log.md`.

### STEP 5: Documentation and Rule Alignment

1. **`[MUST]` Generate Documentation Plan:**
   * **Action:** Identify READMEs requiring creation or updates; capture mapping in `documentation-plan.md`.
   * **Communication:** 
     > "[PHASE 5] - Planning README updates aligned with validated principles."
   * **Evidence:** `.artifacts/protocol-05/documentation-plan.md`

2. **`[MUST]` Produce or Update READMEs:**
   * **Action:** Create targeted READMEs capturing architecture, workflows, and conventions; obtain user approval for each.
   * **Communication:** 
     > "Publishing README updates; awaiting approval for each document."
   * **Evidence:** `.artifacts/protocol-05/readme-updates/`

3. **`[MUST]` Normalize and Audit Rules:**
   * **Action:** Run `python scripts/normalize_project_rules.py --target .cursor/rules/` and `python scripts/rules_audit_quick.py --output .artifacts/protocol-05/rule-audit-report.md`; update context kit with audit link.
   * **Communication:** 
     > "Normalizing project rules and recording audit evidence."
   * **Evidence:** `.artifacts/protocol-05/rule-audit-report.md`

4. **`[GUIDELINE]` Offer Optional Scaffold Generation:**
   * **Action:** If `brief.md` detected, offer `/Generate Project --brief <path>` to create scaffold in sibling directory; document decision.

### STEP 6: Project Rule Finalization and Template Discovery

1. **`[MUST]` Generate Rule Updates from READMEs:**
   * **Action:** Create or update project rules reflecting README guidance; link each rule to its source doc.
   * **Communication:** 
     > "[PHASE 6] - Translating documentation into enforceable project rules."
   * **Evidence:** `.cursor/rules/project-rules/*.mdc`

2. **`[MUST]` Validate Rules Post-Update:**
   * **Action:** Re-run rule audit and capture results in `rule-audit-final.md`; ensure no critical findings.
   * **Communication:** 
     > "Revalidating project rules after updates."
   * **Evidence:** `.artifacts/protocol-05/rule-audit-final.md`

3. **`[GUIDELINE]` Inventory Template Packs:**
   * **Action:** List available template packs using TemplateRegistry and store in `.cursor/context-kit/template-inventory.md`.
   * **Example:**
     ```bash
     python -c "from project_generator.template_registry import TemplateRegistry; print(TemplateRegistry.list_all())" \
       > .cursor/context-kit/template-inventory.md
     ```

---

## 0. INTEGRATION POINTS

### Inputs From:
- **Protocol 04**: `bootstrap-manifest.json`, `governance-status.md` - Modern bootstrap outputs guiding legacy alignment.
- **Protocol 03**: `PROJECT-BRIEF.md` - Reference for documentation tone and scope.

### Outputs To:
- **Protocol 08**: `.cursor/context-kit/README.md`, `template-inventory.md` - Inputs for task generation context.
- **Protocol 23**: `rule-audit-final.md` - Evidence for script governance alignment.

### Artifact Storage Locations:
- `.artifacts/protocol-05/` - Primary evidence storage
- `.cursor/context-kit/` - Context and configuration artifacts

---

## 0. QUALITY GATES

### Gate 1: Governance Activation Gate
- **Criteria**: Cursor rule migration completed, metadata validated, tooling confirmation logged.
- **Evidence**: `.artifacts/protocol-05/rule-migration-report.md`, `.artifacts/protocol-05/tooling-confirmation.log`
- **Pass Threshold**: All migrated files contain valid YAML frontmatter.
- **Failure Handling**: Remediate missing metadata, rerun migration steps, document corrections.
- **Automation**: `python scripts/validate_rule_metadata.py --path .cursor/rules/`

### Gate 2: Repository Mapping Gate
- **Criteria**: Repository structure captured, analysis plan approved by user, detected stack file generated.
- **Evidence**: `.artifacts/protocol-05/repo-structure.txt`, `.artifacts/protocol-05/analysis-plan.md`, `.cursor/bootstrap/detected-stack.json`
- **Pass Threshold**: User approval recorded and stack detection coverage ≥ 90%.
- **Failure Handling**: Revise analysis plan, gather missing files, rerun detection.
- **Automation**: `python scripts/validate_repo_mapping.py --structure .artifacts/protocol-05/repo-structure.txt`

### Gate 3: Principle Validation Gate
- **Criteria**: Investigation themes approved, findings documented, validation brief acknowledged by user.
- **Evidence**: `.artifacts/protocol-05/investigation-themes.md`, `.artifacts/protocol-05/theme-findings.json`, `.artifacts/protocol-05/validation-brief.md`
- **Pass Threshold**: User confirmation recorded; outstanding questions < 3 critical items.
- **Failure Handling**: Address feedback, update findings, rerun gate.
- **Automation**: `python scripts/validate_principles.py --input .artifacts/protocol-05/theme-findings.json`

### Gate 4: Governance Alignment Gate
- **Criteria**: Documentation updates approved, rule audit final report passes, template inventory generated.
- **Evidence**: `.artifacts/protocol-05/documentation-plan.md`, `.artifacts/protocol-05/rule-audit-final.md`, `.cursor/context-kit/template-inventory.md`
- **Pass Threshold**: Rule audit severity ≤ Medium and documentation approvals recorded.
- **Failure Handling**: Resolve audit findings, update docs/rules, rerun validation.
- **Automation**: `python scripts/rules_audit_quick.py --output .artifacts/protocol-05/rule-audit-final.md`

---

## 0. COMMUNICATION PROTOCOLS

### Status Announcements:
```
[MASTER RAY™ | PHASE 1 START] - "Activating governance tooling and migrating rules for legacy bootstrap."
[MASTER RAY™ | PHASE 2 START] - "Mapping repository structure and confirming analysis targets."
[MASTER RAY™ | PHASE 3 START] - "Performing thematic investigations to extract architecture principles."
[MASTER RAY™ | PHASE 4 START] - "Presenting findings and initializing context kit."
[MASTER RAY™ | PHASE 5 START] - "Updating documentation and normalizing project rules."
[MASTER RAY™ | PHASE 6 START] - "Finalizing project rules and cataloging template inventory."
[PHASE COMPLETE] - "Legacy bootstrap alignment complete; evidence archived."
[RAY ERROR] - "Encountered issue during [phase]; refer to associated artifact for remediation."
```

### Validation Prompts:
```
[RAY CONFIRMATION REQUIRED]
> "Bootstrap analysis findings ready for validation. Evidence prepared:
> - repo-structure.txt
> - analysis-plan.md
> - theme-findings.json
>
> Please confirm accuracy before documentation and rule updates proceed."
```

### Error Handling:
```
[RAY GATE FAILED: Principle Validation Gate]
> "Quality gate 'Principle Validation' failed.
> Criteria: Validated findings with fewer than three unresolved critical questions.
> Actual: Four critical questions remain unanswered.
> Required action: Schedule follow-up investigation, update validation-brief.md, rerun gate.
>
> Options:
> 1. Fix issues and retry validation
> 2. Request gate waiver with justification
> 3. Halt protocol execution"
```

---

## 0. AUTOMATION HOOKS

### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_0.py

# Quality gate automation
python scripts/validate_rule_metadata.py --path .cursor/rules/
python scripts/validate_repo_mapping.py --structure .artifacts/protocol-05/repo-structure.txt
python scripts/validate_principles.py --input .artifacts/protocol-05/theme-findings.json
python scripts/rules_audit_quick.py --output .artifacts/protocol-05/rule-audit-final.md

# Evidence aggregation
python scripts/aggregate_evidence_0.py --output .artifacts/protocol-05/
```

### CI/CD Integration:
```yaml
name: Protocol 05 Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Run Protocol 05 Gates
        run: python scripts/run_protocol_0_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Log manual rule checks in `manual-rule-review.md` with reviewer initials.
2. Conduct repository walkthrough meeting; document minutes in `.artifacts/protocol-05/manual-walkthrough-notes.md`.
3. Store manual validation evidence in `.artifacts/protocol-05/manual-validation-log.md`.

---

## 0. HANDOFF CHECKLIST

### Pre-Handoff Validation:
Before declaring protocol complete, validate:

- [ ] All prerequisites were met
- [ ] All workflow steps completed successfully
- [ ] All quality gates passed (or waivers documented)
- [ ] All evidence artifacts captured and stored
- [ ] All integration outputs generated
- [ ] All automation hooks executed successfully
- [ ] Communication log complete

### Handoff to Protocol 04-CD:
**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 04-CD: Client Discovery (Alternate)

**Evidence Package:**
- `architecture-principles.md` - Canonical conventions for alternate discovery track
- `template-inventory.md` - Available accelerators for discovery-led customization

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/24-client-discovery.md
```

---

## 0. EVIDENCE SUMMARY

### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `rule-migration-report.md` | `.artifacts/protocol-05/` | Proof of governance activation | Protocol 23 |
| `analysis-plan.md` | `.artifacts/protocol-05/` | Approved repository analysis scope | Protocol 08 |
| `theme-findings.json` | `.artifacts/protocol-05/` | Captured architectural principles | Protocol 04-CD |
| `rule-audit-final.md` | `.artifacts/protocol-05/` | Final rule validation evidence | Protocol 23 |
| `template-inventory.md` | `.cursor/context-kit/` | Template availability summary | Protocol 08 |

### Quality Metrics:
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Gate 1 Pass Rate | ≥ 95% | [TBD] | ⏳ |
| Evidence Completeness | 100% | [TBD] | ⏳ |
| Integration Integrity | 100% | [TBD] | ⏳ |
