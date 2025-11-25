#!/usr/bin/env python3
"""
Link Outcomes to Plan
Maps protocol execution plan sections to outcome metrics.
"""
import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

def link_outcomes(plan_path: Path, outcomes_dir: Path) -> dict:
    """Link outcomes to execution plan."""
    
    # Load all outcome files
    outcomes = []
    if outcomes_dir.exists():
        for outcome_file in outcomes_dir.glob('*-outcome.json'):
            with open(outcome_file, 'r', encoding='utf-8') as f:
                outcomes.append(json.load(f))
    
    # Create linkage report
    linkage = {
        "timestamp": datetime.now().isoformat(),
        "plan_path": str(plan_path),
        "outcomes_count": len(outcomes),
        "outcomes": outcomes,
        "summary": {
            "total_executions": len(outcomes),
            "successful": 0,
            "failed": 0,
            "pending": 0
        },
        "metrics_summary": {}
    }
    
    # Aggregate metrics
    for outcome in outcomes:
        metrics = outcome.get('metrics', {})
        
        # Deployment success
        if metrics.get('deployment_success') is True:
            linkage['summary']['successful'] += 1
        elif metrics.get('deployment_success') is False:
            linkage['summary']['failed'] += 1
        else:
            linkage['summary']['pending'] += 1
        
        # Aggregate other metrics
        for key, value in metrics.items():
            if key not in linkage['metrics_summary']:
                linkage['metrics_summary'][key] = []
            if value is not None:
                linkage['metrics_summary'][key].append(value)
    
    # Calculate averages for numeric metrics
    for key, values in linkage['metrics_summary'].items():
        if values and all(isinstance(v, (int, float)) for v in values):
            linkage['metrics_summary'][key] = {
                "values": values,
                "average": sum(values) / len(values),
                "min": min(values),
                "max": max(values)
            }
    
    return linkage

def generate_linkage_markdown(linkage: dict) -> str:
    """Generate markdown report for outcome linkage."""
    
    md = f"""# Outcome Linkage Report

**Generated:** {linkage['timestamp']}
**Plan:** {linkage['plan_path']}

---

## Summary

| Metric | Value |
|--------|-------|
| Total Executions | {linkage['summary']['total_executions']} |
| Successful | {linkage['summary']['successful']} |
| Failed | {linkage['summary']['failed']} |
| Pending | {linkage['summary']['pending']} |

---

## Metrics Summary

"""
    
    for key, data in linkage.get('metrics_summary', {}).items():
        if isinstance(data, dict) and 'average' in data:
            md += f"### {key.replace('_', ' ').title()}\n"
            md += f"- Average: {data['average']:.2f}\n"
            md += f"- Min: {data['min']}\n"
            md += f"- Max: {data['max']}\n\n"
    
    md += """---

## Outcome Details

"""
    
    for outcome in linkage.get('outcomes', []):
        md += f"### Execution: {outcome.get('execution_id', 'Unknown')}\n"
        md += f"- Protocol: {outcome.get('protocol_id', 'Unknown')}\n"
        md += f"- Recorded: {outcome.get('recorded_at', 'Unknown')}\n"
        md += f"- Status: {outcome.get('status', 'Unknown')}\n\n"
    
    return md

def main():
    parser = argparse.ArgumentParser(description='Link outcomes to execution plan')
    parser.add_argument('--plan', required=True, help='Path to PROTOCOL-EXECUTION-PLAN.md')
    parser.add_argument('--outcomes-dir', help='Directory containing outcome files')
    parser.add_argument('--output', help='Output report path')
    parser.add_argument('--workspace', default='.', help='Workspace root path')
    args = parser.parse_args()
    
    workspace = Path(args.workspace).resolve()
    
    print(f"[OUTCOMES] Linking outcomes to execution plan...")
    
    plan_path = Path(args.plan)
    if not plan_path.is_absolute():
        plan_path = workspace / plan_path
    
    if args.outcomes_dir:
        outcomes_dir = Path(args.outcomes_dir)
        if not outcomes_dir.is_absolute():
            outcomes_dir = workspace / outcomes_dir
    else:
        outcomes_dir = workspace / '.artifacts' / 'outcomes'
    
    # Link outcomes
    linkage = link_outcomes(plan_path, outcomes_dir)
    
    # Generate markdown report
    report_md = generate_linkage_markdown(linkage)
    
    # Determine output paths
    if args.output:
        json_output = Path(args.output)
        md_output = json_output.with_suffix('.md')
    else:
        json_output = workspace / '.artifacts' / 'outcomes' / 'outcome-linkage.json'
        md_output = workspace / 'outcome-linkage-report.md'
    
    json_output.parent.mkdir(parents=True, exist_ok=True)
    
    with open(json_output, 'w', encoding='utf-8') as f:
        json.dump(linkage, f, indent=2)
    
    with open(md_output, 'w', encoding='utf-8') as f:
        f.write(report_md)
    
    print(f"[OUTCOMES] Linkage complete")
    print(f"  - Outcomes linked: {linkage['outcomes_count']}")
    print(f"  - JSON output: {json_output}")
    print(f"  - Report: {md_output}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

