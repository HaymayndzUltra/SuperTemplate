# Cursor-Independent Execution Guide

**Version**: 1.0  
**Last Updated**: 2025-10-19  
**For**: Teams without Cursor IDE access

---

## Overview

This guide enables execution of the AI-Driven Workflow System without Cursor IDE. All protocols can be run using standard command-line tools, Python scripts, and manual workflows.

---

## Quick Start (5 Minutes)

### Prerequisites
```bash
# Required software
- Python 3.10+
- Git
- Text editor (VS Code, Vim, etc.)
- Terminal/Command line

# Install Python dependencies
pip install -r requirements.txt
```

### Bootstrap a New Project
```bash
# 1. Clone the template
git clone <repo-url> my-project
cd my-project

# 2. Initialize project context
python3 scripts/bootstrap_project.py \
  --project-name "My Project" \
  --project-type "web-app"

# 3. Validate setup
python3 scripts/doctor.py
```

---

## Protocol Execution (Without Cursor)

### Phase 0: Client Engagement

#### Protocol 01: Client Proposal Generation

**Manual Steps:**
1. Create `JOB-POST.md` with client requirements
2. Analyze job post:
```bash
python3 scripts/analyze_jobpost.py \
  --input JOB-POST.md \
  --output .artifacts/protocol-01/jobpost-analysis.json
```

3. Generate tone map:
```bash
python3 scripts/tone_mapper.py \
  --input .artifacts/protocol-01/jobpost-analysis.json \
  --output .artifacts/protocol-01/tone-map.json
```

4. Write proposal in `.artifacts/protocol-01/PROPOSAL.md`

5. Run validation gates:
```bash
python3 scripts/run_protocol_gates.py 01
```

**Alternative (Full Manual):**
- Read `.cursor/ai-driven-workflow/01-client-proposal-generation.md`
- Follow each step manually
- Document in `.artifacts/protocol-01/`
- Check quality gates manually using checklists

#### Protocol 02: Client Discovery Initiation

**Manual Steps:**
1. Schedule discovery call with client
2. Fill out discovery form template:
```bash
cp .cursor/ai-driven-workflow/templates/discovery-form-template.md \
   .artifacts/protocol-02/client-discovery-form.md
```

3. Complete discovery notes during call
4. Run validation:
```bash
python3 scripts/run_protocol_gates.py 02
```

5. Get client approval via email/document

#### Protocol 03: Project Brief Creation

**Manual Steps:**
1. Consolidate discovery artifacts:
```bash
python3 scripts/brief_processor.py \
  --discovery-dir .artifacts/protocol-02 \
  --output .artifacts/protocol-03/PROJECT-BRIEF.md
```

2. Review and edit brief manually
3. Run validation gates:
```bash
python3 scripts/run_protocol_gates.py 03
```

4. Get stakeholder approvals

---

### Phase 1: Planning & Design

#### Protocol 04: Project Bootstrap

**Manual Steps:**
1. Classify project domain:
```bash
python3 scripts/classify_domain.py \
  --brief .artifacts/protocol-03/PROJECT-BRIEF.md \
  --output .artifacts/protocol-04/domain-classification.json
```

2. Generate project structure:
```bash
python3 scripts/generate_from_brief.py \
  --brief .artifacts/protocol-03/PROJECT-BRIEF.md \
  --output ./project-root
```

3. Set up rules and context:
```bash
python3 scripts/normalize_project_rules.py \
  --project-dir ./project-root
```

#### Protocol 06: Create PRD

**Manual Steps:**
1. Generate PRD assets:
```bash
python3 scripts/generate_prd_assets.py \
  --brief .artifacts/protocol-03/PROJECT-BRIEF.md \
  --output .artifacts/protocol-06/
```

2. Manually edit `.artifacts/protocol-06/PRD.md`

3. Validate PRD:
```bash
python3 scripts/validate_prd_gate.py \
  --input .artifacts/protocol-06/PRD.md
```

#### Protocol 08: Generate Tasks

**Manual Steps:**
1. Generate task breakdown:
```bash
python3 scripts/plan_from_brief.py \
  --prd .artifacts/protocol-06/PRD.md \
  --output .artifacts/protocol-08/tasks.json
```

2. Enrich tasks with lifecycle metadata:
```bash
python3 scripts/enrich_tasks.py \
  --input .artifacts/protocol-08/tasks.json \
  --output .artifacts/protocol-08/enriched-tasks.json
```

3. Map to lifecycle phases:
```bash
python3 scripts/lifecycle_tasks.py \
  --input .artifacts/protocol-08/enriched-tasks.json \
  --output .artifacts/protocol-08/lifecycle-plan.json
```

---

### Phase 2: Development

#### Protocol 10: Process Tasks

**Manual Steps:**
1. Pick next task from `.artifacts/protocol-08/lifecycle-plan.json`
2. Implement task following PRD specifications
3. Update task status:
```bash
python3 scripts/update_task_state.py \
  --task-id "TASK-001" \
  --status "completed" \
  --evidence "path/to/implementation.py"
```

4. Run quality checks:
```bash
python3 scripts/quality_gates.py \
  --task-id "TASK-001"
```

---

### Phase 3: Quality & Testing

#### Protocol 12: Quality Audit

**Manual Steps:**
1. Run comprehensive audit:
```bash
python3 scripts/quality_gates.py \
  --full-audit \
  --output .artifacts/protocol-12/audit-report.json
```

2. Collect coverage:
```bash
python3 scripts/collect_coverage.py \
  --output .artifacts/protocol-12/coverage-report.json
```

3. Review audit report and fix issues

---

### Phase 4: Deployment

#### Protocol 15: Production Deployment

**Manual Steps:**
1. Prepare deployment checklist
2. Run pre-deployment validation:
```bash
python3 scripts/enforce_gates.py \
  --phase "pre-deployment" \
  --output .artifacts/protocol-15/gate-results.json
```

3. Execute deployment (follow platform-specific docs)
4. Verify deployment success

---

## Evidence Management (Without Cursor)

### Generating Evidence Manifests

```bash
# For any protocol
python3 scripts/generate_evidence_manifest.py <protocol_id> \
  --artifact "path/to/artifact.json::status::description" \
  --notes "Manual execution notes"

# Examples
python3 scripts/generate_evidence_manifest.py 01 \
  --artifact ".artifacts/protocol-01/proposal.md::generated::Client proposal" \
  --notes "Generated manually via template"

python3 scripts/generate_evidence_manifest.py 06 \
  --artifact ".artifacts/protocol-06/PRD.md::generated::Product requirements" \
  --notes "Created from brief and stakeholder input"
```

### Aggregating Evidence

```bash
# Protocol-specific aggregation
python3 scripts/aggregate_evidence_01.py
python3 scripts/aggregate_evidence_02.py
python3 scripts/aggregate_evidence_03.py

# Generate comprehensive evidence report
python3 scripts/evidence_report.py \
  --protocols "01,02,03,06,08,10,12" \
  --output .artifacts/evidence-summary.json
```

---

## Quality Gates (Without Cursor)

### Running Gates Manually

```bash
# Run all gates for a protocol
python3 scripts/run_protocol_gates.py <protocol_id>

# Run individual gates
python3 scripts/validate_gate_01_jobpost.py
python3 scripts/validate_gate_02_objectives.py
python3 scripts/validate_gate_03_discovery.py

# Check gate results
cat .artifacts/protocol-XX/gate-manifest.json
```

### Manual Gate Checklists

When automation isn't available, use manual checklists:

**Protocol 01 Gates:**
- [ ] Job post analysis complete (objectives, deliverables, tone identified)
- [ ] Tone strategy confidence ≥ 80%
- [ ] Proposal has all required sections (greeting, understanding, approach, deliverables, collaboration, next steps)
- [ ] Each section ≥ 120 words
- [ ] Readability score ≥ 90 (use online tools)
- [ ] No factual discrepancies
- [ ] ≥ 3 empathy tokens present

**Protocol 02 Gates:**
- [ ] Business objectives documented (≥ 3)
- [ ] Target users identified
- [ ] KPIs defined
- [ ] MVP features listed (≥ 5)
- [ ] Technical constraints documented
- [ ] Timeline discussed and documented
- [ ] Budget expectations captured
- [ ] Client approval received (email/signed doc)

**Protocol 03 Gates:**
- [ ] All Protocol 02 artifacts present
- [ ] PROJECT-BRIEF.md has all required sections
- [ ] Traceability map links brief to discovery
- [ ] Client approval recorded with timestamp
- [ ] Internal approval recorded with timestamp

---

## Workflow Orchestration (Without Cursor)

### Sequential Execution

```bash
# Phase 0: Client engagement
python3 scripts/run_protocol_gates.py 01  # Proposal
python3 scripts/run_protocol_gates.py 02  # Discovery
python3 scripts/run_protocol_gates.py 03  # Brief

# Phase 1: Planning
python3 scripts/classify_domain.py ...
python3 scripts/generate_prd_assets.py ...
python3 scripts/plan_from_brief.py ...

# Phase 2: Development
python3 scripts/run_workflow.py \
  --tasks .artifacts/protocol-08/lifecycle-plan.json

# Phase 3: Quality
python3 scripts/quality_gates.py --full-audit

# Phase 4: Deployment
python3 scripts/enforce_gates.py --phase pre-deployment
```

### Workflow Runner

```bash
# Run entire workflow with checkpoints
python3 scripts/run_workflow.py \
  --start-protocol 01 \
  --end-protocol 15 \
  --checkpoint-dir .artifacts/checkpoints \
  --interactive
```

---

## Troubleshooting

### Common Issues

**Issue**: Script not found
```bash
# Solution: Verify script exists
ls scripts/<script-name>.py

# Check registry
cat scripts/script-registry.json | grep <script-name>
```

**Issue**: Missing dependencies
```bash
# Solution: Install requirements
pip install -r requirements.txt

# Or install individually
pip install pyyaml requests pytest
```

**Issue**: Permission denied
```bash
# Solution: Make scripts executable
chmod +x scripts/*.py scripts/*.sh
```

**Issue**: Artifact not found
```bash
# Solution: Check prerequisites
python3 scripts/validate_prerequisites_<protocol-id>.py

# Or create artifacts directory
mkdir -p .artifacts/protocol-XX
```

---

## IDE-Agnostic Tips

### Using VS Code
```bash
# Install Python extension
code --install-extension ms-python.python

# Open workspace
code /path/to/project

# Run scripts from integrated terminal
Ctrl+` (open terminal)
python3 scripts/<script>.py
```

### Using Vim/Neovim
```bash
# Edit protocol documents
vim .cursor/ai-driven-workflow/01-client-proposal-generation.md

# Run scripts from Vim
:!python3 scripts/run_protocol_gates.py 01

# Split window for reference
:split .cursor/ai-driven-workflow/01-client-proposal-generation.md
```

### Using JetBrains IDEs
```bash
# Open project in PyCharm/IntelliJ
pycharm /path/to/project

# Configure Python interpreter: Settings > Project > Python Interpreter
# Run scripts: Right-click > Run
```

---

## Automation Without Cursor

### GitHub Actions Integration

```yaml
# .github/workflows/protocol-gates.yml
name: Protocol Gates
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
      - run: pip install -r requirements.txt
      - run: python3 scripts/run_protocol_gates.py 01
```

### GitLab CI Integration

```yaml
# .gitlab-ci.yml
protocol-validation:
  stage: test
  script:
    - pip install -r requirements.txt
    - python3 scripts/run_protocol_gates.py 01
```

### Pre-commit Hooks

```bash
# .git/hooks/pre-commit
#!/bin/bash
python3 scripts/validate_script_registry.py || exit 1
python3 scripts/doctor.py || exit 1
```

---

## Migration from Cursor

### Step-by-Step Migration

1. **Extract Context**: Export Cursor rules to `.cursor/rules/`
2. **Document Workflows**: Convert Cursor commands to shell scripts
3. **Test Automation**: Verify all scripts work without Cursor
4. **Update Documentation**: Add manual fallback instructions
5. **Train Team**: Conduct walkthrough with team members

---

## Support & Resources

- **Protocol Documentation**: `.cursor/ai-driven-workflow/*.md`
- **Script Reference**: `scripts/script-registry.json`
- **Quick Reference**: `documentation/gate-automation-quick-reference.md`
- **Troubleshooting**: Run `python3 scripts/doctor.py` for diagnostics

---

## FAQ

**Q: Can I use this without any AI tooling?**  
A: Yes! All protocols can be executed manually. The AI scripts are helpers, not requirements.

**Q: What if a script fails?**  
A: Check the error message, verify prerequisites, and consult the protocol documentation for manual fallback procedures.

**Q: How do I know which protocol to run?**  
A: Follow the sequence in `documentation/protocol-sequence.md` or use the MASTER RAY protocol orchestrator prompts.

**Q: Can I customize the workflows?**  
A: Yes! Fork the repository, modify scripts, and update protocol documentation to match your needs.

---

**Version History**
- **1.0** (2025-10-19): Initial release for Cursor-independent execution
