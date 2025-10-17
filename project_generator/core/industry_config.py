"""
Industry-Specific Configuration
Provides industry-specific defaults and requirements
"""

from typing import Dict, List, Any, Optional


class IndustryConfig:
    """Manages industry-specific configurations and requirements"""
    
    def __init__(self, industry: str):
        self.industry = industry
        self.configs = self._load_industry_configs()
        self.current_config = self.configs.get(industry, {})
    
    def _load_industry_configs(self) -> Dict[str, Dict[str, Any]]:
        """Load industry-specific configurations"""
        return {
            'healthcare': {
                'name': 'Healthcare',
                'default_features': [
                    'patient_portal',
                    'appointment_scheduling', 
                    'secure_messaging',
                    'medical_records',
                    'telehealth'
                ],
                'required_features': [
                    'audit_logging',
                    'encryption',
                    'access_control',
                    'data_backup'
                ],
                'compliance': ['hipaa'],
                'recommended_stack': {
                    'frontend': 'nextjs',
                    'backend': 'fastapi',
                    'database': 'postgres',
                    'auth': 'auth0',
                    'deploy': 'aws'
                },
                'security_requirements': {
                    'encryption_at_rest': True,
                    'encryption_in_transit': True,
                    'mfa_required': True,
                    'session_timeout': 15,  # minutes
                    'password_complexity': 'high'
                },
                'templates': {
                    'models': ['patient', 'provider', 'appointment', 'medical_record'],
                    'apis': ['patient_api', 'provider_api', 'scheduling_api'],
                    'pages': ['dashboard', 'patient_list', 'appointment_calendar']
                }
            },
            'finance': {
                'name': 'Financial Services',
                'default_features': [
                    'account_management',
                    'transaction_processing',
                    'reporting',
                    'audit_trails',
                    'risk_assessment'
                ],
                'required_features': [
                    'audit_logging',
                    'encryption',
                    'fraud_detection',
                    'regulatory_reporting'
                ],
                'compliance': ['sox', 'pci'],
                'recommended_stack': {
                    'frontend': 'angular',
                    'backend': 'go',
                    'database': 'postgres',
                    'auth': 'cognito',
                    'deploy': 'aws'
                },
                'security_requirements': {
                    'encryption_at_rest': True,
                    'encryption_in_transit': True,
                    'mfa_required': True,
                    'session_timeout': 10,
                    'password_complexity': 'maximum'
                },
                'templates': {
                    'models': ['account', 'transaction', 'user', 'audit_log'],
                    'apis': ['account_api', 'transaction_api', 'reporting_api'],
                    'pages': ['dashboard', 'accounts', 'transactions', 'reports']
                }
            },
            'ecommerce': {
                'name': 'E-Commerce',
                'default_features': [
                    'product_catalog',
                    'shopping_cart',
                    'checkout',
                    'order_management',
                    'inventory',
                    'reviews'
                ],
                'required_features': [
                    'payment_processing',
                    'secure_checkout',
                    'order_tracking'
                ],
                'compliance': ['pci', 'gdpr'],
                'recommended_stack': {
                    'frontend': 'nextjs',
                    'backend': 'django',
                    'database': 'postgres',
                    'auth': 'firebase',
                    'deploy': 'vercel'
                },
                'security_requirements': {
                    'encryption_at_rest': True,
                    'encryption_in_transit': True,
                    'mfa_required': False,
                    'session_timeout': 30,
                    'password_complexity': 'medium'
                },
                'templates': {
                    'models': ['product', 'order', 'cart', 'customer', 'inventory'],
                    'apis': ['product_api', 'order_api', 'cart_api', 'payment_api'],
                    'pages': ['home', 'product_list', 'product_detail', 'cart', 'checkout']
                }
            },
            'saas': {
                'name': 'Software as a Service',
                'default_features': [
                    'user_management',
                    'subscription_billing',
                    'multi_tenancy',
                    'admin_dashboard',
                    'api_access'
                ],
                'required_features': [
                    'authentication',
                    'authorization',
                    'usage_tracking'
                ],
                'compliance': ['soc2', 'gdpr'],
                'recommended_stack': {
                    'frontend': 'nextjs',
                    'backend': 'nestjs',
                    'database': 'postgres',
                    'auth': 'auth0',
                    'deploy': 'aws'
                },
                'security_requirements': {
                    'encryption_at_rest': True,
                    'encryption_in_transit': True,
                    'mfa_required': True,
                    'session_timeout': 60,
                    'password_complexity': 'high'
                },
                'templates': {
                    'models': ['organization', 'user', 'subscription', 'usage'],
                    'apis': ['auth_api', 'organization_api', 'billing_api'],
                    'pages': ['dashboard', 'settings', 'billing', 'team']
                }
            },
            'enterprise': {
                'name': 'Enterprise',
                'default_features': [
                    'sso_integration',
                    'role_based_access',
                    'audit_logging',
                    'api_gateway',
                    'reporting'
                ],
                'required_features': [
                    'enterprise_auth',
                    'compliance_reporting',
                    'data_governance'
                ],
                'compliance': ['soc2'],
                'recommended_stack': {
                    'frontend': 'angular',
                    'backend': 'nestjs',
                    'database': 'postgres',
                    'auth': 'cognito',
                    'deploy': 'azure'
                },
                'security_requirements': {
                    'encryption_at_rest': True,
                    'encryption_in_transit': True,
                    'mfa_required': True,
                    'session_timeout': 30,
                    'password_complexity': 'high'
                },
                'templates': {
                    'models': ['organization', 'department', 'user', 'role', 'permission'],
                    'apis': ['user_api', 'role_api', 'audit_api'],
                    'pages': ['dashboard', 'users', 'roles', 'audit_logs']
                }
            }
        }
    
    def get_default_features(self) -> List[str]:
        """Get default features for the industry"""
        return self.current_config.get('default_features', [])
    
    def get_required_features(self) -> List[str]:
        """Get required features for the industry"""
        return self.current_config.get('required_features', [])
    
    def get_recommended_stack(self) -> Dict[str, str]:
        """Get recommended technology stack for the industry"""
        return self.current_config.get('recommended_stack', {})
    
    def get_compliance_requirements(self) -> List[str]:
        """Get compliance requirements for the industry"""
        return self.current_config.get('compliance', [])
    
    def get_security_requirements(self) -> Dict[str, Any]:
        """Get security requirements for the industry"""
        return self.current_config.get('security_requirements', {})
    
    def get_template_suggestions(self) -> Dict[str, List[str]]:
        """Get suggested templates for the industry"""
        return self.current_config.get('templates', {})
    
    def merge_features(self, user_features: Optional[str]) -> List[str]:
        """Merge user-specified features with industry defaults"""
        default_features = set(self.get_default_features())
        required_features = set(self.get_required_features())
        
        if user_features:
            user_feature_list = [f.strip() for f in user_features.split(',')]
            default_features.update(user_feature_list)
        
        # Always include required features
        all_features = default_features.union(required_features)
        
        return sorted(list(all_features))