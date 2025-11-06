#!/usr/bin/env python3
"""
Validator for Protocol 22: AI Model Performance Monitoring
Validates monitoring infrastructure, dashboards, alerts, and SLO configuration.
"""

import os
import sys
import json
import yaml
from pathlib import Path
from typing import Dict, List, Tuple

class Protocol22Validator:
    
    def __init__(self, evidence_path: str):
        self.evidence_path = Path(evidence_path)
        self.errors = []
        self.warnings = []
        self.passed = []
    
    def validate(self) -> Tuple[bool, Dict]:
        """Run all validation checks."""
        
        print("🔍 Validating Protocol 22: AI Model Performance Monitoring")
        print("=" * 60)
        
        # Gate 1: Monitoring Infrastructure
        self._validate_prometheus_config()
        self._validate_grafana_dashboard()
        self._validate_alert_rules()
        self._validate_metrics_collection()
        
        # Gate 2: Baseline Establishment
        self._validate_baseline_metrics()
        self._validate_slo_config()
        self._validate_thresholds()
        
        # Gate 3: Alerting Validation
        self._validate_alertmanager_config()
        self._validate_notification_channels()
        self._validate_runbooks()
        
        # Generate report
        return self._generate_report()
    
    def _validate_prometheus_config(self):
        """Validate Prometheus configuration exists and is valid."""
        
        config_path = self.evidence_path / "configs" / "prometheus.yml"
        
        if not config_path.exists():
            self.errors.append("prometheus.yml not found")
            return
        
        try:
            with open(config_path) as f:
                config = yaml.safe_load(f)
            
            # Check required sections
            required_sections = ['global', 'scrape_configs']
            for section in required_sections:
                if section not in config:
                    self.errors.append(f"Missing required section: {section}")
                else:
                    self.passed.append(f"Prometheus config has {section}")
            
            # Validate scrape configs
            if 'scrape_configs' in config:
                if len(config['scrape_configs']) == 0:
                    self.errors.append("No scrape configs defined")
                else:
                    self.passed.append(f"Found {len(config['scrape_configs'])} scrape configs")
            
        except yaml.YAMLError as e:
            self.errors.append(f"Invalid YAML in prometheus.yml: {e}")
        except Exception as e:
            self.errors.append(f"Error reading prometheus.yml: {e}")
    
    def _validate_grafana_dashboard(self):
        """Validate Grafana dashboard configuration."""
        
        dashboard_path = self.evidence_path / "dashboards" / "monitoring-dashboard.json"
        
        if not dashboard_path.exists():
            self.errors.append("monitoring-dashboard.json not found")
            return
        
        try:
            with open(dashboard_path) as f:
                dashboard = json.load(f)
            
            # Check dashboard structure
            if 'dashboard' not in dashboard:
                self.errors.append("Invalid dashboard structure")
                return
            
            dash = dashboard['dashboard']
            
            # Check panels
            if 'panels' not in dash:
                self.errors.append("No panels defined in dashboard")
            else:
                panel_count = len(dash['panels'])
                if panel_count < 5:
                    self.warnings.append(f"Only {panel_count} panels (recommended: 5+)")
                else:
                    self.passed.append(f"Dashboard has {panel_count} panels")
            
            # Check title
            if 'title' in dash:
                self.passed.append(f"Dashboard title: {dash['title']}")
            
        except json.JSONDecodeError as e:
            self.errors.append(f"Invalid JSON in dashboard: {e}")
        except Exception as e:
            self.errors.append(f"Error reading dashboard: {e}")
    
    def _validate_alert_rules(self):
        """Validate alert rules configuration."""
        
        rules_path = self.evidence_path / "configs" / "alert-rules.yaml"
        
        if not rules_path.exists():
            self.errors.append("alert-rules.yaml not found")
            return
        
        try:
            with open(rules_path) as f:
                rules = yaml.safe_load(f)
            
            if 'groups' not in rules:
                self.errors.append("No alert groups defined")
                return
            
            total_alerts = 0
            for group in rules['groups']:
                if 'rules' in group:
                    total_alerts += len(group['rules'])
            
            if total_alerts < 5:
                self.warnings.append(f"Only {total_alerts} alerts defined (recommended: 5+)")
            else:
                self.passed.append(f"Found {total_alerts} alert rules")
            
            # Validate alert structure
            for group in rules['groups']:
                for rule in group.get('rules', []):
                    required_fields = ['alert', 'expr', 'labels', 'annotations']
                    for field in required_fields:
                        if field not in rule:
                            self.warnings.append(f"Alert '{rule.get('alert', 'unknown')}' missing {field}")
            
        except yaml.YAMLError as e:
            self.errors.append(f"Invalid YAML in alert-rules.yaml: {e}")
        except Exception as e:
            self.errors.append(f"Error reading alert-rules.yaml: {e}")
    
    def _validate_metrics_collection(self):
        """Validate metrics are being collected."""
        
        # Check for instrumentation code
        scripts_path = self.evidence_path / "scripts"
        
        if not scripts_path.exists():
            self.warnings.append("No scripts directory found")
            return
        
        instrumentation_files = list(scripts_path.glob("*instrumentation*.py"))
        
        if len(instrumentation_files) == 0:
            self.warnings.append("No instrumentation scripts found")
        else:
            self.passed.append(f"Found {len(instrumentation_files)} instrumentation scripts")
    
    def _validate_baseline_metrics(self):
        """Validate baseline metrics are established."""
        
        baseline_path = self.evidence_path / "reports" / "baseline-metrics.json"
        
        if not baseline_path.exists():
            self.errors.append("baseline-metrics.json not found")
            return
        
        try:
            with open(baseline_path) as f:
                baseline = json.load(f)
            
            required_metrics = ['latency', 'throughput', 'accuracy', 'error_rate']
            
            for metric in required_metrics:
                if metric not in baseline:
                    self.errors.append(f"Missing baseline metric: {metric}")
                else:
                    self.passed.append(f"Baseline established for {metric}")
            
        except json.JSONDecodeError as e:
            self.errors.append(f"Invalid JSON in baseline-metrics.json: {e}")
        except Exception as e:
            self.errors.append(f"Error reading baseline-metrics.json: {e}")
    
    def _validate_slo_config(self):
        """Validate SLO configuration."""
        
        slo_path = self.evidence_path / "configs" / "slo-config.yaml"
        
        if not slo_path.exists():
            self.errors.append("slo-config.yaml not found")
            return
        
        try:
            with open(slo_path) as f:
                slo = yaml.safe_load(f)
            
            if 'service_level_objectives' not in slo:
                self.errors.append("No SLOs defined")
                return
            
            slo_count = len(slo['service_level_objectives'])
            
            if slo_count < 3:
                self.warnings.append(f"Only {slo_count} SLOs defined (recommended: 3+)")
            else:
                self.passed.append(f"Found {slo_count} SLOs")
            
            # Validate SLO structure
            for slo_item in slo['service_level_objectives']:
                required_fields = ['name', 'metric', 'target', 'window']
                for field in required_fields:
                    if field not in slo_item:
                        self.errors.append(f"SLO '{slo_item.get('name', 'unknown')}' missing {field}")
            
        except yaml.YAMLError as e:
            self.errors.append(f"Invalid YAML in slo-config.yaml: {e}")
        except Exception as e:
            self.errors.append(f"Error reading slo-config.yaml: {e}")
    
    def _validate_thresholds(self):
        """Validate performance thresholds are set."""
        
        # Thresholds should be in alert rules
        rules_path = self.evidence_path / "configs" / "alert-rules.yaml"
        
        if not rules_path.exists():
            return
        
        try:
            with open(rules_path) as f:
                rules = yaml.safe_load(f)
            
            threshold_alerts = []
            for group in rules.get('groups', []):
                for rule in group.get('rules', []):
                    if 'for' in rule:  # Has threshold duration
                        threshold_alerts.append(rule['alert'])
            
            if len(threshold_alerts) > 0:
                self.passed.append(f"Found {len(threshold_alerts)} alerts with thresholds")
            
        except Exception:
            pass
    
    def _validate_alertmanager_config(self):
        """Validate Alertmanager configuration."""
        
        am_path = self.evidence_path / "configs" / "alertmanager.yml"
        
        if not am_path.exists():
            self.warnings.append("alertmanager.yml not found")
            return
        
        try:
            with open(am_path) as f:
                config = yaml.safe_load(f)
            
            if 'route' not in config:
                self.errors.append("No routing configuration in alertmanager")
            else:
                self.passed.append("Alertmanager routing configured")
            
            if 'receivers' not in config:
                self.errors.append("No receivers configured in alertmanager")
            else:
                receiver_count = len(config['receivers'])
                self.passed.append(f"Found {receiver_count} alert receivers")
            
        except yaml.YAMLError as e:
            self.errors.append(f"Invalid YAML in alertmanager.yml: {e}")
        except Exception as e:
            self.errors.append(f"Error reading alertmanager.yml: {e}")
    
    def _validate_notification_channels(self):
        """Validate notification channels are configured."""
        
        am_path = self.evidence_path / "configs" / "alertmanager.yml"
        
        if not am_path.exists():
            return
        
        try:
            with open(am_path) as f:
                config = yaml.safe_load(f)
            
            channels = []
            for receiver in config.get('receivers', []):
                if 'slack_configs' in receiver:
                    channels.append('slack')
                if 'pagerduty_configs' in receiver:
                    channels.append('pagerduty')
                if 'email_configs' in receiver:
                    channels.append('email')
            
            if len(channels) == 0:
                self.warnings.append("No notification channels configured")
            else:
                self.passed.append(f"Notification channels: {', '.join(set(channels))}")
            
        except Exception:
            pass
    
    def _validate_runbooks(self):
        """Validate runbooks exist."""
        
        runbook_path = self.evidence_path / "runbooks" / "monitoring-runbook.md"
        
        if not runbook_path.exists():
            self.warnings.append("monitoring-runbook.md not found")
        else:
            self.passed.append("Monitoring runbook exists")
    
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
            'protocol': '22-performance-monitoring',
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
        print("Usage: validate_monitoring.py <evidence_path>")
        sys.exit(1)
    
    evidence_path = sys.argv[1]
    
    validator = Protocol22Validator(evidence_path)
    success, report = validator.validate()
    
    # Save report
    report_path = Path(evidence_path) / "validation-report.json"
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n📄 Report saved to: {report_path}")
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
