#!/usr/bin/env python3
"""
Validator for Protocol 23: AI Data Drift & Concept Drift Detection
Validates drift detection configuration, monitoring, and alerting.
"""

import os
import sys
import json
import yaml
from pathlib import Path
from typing import Dict, List, Tuple

class Protocol23Validator:
    
    def __init__(self, evidence_path: str):
        self.evidence_path = Path(evidence_path)
        self.errors = []
        self.warnings = []
        self.passed = []
    
    def validate(self) -> Tuple[bool, Dict]:
        """Run all validation checks."""
        
        print("🔍 Validating Protocol 23: AI Data Drift & Concept Drift Detection")
        print("=" * 60)
        
        # Gate 1: Detection Setup
        self._validate_drift_config()
        self._validate_reference_data()
        self._validate_detection_scripts()
        
        # Gate 2: Alert Configuration
        self._validate_alert_config()
        self._validate_thresholds()
        
        # Gate 3: Validation
        self._validate_drift_reports()
        self._validate_root_cause_analysis()
        
        return self._generate_report()
    
    def _validate_drift_config(self):
        """Validate drift detection configuration."""
        
        config_path = self.evidence_path / "configs" / "drift-detection-config.yaml"
        
        if not config_path.exists():
            self.errors.append("drift-detection-config.yaml not found")
            return
        
        try:
            with open(config_path) as f:
                config = yaml.safe_load(f)
            
            if 'drift_monitoring' not in config:
                self.errors.append("No drift_monitoring section in config")
                return
            
            dm = config['drift_monitoring']
            
            # Check required fields
            required_fields = ['enabled', 'check_interval', 'thresholds']
            for field in required_fields:
                if field not in dm:
                    self.errors.append(f"Missing required field: {field}")
                else:
                    self.passed.append(f"Config has {field}")
            
            # Validate thresholds
            if 'thresholds' in dm:
                threshold_types = ['psi', 'ks_test', 'chi_square']
                for t_type in threshold_types:
                    if t_type in dm['thresholds']:
                        self.passed.append(f"Threshold configured for {t_type}")
                    else:
                        self.warnings.append(f"No threshold for {t_type}")
            
        except yaml.YAMLError as e:
            self.errors.append(f"Invalid YAML in config: {e}")
        except Exception as e:
            self.errors.append(f"Error reading config: {e}")
    
    def _validate_reference_data(self):
        """Validate reference data exists."""
        
        ref_data_path = self.evidence_path / "data" / "reference-data.parquet"
        
        if not ref_data_path.exists():
            self.errors.append("reference-data.parquet not found")
        else:
            file_size = ref_data_path.stat().st_size
            if file_size < 1024:  # Less than 1KB
                self.warnings.append("Reference data file seems too small")
            else:
                self.passed.append(f"Reference data exists ({file_size / 1024:.1f} KB)")
    
    def _validate_detection_scripts(self):
        """Validate drift detection scripts exist."""
        
        scripts_path = self.evidence_path / "scripts"
        
        if not scripts_path.exists():
            self.errors.append("Scripts directory not found")
            return
        
        required_scripts = [
            'statistical_tests.py',
            'drift_monitor.py'
        ]
        
        for script in required_scripts:
            script_path = scripts_path / script
            if not script_path.exists():
                self.errors.append(f"Missing required script: {script}")
            else:
                self.passed.append(f"Found script: {script}")
    
    def _validate_alert_config(self):
        """Validate alert configuration."""
        
        config_path = self.evidence_path / "configs" / "drift-detection-config.yaml"
        
        if not config_path.exists():
            return
        
        try:
            with open(config_path) as f:
                config = yaml.safe_load(f)
            
            if 'alerting' in config.get('drift_monitoring', {}):
                alerting = config['drift_monitoring']['alerting']
                
                if 'channels' in alerting:
                    channels = alerting['channels']
                    self.passed.append(f"Alert channels configured: {len(channels)}")
                else:
                    self.warnings.append("No alert channels configured")
            else:
                self.warnings.append("No alerting configuration found")
        
        except Exception:
            pass
    
    def _validate_thresholds(self):
        """Validate drift thresholds are calibrated."""
        
        config_path = self.evidence_path / "configs" / "drift-detection-config.yaml"
        
        if not config_path.exists():
            return
        
        try:
            with open(config_path) as f:
                config = yaml.safe_load(f)
            
            thresholds = config.get('drift_monitoring', {}).get('thresholds', {})
            
            if len(thresholds) == 0:
                self.errors.append("No drift thresholds configured")
            else:
                for test_type, values in thresholds.items():
                    if isinstance(values, dict):
                        self.passed.append(f"Thresholds set for {test_type}")
        
        except Exception:
            pass
    
    def _validate_drift_reports(self):
        """Validate drift reports are generated."""
        
        reports_path = self.evidence_path / "reports"
        
        if not reports_path.exists():
            self.warnings.append("Reports directory not found")
            return
        
        drift_reports = list(reports_path.glob("drift-report*.md"))
        
        if len(drift_reports) == 0:
            self.warnings.append("No drift reports found")
        else:
            self.passed.append(f"Found {len(drift_reports)} drift reports")
    
    def _validate_root_cause_analysis(self):
        """Validate root cause analysis exists."""
        
        rca_path = self.evidence_path / "reports" / "root-cause-analysis.md"
        
        if not rca_path.exists():
            self.warnings.append("root-cause-analysis.md not found")
        else:
            self.passed.append("Root cause analysis documented")
    
    def _generate_report(self) -> Tuple[bool, Dict]:
        """Generate validation report."""
        
        total_checks = len(self.passed) + len(self.warnings) + len(self.errors)
        success = len(self.errors) == 0
        
        print(f"\n✅ Passed: {len(self.passed)}")
        print(f"⚠️  Warnings: {len(self.warnings)}")
        print(f"❌ Errors: {len(self.errors)}")
        print("=" * 60)
        
        if self.errors:
            print("\n❌ ERRORS:")
            for error in self.errors:
                print(f"  - {error}")
        
        if self.warnings:
            print("\n⚠️  WARNINGS:")
            for warning in self.warnings:
                print(f"  - {warning}")
        
        report = {
            'protocol': '23-drift-detection',
            'success': success,
            'total_checks': total_checks,
            'passed': len(self.passed),
            'warnings': len(self.warnings),
            'errors': len(self.errors),
            'details': {
                'passed': self.passed,
                'warnings': self.warnings,
                'errors': self.errors
            }
        }
        
        return success, report

def main():
    if len(sys.argv) < 2:
        print("Usage: validate_drift.py <evidence_path>")
        sys.exit(1)
    
    evidence_path = sys.argv[1]
    
    validator = Protocol23Validator(evidence_path)
    success, report = validator.validate()
    
    report_path = Path(evidence_path) / "validation-report.json"
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n📄 Report saved to: {report_path}")
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
