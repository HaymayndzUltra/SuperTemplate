# MASTER RAY™ System Architecture

**Version:** 1.0.0  
**Last Updated:** 2025-11-25  
**Status:** Production Ready

---

## 📐 Architecture Overview

MASTER RAY™ is a layered architecture system that transforms chaotic software development into structured, validated, and auditable workflows.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           MASTER RAY™ ARCHITECTURE                          │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  LAYER 1: GOVERNANCE (Rules & Constraints)                                  │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐           │
│  │   Master    │ │   Common    │ │  Project    │ │   Always    │           │
│  │   Rules     │ │   Rules     │ │   Rules     │ │   Applied   │           │
│  │   (1-6)     │ │  (Shared)   │ │ (Specific)  │ │   Rules     │           │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘           │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  LAYER 2: ORCHESTRATION (Protocol Router 05b)                               │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │  INPUT                PROCESS                        OUTPUT           │ │
│  │  ─────                ───────                        ──────           │ │
│  │  PROJECT-BRIEF.md  ──► Classification (27+ dims)  ──► EXECUTION-PLAN  │ │
│  │  architecture.md   ──► Protocol Selection         ──► CHECKLIST       │ │
│  │  bootstrap.json    ──► Gap Detection (Protocol 0) ──► handoff.zip     │ │
│  │                    ──► Sequencing & Timeline                          │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│                          7 Quality Gates                                    │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  LAYER 3: PROTOCOLS (Dual-Track Execution)                                  │
│  ┌──────────────────────────────┐ ┌──────────────────────────────┐         │
│  │     GENERIC TRACK            │ │     AI/ML TRACK              │         │
│  │     ══════════════           │ │     ════════════             │         │
│  │  Phase 0: Foundation (01-05) │ │  Phase 0: Foundation (01-05) │         │
│  │  Phase 1: Planning (06-09)   │ │  Phase 1: AI Planning (06-07)│         │
│  │  Phase 3: Development (10-11)│ │  Phase 2: Data Prep (08-11)  │         │
│  │  Phase 4: Quality (12-14)    │ │  Phase 3: Model Dev (12-14)  │         │
│  │  Phase 5: Deployment (15-18) │ │  Phase 4: Testing (15-17)    │         │
│  │  Phase 6: Closure (19-23)    │ │  Phase 5+: MLOps (18-28)     │         │
│  └──────────────────────────────┘ └──────────────────────────────┘         │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  LAYER 4: VALIDATION (11 Validators × 5 Dimensions = 50 Checks)             │
│  ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐                         │
│  │ V1:ID │ │V2:Role│ │V3:Work│ │V4:Gate│ │V5:Scrp│  Pass: ≥0.95            │
│  └───────┘ └───────┘ └───────┘ └───────┘ └───────┘                         │
│  ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐  Warn: 0.80-0.94        │
│  │V6:Comm│ │V7:Evid│ │V8:Hand│ │V9:Reas│ │V10:Ref│  Fail: <0.80            │
│  └───────┘ └───────┘ └───────┘ └───────┘ └───────┘                         │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  LAYER 5: EVIDENCE (Complete Audit Trail)                                   │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │  .artifacts/                                                          │ │
│  │  ├── protocol-{id}/        Per-protocol evidence                     │ │
│  │  │   ├── *.json            Structured data                           │ │
│  │  │   ├── *.md              Human-readable docs                       │ │
│  │  │   └── evidence-manifest.json                                      │ │
│  │  ├── validation/           Validator reports                         │ │
│  │  │   └── protocol-{id}-{validator}.json                              │ │
│  │  └── handoff-package.zip   Complete context bundle                   │ │
│  │      ├── checksums.sha256  Integrity verification                    │ │
│  │      └── evidence-manifest.json                                      │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  LAYER 6: AUTOMATION (82+ Scripts)                                          │
│  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐               │
│  │  ORCHESTRATION  │ │   VALIDATION    │ │   AI/ML         │               │
│  │  37 scripts     │ │   11 scripts    │ │   20+ scripts   │               │
│  │  Protocol 05b   │ │   Validators    │ │   Data/Model    │               │
│  └─────────────────┘ └─────────────────┘ └─────────────────┘               │
│  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐               │
│  │   QUALITY       │ │   DEPLOYMENT    │ │   GOVERNANCE    │               │
│  │   Gates, Audit  │ │   CI/CD         │ │   Registry      │               │
│  └─────────────────┘ └─────────────────┘ └─────────────────┘               │
│                                                                             │
│  Registry: scripts/script-registry.json                                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🔄 Data Flow Diagram

```
                                 ┌─────────────────┐
                                 │  CLIENT INPUT   │
                                 │  (Job Post,     │
                                 │   Requirements) │
                                 └────────┬────────┘
                                          │
                                          ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                        PHASE 0: FOUNDATION & DISCOVERY                       │
│                                                                              │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │ Protocol 01 │───▶│ Protocol 02 │───▶│ Protocol 03 │───▶│ Protocol 04 │  │
│  │  Proposal   │    │  Discovery  │    │ Brief       │    │  Bootstrap  │  │
│  └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘  │
│                                                                    │        │
│                                              ┌─────────────┐       │        │
│                                              │ Protocol 05 │◄──────┘        │
│                                              │  Project    │                │
│                                              │  Setup      │                │
│                                              └──────┬──────┘                │
└─────────────────────────────────────────────────────┼───────────────────────┘
                                                      │
                              ┌────────────────────────────────────────┐
                              │         FOUNDATION ARTIFACTS            │
                              │  • PROJECT-BRIEF.md                     │
                              │  • architecture-principles.md           │
                              │  • bootstrap-manifest.json              │
                              │  • .cursor/context/*                    │
                              └────────────────────┬───────────────────┘
                                                   │
                                                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                     PROTOCOL 05B: INTELLIGENT ROUTER                         │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                         8 PHASES                                     │   │
│  │                                                                      │   │
│  │  PHASE 0 ──▶ PHASE 1 ──▶ PHASE 2 ──▶ PHASE 3 ──▶ PHASE 4 ──▶      │   │
│  │  Pre-Flight  Context    Classify    Select     Gap                  │   │
│  │  Validation  Loading    Project     Protocols  Detection            │   │
│  │     │           │          │           │          │                 │   │
│  │     ▼           │          ▼           │          ▼                 │   │
│  │  Gate 0         │       Gate 1      Gate 2-3   Protocol 0           │   │
│  │                 │                               (if gaps)           │   │
│  │                 │                                  │                │   │
│  │  PHASE 5 ◄──────┘                                  │                │   │
│  │  Sequence                                          │                │   │
│  │     │                                              │                │   │
│  │     ▼                                              │                │   │
│  │  PHASE 6 ──▶ PHASE 7                               │                │   │
│  │  Generate    Protocol                              │                │   │
│  │  Plan        Generation ◄──────────────────────────┘                │   │
│  │     │           │                                                   │   │
│  │  Gate 5-6    Gate 7                                                 │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  27+ Classification Dimensions:                                              │
│  • AI/ML (7): training, deployment, pipeline, features, monitoring...       │
│  • Data (7): SQL, NoSQL, Vector, volume, realtime, batch, migration...      │
│  • Application (6): auth, users, uploads, realtime, i18n, multitenancy...   │
│  • Infrastructure (7): AWS/GCP/Azure, containers, CI/CD, monitoring...      │
│  • Compliance (4): GDPR, HIPAA, SOC2, security audit...                     │
│  • Team (4): solo, team, frontend/backend split, DevOps capability...       │
└─────────────────────────────────────────────────────────────────────────────┘
                                          │
                                          ▼
                              ┌────────────────────────────────────────┐
                              │         ROUTER OUTPUTS                  │
                              │  • PROTOCOL-EXECUTION-PLAN.md           │
                              │  • PROTOCOL-CHECKLIST.md                │
                              │  • .cursor/project-protocols/*          │
                              │  • handoff-package.zip                  │
                              └────────────────────┬───────────────────┘
                                                   │
                    ┌──────────────────────────────┴──────────────────────────┐
                    │                                                          │
                    ▼                                                          ▼
┌─────────────────────────────────────┐     ┌─────────────────────────────────────┐
│        GENERIC WEB TRACK            │     │        AI/ML TRACK                  │
│                                     │     │                                     │
│  Phase 1-2: Planning & Design       │     │  Phase 1: AI Planning               │
│  ├── 06: Create PRD                 │     │  ├── 06: AI Use Case Definition     │
│  ├── 07: Technical Design           │     │  └── 07: Data Strategy Planning     │
│  ├── 08: Generate Tasks             │     │                                     │
│  └── 09: Environment Setup          │     │  Phase 2: Data Preparation          │
│                                     │     │  ├── 08: Data Collection            │
│  Phase 3: Development               │     │  ├── 09: Data Cleaning              │
│  ├── 10: Process Tasks              │     │  ├── 10: Feature Engineering        │
│  └── 11: Integration Testing        │     │  └── 11: Dataset Preparation        │
│                                     │     │                                     │
│  Phase 4: Quality & Testing         │     │  Phase 3: Model Development         │
│  ├── 12: Quality Audit              │     │  ├── 12: Algorithm Selection        │
│  ├── 13: UAT Coordination           │     │  ├── 13: Model Training             │
│  └── 14: Pre-Deployment Staging     │     │  └── 14: Model Validation           │
│                                     │     │                                     │
│  Phase 5: Deployment & Operations   │     │  Phase 4: Model Testing             │
│  ├── 15: Production Deployment      │     │  └── 15: Edge Case Validation       │
│  ├── 16: Monitoring & Observability │     │                                     │
│  ├── 17: Incident Response          │     │  Phase 5-7: MLOps (16-28)           │
│  └── 18: Performance Optimization   │     │  (Deployment, Monitoring,           │
│                                     │     │   Drift Detection, Retraining...)   │
│  Phase 6: Closure & Maintenance     │     │                                     │
│  ├── 19: Documentation              │     │                                     │
│  ├── 20: Project Closure            │     │                                     │
│  ├── 21: Maintenance Support        │     │                                     │
│  ├── 22: Retrospective              │     │                                     │
│  └── 23: Script Governance          │     │                                     │
└─────────────────────────────────────┘     └─────────────────────────────────────┘
                    │                                                          │
                    └──────────────────────────────┬──────────────────────────┘
                                                   │
                                                   ▼
                              ┌────────────────────────────────────────┐
                              │         VALIDATION LAYER                │
                              │  11 Validators × 5 Dimensions           │
                              │  Pass Threshold: ≥0.95                  │
                              │                                         │
                              │  Validation Reports:                    │
                              │  .artifacts/validation/protocol-*.json  │
                              └────────────────────┬───────────────────┘
                                                   │
                                                   ▼
                              ┌────────────────────────────────────────┐
                              │         EVIDENCE LEDGER                 │
                              │  Complete Audit Trail                   │
                              │                                         │
                              │  • Per-protocol artifacts               │
                              │  • Checksum verification                │
                              │  • Manifest tracking                    │
                              │  • Retention policies                   │
                              └────────────────────┬───────────────────┘
                                                   │
                                                   ▼
                                 ┌─────────────────┐
                                 │    DELIVERY     │
                                 │  (Production    │
                                 │   System)       │
                                 └─────────────────┘
```

---

## 🔌 Component Interactions

### Protocol Router (05b) Interactions

```
                    ┌────────────────────────────────┐
                    │        PROTOCOL 05b            │
                    │   (Workflow Orchestrator)      │
                    └────────────────────────────────┘
                                    │
         ┌──────────────────────────┼──────────────────────────┐
         │                          │                          │
         ▼                          ▼                          ▼
┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│  INPUTS FROM    │      │  LATERAL TO     │      │  OUTPUTS TO     │
│  UPSTREAM       │      │  SYSTEM         │      │  DOWNSTREAM     │
├─────────────────┤      ├─────────────────┤      ├─────────────────┤
│ Protocol 03:    │      │ Protocol 0:     │      │ Variable:       │
│ PROJECT-BRIEF   │      │ Gap Creation    │      │ Next Protocol   │
│                 │      │                 │      │ (06 or AI:06)   │
│ Protocol 04:    │      │ Validators:     │      │                 │
│ .cursor/context │      │ Score ≥0.95     │      │ Deliverables:   │
│                 │      │                 │      │ EXECUTION-PLAN  │
│ Protocol 05:    │      │ Script Registry │      │ CHECKLIST       │
│ bootstrap.json  │      │ Registration    │      │ handoff.zip     │
│ architecture.md │      │                 │      │                 │
└─────────────────┘      └─────────────────┘      └─────────────────┘
```

### Validator System Interactions

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         VALIDATOR SYSTEM                                     │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐
│   PROTOCOL      │         │   VALIDATORS    │         │   OUTPUTS       │
│   FILES         │         │   (11 Scripts)  │         │                 │
├─────────────────┤         ├─────────────────┤         ├─────────────────┤
│ .cursor/        │ ──────▶ │ V1: Identity    │ ──────▶ │ Score: 0.0-1.0  │
│ ai-driven-      │         │ V2: AI Role     │         │                 │
│ workflow/*.md   │         │ V3: Workflow    │         │ Status:         │
│                 │         │ V4: Gates       │         │ PASS/WARN/FAIL  │
│ AI-project-     │         │ V5: Scripts     │         │                 │
│ workflow/*.md   │         │ V6: Communication│        │ Evidence:       │
│                 │         │ V7: Evidence    │         │ .artifacts/     │
│                 │         │ V8: Handoff     │         │ validation/     │
│                 │         │ V9: Reasoning   │         │                 │
│                 │         │ V10: Reflection │         │                 │
└─────────────────┘         └─────────────────┘         └─────────────────┘
        │                           │                           │
        │                           │                           │
        ▼                           ▼                           ▼
┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐
│   GATE CONFIGS  │         │   THRESHOLDS    │         │   REPORTS       │
├─────────────────┤         ├─────────────────┤         ├─────────────────┤
│ config/         │         │ Pass: ≥0.95     │         │ protocol-XX-    │
│ protocol_gates/ │         │ Warn: 0.80-0.94 │         │ identity.json   │
│ *.yaml          │         │ Fail: <0.80     │         │                 │
│                 │         │                 │         │ master-report   │
│ Gate triggers   │         │ Per-dimension   │         │ .json           │
│ Prerequisites   │         │ ≥0.90 required  │         │                 │
└─────────────────┘         └─────────────────┘         └─────────────────┘
```

---

## 🎛️ Extension Points

### Adding New Protocols

1. **Create Protocol File**: Follow template in `.cursor/ai-driven-workflow/`
2. **Run Validators**: Achieve ≥0.95 score
3. **Register Scripts**: Update `scripts/script-registry.json`
4. **Update Router**: Add to `config/classification-dimensions.yaml`
5. **Document**: Update integration map and this architecture

### Adding New Validators

1. **Create Script**: `validators-system/scripts/validate_protocol_{name}.py`
2. **Follow Pattern**: Use `validator_utils.py` base
3. **Add Tests**: `validators-system/tests/test_*.sh`
4. **Update Master**: Register in `validate_all_protocols.py`

### Adding New Rules

1. **Create MDC File**: `.cursor/rules/{category}/{name}.mdc`
2. **Follow Format**: YAML frontmatter with TAGS, TRIGGERS, SCOPE
3. **Set Priority**: `alwaysApply: true/false`
4. **Test Discovery**: Verify Context Discovery Protocol loads it

---

## 📊 Metrics & Monitoring

### System Health Indicators

| Metric | Target | Location |
|--------|--------|----------|
| Protocol Validation Score | ≥0.95 | `.artifacts/validation/` |
| Coverage Percentage | ≥95% | `gap-analysis.json` |
| Classification Confidence | ≥85% | `project-classification.json` |
| Evidence Completeness | 100% | `evidence-manifest.json` |
| Gate Pass Rate | 7/7 | Protocol 05b gates |

### Audit Trail

All actions generate evidence in `.artifacts/` with:
- Timestamped JSON artifacts
- SHA-256 checksums
- Manifest tracking
- Retention policies (permanent for audit)

---

## 🔐 Security Considerations

### Access Control
- Rule system controls AI behavior
- Manual gates for sensitive decisions
- Approval records with timestamps

### Data Integrity
- SHA-256 checksums for all artifacts
- Evidence manifests track all files
- Read-only artifacts after handoff

### Compliance
- GDPR/HIPAA characteristic detection
- Compliance requirements in classification
- Audit trail for regulatory needs

---

## 📚 Related Documentation

- [README.md](./README.md) - Quick start and overview
- [validators-system/README.md](./validators-system/README.md) - Validator details
- [scripts/README.md](./scripts/README.md) - Script documentation
- [.cursor/rules/README.md](./.cursor/rules/README.md) - Rule system guide

---

**MASTER RAY™** - Where every line of code tells a story of validation, evidence, and continuous improvement.

