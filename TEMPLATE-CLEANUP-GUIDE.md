# Template Repository Cleanup Guide

**Purpose:** Transform this repository into a clean, reusable project template by removing project-specific artifacts while preserving core template infrastructure.

---

## 🎯 Template Philosophy

A template repository should:
- ✅ **Contain reusable infrastructure** (scripts, generators, protocols, templates)
- ✅ **Include example/documentation** (README, setup guides, sample configs)
- ❌ **Exclude project-specific data** (artifacts, generated files, personal configs)
- ❌ **Exclude development artifacts** (cache, coverage, logs from development)

---

## 📋 Cleanup Checklist

### ✅ KEEP: Core Template Infrastructure

These directories/files are essential for the template to function:

```
✅ .cursor/
   ✅ ai-driven-workflow/          # Protocol definitions (core templates)
   ✅ rules/                        # Governance rules
   ✅ commands/                     # Command definitions
   ✅ templates/                    # Template files

✅ AI-project-workflow/            # AI/ML project protocol definitions (28-protocol lifecycle)
   ✅ 01-05: Foundation & Discovery protocols
   ✅ 06-09: AI Project Planning protocols
   ✅ 10-14: Model Development protocols
   ✅ 15-17: Model Testing & Quality protocols
   ✅ 18-21: MLOps & Deployment protocols
   ✅ 22-28: Monitoring, Governance & Closure protocols

✅ dev-workflow/                   # Development workflow protocols (The Governor Workflow)
   ✅ 0-bootstrap-your-project.md   # Bootstrap protocol
   ✅ 1-create-prd.md              # PRD creation protocol
   ✅ 2-generate-tasks.md          # Task generation protocol
   ✅ 3-process-tasks.md            # Task execution protocol
   ✅ 4-quality-audit.md           # Quality audit protocol
   ✅ 5-implementation-retrospective.md  # Retrospective protocol
   ✅ protocol-creation/            # Protocol creation utilities
   ✅ review-protocols/             # Review protocol utilities
   ✅ README.md                     # Workflow documentation

✅ scripts/                        # All automation scripts
✅ project_generator/              # Project generation engine
✅ template-packs/                 # Template packs (frontend/backend/etc)
✅ generators/                     # Meta-generators
✅ validators-system/              # Validation infrastructure
✅ unified_workflow/               # Workflow orchestration
✅ transformation-engine/          # Transformation logic
✅ config/                         # Configuration templates
✅ docs/                           # Documentation
✅ tests/                          # Test infrastructure (if template tests)

✅ README.md                       # Main documentation
✅ requirements.txt                # Python dependencies
✅ .gitignore                      # Git ignore rules (needs enhancement)
```

### ❌ REMOVE: Project-Specific Artifacts

These contain data from actual project usage:

```
❌ .artifacts/
   ❌ protocol-01/                 # Generated artifacts from Protocol 01
   ❌ protocol-02/                  # Generated artifacts from Protocol 02
   ❌ protocol-03/                  # Generated artifacts from Protocol 03
   ❌ protocol-04/                  # Generated artifacts from Protocol 04
   ❌ protocol-07/                  # Generated artifacts from Protocol 07
   ❌ protocol-09/                  # Generated artifacts from Protocol 09
   ❌ protocol-10/                  # Generated artifacts from Protocol 10
   ❌ protocol-19/                  # Generated artifacts from Protocol 19
   ❌ protocol-20/                  # Generated artifacts from Protocol 20
   ❌ protocol-21/                  # Generated artifacts from Protocol 21
   ❌ protocol-22/                  # Generated artifacts from Protocol 22
   ❌ analysis-2025/                # Analysis artifacts
   ❌ meta-upgrades/                # Upgrade artifacts
   ❌ validation/                   # Validation results
   ❌ gate-results/                 # Gate results
   ❌ performance/                  # Performance data
   ❌ protocol-generation/          # Generated protocol instances
   ❌ protocol-verification/        # Verification results
   ❌ causal-ledger/                # Project-specific ledger
   ❌ reasoning-dna/               # Project-specific reasoning
   ❌ phase-0-kickoff/              # Phase-specific artifacts
   ❌ phase-4-remediation/          # Phase-specific artifacts
   ❌ phase-5-remediation/          # Phase-specific artifacts
   ❌ plano-validation/             # Validation artifacts
   ❌ protocol-creation/             # Creation artifacts
   ❌ scripts/                      # Generated scripts
   ⚠️  Keep: START_HERE.md (if template guide)
   ⚠️  Keep: SYSTEM_SUMMARY.md (if template documentation)

❌ SAMPLE-AI-PROJECT/              # Sample project (unless it's a template example)
```

### ❌ REMOVE: Project-Specific Documentation

Files created for specific projects/clients:

```
❌ JOB-POST.md                      # Specific job post
❌ PROPOSAL.md                      # Specific proposal
❌ brief.md                         # Specific project brief
❌ plan.md                          # Specific project plan
❌ plan-enhanced.md                 # Enhanced plan
❌ plano.md                         # Project plan
❌ prd-new-ai-protocols.md          # Specific PRD
❌ a.md                             # Temporary/scratch file
❌ IMPLEMENTATION-SUMMARY.md        # Project-specific summary
❌ AGENTS.md                        # Project-specific agents
❌ DECISION-FRAMEWORK.md            # If project-specific
❌ storage-structure.md             # If project-specific
❌ dependency_trace.txt             # Dependency trace
❌ dependency-map.mermaid           # Project-specific diagram
❌ protocol-inventory.json          # Generated inventory
```

### ❌ REMOVE: Development Artifacts

Build/cache/temporary files:

```
❌ __pycache__/                     # Python cache (all directories)
❌ *.pyc                            # Compiled Python files
❌ coverage/                        # Test coverage reports
❌ .pytest_cache/                   # Pytest cache
❌ .coverage                        # Coverage data
❌ .env                             # Environment variables (already in .gitignore)
❌ .env.local                       # Local environment
❌ *.log                            # Log files
❌ metrics/                         # Generated metrics (unless template metrics)
```

### ❌ REMOVE: Personal/Development Files

```
❌ setup-github-token.sh            # Personal setup script
❌ review_pr.py                     # Personal review script
❌ run_review.sh                    # Personal review script
❌ update-master-rules-protocols.sh # Personal update script
❌ gates_config.yaml                # If project-specific
```

### ⚠️ EVALUATE: Meta-Analysis & Documentation

Review these - keep if they're template documentation, remove if project-specific:

```
⚠️  meta-analysis/                  # Keep if template analysis, remove if project-specific
⚠️  docs/                           # Keep template docs, remove project-specific docs
```

**Note:** `dev-workflow/` and `AI-project-workflow/` are now confirmed as template infrastructure and should be KEPT (see KEEP section above).

---

## 🛠️ Recommended Actions

### 1. Enhanced .gitignore

Update `.gitignore` to exclude common artifacts:

```gitignore
# Environment
.env
.env.local
.env.*.local

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
*.egg-info/
dist/
build/
.pytest_cache/
.coverage
htmlcov/

# Project Artifacts
.artifacts/protocol-*/
.artifacts/analysis-*/
.artifacts/meta-upgrades/
.artifacts/validation/
.artifacts/gate-results/
.artifacts/performance/
.artifacts/protocol-generation/
.artifacts/protocol-verification/
.artifacts/causal-ledger/
.artifacts/reasoning-dna/
.artifacts/phase-*/
.artifacts/plano-validation/
.artifacts/protocol-creation/
.artifacts/scripts/

# Logs
*.log
logs/

# Coverage
coverage/
.coverage

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Project-specific (add patterns as needed)
JOB-POST.md
PROPOSAL.md
brief.md
plan*.md
plano.md
prd-*.md
IMPLEMENTATION-SUMMARY.md
dependency_trace.txt
dependency-map.mermaid
protocol-inventory.json
```

### 2. Create Template Setup Script

Create `scripts/template-setup.sh`:

```bash
#!/bin/bash
# Template Setup Script
# Initializes a new project from this template

set -e

echo "🚀 Setting up new project from template..."

# Create .artifacts directory structure
mkdir -p .artifacts/{protocol-01,protocol-02,protocol-03,protocol-04,protocol-05}

# Create example .env file
if [ ! -f .env ]; then
    cp .env.example .env 2>/dev/null || echo "# Add your environment variables here" > .env
fi

# Install dependencies
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
fi

# Make scripts executable
chmod +x scripts/*.sh 2>/dev/null || true
chmod +x scripts/*.py 2>/dev/null || true

echo "✅ Template setup complete!"
echo "📝 Next steps:"
echo "   1. Update .env with your configuration"
echo "   2. Review README.md for usage instructions"
echo "   3. Run: python scripts/generate_from_brief.py --help"
```

### 3. Create .env.example

Create `.env.example` as a template:

```bash
# AI Configuration
AI_API_KEY=your-api-key-here
AI_PROVIDER=claude
AI_MODEL=claude-3-sonnet

# Project Configuration
PROJECT_NAME=your-project-name
PROJECT_ROOT=.

# Evidence Storage
EVIDENCE_DIR=.artifacts

# Logging
LOG_LEVEL=INFO
```

### 4. Create TEMPLATE-README.md

Create a template-specific README section or separate file explaining:
- What this template provides
- How to use it
- What gets generated
- Customization points

---

## 📝 Execution Plan

### Phase 1: Backup Current State
```bash
# Create backup branch
git checkout -b backup-before-template-cleanup
git push origin backup-before-template-cleanup

# Return to master
git checkout master
```

### Phase 2: Remove Project-Specific Artifacts
```bash
# Remove .artifacts subdirectories (keep structure)
rm -rf .artifacts/protocol-*/
rm -rf .artifacts/analysis-*/
rm -rf .artifacts/meta-upgrades/
rm -rf .artifacts/validation/
rm -rf .artifacts/gate-results/
rm -rf .artifacts/performance/
rm -rf .artifacts/protocol-generation/
rm -rf .artifacts/protocol-verification/
rm -rf .artifacts/causal-ledger/
rm -rf .artifacts/reasoning-dna/
rm -rf .artifacts/phase-*/
rm -rf .artifacts/plano-validation/
rm -rf .artifacts/protocol-creation/
rm -rf .artifacts/scripts/

# Remove project-specific docs
rm -f JOB-POST.md PROPOSAL.md brief.md plan*.md plano.md prd-*.md
rm -f IMPLEMENTATION-SUMMARY.md AGENTS.md DECISION-FRAMEWORK.md
rm -f storage-structure.md dependency_trace.txt dependency-map.mermaid
rm -f protocol-inventory.json a.md

# Remove development artifacts
find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
find . -name "*.pyc" -delete
rm -rf coverage/ .pytest_cache/ .coverage

# Remove personal scripts (evaluate first)
# rm -f setup-github-token.sh review_pr.py run_review.sh
# rm -f update-master-rules-protocols.sh
```

### Phase 3: Clean Python Cache
```bash
# Remove all Python cache
find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
find . -name "*.pyc" -delete
find . -name "*.pyo" -delete
find . -name "*.pyd" -delete
```

### Phase 4: Update .gitignore
```bash
# Add comprehensive ignore patterns (see Enhanced .gitignore above)
```

### Phase 5: Create Template Files
```bash
# Create .env.example
# Create scripts/template-setup.sh
# Create TEMPLATE-README.md (if separate)
```

### Phase 6: Verify Template Structure
```bash
# Test template generation
python scripts/generate_from_brief.py --help

# Verify all required files present
# Check README.md is accurate
```

---

## 🎯 Final Template Structure

After cleanup, your template should have:

```
SuperTemplate/
├── .cursor/                    # Template rules and protocols
├── .gitignore                  # Enhanced ignore patterns
├── .env.example                # Template environment config
├── README.md                   # Template documentation
├── requirements.txt            # Dependencies
├── AI-project-workflow/        # AI/ML project protocols (28-protocol lifecycle)
├── dev-workflow/               # Development workflow protocols (The Governor Workflow)
├── scripts/                    # Template scripts
├── project_generator/          # Generation engine
├── template-packs/             # Template packs
├── generators/                 # Meta-generators
├── validators-system/          # Validation system
├── unified_workflow/           # Workflow orchestration
├── transformation-engine/      # Transformation logic
├── config/                     # Config templates
├── docs/                       # Template documentation
├── tests/                      # Template tests
└── .artifacts/                 # Empty structure (created on use)
    └── README.md               # Explains artifact structure
```

---

## ✅ Validation Checklist

Before considering the template "clean":

- [ ] No project-specific artifacts in `.artifacts/`
- [ ] No personal/project-specific documentation files
- [ ] No `__pycache__` directories
- [ ] No `.env` file (only `.env.example`)
- [ ] `.gitignore` excludes all generated artifacts
- [ ] `README.md` explains template usage
- [ ] `requirements.txt` is up to date
- [ ] Template setup script works
- [ ] All scripts are executable
- [ ] No hardcoded project names/paths
- [ ] Example configs use placeholders

---

## 🚀 Next Steps After Cleanup

1. **Tag as Template Version:**
   ```bash
   git tag -a v1.0.0-template -m "Initial template release"
   git push origin v1.0.0-template
   ```

2. **Create Template Documentation:**
   - Usage guide
   - Customization guide
   - Example workflows

3. **Set Up Template Repository:**
   - Use GitHub template repository feature
   - Add template metadata
   - Create example projects

4. **Maintain Template:**
   - Keep core infrastructure updated
   - Don't commit project-specific artifacts
   - Use branches for template development

---

## 📚 Additional Resources

- [GitHub Template Repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository)
- [Best Practices for Template Repos](https://github.com/github/docs/blob/main/contributing/template-repository-guidelines.md)

---

**Last Updated:** 2025-01-XX  
**Maintained By:** Template Maintainers

