#!/usr/bin/env python3
"""
Script: prioritize_improvements.py
Protocol: 05 (Protocol Retrospective)
Purpose: Prioritize improvements using impact/effort matrix
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Any, Tuple


def calculate_priority(impact: str, effort: str) -> Tuple[float, str]:
    """
    Calculate priority score (0-1)
    
    Impact: High=3, Medium=2, Low=1
    Effort: High=3, Medium=2, Low=1
    
    Formula: (Impact×3 + (4-Effort)) / 7
    """
    impact_value = {'High': 3, 'Medium': 2, 'Low': 1}.get(impact, 1)
    effort_value = {'High': 3, 'Medium': 2, 'Low': 1}.get(effort, 1)
    
    score = (impact_value * 3 + (4 - effort_value)) / 7
    
    if score > 0.7:
        return score, "Do Now"
    elif score > 0.4:
        return score, "Next Sprint"
    else:
        return score, "Backlog"


def prioritize_improvements(improvements: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Prioritize list of improvements"""
    
    prioritized = []
    
    for imp in improvements:
        # Validate required fields
        if 'item' not in imp or 'impact' not in imp or 'effort' not in imp:
            print(f"Warning: Skipping invalid improvement: {imp}")
            continue
        
        # Calculate priority
        score, action = calculate_priority(imp['impact'], imp['effort'])
        
        # Add calculated fields
        imp['priority_score'] = round(score, 2)
        imp['action'] = action
        
        # Add optional fields if not present
        if 'estimated_time' not in imp:
            imp['estimated_time'] = estimate_time(imp['effort'])
        if 'expected_impact' not in imp:
            imp['expected_impact'] = describe_impact(imp['impact'])
        
        prioritized.append(imp)
    
    # Sort by priority score (descending)
    prioritized.sort(key=lambda x: x['priority_score'], reverse=True)
    
    # Group by action
    grouped = {
        'Do Now': [i for i in prioritized if i['action'] == 'Do Now'],
        'Next Sprint': [i for i in prioritized if i['action'] == 'Next Sprint'],
        'Backlog': [i for i in prioritized if i['action'] == 'Backlog']
    }
    
    return {
        'total_improvements': len(prioritized),
        'prioritized_list': prioritized,
        'grouped': grouped,
        'summary': {
            'do_now': len(grouped['Do Now']),
            'next_sprint': len(grouped['Next Sprint']),
            'backlog': len(grouped['Backlog'])
        }
    }


def estimate_time(effort: str) -> str:
    """Estimate time based on effort level"""
    time_map = {
        'High': '6-8 hours',
        'Medium': '2-4 hours',
        'Low': '15-60 minutes'
    }
    return time_map.get(effort, 'Unknown')


def describe_impact(impact: str) -> str:
    """Describe expected impact"""
    impact_map = {
        'High': 'Significant improvement in protocol quality/efficiency',
        'Medium': 'Moderate improvement in specific areas',
        'Low': 'Minor enhancement or fix'
    }
    return impact_map.get(impact, 'Unknown impact')


def generate_markdown_report(results: Dict[str, Any]) -> str:
    """Generate markdown report of prioritized improvements"""
    
    report = []
    report.append("# IMPROVEMENT PLAN\n")
    report.append(f"**Total Improvements**: {results['total_improvements']}\n")
    report.append(f"**Summary**: {results['summary']['do_now']} Do Now, "
                  f"{results['summary']['next_sprint']} Next Sprint, "
                  f"{results['summary']['backlog']} Backlog\n")
    report.append("\n---\n")
    
    # Do Now section
    if results['grouped']['Do Now']:
        report.append("\n## Do Now (Priority >0.7)\n")
        for idx, imp in enumerate(results['grouped']['Do Now'], 1):
            report.append(f"\n### {idx}. **{imp['item']}**\n")
            report.append(f"- **Impact**: {imp['impact']}\n")
            report.append(f"- **Effort**: {imp['effort']}\n")
            report.append(f"- **Priority Score**: {imp['priority_score']}\n")
            report.append(f"- **Estimated Time**: {imp['estimated_time']}\n")
            report.append(f"- **Expected Impact**: {imp['expected_impact']}\n")
            if 'owner' in imp:
                report.append(f"- **Owner**: {imp['owner']}\n")
            if 'description' in imp:
                report.append(f"- **Description**: {imp['description']}\n")
    
    # Next Sprint section
    if results['grouped']['Next Sprint']:
        report.append("\n## Next Sprint (Priority 0.4-0.7)\n")
        for idx, imp in enumerate(results['grouped']['Next Sprint'], 1):
            report.append(f"\n### {idx}. **{imp['item']}**\n")
            report.append(f"- **Impact**: {imp['impact']}\n")
            report.append(f"- **Effort**: {imp['effort']}\n")
            report.append(f"- **Priority Score**: {imp['priority_score']}\n")
            report.append(f"- **Estimated Time**: {imp['estimated_time']}\n")
            report.append(f"- **Expected Impact**: {imp['expected_impact']}\n")
            if 'owner' in imp:
                report.append(f"- **Owner**: {imp['owner']}\n")
    
    # Backlog section
    if results['grouped']['Backlog']:
        report.append("\n## Backlog (Priority <0.4)\n")
        for idx, imp in enumerate(results['grouped']['Backlog'], 1):
            report.append(f"\n### {idx}. **{imp['item']}**\n")
            report.append(f"- **Impact**: {imp['impact']}\n")
            report.append(f"- **Effort**: {imp['effort']}\n")
            report.append(f"- **Priority Score**: {imp['priority_score']}\n")
            report.append(f"- **Estimated Time**: {imp['estimated_time']}\n")
    
    report.append("\n---\n")
    report.append("\n## Prioritization Matrix\n")
    report.append("\n| Improvement | Impact | Effort | Priority Score | Action |\n")
    report.append("|-------------|--------|--------|----------------|--------|\n")
    
    for imp in results['prioritized_list']:
        report.append(f"| {imp['item']} | {imp['impact']} | {imp['effort']} | "
                      f"{imp['priority_score']} | {imp['action']} |\n")
    
    return ''.join(report)


def main():
    parser = argparse.ArgumentParser(description='Prioritize improvements using impact/effort matrix')
    parser.add_argument('--improvements', required=True, help='Path to improvements JSON file')
    parser.add_argument('--output', help='Output JSON file (optional)')
    parser.add_argument('--markdown', help='Output markdown report (optional)')
    parser.add_argument('--verbose', action='store_true', help='Show detailed output')
    
    args = parser.parse_args()
    
    # Load improvements
    improvements_path = Path(args.improvements)
    if not improvements_path.exists():
        print(f"Error: Improvements file not found: {improvements_path}")
        sys.exit(1)
    
    try:
        improvements_data = json.loads(improvements_path.read_text())
        
        # Handle both list and dict formats
        if isinstance(improvements_data, dict) and 'improvements' in improvements_data:
            improvements = improvements_data['improvements']
        elif isinstance(improvements_data, list):
            improvements = improvements_data
        else:
            print("Error: Invalid improvements format. Expected list or dict with 'improvements' key")
            sys.exit(1)
            
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in improvements file: {e}")
        sys.exit(1)
    
    # Prioritize improvements
    results = prioritize_improvements(improvements)
    
    # Display results
    print(f"\n{'='*60}")
    print(f"IMPROVEMENT PRIORITIZATION REPORT")
    print(f"{'='*60}")
    print(f"\nTotal Improvements: {results['total_improvements']}")
    print(f"\nSummary:")
    print(f"  - Do Now (>0.7): {results['summary']['do_now']}")
    print(f"  - Next Sprint (0.4-0.7): {results['summary']['next_sprint']}")
    print(f"  - Backlog (<0.4): {results['summary']['backlog']}")
    print(f"\n{'='*60}")
    print(f"PRIORITIZED LIST:")
    print(f"{'='*60}\n")
    
    for imp in results['prioritized_list']:
        print(f"{imp['priority_score']:.2f} | {imp['action']:12} | {imp['item']}")
        if args.verbose:
            print(f"       Impact: {imp['impact']}, Effort: {imp['effort']}")
            print(f"       Time: {imp['estimated_time']}")
            print()
    
    # Save JSON if requested
    if args.output:
        output_path = Path(args.output)
        output_path.write_text(json.dumps(results, indent=2))
        print(f"\nJSON results saved to: {output_path}")
    
    # Save markdown if requested
    if args.markdown:
        markdown_path = Path(args.markdown)
        markdown_content = generate_markdown_report(results)
        markdown_path.write_text(markdown_content)
        print(f"Markdown report saved to: {markdown_path}")
    
    print(f"\n{'='*60}\n")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
