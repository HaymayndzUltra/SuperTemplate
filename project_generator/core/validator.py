"""
Project Configuration Validator
Validates technology combinations and compliance requirements
"""

from typing import Dict, List, Any
from shutil import which
import subprocess


class ProjectValidator:
    """Validates project configurations for compatibility and best practices"""
    
    def __init__(self):
        self.compatibility_matrix = self._load_compatibility_matrix()
        self.compliance_requirements = self._load_compliance_requirements()
    
    def _load_compatibility_matrix(self) -> Dict[str, Dict[str, List[str]]]:
        """Define technology compatibility rules"""
        return {
            'frontend': {
                'nextjs': {
                    'backend': ['fastapi', 'django', 'nestjs', 'go', 'none'],
                    'auth': ['auth0', 'firebase', 'cognito', 'custom'],
                    'deploy': ['vercel', 'aws', 'azure', 'gcp']
                },
                'nuxt': {
                    'backend': ['fastapi', 'django', 'nestjs', 'go', 'none'],
                    'auth': ['auth0', 'firebase', 'cognito', 'custom'],
                    'deploy': ['vercel', 'aws', 'azure', 'gcp']
                },
                'angular': {
                    'backend': ['fastapi', 'django', 'nestjs', 'go'],
                    'auth': ['auth0', 'cognito', 'custom'],
                    'deploy': ['aws', 'azure', 'gcp']
                },
                'expo': {
                    'backend': ['fastapi', 'django', 'nestjs', 'go'],
                    'auth': ['auth0', 'firebase', 'cognito'],
                    'deploy': ['aws', 'azure', 'gcp']
                }
            },
            'backend': {
                'fastapi': {
                    'database': ['postgres', 'mongodb'],
                    'deploy': ['aws', 'azure', 'gcp', 'self-hosted']
                },
                'django': {
                    'database': ['postgres', 'mongodb'],
                    'deploy': ['aws', 'azure', 'gcp', 'self-hosted']
                },
                'nestjs': {
                    'database': ['postgres', 'mongodb'],
                    'deploy': ['aws', 'azure', 'gcp', 'self-hosted']
                },
                'go': {
                    'database': ['postgres', 'mongodb'],
                    'deploy': ['aws', 'azure', 'gcp', 'self-hosted']
                }
            },
            'project_type': {
                'web': {
                    'required': ['frontend'],
                    'optional': ['backend', 'database', 'auth']
                },
                'mobile': {
                    'required': ['frontend'],
                    'frontend_allowed': ['expo'],
                    'optional': ['backend', 'database', 'auth']
                },
                'api': {
                    'required': ['backend'],
                    'optional': ['database', 'auth'],
                    'excluded': ['frontend']
                },
                'fullstack': {
                    'required': ['frontend', 'backend'],
                    'optional': ['database', 'auth']
                },
                'microservices': {
                    'required': ['backend'],
                    'optional': ['frontend', 'database', 'auth']
                }
            }
        }
    
    def _load_compliance_requirements(self) -> Dict[str, Dict[str, Any]]:
        """Define compliance-specific requirements"""
        return {
            'hipaa': {
                'required_features': ['encryption', 'audit_logging', 'access_control'],
                'required_auth': ['auth0', 'cognito'],
                'deploy_allowed': ['aws', 'azure'],
                'warnings': ['Requires BAA with cloud provider', 'PHI data handling procedures needed']
            },
            'gdpr': {
                'required_features': ['data_privacy', 'consent_management', 'data_deletion'],
                'warnings': ['Privacy policy required', 'Data processing agreements needed']
            },
            'sox': {
                'required_features': ['audit_trails', 'access_control', 'change_management'],
                'required_auth': ['cognito', 'auth0'],
                'warnings': ['Financial controls documentation required']
            },
            'pci': {
                'required_features': ['encryption', 'tokenization', 'secure_storage'],
                'warnings': ['PCI DSS assessment required', 'Network segmentation needed']
            },
            'soc2': {
                'required_features': ['security_monitoring', 'access_control', 'audit_logging'],
                'warnings': ['Security policies required', 'Regular audits needed']
            }
        }
    
    def validate_configuration(self, args) -> Dict[str, Any]:
        """Validate the entire project configuration"""
        errors = []
        warnings = []
        
        # Validate project type requirements
        project_rules = self.compatibility_matrix['project_type'].get(args.project_type, {})
        
        # Check required components
        for component in project_rules.get('required', []):
            if component == 'frontend' and args.frontend == 'none':
                errors.append(f"Project type '{args.project_type}' requires a frontend framework")
            elif component == 'backend' and args.backend == 'none':
                errors.append(f"Project type '{args.project_type}' requires a backend framework")
        
        # Check excluded components
        for component in project_rules.get('excluded', []):
            if component == 'frontend' and args.frontend != 'none':
                errors.append(f"Project type '{args.project_type}' should not have a frontend framework")
        
        # Validate frontend compatibility
        if args.frontend != 'none':
            frontend_rules = self.compatibility_matrix['frontend'].get(args.frontend, {})
            
            # Check backend compatibility
            if args.backend != 'none' and args.backend not in frontend_rules.get('backend', []):
                warnings.append(f"Frontend '{args.frontend}' may have compatibility issues with backend '{args.backend}'")
            
            # Check auth compatibility
            if args.auth != 'none' and args.auth not in frontend_rules.get('auth', []):
                warnings.append(f"Frontend '{args.frontend}' may have limited support for auth '{args.auth}'")
            
            # Check deployment compatibility
            if args.deploy not in frontend_rules.get('deploy', []):
                warnings.append(f"Frontend '{args.frontend}' may require additional configuration for deployment to '{args.deploy}'")
        
        # Validate backend compatibility
        if args.backend != 'none':
            backend_rules = self.compatibility_matrix['backend'].get(args.backend, {})
            
            # Check database compatibility
            if args.database != 'none' and args.database not in backend_rules.get('database', []):
                warnings.append(f"Backend '{args.backend}' may have limited support for database '{args.database}'")
        
        # Validate compliance requirements
        if args.compliance:
            compliance_list = [c.strip().lower() for c in args.compliance.split(',')]
            
            for compliance in compliance_list:
                if compliance in self.compliance_requirements:
                    req = self.compliance_requirements[compliance]
                    
                    # Check required auth
                    if 'required_auth' in req and args.auth not in req['required_auth']:
                        errors.append(f"Compliance '{compliance}' requires auth provider: {', '.join(req['required_auth'])}")
                    
                    # Check allowed deployment
                    if 'deploy_allowed' in req and args.deploy not in req['deploy_allowed']:
                        errors.append(f"Compliance '{compliance}' only allows deployment to: {', '.join(req['deploy_allowed'])}")
                    
                    # Add compliance warnings
                    warnings.extend([f"{compliance.upper()}: {w}" for w in req.get('warnings', [])])
                else:
                    warnings.append(f"Unknown compliance requirement: {compliance}")
        
        # Industry-specific validations
        if args.industry == 'healthcare' and 'hipaa' not in (args.compliance or ''):
            warnings.append("Healthcare projects typically require HIPAA compliance")
        
        if args.industry == 'finance' and not any(c in (args.compliance or '') for c in ['sox', 'pci']):
            warnings.append("Financial projects typically require SOX or PCI compliance")
        
        return {
            'valid': len(errors) == 0,
            'errors': errors,
            'warnings': warnings
        }
    
    def get_required_features(self, compliance: str) -> List[str]:
        """Get required features for a compliance standard"""
        return self.compliance_requirements.get(
            compliance.lower(), {}
        ).get('required_features', [])
    
    def validate_comprehensive(self, args) -> Dict[str, Any]:
        """Comprehensive validation: tech compatibility + features + compliance + system deps"""
        errors = []
        warnings = []
        
        # 1. Tech-stack compatibility checks
        config_result = self.validate_configuration(args)
        errors.extend(config_result['errors'])
        warnings.extend(config_result['warnings'])
        
        # 2. Feature prerequisite checks
        if args.features:
            feature_errors, feature_warnings = self._validate_features(args)
            errors.extend(feature_errors)
            warnings.extend(feature_warnings)
        
        # 3. Compliance prerequisites
        if args.compliance:
            comp_errors, comp_warnings = self._validate_compliance_prerequisites(args)
            errors.extend(comp_errors)
            warnings.extend(comp_warnings)
        
        # 4. System dependency checks (allow override via --skip-system-checks or --dry-run)
        skip_checks = bool(getattr(args, 'skip_system_checks', False))
        if not getattr(args, 'dry_run', False) and not skip_checks:
            sys_errors, sys_warnings = self._validate_system_dependencies(args)
            errors.extend(sys_errors)
            warnings.extend(sys_warnings)
        
        return {
            'valid': len(errors) == 0,
            'errors': errors,
            'warnings': warnings
        }
    
    def _validate_features(self, args) -> tuple[List[str], List[str]]:
        """Validate feature prerequisites"""
        errors = []
        warnings = []
        
        features = [f.strip().lower() for f in args.features.split(',') if f.strip()]
        
        for feature in features:
            if feature == 'realtime':
                if args.database == 'none':
                    errors.append("Feature 'realtime' requires a database (Firebase or WebSocket support needed)")
                elif args.database not in ['firebase', 'mongodb']:
                    warnings.append("Feature 'realtime' works best with Firebase or MongoDB (change streams)")
            
            elif feature == 'offline_sync':
                if args.frontend == 'none':
                    errors.append("Feature 'offline_sync' requires a frontend framework")
                if args.database not in ['firebase', 'mongodb']:
                    warnings.append("Feature 'offline_sync' requires client-side database support (Firebase/MongoDB recommended)")
            
            elif feature == 'push_notifications':
                if args.frontend not in ['expo', 'nextjs', 'nuxt']:
                    warnings.append("Feature 'push_notifications' requires mobile (Expo) or web push support")
            
            elif feature == 'file_upload':
                if args.backend == 'none':
                    errors.append("Feature 'file_upload' requires a backend framework")
                if args.deploy == 'vercel':
                    warnings.append("Feature 'file_upload' on Vercel has size/duration limits; consider cloud storage")
            
            elif feature == 'analytics':
                if args.frontend == 'none':
                    errors.append("Feature 'analytics' requires a frontend framework")
        
        return errors, warnings
    
    def _validate_compliance_prerequisites(self, args) -> tuple[List[str], List[str]]:
        """Validate compliance prerequisites beyond basic auth/deploy checks"""
        errors = []
        warnings = []
        
        compliance_list = [c.strip().lower() for c in args.compliance.split(',')]
        
        for compliance in compliance_list:
            if compliance == 'hipaa':
                if args.backend == 'none':
                    errors.append("HIPAA compliance requires audit logging - backend framework needed")
                if args.database == 'none':
                    warnings.append("HIPAA compliance typically requires encrypted database storage")
            
            elif compliance == 'sox':
                if args.backend == 'none':
                    errors.append("SOX compliance requires audit trails and change management - backend framework needed")
                if args.database == 'none':
                    warnings.append("SOX compliance requires audit trail storage - database recommended")
            
            elif compliance == 'pci':
                if args.backend == 'none':
                    errors.append("PCI DSS compliance requires secure payment processing - backend framework needed")
                if args.auth == 'none':
                    warnings.append("PCI DSS typically requires strong authentication for cardholder data access")
            
            elif compliance == 'gdpr':
                if args.backend == 'none':
                    warnings.append("GDPR compliance features (data export, deletion) typically require backend APIs")
        
        return errors, warnings
    
    def _validate_system_dependencies(self, args) -> tuple[List[str], List[str]]:
        """Validate required system dependencies are available"""
        errors = []
        warnings = []
        
        # Always required (skip hard-block on dry-run)
        dry_run_flag = (getattr(args, 'dry_run', False) is True)
        if which('docker') is None:
            if dry_run_flag:
                warnings.append("Docker not found; proceeding due to --dry-run")
            else:
                errors.append("Docker is required for development environment (install from https://docker.com)")
        
        # Frontend dependencies
        if args.frontend != 'none' or args.backend == 'nestjs':
            if which('node') is None:
                errors.append("Node.js 18+ is required (install from https://nodejs.org)")
            else:
                # Check Node version if possible
                try:
                    result = subprocess.run(['node', '--version'], capture_output=True, text=True, timeout=5)
                    if result.returncode == 0:
                        version = result.stdout.strip().lstrip('v')
                        major_version = int(version.split('.')[0]) if version else 0
                        if major_version < 18:
                            warnings.append(f"Node.js {version} detected; Node.js 18+ recommended")
                except (subprocess.TimeoutExpired, ValueError, FileNotFoundError):
                    pass
            
            if which('npm') is None:
                errors.append("npm is required for Node.js projects (usually bundled with Node.js)")
        
        # Python backends
        if args.backend in ['fastapi', 'django']:
            python_cmd = 'python3' if which('python3') else ('python' if which('python') else None)
            if python_cmd is None:
                errors.append("Python 3.11+ is required for Python backends (install from https://python.org)")
            else:
                # Check Python version if possible
                try:
                    result = subprocess.run([python_cmd, '--version'], capture_output=True, text=True, timeout=5)
                    if result.returncode == 0:
                        version_line = result.stdout.strip()
                        if 'Python' in version_line:
                            version = version_line.split()[1]
                            major, minor = map(int, version.split('.')[:2])
                            if major < 3 or (major == 3 and minor < 11):
                                warnings.append(f"Python {version} detected; Python 3.11+ recommended")
                except (subprocess.TimeoutExpired, ValueError, FileNotFoundError, IndexError):
                    pass
            
            if which('pip') is None and which('pip3') is None:
                warnings.append("pip/pip3 not found; ensure virtualenv can install requirements")
        
        # Go backend
        if args.backend == 'go':
            if which('go') is None:
                errors.append("Go 1.21+ is required for Go backends (install from https://golang.org)")
            else:
                # Check Go version if possible
                try:
                    result = subprocess.run(['go', 'version'], capture_output=True, text=True, timeout=5)
                    if result.returncode == 0:
                        version_line = result.stdout.strip()
                        if 'go' in version_line:
                            version = version_line.split()[2].lstrip('go')
                            major, minor = map(int, version.split('.')[:2])
                            if major < 1 or (major == 1 and minor < 21):
                                warnings.append(f"Go {version} detected; Go 1.21+ recommended")
                except (subprocess.TimeoutExpired, ValueError, FileNotFoundError, IndexError):
                    pass
        
        return errors, warnings
    
    def validate_config(self, config: Dict[str, Any]) -> tuple[bool, List[str]]:
        """Validate configuration dictionary format (for tests)"""
        errors = []
        
        # Required fields
        required_fields = ['name', 'industry', 'project_type']
        for field in required_fields:
            if field not in config or not config[field]:
                errors.append(f"Missing required field: {field}")
        
        # Validate individual fields
        if 'name' in config and not self.validate_project_name(config['name']):
            errors.append("Invalid project name")
        
        if 'industry' in config and not self.validate_industry(config['industry']):
            errors.append("Invalid industry")
        
        if 'project_type' in config and not self.validate_project_type(config['project_type']):
            errors.append("Invalid project_type")
        
        # Validate technology compatibility
        if all(k in config for k in ['project_type', 'frontend', 'backend']):
            if not self.validate_technology_compatibility(
                config['project_type'], 
                config.get('frontend'), 
                config.get('backend')
            ):
                errors.append("Invalid technology compatibility")
        
        # Validate individual technology fields
        if 'frontend' in config and config['frontend'] and config['frontend'] != 'none':
            valid_frontends = {'nextjs', 'nuxt', 'angular', 'expo'}
            if config['frontend'].lower() not in valid_frontends:
                errors.append("Invalid frontend framework")
        
        if 'backend' in config and config['backend'] and config['backend'] != 'none':
            valid_backends = {'fastapi', 'django', 'nestjs', 'go'}
            if config['backend'].lower() not in valid_backends:
                errors.append("Invalid backend framework")
        
        if 'database' in config and config['database'] and config['database'] != 'none':
            valid_databases = {'postgres', 'mongodb', 'firebase'}
            if config['database'].lower() not in valid_databases:
                errors.append("Invalid database")
        
        if 'auth' in config and config['auth'] and config['auth'] != 'none':
            valid_auths = {'auth0', 'firebase', 'cognito', 'custom'}
            if config['auth'].lower() not in valid_auths:
                errors.append("Invalid auth provider")
        
        if 'deploy' in config and config['deploy']:
            valid_deploys = {'aws', 'azure', 'gcp', 'vercel', 'self-hosted'}
            if config['deploy'].lower() not in valid_deploys:
                errors.append("Invalid deployment target")
        
        # Validate compliance-industry match
        if 'industry' in config and 'compliance' in config and config['compliance']:
            # Handle both list and string compliance
            if isinstance(config['compliance'], list):
                compliance_list = config['compliance']
            else:
                compliance_list = [c.strip() for c in config['compliance'].split(',')]
            
            # Validate compliance values
            valid_compliance = {'hipaa', 'gdpr', 'sox', 'pci', 'soc2'}
            for compliance in compliance_list:
                if compliance.lower() not in valid_compliance:
                    errors.append("Invalid compliance standard")
                    break
            
            if not self.validate_compliance_industry_match(config['industry'], compliance_list):
                errors.append("Compliance standards don't match industry")
        
        return len(errors) == 0, errors
    
    def validate_project_name(self, name: str) -> bool:
        """Validate project name format"""
        if not name or not name.strip():
            return False
        
        # Allow alphanumeric, hyphens, underscores
        import re
        return bool(re.match(r'^[a-zA-Z0-9_-]+$', name.strip()))
    
    def validate_industry(self, industry: str) -> bool:
        """Validate industry value"""
        valid_industries = {'healthcare', 'finance', 'ecommerce', 'saas', 'enterprise'}
        return industry.lower() in valid_industries
    
    def validate_project_type(self, project_type: str) -> bool:
        """Validate project type value"""
        valid_types = {'web', 'mobile', 'api', 'fullstack', 'microservices'}
        return project_type.lower() in valid_types
    
    def validate_technology_compatibility(self, project_type: str, frontend: str, backend: str) -> bool:
        """Validate technology stack compatibility"""
        project_type = project_type.lower() if project_type else ''
        frontend = frontend.lower() if frontend else 'none'
        backend = backend.lower() if backend else 'none'
        
        # Mobile projects should use expo
        if project_type == 'mobile' and frontend not in ['expo', 'none']:
            return False
        
        # Web projects shouldn't use expo
        if project_type == 'web' and frontend == 'expo':
            return False
        
        # API projects shouldn't have frontend
        if project_type == 'api' and frontend != 'none':
            return False
        
        return True
    
    def validate_compliance_industry_match(self, industry: str, compliance_list: List[str]) -> bool:
        """Validate compliance standards match industry"""
        industry = industry.lower() if industry else ''
        compliance_set = {c.lower() for c in compliance_list}
        
        # Healthcare should use HIPAA
        if industry == 'healthcare' and compliance_set and 'hipaa' not in compliance_set:
            return False
        
        # Finance should use SOX/PCI
        if industry == 'finance' and compliance_set and not compliance_set.intersection({'sox', 'pci'}):
            return False
        
        # Non-healthcare shouldn't use HIPAA
        if industry != 'healthcare' and 'hipaa' in compliance_set:
            return False
        
        return True
    
    def get_validation_errors(self, field: str, error_type: str) -> str:
        """Get validation error message for field and error type"""
        error_messages = {
            'name': {
                'empty': 'Project name cannot be empty',
                'invalid': 'Project name contains invalid characters'
            },
            'industry': {
                'invalid': 'Invalid industry selection'
            },
            'project_type': {
                'invalid': 'Invalid project type selection'
            }
        }
        
        return error_messages.get(field, {}).get(error_type, f"Validation error in {field}: {error_type}")