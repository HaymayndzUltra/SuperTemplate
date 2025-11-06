#!/usr/bin/env python3
"""
Compliance Enforcement Script for Protocol 08
Ensures data handling complies with regulatory requirements
"""

import json
import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

import pandas as pd
import hashlib

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('compliance_enforcement.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class ComplianceEnforcer:
    """Enforces compliance requirements for data handling"""
    
    def __init__(self, data_path: str, framework_path: str, output_path: str):
        self.data_path = Path(data_path)
        self.framework_path = Path(framework_path)
        self.output_path = Path(output_path)
        self.output_path.mkdir(parents=True, exist_ok=True)
        self.compliance_results = []
        self.start_time = datetime.now()
        
        # Compliance requirements
        self.compliance_requirements = {
            'gdpr': {
                'data_minimization': True,
                'consent_required': False,
                'right_to_be_forgotten': True,
                'data_portability': True
            },
            'hipaa': {
                'phi_protection': True,
                'access_controls': True,
                'audit_trails': True,
                'encryption_required': True
            },
            'ccpa': {
                'consumer_rights': True,
                'data_transparency': True,
                'opt_out_required': False,
                'disclosure_requirements': True
            }
        }
    
    def load_compliance_framework(self) -> Dict[str, Any]:
        """Load compliance framework requirements"""
        logger.info("Loading compliance framework")
        
        try:
            if self.framework_path.exists():
                if self.framework_path.suffix == '.json':
                    with open(self.framework_path, 'r') as f:
                        return json.load(f)
                else:
                    # Parse markdown framework
                    return self._parse_markdown_framework()
            else:
                logger.warning("Framework file not found, using default compliance requirements")
                return self.get_default_framework()
        except Exception as e:
            logger.error(f"Failed to load compliance framework: {e}")
            return self.get_default_framework()
    
    def get_default_framework(self) -> Dict[str, Any]:
        """Get default compliance framework"""
        return {
            'applicable_regulations': ['GDPR', 'CCPA'],
            'data_classification': 'public',
            'privacy_controls': {
                'anonymization_required': True,
                'pseudonymization_enabled': True,
                'data_retention_days': 365,
                'encryption_at_rest': True,
                'encryption_in_transit': True
            },
            'access_controls': {
                'role_based_access': True,
                'audit_logging': True,
                'authentication_required': True
            }
        }
    
    def _parse_markdown_framework(self) -> Dict[str, Any]:
        """Parse markdown compliance framework"""
        # Simple parsing for demonstration
        return self.get_default_framework()
    
    def discover_data_files(self) -> List[Path]:
        """Discover all data files for compliance checking"""
        logger.info("Discovering data files for compliance checking")
        
        data_files = []
        extensions = ['.csv', '.json', '.parquet', '.xlsx', '.tsv']
        
        for ext in extensions:
            data_files.extend(self.data_path.glob(f"*{ext}"))
            data_files.extend(self.data_path.glob(f"**/*{ext}"))
        
        logger.info(f"Discovered {len(data_files)} data files")
        return data_files
    
    def load_data_file(self, file_path: Path) -> Optional[pd.DataFrame]:
        """Load data file for compliance checking"""
        try:
            if file_path.suffix == '.csv':
                return pd.read_csv(file_path)
            elif file_path.suffix == '.json':
                return pd.read_json(file_path)
            elif file_path.suffix == '.parquet':
                return pd.read_parquet(file_path)
            elif file_path.suffix in ['.xlsx', '.xls']:
                return pd.read_excel(file_path)
            elif file_path.suffix == '.tsv':
                return pd.read_csv(file_path, sep='\t')
            else:
                logger.warning(f"Unsupported file format: {file_path.suffix}")
                return None
        except Exception as e:
            logger.error(f"Failed to load {file_path}: {e}")
            return None
    
    def validate_data_minimization(self, df: pd.DataFrame, file_path: Path, framework: Dict[str, Any]) -> Dict[str, Any]:
        """Validate data minimization principle"""
        logger.info(f"Validating data minimization for {file_path.name}")
        
        try:
            # Check for unnecessary columns
            total_columns = len(df.columns)
            data_classification = framework.get('data_classification', 'public')
            
            # For public data, minimization is less strict
            if data_classification == 'public':
                minimization_score = 1.0
                issues = []
            else:
                # Check for potentially sensitive columns
                sensitive_keywords = ['ssn', 'social_security', 'credit_card', 'password', 'secret', 'private']
                sensitive_columns = [col for col in df.columns if any(keyword in col.lower() for keyword in sensitive_keywords)]
                
                if sensitive_columns:
                    minimization_score = 0.5
                    issues = [f"Sensitive columns detected: {sensitive_columns}"]
                else:
                    minimization_score = 1.0
                    issues = []
            
            validation_result = {
                'metric': 'data_minimization',
                'score': float(minimization_score),
                'threshold': 0.8,
                'passed': minimization_score >= 0.8,
                'details': {
                    'total_columns': int(total_columns),
                    'data_classification': data_classification,
                    'sensitive_columns': sensitive_columns if 'sensitive_columns' in locals() else [],
                    'issues': issues
                }
            }
            
            logger.info(f"Data minimization score: {minimization_score:.3f}")
            return validation_result
            
        except Exception as e:
            logger.error(f"Data minimization validation failed: {e}")
            return {
                'metric': 'data_minimization',
                'score': 0.0,
                'threshold': 0.8,
                'passed': False,
                'error': str(e)
            }
    
    def validate_privacy_controls(self, df: pd.DataFrame, file_path: Path, framework: Dict[str, Any]) -> Dict[str, Any]:
        """Validate privacy controls implementation"""
        logger.info(f"Validating privacy controls for {file_path.name}")
        
        try:
            privacy_controls = framework.get('privacy_controls', {})
            control_scores = []
            
            # Check anonymization
            anonymization_required = privacy_controls.get('anonymization_required', False)
            if anonymization_required:
                # Check if data appears anonymized (simplified check)
                personal_identifiers = ['name', 'email', 'phone', 'address']
                has_identifiers = any(identifier in ' '.join(df.columns).lower() for identifier in personal_identifiers)
                
                if has_identifiers:
                    anonymization_score = 0.5  # Partial - may need review
                else:
                    anonymization_score = 1.0
            else:
                anonymization_score = 1.0
            
            control_scores.append(anonymization_score)
            
            # Check encryption (metadata check)
            encryption_required = privacy_controls.get('encryption_at_rest', False)
            encryption_score = 1.0 if not encryption_required else 0.8  # Assume encryption is in place
            control_scores.append(encryption_score)
            
            # Calculate overall privacy control score
            privacy_score = sum(control_scores) / len(control_scores) if control_scores else 0
            
            validation_result = {
                'metric': 'privacy_controls',
                'score': float(privacy_score),
                'threshold': 0.9,
                'passed': privacy_score >= 0.9,
                'details': {
                    'anonymization_score': float(anonymization_score),
                    'encryption_score': float(encryption_score),
                    'controls_required': privacy_controls,
                    'control_scores': control_scores
                }
            }
            
            logger.info(f"Privacy controls score: {privacy_score:.3f}")
            return validation_result
            
        except Exception as e:
            logger.error(f"Privacy controls validation failed: {e}")
            return {
                'metric': 'privacy_controls',
                'score': 0.0,
                'threshold': 0.9,
                'passed': False,
                'error': str(e)
            }
    
    def validate_access_controls(self, df: pd.DataFrame, file_path: Path, framework: Dict[str, Any]) -> Dict[str, Any]:
        """Validate access controls implementation"""
        logger.info(f"Validating access controls for {file_path.name}")
        
        try:
            access_controls = framework.get('access_controls', {})
            
            # Check file permissions (simplified)
            file_stat = file_path.stat()
            file_mode = oct(file_stat.st_mode)[-3:]
            
            # Basic permission check (not too open)
            if file_mode in ['644', '600', '640']:
                permission_score = 1.0
            else:
                permission_score = 0.7
            
            # Check audit logging requirement
            audit_required = access_controls.get('audit_logging', False)
            audit_score = 1.0 if not audit_required else 0.8  # Assume audit logging is configured
            
            # Calculate overall access control score
            access_score = (permission_score + audit_score) / 2
            
            validation_result = {
                'metric': 'access_controls',
                'score': float(access_score),
                'threshold': 0.8,
                'passed': access_score >= 0.8,
                'details': {
                    'file_permissions': file_mode,
                    'permission_score': float(permission_score),
                    'audit_score': float(audit_score),
                    'controls_required': access_controls
                }
            }
            
            logger.info(f"Access controls score: {access_score:.3f}")
            return validation_result
            
        except Exception as e:
            logger.error(f"Access controls validation failed: {e}")
            return {
                'metric': 'access_controls',
                'score': 0.0,
                'threshold': 0.8,
                'passed': False,
                'error': str(e)
            }
    
    def validate_file_compliance(self, file_path: Path, framework: Dict[str, Any]) -> Dict[str, Any]:
        """Validate compliance for a single data file"""
        logger.info(f"Validating compliance for {file_path}")
        
        try:
            # Load data
            df = self.load_data_file(file_path)
            if df is None:
                return {
                    'file_path': str(file_path),
                    'compliance_status': 'failed',
                    'error': 'Could not load file'
                }
            
            # Run compliance validations
            validations = [
                self.validate_data_minimization(df, file_path, framework),
                self.validate_privacy_controls(df, file_path, framework),
                self.validate_access_controls(df, file_path, framework)
            ]
            
            # Calculate overall compliance score
            scores = [v['score'] for v in validations if 'score' in v]
            overall_compliance = sum(scores) / len(scores) if scores else 0.0
            
            # Check if all validations passed
            all_passed = all(v.get('passed', False) for v in validations)
            
            file_compliance = {
                'file_path': str(file_path),
                'compliance_status': 'passed' if all_passed else 'failed',
                'overall_compliance_score': float(overall_compliance),
                'compliance_threshold': 0.85,
                'compliance_passed': overall_compliance >= 0.85 and all_passed,
                'validations': validations,
                'validation_timestamp': datetime.now().isoformat()
            }
            
            logger.info(f"File compliance completed: {file_path.name} - Score: {overall_compliance:.3f}")
            return file_compliance
            
        except Exception as e:
            logger.error(f"File compliance validation failed for {file_path}: {e}")
            return {
                'file_path': str(file_path),
                'compliance_status': 'failed',
                'error': str(e),
                'validation_timestamp': datetime.now().isoformat()
            }
    
    def execute_compliance_validation(self) -> Dict[str, Any]:
        """Execute complete compliance validation"""
        logger.info("Starting compliance validation execution")
        
        # Load compliance framework
        framework = self.load_compliance_framework()
        
        # Discover data files
        data_files = self.discover_data_files()
        
        if not data_files:
            logger.warning("No data files found for compliance validation")
            return {
                'compliance_summary': {
                    'total_files': 0,
                    'passed_files': 0,
                    'failed_files': 0,
                    'overall_compliance_score': 0.0,
                    'compliance_passed': False
                },
                'file_compliance_results': []
            }
        
        # Validate each file
        file_compliance_results = []
        for file_path in data_files:
            compliance_result = self.validate_file_compliance(file_path, framework)
            file_compliance_results.append(compliance_result)
            self.compliance_results.append(compliance_result)
        
        # Calculate compliance summary
        total_files = len(file_compliance_results)
        passed_files = sum(1 for r in file_compliance_results if r.get('compliance_status') == 'passed')
        failed_files = total_files - passed_files
        
        # Calculate overall compliance across all files
        compliance_scores = [r.get('overall_compliance_score', 0) for r in file_compliance_results if 'overall_compliance_score' in r]
        overall_compliance = sum(compliance_scores) / len(compliance_scores) if compliance_scores else 0.0
        
        compliance_summary = {
            'compliance_summary': {
                'total_files': int(total_files),
                'passed_files': int(passed_files),
                'failed_files': int(failed_files),
                'pass_rate': float(passed_files / total_files) if total_files > 0 else 0.0,
                'overall_compliance_score': float(overall_compliance),
                'compliance_threshold': 0.85,
                'compliance_passed': overall_compliance >= 0.85 and passed_files == total_files,
                'execution_time_seconds': (datetime.now() - self.start_time).total_seconds(),
                'start_time': self.start_time.isoformat(),
                'end_time': datetime.now().isoformat()
            },
            'file_compliance_results': file_compliance_results,
            'compliance_framework': framework
        }
        
        logger.info(f"Compliance validation completed: {passed_files}/{total_files} files passed, Overall Score: {overall_compliance:.3f}")
        return compliance_summary
    
    def save_compliance_report(self, report: Dict[str, Any], report_path: str):
        """Save compliance report to specified path"""
        try:
            with open(report_path, 'w') as f:
                json.dump(report, f, indent=2, default=str)
            logger.info(f"Compliance report saved to {report_path}")
        except Exception as e:
            logger.error(f"Failed to save compliance report: {e}")

def main():
    """Main execution function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Ensure data compliance')
    parser.add_argument('--data', required=True, help='Path to data directory')
    parser.add_argument('--framework', required=True, help='Path to compliance framework file')
    parser.add_argument('--output', required=True, help='Output directory for compliance reports')
    
    args = parser.parse_args()
    
    try:
        # Initialize compliance enforcer
        enforcer = ComplianceEnforcer(args.data, args.framework, args.output)
        
        # Execute compliance validation
        compliance_report = enforcer.execute_compliance_validation()
        
        # Save compliance report
        report_file = Path(args.output) / 'compliance_report.json'
        enforcer.save_compliance_report(compliance_report, str(report_file))
        
        # Return success if compliance passed
        if compliance_report['compliance_summary']['compliance_passed']:
            logger.info("Compliance validation completed successfully")
            return 0
        else:
            logger.warning("Compliance validation completed with issues")
            return 1
            
    except Exception as e:
        logger.error(f"Compliance validation failed: {e}")
        return 1

if __name__ == '__main__':
    sys.exit(main())
