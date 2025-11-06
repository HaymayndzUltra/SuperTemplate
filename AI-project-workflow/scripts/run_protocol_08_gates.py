#!/usr/bin/env python3
"""
Protocol 08 Gates Runner
Runs all quality gates for Protocol 08: AI Data Collection & Ingestion
"""

import json
import logging
import os
import sys
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('protocol_08_gates.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class Protocol08GatesRunner:
    """Runs all quality gates for Protocol 08"""
    
    def __init__(self, workspace_root: str):
        self.workspace_root = Path(workspace_root)
        self.protocols_dir = self.workspace_root / "protocols"
        self.scripts_dir = self.workspace_root / "scripts" / "ai"
        self.artifacts_dir = self.workspace_root / ".artifacts" / "protocol-08"
        self.artifacts_dir.mkdir(parents=True, exist_ok=True)
        self.gate_results = []
        self.start_time = datetime.now()
        
        # Quality gates configuration
        self.quality_gates = [
            {
                'name': 'pipeline_configuration_validation',
                'script': 'validate_pipeline_config.py',
                'threshold': 0.95,
                'description': 'Pipeline configuration and connectivity validation'
            },
            {
                'name': 'data_collection_quality',
                'script': 'validate_ingested_data.py',
                'threshold': 0.9,
                'description': 'Data collection quality and completeness validation'
            },
            {
                'name': 'compliance_validation',
                'script': 'ensure_compliance.py',
                'threshold': 1.0,
                'description': 'Compliance requirements validation'
            },
            {
                'name': 'handoff_readiness',
                'script': 'aggregate_evidence_08.py',
                'threshold': 0.95,
                'description': 'Handoff readiness validation'
            }
        ]
    
    def run_script(self, script_name: str, args: List[str]) -> Dict[str, Any]:
        """Run a script and capture results"""
        try:
            script_path = self.scripts_dir / script_name
            if not script_path.exists():
                return {
                    'status': 'failed',
                    'error': f'Script not found: {script_path}',
                    'exit_code': -1
                }
            
            cmd = ['python3', str(script_path)] + args
            logger.info(f"Running script: {' '.join(cmd)}")
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout
            )
            
            return {
                'status': 'success' if result.returncode == 0 else 'failed',
                'exit_code': result.returncode,
                'stdout': result.stdout,
                'stderr': result.stderr
            }
            
        except subprocess.TimeoutExpired:
            return {
                'status': 'failed',
                'error': 'Script execution timeout',
                'exit_code': -2
            }
        except Exception as e:
            return {
                'status': 'failed',
                'error': str(e),
                'exit_code': -3
            }
    
    def extract_score_from_report(self, report_path: str, gate_name: str) -> float:
        """Extract validation score from report file"""
        try:
            with open(report_path, 'r') as f:
                report = json.load(f)
            
            # Look for score in different possible locations
            if 'validation_summary' in report:
                return float(report['validation_summary'].get('overall_score', 0.0))
            elif 'compliance_summary' in report:
                return float(report['compliance_summary'].get('overall_compliance_score', 0.0))
            elif 'aggregation_summary' in report:
                return float(report['aggregation_summary'].get('aggregation_complete', 0.0))
            else:
                logger.warning(f"Could not find score in report for {gate_name}")
                return 0.0
                
        except Exception as e:
            logger.error(f"Failed to extract score from {report_path}: {e}")
            return 0.0
    
    def run_gate(self, gate_config: Dict[str, Any]) -> Dict[str, Any]:
        """Run a single quality gate"""
        gate_name = gate_config['name']
        script_name = gate_config['script']
        threshold = gate_config['threshold']
        
        logger.info(f"Running quality gate: {gate_name}")
        
        gate_start_time = datetime.now()
        
        # Prepare script arguments based on gate type
        if gate_name == 'pipeline_configuration_validation':
            args = ['--input', 'config/', '--output', str(self.artifacts_dir)]
        elif gate_name == 'data_collection_quality':
            args = ['--input', 'data/collected/', '--output', str(self.artifacts_dir)]
        elif gate_name == 'compliance_validation':
            args = ['--data', 'data/collected/', '--framework', 'compliance-framework.md', '--output', str(self.artifacts_dir)]
        elif gate_name == 'handoff_readiness':
            args = ['--output', str(self.artifacts_dir), '--protocol-id', '08']
        else:
            args = ['--output', str(self.artifacts_dir)]
        
        # Run the script
        script_result = self.run_script(script_name, args)
        
        # Calculate gate execution time
        execution_time = (datetime.now() - gate_start_time).total_seconds()
        
        # Determine gate result
        gate_passed = False
        score = 0.0
        issues = []
        
        if script_result['status'] == 'success':
            # Try to extract score from generated report
            report_files = list(self.artifacts_dir.glob("*.json"))
            if report_files:
                latest_report = max(report_files, key=lambda f: f.stat().st_mtime)
                score = self.extract_score_from_report(str(latest_report), gate_name)
                gate_passed = score >= threshold
            else:
                issues.append("No report file generated")
        else:
            issues.append(f"Script execution failed: {script_result.get('error', script_result.get('stderr', 'Unknown error'))}")
        
        gate_result = {
            'gate_name': gate_name,
            'gate_description': gate_config['description'],
            'threshold': threshold,
            'score': float(score),
            'passed': gate_passed,
            'execution_time_seconds': execution_time,
            'script_result': script_result,
            'issues': issues,
            'execution_timestamp': gate_start_time.isoformat()
        }
        
        logger.info(f"Gate {gate_name}: {'PASSED' if gate_passed else 'FAILED'} (Score: {score:.3f}, Threshold: {threshold})")
        return gate_result
    
    def run_all_gates(self) -> Dict[str, Any]:
        """Run all quality gates"""
        logger.info("Starting Protocol 08 quality gates execution")
        
        gate_results = []
        passed_gates = 0
        total_gates = len(self.quality_gates)
        
        for gate_config in self.quality_gates:
            gate_result = self.run_gate(gate_config)
            gate_results.append(gate_result)
            self.gate_results.append(gate_result)
            
            if gate_result['passed']:
                passed_gates += 1
        
        # Calculate overall results
        overall_score = sum(g['score'] for g in gate_results) / total_gates if total_gates > 0 else 0.0
        all_passed = passed_gates == total_gates
        
        gates_summary = {
            'total_gates': int(total_gates),
            'passed_gates': int(passed_gates),
            'failed_gates': int(total_gates - passed_gates),
            'pass_rate': float(passed_gates / total_gates) if total_gates > 0 else 0.0,
            'overall_score': float(overall_score),
            'all_passed': all_passed,
            'execution_passed': all_passed and overall_score >= 0.75
        }
        
        execution_summary = {
            'protocol_id': '08',
            'execution_status': 'passed' if all_passed else 'failed',
            'gates_summary': gates_summary,
            'execution_time_seconds': (datetime.now() - self.start_time).total_seconds(),
            'start_time': self.start_time.isoformat(),
            'end_time': datetime.now().isoformat()
        }
        
        gates_report = {
            'execution_summary': execution_summary,
            'gate_results': gate_results,
            'quality_gates_config': self.quality_gates
        }
        
        logger.info(f"Protocol 08 gates completed: {passed_gates}/{total_gates} passed, Overall Score: {overall_score:.3f}")
        return gates_report
    
    def save_gates_report(self, report: Dict[str, Any], report_path: str):
        """Save gates execution report"""
        try:
            with open(report_path, 'w') as f:
                json.dump(report, f, indent=2, default=str)
            logger.info(f"Gates report saved to {report_path}")
        except Exception as e:
            logger.error(f"Failed to save gates report: {e}")
    
    def generate_summary_report(self, gates_report: Dict[str, Any]) -> str:
        """Generate human-readable summary report"""
        summary = []
        summary.append("=" * 60)
        summary.append("PROTOCOL 08: AI DATA COLLECTION & INGESTION - QUALITY GATES REPORT")
        summary.append("=" * 60)
        summary.append(f"Execution Status: {gates_report['execution_summary']['execution_status'].upper()}")
        summary.append(f"Overall Score: {gates_report['execution_summary']['gates_summary']['overall_score']:.3f}")
        summary.append(f"Pass Rate: {gates_report['execution_summary']['gates_summary']['pass_rate']:.1%}")
        summary.append(f"Execution Time: {gates_report['execution_summary']['execution_time_seconds']:.2f} seconds")
        summary.append("")
        
        summary.append("GATE RESULTS:")
        summary.append("-" * 40)
        
        for gate_result in gates_report['gate_results']:
            status = "✅ PASSED" if gate_result['passed'] else "❌ FAILED"
            summary.append(f"{gate_result['gate_name']}: {status}")
            summary.append(f"  Score: {gate_result['score']:.3f} (Threshold: {gate_result['threshold']})")
            summary.append(f"  Time: {gate_result['execution_time_seconds']:.2f}s")
            if gate_result['issues']:
                summary.append(f"  Issues: {', '.join(gate_result['issues'])}")
            summary.append("")
        
        summary.append("=" * 60)
        
        return "\n".join(summary)

def main():
    """Main execution function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Run Protocol 08 quality gates')
    parser.add_argument('--workspace', default='.', help='Workspace root directory')
    
    args = parser.parse_args()
    
    try:
        # Initialize gates runner
        runner = Protocol08GatesRunner(args.workspace)
        
        # Run all gates
        gates_report = runner.run_all_gates()
        
        # Save detailed report
        report_file = runner.artifacts_dir / 'protocol_08_gates_report.json'
        runner.save_gates_report(gates_report, str(report_file))
        
        # Generate and save summary report
        summary_text = runner.generate_summary_report(gates_report)
        summary_file = runner.artifacts_dir / 'protocol_08_gates_summary.txt'
        with open(summary_file, 'w') as f:
            f.write(summary_text)
        
        # Print summary
        print(summary_text)
        
        # Return success if all gates passed
        if gates_report['execution_summary']['execution_status'] == 'passed':
            logger.info("Protocol 08 quality gates all passed")
            return 0
        else:
            logger.warning("Protocol 08 quality gates failed")
            return 1
            
    except Exception as e:
        logger.error(f"Protocol 08 gates execution failed: {e}")
        return 1

if __name__ == '__main__':
    sys.exit(main())
