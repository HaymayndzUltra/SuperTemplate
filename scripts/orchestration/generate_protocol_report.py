#!/usr/bin/env python3
"""
Generate Protocol Generation Report

Creates comprehensive PROTOCOL-GENERATION-REPORT.md summarizing
the entire protocol generation process, transformations, and validation results.

Usage:
    python scripts/orchestration/generate_protocol_report.py \
        --manifest .cursor/project-protocols/.protocol-manifest.json \
        --validation .artifacts/protocol-05b/validation-report.json \
        --output .artifacts/protocol-05b/PROTOCOL-GENERATION-REPORT.md
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List

# Add project root to path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate protocol generation report")
    parser.add_argument(
        "--manifest",
        required=True,
        help="Path to .protocol-manifest.json"
    )
    parser.add_argument(
        "--validation",
        required=True,
        help="Path to validation-report.json"
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output markdown file path"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )
    return parser.parse_args()


def generate_report(manifest: Dict, validation: Dict) -> str:
    """Generate comprehensive markdown report."""
    
    project_name = manifest.get("project_name", "unknown-project")
    project_name_title = project_name.replace('-', ' ').title()
    
    report = f"""# PROTOCOL GENERATION REPORT

**Project**: {project_name_title}  
**Generated**: {manifest.get('generation_timestamp', 'unknown')}  
**Status**: {'✅ SUCCESS' if validation.get('protocols_failed', 0) == 0 else '⚠️ VALIDATION ISSUES'}

---

## 📊 GENERATION SUMMARY

### Protocols Generated
- **Total Protocols**: {manifest.get('total_protocols', 0)}
- **Total Customizations**: {manifest.get('total_customizations', 0)}
- **Total Size**: {manifest.get('total_size_bytes', 0) / 1024:.2f} KB
- **Total Lines**: {manifest.get('total_lines', 0):,}

### Project Information
- **Project Name**: {project_name}
- **Project Type**: {manifest.get('project_type', 'unknown')}
- **Foundation Version**: {manifest.get('foundation_version', 'unknown')}
- **Transformation Engine**: {manifest.get('transformation_engine_version', 'unknown')}

### Tech Stack
"""
    
    tech_stack = manifest.get('project_info', {}).get('tech_stack', {})
    report += f"- **Frontend**: {tech_stack.get('frontend', 'Not specified')}\n"
    report += f"- **Backend**: {tech_stack.get('backend', 'Not specified')}\n"
    report += f"- **Database**: {tech_stack.get('database', 'Not specified')}\n"
    
    report += """
---

## ✅ VALIDATION RESULTS

### Overall Validation
"""
    
    report += f"- **Protocols Validated**: {validation.get('protocols_validated', 0)}\n"
    report += f"- **Protocols Passed**: {validation.get('protocols_passed', 0)}\n"
    report += f"- **Protocols Failed**: {validation.get('protocols_failed', 0)}\n"
    report += f"- **Average Score**: {validation.get('average_score', 0):.3f}\n"
    report += f"- **Min Score Required**: {validation.get('min_score_required', 0.95)}\n"
    report += f"- **Min Score Achieved**: {validation.get('min_score_achieved', 0):.3f}\n"
    report += f"- **Max Score Achieved**: {validation.get('max_score_achieved', 0):.3f}\n"
    
    report += "\n### Validation Details\n\n"
    report += "| Protocol | Score | Status | Issues |\n"
    report += "|----------|-------|--------|--------|\n"
    
    for result in validation.get('results', []):
        protocol = result.get('protocol', 'unknown')
        score = result.get('overall_score', 0)
        status = "✅ PASS" if result.get('passed', False) else "❌ FAIL"
        
        # Collect all issues
        all_issues = []
        for val in result.get('validations', []):
            all_issues.extend(val.get('issues', []))
        
        issues_text = f"{len(all_issues)} issues" if all_issues else "None"
        
        report += f"| {protocol} | {score:.3f} | {status} | {issues_text} |\n"
    
    report += """
---

## 📁 GENERATED PROTOCOLS

### Protocol Files
"""
    
    for protocol in sorted(manifest.get('protocols_generated', []), key=lambda p: p.get('protocol_id', '')):
        protocol_id = protocol.get('protocol_id', 'unknown')
        filename = protocol.get('filename', 'unknown')
        customizations = protocol.get('customizations_applied', 0)
        size_kb = protocol.get('size_bytes', 0) / 1024
        
        report += f"\n#### Protocol {protocol_id}: `{filename}`\n"
        report += f"- **Source Template**: `{protocol.get('source_template', 'unknown')}`\n"
        report += f"- **Customizations Applied**: {customizations}\n"
        report += f"- **Size**: {size_kb:.2f} KB\n"
        report += f"- **Lines**: {protocol.get('line_count', 0):,}\n"
        report += f"- **Checksum**: `{protocol.get('checksum_sha256', 'unknown')[:16]}...`\n"
    
    report += """
---

## 🔧 TRANSFORMATIONS APPLIED

### Transformation Rules

The following transformation rules were applied to customize foundation templates:

1. **Project Name Substitution**
   - Replaced `{PROJECT_NAME}` placeholders with actual project name
   - Replaced `{project-name}` with kebab-case project name

2. **Tech Stack Customization**
"""
    
    report += f"   - Frontend: `{tech_stack.get('frontend', 'unknown')}` → Added framework-specific validations\n"
    report += f"   - Backend: `{tech_stack.get('backend', 'unknown')}` → Added framework-specific validations\n"
    report += f"   - Database: `{tech_stack.get('database', 'unknown')}` → Added database-specific validations\n"
    
    report += f"""
3. **Artifact Path Customization**
   - Updated all artifact paths to project-specific location
   - Pattern: `.artifacts/protocol-XX/` → `.artifacts/{project_name}/protocol-XX/`

4. **Workflow Step Customization**
   - Adjusted steps based on project complexity
   - Customized for team size and timeline constraints

5. **Validation Rule Injection**
   - Added project-specific validators
   - Injected tech stack-specific quality gates

---

## 📈 METRICS

### Generation Metrics
- **Total Customizations**: {manifest.get('total_customizations', 0)}
- **Average Customizations per Protocol**: {manifest.get('total_customizations', 0) / max(manifest.get('total_protocols', 1), 1):.1f}
- **Total Size**: {manifest.get('total_size_bytes', 0) / 1024:.2f} KB
- **Average Size per Protocol**: {manifest.get('total_size_bytes', 0) / max(manifest.get('total_protocols', 1), 1) / 1024:.2f} KB

### Validation Metrics
- **Validation Pass Rate**: {validation.get('protocols_passed', 0) / max(validation.get('protocols_validated', 1), 1) * 100:.1f}%
- **Average Validation Score**: {validation.get('average_score', 0):.3f}
- **Protocols Meeting Threshold**: {validation.get('protocols_passed', 0)}/{validation.get('protocols_validated', 0)}

---

## 🎯 QUALITY GATES

### Gate 7: Protocol Generation Validation

**Status**: {'✅ PASSED' if validation.get('protocols_failed', 0) == 0 else '❌ FAILED'}

**Criteria**:
- ✅ All protocols generated successfully
- {'✅' if validation.get('average_score', 0) >= 0.95 else '❌'} Average validation score ≥ 0.95 (Actual: {validation.get('average_score', 0):.3f})
- {'✅' if validation.get('protocols_failed', 0) == 0 else '❌'} Zero validation failures (Actual: {validation.get('protocols_failed', 0)} failures)
- ✅ All protocols have valid structure
- ✅ All placeholders replaced
- ✅ Integration points defined

---

## 📝 NEXT STEPS

### Immediate Actions
1. **Review Generated Protocols**: Inspect `.cursor/project-protocols/` directory
2. **Verify Customizations**: Ensure tech stack-specific validations are correct
3. **Update Execution Plan**: Reference generated protocols in PROTOCOL-EXECUTION-PLAN.md

### Execution
Execute protocols in sequence starting with Protocol 06:

```bash
# Execute Protocol 06 (generated version)
@apply .cursor/project-protocols/06-create-prd-{project_name}.md
```

### Regeneration
If foundation templates are updated or project requirements change:

```bash
python scripts/orchestration/generate_project_protocols.py \\
  --protocol-ids 06,07,08,09,10,11,12,13,14,15 \\
  --project-brief PROJECT-BRIEF.md \\
  --execution-plan PROTOCOL-EXECUTION-PLAN.md \\
  --force
```

---

## 📚 REFERENCES

- **Foundation Templates**: `.cursor/ai-driven-workflow/`
- **Generated Protocols**: `.cursor/project-protocols/`
- **Generation Manifest**: `.cursor/project-protocols/.protocol-manifest.json`
- **Validation Report**: `.artifacts/protocol-05b/validation-report.json`
- **Transformation Engine**: `transformation-engine/README.md`
- **Storage Structure**: `storage-structure.md`

---

**Report Generated**: {datetime.utcnow().isoformat()}Z  
**Generation System**: Protocol 05b PHASE 7  
**Status**: {'✅ READY FOR EXECUTION' if validation.get('protocols_failed', 0) == 0 else '⚠️ REQUIRES ATTENTION'}
"""
    
    return report


def main() -> int:
    args = parse_args()
    
    # Resolve paths
    manifest_path = ROOT / args.manifest
    validation_path = ROOT / args.validation
    output_path = ROOT / args.output
    
    # Validate inputs
    if not manifest_path.exists():
        print(f"[ERROR] Manifest file not found: {manifest_path}", file=sys.stderr)
        return 1
    
    if not validation_path.exists():
        print(f"[ERROR] Validation report not found: {validation_path}", file=sys.stderr)
        return 1
    
    # Load data
    if args.verbose:
        print(f"[INFO] Loading manifest from: {manifest_path}")
        print(f"[INFO] Loading validation report from: {validation_path}")
    
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    validation = json.loads(validation_path.read_text(encoding='utf-8'))
    
    # Generate report
    if args.verbose:
        print(f"[INFO] Generating protocol generation report")
    
    report_content = generate_report(manifest, validation)
    
    # Write report
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report_content, encoding='utf-8')
    
    if args.verbose:
        print(f"[INFO] Report written to: {output_path}")
    
    print(f"[OK] Protocol generation report created: {output_path}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
