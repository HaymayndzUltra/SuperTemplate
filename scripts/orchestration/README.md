# MASTER RAY™ Orchestration Scripts

**Protocol 05b Automation - Intelligent Project Routing & Execution Planning**

---

## 🎯 Overview

This directory contains the Python scripts that power **Protocol 05b (Project Protocol Orchestration)**. These scripts implement the 8-phase workflow that classifies projects, selects protocols, and generates execution plans.

### Key Features

- **27+ Classification Dimensions**: Intelligent project type detection
- **Dependency Graph**: Protocol sequencing based on dependencies
- **Customization Engine**: Adjust parameters per project
- **Evidence Packaging**: Audit-ready artifact collection
- **Validation Integration**: Verify generated protocols

---

## 📂 Script Inventory

| Script | Protocol Phase | Purpose |
|--------|----------------|---------|
| `run_pre_flight_checks.py` | Phase 1: Pre-flight | Verify prerequisites before orchestration |
| `validate_project_inputs.py` | Phase 2: Input Validation | Validate required artifacts exist |
| `classify_project_type.py` | Phase 3: Classification | Detect project type using 27+ dimensions |
| `detect_characteristics.py` | Phase 3: Classification | Extract project characteristics |
| `select_protocols.py` | Phase 4: Selection | Select applicable protocols |
| `sequence_protocols.py` | Phase 6: Sequencing | Order protocols by dependencies |
| `customize_parameters.py` | Phase 6: Customization | Adjust protocol parameters |
| `generate_execution_plan.py` | Phase 7: Plan Generation | Create final execution plan |
| `validate_generated_protocols.py` | Phase 5: Validation | Validate new protocols from Protocol 0 |
| `package_evidence.py` | Phase 8: Handoff | Package artifacts for handoff |
| `create_dependency_graph.py` | Utility | Visualize protocol dependencies |

---

## 🔄 Execution Flow

```
                    Protocol 05b Workflow
                          │
          ┌───────────────┼───────────────┐
          │               │               │
          ▼               ▼               ▼
   ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
   │ Pre-flight  │ │ Input       │ │ Classify    │
   │ Checks      │ │ Validation  │ │ Project     │
   └─────────────┘ └─────────────┘ └─────────────┘
          │               │               │
          │     Phase 1-2 │    Phase 3    │
          └───────────────┴───────┬───────┘
                                  │
                                  ▼
                    ┌─────────────────────────┐
                    │   Protocol Selection    │
                    │   (Phase 4)             │
                    └─────────────────────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
                    ▼                           ▼
          ┌─────────────────┐         ┌─────────────────┐
          │ Protocol 0      │         │ Skip if no      │
          │ Generation      │         │ new protocols   │
          │ (Phase 5)       │         │ needed          │
          └─────────────────┘         └─────────────────┘
                    │                           │
                    └─────────────┬─────────────┘
                                  │
                                  ▼
                    ┌─────────────────────────┐
                    │   Sequence & Customize  │
                    │   (Phase 6)             │
                    └─────────────────────────┘
                                  │
                                  ▼
                    ┌─────────────────────────┐
                    │   Generate Plan         │
                    │   (Phase 7)             │
                    └─────────────────────────┘
                                  │
                                  ▼
                    ┌─────────────────────────┐
                    │   Package Evidence      │
                    │   (Phase 8)             │
                    └─────────────────────────┘
```

---

## 📜 Script Details

### 1. `run_pre_flight_checks.py`

**Phase**: 1 - Pre-flight  
**Purpose**: Verify all prerequisites are met before orchestration begins.

```bash
python run_pre_flight_checks.py \
  --config ../config/orchestration-config.yaml \
  --output ./output/pre-flight-report.json
```

**Checks Performed**:
- [ ] Configuration files exist
- [ ] Required directories present
- [ ] Dependencies installed
- [ ] Environment variables set
- [ ] Previous protocol outputs available

**Output**:
```json
{
  "status": "pass|fail",
  "checks": [
    {"name": "config_exists", "passed": true},
    {"name": "deps_installed", "passed": true}
  ],
  "blockers": []
}
```

---

### 2. `validate_project_inputs.py`

**Phase**: 2 - Input Validation  
**Purpose**: Validate that all required input artifacts exist and are valid.

```bash
python validate_project_inputs.py \
  --project-brief ./project-brief.md \
  --context-file ./context.json \
  --output ./output/input-validation.json
```

**Validated Inputs**:
- Project brief (required)
- Context file (optional)
- Constraints (optional)
- Existing protocols (optional)

**Output**:
```json
{
  "valid": true,
  "inputs": {
    "project_brief": {"exists": true, "valid": true},
    "context_file": {"exists": true, "valid": true}
  },
  "warnings": []
}
```

---

### 3. `classify_project_type.py`

**Phase**: 3 - Classification  
**Purpose**: Classify project type using 27+ dimensions from configuration.

```bash
python classify_project_type.py \
  --project-brief ./project-brief.md \
  --config ../config/classification-dimensions.yaml \
  --output ./output/classification.json
```

**Classification Dimensions**:

| Category | Dimensions |
|----------|------------|
| **AI/ML** | ml_training, ml_inference, llm_integration, computer_vision, nlp |
| **Data** | data_pipeline, data_warehouse, real_time_streaming, batch_processing |
| **Application** | web_application, mobile_app, api_service, microservices |
| **Infrastructure** | cloud_native, containerization, ci_cd_automation, iac |
| **Compliance** | hipaa_compliance, gdpr_compliance, sox_compliance, pci_dss |
| **Team** | distributed_team, cross_functional, startup, enterprise |

**Output**:
```json
{
  "primary_type": "ai_ml_application",
  "secondary_types": ["web_application", "api_service"],
  "confidence": 0.87,
  "dimension_scores": {
    "ml_training": 0.92,
    "ml_inference": 0.85,
    "web_application": 0.78
  },
  "classification_rationale": "..."
}
```

---

### 4. `detect_characteristics.py`

**Phase**: 3 - Classification  
**Purpose**: Extract detailed project characteristics from brief and context.

```bash
python detect_characteristics.py \
  --project-brief ./project-brief.md \
  --classification ./output/classification.json \
  --output ./output/characteristics.json
```

**Detected Characteristics**:
- Technology stack (languages, frameworks)
- Team composition
- Compliance requirements
- Performance constraints
- Timeline expectations
- Risk factors

**Output**:
```json
{
  "tech_stack": {
    "languages": ["python", "typescript"],
    "frameworks": ["fastapi", "react"],
    "databases": ["postgresql", "redis"]
  },
  "compliance": ["gdpr"],
  "team_size": "small",
  "timeline": "standard",
  "risk_level": "medium"
}
```

---

### 5. `select_protocols.py`

**Phase**: 4 - Selection  
**Purpose**: Select applicable protocols based on classification and characteristics.

```bash
python select_protocols.py \
  --classification ./output/classification.json \
  --characteristics ./output/characteristics.json \
  --protocol-registry ../config/protocol-registry.json \
  --output ./output/selected-protocols.json
```

**Selection Logic**:
1. Match project type to protocol tracks (Generic, AI/ML)
2. Filter by characteristics (compliance, team size)
3. Include mandatory protocols
4. Include optional protocols based on scoring
5. Exclude inapplicable protocols

**Output**:
```json
{
  "selected_protocols": [
    {"id": "01", "track": "generic", "reason": "mandatory"},
    {"id": "06", "track": "ai_ml", "reason": "ml_training > 0.8"},
    {"id": "12", "track": "generic", "reason": "quality_audit required"}
  ],
  "excluded_protocols": [
    {"id": "24", "reason": "alternate track not selected"}
  ]
}
```

---

### 6. `sequence_protocols.py`

**Phase**: 6 - Sequencing  
**Purpose**: Order protocols based on dependency graph and critical path.

```bash
python sequence_protocols.py \
  --selected-protocols ./output/selected-protocols.json \
  --dependency-graph ../config/protocol-dependencies.json \
  --output ./output/sequenced-protocols.json
```

**Sequencing Logic**:
1. Build dependency graph
2. Topological sort for ordering
3. Identify critical path
4. Find parallelization opportunities
5. Assign phase groupings

**Output**:
```json
{
  "sequence": [
    {"phase": 1, "protocols": ["01", "02"], "parallel": true},
    {"phase": 2, "protocols": ["03"], "parallel": false},
    {"phase": 3, "protocols": ["04", "05b"], "parallel": false}
  ],
  "critical_path": ["01", "03", "05b", "06", "10", "15"],
  "estimated_duration": "12 weeks"
}
```

---

### 7. `customize_parameters.py`

**Phase**: 6 - Customization  
**Purpose**: Adjust protocol parameters based on project characteristics.

```bash
python customize_parameters.py \
  --sequenced-protocols ./output/sequenced-protocols.json \
  --characteristics ./output/characteristics.json \
  --output ./output/customized-protocols.json
```

**Customization Areas**:
- Quality gate thresholds
- Documentation depth
- Testing coverage requirements
- Communication frequency
- Evidence granularity

**Output**:
```json
{
  "customizations": {
    "12": {
      "coverage_threshold": 0.90,
      "reason": "high_compliance requirements"
    },
    "15": {
      "deployment_strategy": "blue_green",
      "reason": "enterprise classification"
    }
  }
}
```

---

### 8. `generate_execution_plan.py`

**Phase**: 7 - Plan Generation  
**Purpose**: Generate the final execution plan with all details.

```bash
python generate_execution_plan.py \
  --customized-protocols ./output/customized-protocols.json \
  --project-context ./context.json \
  --output ./output/execution-plan.md
```

**Plan Contents**:
- Executive summary
- Phase breakdown
- Protocol sequence with customizations
- Timeline and milestones
- Resource allocation
- Risk mitigation
- Communication plan

---

### 9. `validate_generated_protocols.py`

**Phase**: 5 - Validation  
**Purpose**: Validate protocols generated by Protocol 0 (Meta-Generator).

```bash
python validate_generated_protocols.py \
  --protocol-file ./generated/new-protocol.md \
  --validators-config ../validators-system/config.json \
  --output ./output/validation-report.json
```

**Validation Checks**:
- All 11 validator dimensions
- Score ≥0.95 required
- Integration compatibility

---

### 10. `package_evidence.py`

**Phase**: 8 - Handoff  
**Purpose**: Package all artifacts for handoff to next protocol or archive.

```bash
python package_evidence.py \
  --artifacts-dir ./output/ \
  --manifest ./evidence-manifest.json \
  --output ./handoff/evidence-package.zip
```

**Package Contents**:
- All generated artifacts
- Evidence manifest
- Checksums (SHA-256)
- Timestamps (ISO 8601)

---

### 11. `create_dependency_graph.py`

**Phase**: Utility  
**Purpose**: Visualize protocol dependencies as a graph.

```bash
python create_dependency_graph.py \
  --protocols ./output/selected-protocols.json \
  --output ./output/dependency-graph.svg
```

---

## ⚙️ Configuration

### Classification Dimensions

Located at: `config/classification-dimensions.yaml`

```yaml
dimensions:
  - id: ml_training
    name: "Machine Learning Training"
    category: ai_ml
    keywords: ["train", "model", "neural", "deep learning"]
    tech_indicators: ["tensorflow", "pytorch", "sklearn"]
    confidence_weight: 1.2

classification_rules:
  - type: ai_ml_application
    required_dimensions: [ml_training, ml_inference]
    min_confidence: 0.7
```

### Protocol Dependencies

Located at: `config/protocol-dependencies.json`

```json
{
  "01": {"depends_on": []},
  "02": {"depends_on": ["01"]},
  "03": {"depends_on": ["02"]},
  "05b": {"depends_on": ["04"]}
}
```

---

## 🛠️ Development

### Running Tests

```bash
cd scripts/orchestration
python -m pytest tests/ -v
```

### Adding a New Script

1. Create script following template in `../README.md`
2. Register in `../script-registry.json`
3. Add tests in `tests/`
4. Update this README
5. Update Protocol 05b automation hooks

---

## 📚 Related Documentation

- [Protocol 05b](../../.cursor/ai-driven-workflow/05b-project-protocol-orchestration-v2.md) - Full protocol specification
- [Classification Config](../../config/classification-dimensions.yaml) - Dimension definitions
- [Script Registry](../script-registry.json) - All scripts metadata
- [Validator System](../../validators-system/README.md) - Protocol validation

---

**MASTER RAY™ Orchestration** - Intelligent routing for validated workflows.

