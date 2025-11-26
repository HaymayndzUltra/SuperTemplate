# MASTER RAY™ AI-Driven Workflow Platform

**Transform chaotic development into validated, auditable excellence.**

[![Protocols](https://img.shields.io/badge/Protocols-30+-blue)](#-protocol-system)
[![Validators](https://img.shields.io/badge/Validators-11-green)](#-validation-system)
[![Scripts](https://img.shields.io/badge/Scripts-82+-orange)](#-automation-scripts)
[![License](https://img.shields.io/badge/License-Proprietary-red)](#)

---

## 🎯 What is MASTER RAY™?

**MASTER RAY™** is a comprehensive AI-driven workflow orchestration platform that provides **30+ validated protocols** covering the complete software development lifecycle—from client conversation to production deployment and maintenance. It features:

- **🧠 Intelligent Protocol Router (05b)**: Analyzes projects across 27+ dimensions to select optimal protocols
- **✅ 11-Validator System**: Scores protocols on 50 dimensions with ≥0.95 pass threshold
- **🔀 Dual-Track Support**: Generic web development AND AI/ML project workflows
- **📋 Complete Audit Trail**: Evidence tracking with SHA-256 checksums
- **🔧 82+ Automation Scripts**: Orchestration, validation, and deployment automation

### Who Is This For?

- **AI/ML Engineers** building production machine learning systems
- **Full-Stack Developers** seeking standardized, quality-assured workflows
- **Freelancers & Agencies** needing reproducible delivery processes
- **Organizations** requiring auditable, compliant development

---

## 🚀 Quick Start

### Option 1: Streamlined Development Workflow (5 Protocols)

For rapid feature development using the simplified workflow:

```bash
# 1. Bootstrap your project
@apply dev-workflow/0-bootstrap-your-project.md

# 2. Create requirements document
@apply dev-workflow/1-create-prd.md

# 3. Generate tasks
@apply dev-workflow/2-generate-tasks.md

# 4. Execute with quality gates
@apply dev-workflow/3-process-tasks.md

# 5. Quality audit
@apply dev-workflow/4-quality-audit.md
```

### Option 2: Full 23-Protocol Lifecycle

For complete project lifecycle with all quality gates:

```bash
# Install dependencies
pip install -r requirements.txt

# Validate environment
python scripts/doctor.py --strict

# Analyze project brief
python scripts/analyze_brief.py PROJECT-BRIEF.md --output brief-analysis.json

# Run full workflow orchestration
python scripts/run_workflow.py \
  --project-name "my-project" \
  --phases "0-6" \
  --brief brief-analysis.json
```

---

## 📐 System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           MASTER RAY™ ARCHITECTURE                          │
└─────────────────────────────────────────────────────────────────────────────┘

  CLIENT BRIEF                                                    DELIVERY
       │                                                               ▲
       ▼                                                               │
┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   PHASE 0    │───▶│   PHASE 1-2  │───▶│   PHASE 3-4  │───▶│   PHASE 5-6  │
│  Foundation  │    │   Planning   │    │ Development  │    │   Delivery   │
│  & Discovery │    │   & Design   │    │   & Testing  │    │   & Closure  │
└──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘
  Protocols 01-05    Protocols 06-09    Protocols 10-14     Protocols 15-23
       │
       ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│                     PROTOCOL 05B: INTELLIGENT ROUTER                         │
│                                                                              │
│  • Classifies project across 27+ dimensions (AI/ML, Data, Infrastructure)   │
│  • Selects optimal protocol path (Generic vs AI/ML vs Hybrid)               │
│  • Detects coverage gaps and invokes Protocol 0 for new protocols           │
│  • Generates customized PROTOCOL-EXECUTION-PLAN.md                          │
│                                                                              │
│  7 Quality Gates │ 8 Phases │ 26 Automation Scripts │ 35+ Artifacts         │
└──────────────────────────────────────────────────────────────────────────────┘
       │
       ├── Coverage ≥95% ────────────────────────────────────────┐
       │                                                          │
       └── Coverage <95% ─▶ PROTOCOL 0 (Gap Creation) ─▶ New Protocols ≥0.95
```

**[→ Full Architecture Details](./ARCHITECTURE.md)**

---

## 📋 Protocol System

### Dual-Track Design

MASTER RAY™ supports two parallel tracks that can be mixed based on project needs:

| Track | Directory | Protocols | Use Case |
|-------|-----------|-----------|----------|
| **Generic Track** | `.cursor/ai-driven-workflow/` | 01-23 + docs | Web apps, APIs, Mobile |
| **AI/ML Track** | `AI-project-workflow/` | 01-15 | Machine learning projects |

### Protocol Overview

#### Phase 0: Foundation & Discovery (Protocols 01-05)
| ID | Protocol | Purpose |
|----|----------|---------|
| 01 | Client Proposal Generation | Generate winning freelance proposals |
| 02 | Client Discovery Initiation | Structured discovery conversation |
| 03 | Project Brief Creation | Comprehensive requirements document |
| 04 | Project Bootstrap & Context | Context engineering and setup |
| 05 | Bootstrap Your Project | Project scaffolding and structure |
| **05b** | **Protocol Orchestration** | **Intelligent protocol router** |

#### Phase 1-2: Planning & Design (Protocols 06-09)
| ID | Protocol | Purpose |
|----|----------|---------|
| 06 | Create PRD | Product Requirements Document |
| 07 | Technical Design | Architecture and design specs |
| 08 | Generate Tasks | Task breakdown and planning |
| 09 | Environment Setup | Development environment validation |

#### Phase 3-4: Development & Quality (Protocols 10-14)
| ID | Protocol | Purpose |
|----|----------|---------|
| 10 | Process Tasks | Execute development tasks |
| 11 | Integration Testing | Cross-component testing |
| 12 | Quality Audit | Code quality assessment |
| 13 | UAT Coordination | User acceptance testing |
| 14 | Pre-Deployment Staging | Staging validation |

#### Phase 5-6: Deployment & Closure (Protocols 15-23)
| ID | Protocol | Purpose |
|----|----------|---------|
| 15 | Production Deployment | Live deployment execution |
| 16 | Monitoring & Observability | System monitoring setup |
| 17 | Incident Response | Emergency procedures |
| 18 | Performance Optimization | Performance tuning |
| 19 | Documentation | Knowledge transfer |
| 20 | Project Closure | Formal completion |
| 21 | Maintenance Support | Ongoing support |
| 22 | Retrospective | Lessons learned |
| 23 | Script Governance | Automation management |

---

## ✅ Validation System

Every protocol must pass **11 validators** scoring **50 dimensions** with a **≥0.95 pass threshold**.

| Validator | Dimensions | Status |
|-----------|------------|--------|
| 1. Protocol Identity | Metadata, compliance, versioning | ✅ Implemented |
| 2. AI Role | Role definition, mission, constraints | 📋 Ready |
| 3. Workflow Algorithm | Steps, sequences, halt conditions | 📋 Ready |
| 4. Quality Gates | Checkpoints, criteria, automation | 📋 Ready |
| 5. Script Integration | References, existence, registration | 📋 Ready |
| 6. Communication Protocol | Status announcements, prompts | 📋 Ready |
| 7. Evidence Package | Artifacts, storage, manifest | 📋 Ready |
| 8. Handoff Checklist | Integration, sign-offs | 📋 Ready |
| 9. Cognitive Reasoning | Decision logic, learning | 📋 Ready |
| 10. Meta-Reflection | Improvement, knowledge | 📋 Ready |

### Validation Commands

```bash
# Validate single protocol
python validators-system/scripts/validate_protocol_identity.py --protocol 01

# Validate all protocols
python validators-system/scripts/validate_all_protocols.py \
  --workspace . \
  --protocol-dir .cursor/ai-driven-workflow
```

**[→ Validator System Details](./validators-system/README.md)**

---

## 🔧 Automation Scripts

**82+ scripts** organized by function:

| Category | Location | Count | Purpose |
|----------|----------|-------|---------|
| **Orchestration** | `scripts/orchestration/` | 37 | Protocol 05b automation |
| **Validators** | `validators-system/scripts/` | 11 | Protocol validation |
| **AI/ML** | `scripts/ai/` | 20+ | Data and model operations |
| **Quality** | `scripts/` | 20+ | Gates and auditing |
| **Deployment** | `scripts/` | 10+ | CI/CD and deployment |

### Script Registry

All scripts are tracked in `scripts/script-registry.json`:

```json
{
  "scripts": {
    "classify_project_type": {
      "path": "scripts/orchestration/classify_project_type.py",
      "protocol": "05b",
      "phase": "PHASE 2",
      "purpose": "Project classification across 27+ dimensions",
      "status": "active"
    }
  }
}
```

**[→ Script Documentation](./scripts/README.md)**

---

## 📂 Directory Structure

```
SuperTemplate-1/
├── .cursor/
│   ├── ai-driven-workflow/          # 📋 Generic protocols (01-23+)
│   ├── rules/                       # 📜 AI governance rules
│   │   ├── master-rules/            #    6 Master Rules
│   │   ├── common-rules/            #    Shared rules
│   │   └── project-rules/           #    Project-specific
│   └── project-protocols/           # 🎯 Generated protocols
│
├── AI-project-workflow/             # 🤖 AI/ML protocols (01-15)
│
├── validators-system/               # ✅ 11-Validator system
│   ├── scripts/                     #    Validator implementations
│   └── documentation/               #    Specs and guides
│
├── scripts/                         # 🔧 82+ automation scripts
│   ├── orchestration/               #    Protocol 05b scripts
│   ├── ai/                          #    AI/ML scripts
│   └── script-registry.json         #    Script registry
│
├── config/                          # ⚙️ System configuration
│   ├── classification-dimensions.yaml
│   ├── protocol_gates/              #    Gate definitions
│   └── schemas/                     #    JSON schemas
│
├── generators/                      # 🏭 Protocol generation
│   └── protocol-workflow/           #    Protocol 0 system
│
├── .artifacts/                      # 📦 Generated evidence
│   ├── protocol-{id}/               #    Per-protocol artifacts
│   └── validation/                  #    Validation reports
│
├── dev-workflow/                    # ⚡ Streamlined 5-protocol workflow
├── template-packs/                  # 📁 Code scaffolding templates
├── documentation/                   # 📚 System documentation
│
├── ARCHITECTURE.md                  # 🏛️ System architecture
├── PROJECT-BRIEF.md                 # 📄 Project requirements
├── PROTOCOL-EXECUTION-PLAN.md       # 📋 Generated execution plan
└── PROTOCOL-CHECKLIST.md            # ☑️ Execution tracking
```

---

## 📜 Rule System

MASTER RAY™ uses a sophisticated rule system to govern AI behavior:

### Master Rules (Always Applied)
| Rule | Purpose |
|------|---------|
| 1. Context Discovery | System BIOS - discovers and loads rules |
| 2. AI Collaboration | Think-First protocol, task planning |
| 3. Code Quality | Development standards and practices |
| 4. Modification Safety | Change management and validation |
| 5. Documentation | Context and README guidelines |
| 6. Rule Creation | Governance for creating rules |

### Rule Directives
- `[STRICT]` - Non-negotiable, mandatory
- `[GUIDELINE]` - Strong recommendation, can deviate with justification

**[→ Rule System Details](./.cursor/rules/README.md)**

---

## 🎯 Key Concepts

### Protocol Router (05b)
The "brain" of MASTER RAY™ that:
1. **Classifies** projects across 27+ dimensions
2. **Selects** optimal protocols (Generic vs AI/ML vs Hybrid)
3. **Detects gaps** when coverage <95%
4. **Invokes Protocol 0** to generate new protocols
5. **Sequences** protocols respecting dependencies
6. **Generates** customized execution plans

### Protocol 0 (Meta-Generator)
Creates NEW protocols when the router detects gaps:
1. Analyzes gap specification
2. Generates protocol from templates
3. Validates with ≥0.95 score
4. Registers in script registry
5. Integrates into execution plan

### Evidence System
Complete audit trail for every action:
- **Artifacts**: JSON/MD files per protocol
- **Manifests**: `evidence-manifest.json`
- **Integrity**: `checksums.sha256`
- **Packages**: `handoff-package.zip`

---

## 📊 Current Status

### Implementation Progress
| Component | Status | Notes |
|-----------|--------|-------|
| Generic Protocols (01-23) | ✅ 100% | Complete lifecycle |
| AI/ML Protocols (01-15) | ✅ 50% | Through Model Testing |
| Protocol Router (05b) | ✅ 100% | Full implementation |
| Validator System | 🟡 10% | 1/11 validators |
| Orchestration Scripts | ✅ 100% | 37 scripts |
| Evidence System | ✅ 100% | Full tracking |

### Roadmap
1. **Q1 2025**: Complete Validators 2-4 (AI Role, Workflow, Gates)
2. **Q2 2025**: AI/ML Protocols 16-28 (MLOps lifecycle)
3. **Q3 2025**: Full validator implementation (5-10)
4. **Q4 2025**: CI/CD integration and GitHub workflows

---

## 📚 Documentation

| Document | Purpose |
|----------|---------|
| [ARCHITECTURE.md](./ARCHITECTURE.md) | System architecture and data flow |
| [validators-system/README.md](./validators-system/README.md) | Validator specifications |
| [scripts/README.md](./scripts/README.md) | Script documentation |
| [.cursor/rules/README.md](./.cursor/rules/README.md) | Rule system guide |
| [.cursor/ai-driven-workflow/README.md](./.cursor/ai-driven-workflow/README.md) | Generic protocols |
| [AI-project-workflow/README.md](./AI-project-workflow/README.md) | AI/ML protocols |
| [dev-workflow/README.md](./dev-workflow/README.md) | Streamlined workflow |

---

## 🤝 Contributing

1. **Review** relevant protocol and rules
2. **Follow** the 11-validator requirements
3. **Test** with `validate_all_protocols.py`
4. **Document** changes appropriately
5. **Submit** with evidence package

---

## 📞 Support

- **Protocol Questions**: Review `.cursor/ai-driven-workflow/AGENTS.md`
- **Validation Issues**: Check `validators-system/documentation/`
- **Script Problems**: See `scripts/README.md`
- **Architecture**: Consult `ARCHITECTURE.md`

---

## 📄 License

**MASTER RAY™ AI-Driven Workflow Protocol**  
© 2025 - All Rights Reserved

---

**MASTER RAY™** - Where every line of code tells a story of validation, evidence, and continuous improvement.

*"Kaya natin to!"* 💪
