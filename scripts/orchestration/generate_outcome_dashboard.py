#!/usr/bin/env python3
"""
Generate Outcome Dashboard
Creates a dashboard report aggregating validator scores and outcome metrics.
"""
import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

def load_validator_scores(workspace: Path) -> list:
    """Load validator scores from validation artifacts."""
    scores = []
    validation_dir = workspace / '.artifacts' / 'validation'
    
    if validation_dir.exists():
        for score_file in validation_dir.glob('*.json'):
            with open(score_file, 'r', encoding='utf-8') as f:
                scores.append(json.load(f))
    
    return scores

def load_outcomes(workspace: Path) -> list:
    """Load outcome records."""
    outcomes = []
    outcomes_dir = workspace / '.artifacts' / 'outcomes'
    
    if outcomes_dir.exists():
        for outcome_file in outcomes_dir.glob('*-outcome.json'):
            with open(outcome_file, 'r', encoding='utf-8') as f:
                outcomes.append(json.load(f))
    
    return outcomes

def identify_discrepancies(validator_scores: list, outcomes: list) -> list:
    """Identify discrepancies between high scores and poor outcomes."""
    discrepancies = []
    
    # This is a simplified check - in production would match by execution ID
    for outcome in outcomes:
        metrics = outcome.get('metrics', {})
        
        # Check for high validator score but poor outcome
        if metrics.get('deployment_success') is False:
            discrepancies.append({
                "execution_id": outcome.get('execution_id'),
                "protocol_id": outcome.get('protocol_id'),
                "issue": "Deployment failed despite passing validation",
                "severity": "high"
            })
        
        if metrics.get('test_pass_rate') is not None and metrics.get('test_pass_rate') < 0.8:
            discrepancies.append({
                "execution_id": outcome.get('execution_id'),
                "protocol_id": outcome.get('protocol_id'),
                "issue": f"Low test pass rate: {metrics.get('test_pass_rate')}",
                "severity": "medium"
            })
    
    return discrepancies

def generate_dashboard_html(validator_scores: list, outcomes: list, discrepancies: list) -> str:
    """Generate HTML dashboard."""
    
    html = """<!DOCTYPE html>
<html>
<head>
    <title>Protocol Outcome Dashboard</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 20px; background: #f5f5f5; }
        .container { max-width: 1200px; margin: 0 auto; }
        .card { background: white; border-radius: 8px; padding: 20px; margin: 20px 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        h1 { color: #333; }
        h2 { color: #666; border-bottom: 2px solid #eee; padding-bottom: 10px; }
        .metric { display: inline-block; margin: 10px 20px 10px 0; }
        .metric-value { font-size: 2em; font-weight: bold; color: #2196F3; }
        .metric-label { color: #666; font-size: 0.9em; }
        table { width: 100%; border-collapse: collapse; }
        th, td { padding: 12px; text-align: left; border-bottom: 1px solid #eee; }
        th { background: #f9f9f9; }
        .status-success { color: #4CAF50; }
        .status-fail { color: #f44336; }
        .status-pending { color: #FF9800; }
        .severity-high { background: #ffebee; }
        .severity-medium { background: #fff3e0; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Protocol Outcome Dashboard</h1>
        <p>Generated: """ + datetime.now().isoformat() + """</p>
        
        <div class="card">
            <h2>Summary</h2>
            <div class="metric">
                <div class="metric-value">""" + str(len(outcomes)) + """</div>
                <div class="metric-label">Total Executions</div>
            </div>
            <div class="metric">
                <div class="metric-value">""" + str(len(validator_scores)) + """</div>
                <div class="metric-label">Validation Reports</div>
            </div>
            <div class="metric">
                <div class="metric-value">""" + str(len(discrepancies)) + """</div>
                <div class="metric-label">Discrepancies</div>
            </div>
        </div>
        
        <div class="card">
            <h2>Outcome Records</h2>
            <table>
                <tr>
                    <th>Execution ID</th>
                    <th>Protocol</th>
                    <th>Recorded</th>
                    <th>Deployment</th>
                    <th>Test Rate</th>
                </tr>
"""
    
    for outcome in outcomes:
        metrics = outcome.get('metrics', {})
        deployment = metrics.get('deployment_success')
        test_rate = metrics.get('test_pass_rate')
        
        deployment_class = 'status-success' if deployment is True else ('status-fail' if deployment is False else 'status-pending')
        deployment_text = 'Success' if deployment is True else ('Failed' if deployment is False else 'Pending')
        
        html += f"""
                <tr>
                    <td>{outcome.get('execution_id', 'N/A')}</td>
                    <td>{outcome.get('protocol_id', 'N/A')}</td>
                    <td>{outcome.get('recorded_at', 'N/A')[:19]}</td>
                    <td class="{deployment_class}">{deployment_text}</td>
                    <td>{f'{test_rate:.0%}' if test_rate is not None else 'N/A'}</td>
                </tr>
"""
    
    html += """
            </table>
        </div>
"""
    
    if discrepancies:
        html += """
        <div class="card">
            <h2>Discrepancies</h2>
            <table>
                <tr>
                    <th>Execution ID</th>
                    <th>Protocol</th>
                    <th>Issue</th>
                    <th>Severity</th>
                </tr>
"""
        for disc in discrepancies:
            severity_class = f"severity-{disc.get('severity', 'medium')}"
            html += f"""
                <tr class="{severity_class}">
                    <td>{disc.get('execution_id', 'N/A')}</td>
                    <td>{disc.get('protocol_id', 'N/A')}</td>
                    <td>{disc.get('issue', 'N/A')}</td>
                    <td>{disc.get('severity', 'N/A').upper()}</td>
                </tr>
"""
        html += """
            </table>
        </div>
"""
    
    html += """
    </div>
</body>
</html>
"""
    
    return html

def main():
    parser = argparse.ArgumentParser(description='Generate outcome dashboard')
    parser.add_argument('--output', help='Output HTML file path')
    parser.add_argument('--workspace', default='.', help='Workspace root path')
    args = parser.parse_args()
    
    workspace = Path(args.workspace).resolve()
    
    print(f"[DASHBOARD] Generating outcome dashboard...")
    
    # Load data
    validator_scores = load_validator_scores(workspace)
    outcomes = load_outcomes(workspace)
    discrepancies = identify_discrepancies(validator_scores, outcomes)
    
    # Generate dashboard
    html = generate_dashboard_html(validator_scores, outcomes, discrepancies)
    
    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = workspace / 'outcome-dashboard.html'
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"[DASHBOARD] Dashboard generated")
    print(f"  - Outcomes: {len(outcomes)}")
    print(f"  - Validator scores: {len(validator_scores)}")
    print(f"  - Discrepancies: {len(discrepancies)}")
    print(f"  - Output: {output_path}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

