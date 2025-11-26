# MASTER RAY™ Scripts

**Automation Layer - Python Scripts Powering Protocol Execution**

---

## 🎯 Overview

This directory contains all automation scripts that power the MASTER RAY™ workflow system. Scripts are organized by function and integrate with protocols through defined automation hooks.

### Key Features

- **Orchestration Scripts**: Power Protocol 05b's routing logic
- **Validator Scripts**: Execute protocol validation
- **Utility Scripts**: Support functions for evidence and packaging
- **Script Registry**: Centralized metadata in `script-registry.json`

---

## 📂 Directory Structure

```
scripts/
├── README.md                    # This file
├── script-registry.json         # Central script metadata registry
│
├── orchestration/               # Protocol 05b automation
│   ├── README.md               # Orchestration scripts guide
│   ├── classify_project_type.py
│   ├── detect_characteristics.py
│   ├── validate_project_inputs.py
│   ├── select_protocols.py
│   ├── sequence_protocols.py
│   ├── customize_parameters.py
│   ├── generate_execution_plan.py
│   ├── run_pre_flight_checks.py
│   ├── validate_generated_protocols.py
│   ├── package_evidence.py
│   └── create_dependency_graph.py
│
├── ai/                          # AI/ML specific automation
│   ├── README.md               # AI scripts guide
│   └── ...
│
└── [other-categories]/          # Additional script categories
```

---

## 📝 Script Registry

The `script-registry.json` file is the **single source of truth** for all scripts.

### Registry Structure

```json
{
  "version": "1.0.0",
  "last_updated": "2025-01-15",
  "scripts": [
    {
      "id": "orch-001",
      "name": "classify_project_type.py",
      "path": "scripts/orchestration/classify_project_type.py",
      "protocol": "05b",
      "phase": "3-classification",
      "purpose": "Classify project type using 27+ dimensions",
      "owner": "orchestration-team",
      "dependencies": ["pyyaml", "jsonschema"],
      "version": "1.0.0",
      "status": "active"
    }
  ]
}
```

### Registry Fields

| Field | Description |
|-------|-------------|
| `id` | Unique script identifier |
| `name` | Script filename |
| `path` | Relative path from repo root |
| `protocol` | Associated protocol ID |
| `phase` | Workflow phase |
| `purpose` | One-line description |
| `owner` | Responsible team/person |
| `dependencies` | Python package requirements |
| `version` | Script version |
| `status` | `active`, `stub`, `deprecated` |

---

## 🔧 Script Categories

### Orchestration Scripts (`scripts/orchestration/`)

Power Protocol 05b's intelligent routing:

| Script | Purpose | Protocol Phase |
|--------|---------|----------------|
| `run_pre_flight_checks.py` | Verify prerequisites | Pre-flight |
| `validate_project_inputs.py` | Validate input artifacts | Input Validation |
| `classify_project_type.py` | Classify using 27+ dimensions | Classification |
| `detect_characteristics.py` | Detect project characteristics | Classification |
| `select_protocols.py` | Select applicable protocols | Selection |
| `sequence_protocols.py` | Order by dependencies | Sequencing |
| `customize_parameters.py` | Adjust protocol parameters | Customization |
| `generate_execution_plan.py` | Create final plan | Plan Generation |
| `validate_generated_protocols.py` | Validate new protocols | Validation |
| `package_evidence.py` | Package artifacts | Evidence |
| `create_dependency_graph.py` | Build protocol graph | Visualization |

### Validator Scripts (`validators-system/scripts/`)

Execute protocol validation:

| Script | Purpose |
|--------|---------|
| `validate_protocol_identity.py` | Check identity fields |
| `validate_protocol_role.py` | Check AI role definition |
| `validate_protocol_workflow.py` | Check workflow phases |
| `validate_all_protocols.py` | Run all validators |

See [validators-system/README.md](../validators-system/README.md) for details.

---

## 🚀 Usage

### Running a Script

```bash
# From repository root
python scripts/orchestration/classify_project_type.py \
  --project-brief ./project-brief.md \
  --config ./config/classification-dimensions.yaml \
  --output ./output/classification.json
```

### Common Arguments

| Argument | Description |
|----------|-------------|
| `--project-brief` | Path to project brief |
| `--config` | Configuration file path |
| `--output` | Output file path |
| `--verbose` | Enable detailed logging |
| `--dry-run` | Simulate without changes |

### Environment Variables

```bash
MASTER_RAY_ROOT=/path/to/SuperTemplate-1
MASTER_RAY_CONFIG=$MASTER_RAY_ROOT/config
MASTER_RAY_OUTPUT=$MASTER_RAY_ROOT/.artifacts
```

---

## 🔌 Protocol Integration

### Automation Hooks

Each protocol defines automation hooks in its `## 7. Automation Hooks` section:

```markdown
## 7. Automation Hooks

| Script | Trigger | Parameters |
|--------|---------|------------|
| `classify_project_type.py` | Phase 3 start | `--brief {brief_path}` |
| `detect_characteristics.py` | After classification | `--type {project_type}` |
```

### Execution Flow

```
Protocol Execution
       │
       ▼
┌─────────────────┐
│ Automation Hook │  ← Protocol defines hook
└─────────────────┘
       │
       ▼
┌─────────────────┐
│ Script Registry │  ← Look up script details
└─────────────────┘
       │
       ▼
┌─────────────────┐
│ Execute Script  │  ← Run with parameters
└─────────────────┘
       │
       ▼
┌─────────────────┐
│ Capture Output  │  ← Store as evidence
└─────────────────┘
```

---

## 📋 Creating New Scripts

### 1. Choose Location

| Category | Location | When |
|----------|----------|------|
| Orchestration | `scripts/orchestration/` | Protocol 05b automation |
| Validators | `validators-system/scripts/` | Protocol validation |
| AI/ML | `scripts/ai/` | ML-specific automation |
| Utilities | `scripts/utils/` | General utilities |

### 2. Script Template

```python
#!/usr/bin/env python3
"""
Script: {script_name}.py
Protocol: {protocol_id}
Phase: {phase_name}
Purpose: {one_line_description}

Usage:
    python {script_name}.py --input <path> --output <path>

Dependencies:
    - {dependency_1}
    - {dependency_2}
"""

import argparse
import json
import sys
from pathlib import Path

def main(input_path: Path, output_path: Path, verbose: bool = False) -> int:
    """Main execution function.
    
    Args:
        input_path: Path to input file
        output_path: Path to output file
        verbose: Enable verbose logging
        
    Returns:
        0 on success, non-zero on failure
    """
    try:
        # 1. Load input
        with open(input_path) as f:
            data = json.load(f)
        
        # 2. Process
        result = process(data)
        
        # 3. Write output
        with open(output_path, 'w') as f:
            json.dump(result, f, indent=2)
        
        return 0
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

def process(data: dict) -> dict:
    """Core processing logic."""
    # Implementation here
    return {}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--verbose", action="store_true")
    
    args = parser.parse_args()
    sys.exit(main(args.input, args.output, args.verbose))
```

### 3. Register in Registry

Add entry to `script-registry.json`:

```json
{
  "id": "category-###",
  "name": "{script_name}.py",
  "path": "scripts/{category}/{script_name}.py",
  "protocol": "{protocol_id}",
  "phase": "{phase_name}",
  "purpose": "{one_line_description}",
  "owner": "{team}",
  "dependencies": [],
  "version": "1.0.0",
  "status": "active"
}
```

---

## ✅ Script Quality Standards

### Requirements

- [ ] Docstring with purpose, usage, dependencies
- [ ] Type hints for all functions
- [ ] Error handling with meaningful messages
- [ ] Return codes (0 = success, non-zero = failure)
- [ ] CLI argument parsing
- [ ] Registered in `script-registry.json`

### Testing

```bash
# Run script tests
python -m pytest scripts/tests/

# Test specific script
python -m pytest scripts/tests/test_classify_project_type.py
```

---

## 📚 Related Documentation

- [Orchestration Scripts](./orchestration/README.md) - Detailed orchestration guide
- [Validator Scripts](../validators-system/README.md) - Validation system
- [Protocol 05b](../.cursor/ai-driven-workflow/05b-project-protocol-orchestration-v2.md) - Orchestration protocol
- [Script Registry](./script-registry.json) - Central metadata

---

**MASTER RAY™ Scripts** - Automation that enables validated, reproducible workflows.
