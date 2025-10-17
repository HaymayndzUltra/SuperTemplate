"""
Unit tests for ProjectValidator functionality
"""

import pytest
from project_generator.core.validator import ProjectValidator


class TestProjectValidator:
    """Test cases for ProjectValidator class"""

    def test_initialization(self):
        """Test ProjectValidator initialization"""
        validator = ProjectValidator()
        assert validator is not None

    def test_validate_config_valid(self):
        """Test validation with valid configuration"""
        validator = ProjectValidator()
        config = {
            'name': 'test-project',
            'industry': 'healthcare',
            'project_type': 'fullstack',
            'frontend': 'nextjs',
            'backend': 'fastapi',
            'database': 'postgres',
            'auth': 'auth0',
            'deploy': 'aws',
            'compliance': ['hipaa'],
            'features': ['patient-portal']
        }
        
        is_valid, errors = validator.validate_config(config)
        
        assert is_valid is True
        assert errors == []

    def test_validate_config_missing_required_fields(self):
        """Test validation with missing required fields"""
        validator = ProjectValidator()
        config = {
            'name': 'test-project',
            'industry': 'healthcare'
            # Missing project_type
        }
        
        is_valid, errors = validator.validate_config(config)
        
        assert is_valid is False
        assert 'project_type' in str(errors)

    def test_validate_config_invalid_industry(self):
        """Test validation with invalid industry"""
        validator = ProjectValidator()
        config = {
            'name': 'test-project',
            'industry': 'invalid-industry',
            'project_type': 'fullstack'
        }
        
        is_valid, errors = validator.validate_config(config)
        
        assert is_valid is False
        assert 'industry' in str(errors)

    def test_validate_config_invalid_project_type(self):
        """Test validation with invalid project type"""
        validator = ProjectValidator()
        config = {
            'name': 'test-project',
            'industry': 'healthcare',
            'project_type': 'invalid-type'
        }
        
        is_valid, errors = validator.validate_config(config)
        
        assert is_valid is False
        assert 'project_type' in str(errors)

    def test_validate_config_invalid_frontend(self):
        """Test validation with invalid frontend framework"""
        validator = ProjectValidator()
        config = {
            'name': 'test-project',
            'industry': 'healthcare',
            'project_type': 'web',
            'frontend': 'invalid-frontend'
        }
        
        is_valid, errors = validator.validate_config(config)
        
        assert is_valid is False
        assert 'frontend' in str(errors)

    def test_validate_config_invalid_backend(self):
        """Test validation with invalid backend framework"""
        validator = ProjectValidator()
        config = {
            'name': 'test-project',
            'industry': 'healthcare',
            'project_type': 'api',
            'backend': 'invalid-backend'
        }
        
        is_valid, errors = validator.validate_config(config)
        
        assert is_valid is False
        assert 'backend' in str(errors)

    def test_validate_config_invalid_database(self):
        """Test validation with invalid database"""
        validator = ProjectValidator()
        config = {
            'name': 'test-project',
            'industry': 'healthcare',
            'project_type': 'fullstack',
            'frontend': 'nextjs',
            'backend': 'fastapi',
            'database': 'invalid-database'
        }
        
        is_valid, errors = validator.validate_config(config)
        
        assert is_valid is False
        assert 'database' in str(errors)

    def test_validate_config_invalid_auth(self):
        """Test validation with invalid auth provider"""
        validator = ProjectValidator()
        config = {
            'name': 'test-project',
            'industry': 'healthcare',
            'project_type': 'fullstack',
            'frontend': 'nextjs',
            'backend': 'fastapi',
            'database': 'postgres',
            'auth': 'invalid-auth'
        }
        
        is_valid, errors = validator.validate_config(config)
        
        assert is_valid is False
        assert 'auth' in str(errors)

    def test_validate_config_invalid_deploy(self):
        """Test validation with invalid deployment target"""
        validator = ProjectValidator()
        config = {
            'name': 'test-project',
            'industry': 'healthcare',
            'project_type': 'fullstack',
            'frontend': 'nextjs',
            'backend': 'fastapi',
            'database': 'postgres',
            'auth': 'auth0',
            'deploy': 'invalid-deploy'
        }
        
        is_valid, errors = validator.validate_config(config)
        
        assert is_valid is False
        assert 'deploy' in str(errors)

    def test_validate_config_invalid_compliance(self):
        """Test validation with invalid compliance standards"""
        validator = ProjectValidator()
        config = {
            'name': 'test-project',
            'industry': 'healthcare',
            'project_type': 'fullstack',
            'frontend': 'nextjs',
            'backend': 'fastapi',
            'database': 'postgres',
            'auth': 'auth0',
            'deploy': 'aws',
            'compliance': ['invalid-compliance']
        }
        
        is_valid, errors = validator.validate_config(config)
        
        assert is_valid is False
        assert 'compliance' in str(errors)

    def test_validate_config_empty_name(self):
        """Test validation with empty project name"""
        validator = ProjectValidator()
        config = {
            'name': '',
            'industry': 'healthcare',
            'project_type': 'fullstack'
        }
        
        is_valid, errors = validator.validate_config(config)
        
        assert is_valid is False
        assert 'name' in str(errors)

    def test_validate_config_invalid_name_characters(self):
        """Test validation with invalid project name characters"""
        validator = ProjectValidator()
        config = {
            'name': 'test@project!',
            'industry': 'healthcare',
            'project_type': 'fullstack'
        }
        
        is_valid, errors = validator.validate_config(config)
        
        assert is_valid is False
        assert 'name' in str(errors)

    def test_validate_config_technology_compatibility(self):
        """Test validation of technology compatibility"""
        validator = ProjectValidator()
        config = {
            'name': 'test-project',
            'industry': 'healthcare',
            'project_type': 'mobile',
            'frontend': 'nextjs',  # Next.js not suitable for mobile
            'backend': 'fastapi',
            'database': 'postgres',
            'auth': 'auth0',
            'deploy': 'aws'
        }
        
        is_valid, errors = validator.validate_config(config)
        
        assert is_valid is False
        assert 'compatibility' in str(errors)

    def test_validate_config_industry_compliance_mismatch(self):
        """Test validation of industry and compliance mismatch"""
        validator = ProjectValidator()
        config = {
            'name': 'test-project',
            'industry': 'healthcare',
            'project_type': 'fullstack',
            'frontend': 'nextjs',
            'backend': 'fastapi',
            'database': 'postgres',
            'auth': 'auth0',
            'deploy': 'aws',
            'compliance': ['pci']  # PCI not suitable for healthcare
        }
        
        is_valid, errors = validator.validate_config(config)
        
        assert is_valid is False
        assert 'compliance' in str(errors)

    def test_validate_config_multiple_errors(self):
        """Test validation with multiple errors"""
        validator = ProjectValidator()
        config = {
            'name': '',  # Empty name
            'industry': 'invalid',  # Invalid industry
            'project_type': 'invalid'  # Invalid project type
        }
        
        is_valid, errors = validator.validate_config(config)
        
        assert is_valid is False
        assert len(errors) >= 3

    def test_validate_project_name(self):
        """Test project name validation"""
        validator = ProjectValidator()
        
        # Valid names
        assert validator.validate_project_name('test-project') is True
        assert validator.validate_project_name('test123') is True
        assert validator.validate_project_name('test_project') is True
        
        # Invalid names
        assert validator.validate_project_name('') is False
        assert validator.validate_project_name('test@project') is False
        assert validator.validate_project_name('test project') is False
        assert validator.validate_project_name('test.project') is False

    def test_validate_industry(self):
        """Test industry validation"""
        validator = ProjectValidator()
        
        # Valid industries
        assert validator.validate_industry('healthcare') is True
        assert validator.validate_industry('finance') is True
        assert validator.validate_industry('ecommerce') is True
        assert validator.validate_industry('saas') is True
        assert validator.validate_industry('enterprise') is True
        
        # Invalid industries
        assert validator.validate_industry('invalid') is False
        assert validator.validate_industry('') is False

    def test_validate_project_type(self):
        """Test project type validation"""
        validator = ProjectValidator()
        
        # Valid project types
        assert validator.validate_project_type('web') is True
        assert validator.validate_project_type('mobile') is True
        assert validator.validate_project_type('api') is True
        assert validator.validate_project_type('fullstack') is True
        assert validator.validate_project_type('microservices') is True
        
        # Invalid project types
        assert validator.validate_project_type('invalid') is False
        assert validator.validate_project_type('') is False

    def test_validate_technology_compatibility(self):
        """Test technology compatibility validation"""
        validator = ProjectValidator()
        
        # Valid combinations
        assert validator.validate_technology_compatibility('web', 'nextjs', 'fastapi') is True
        assert validator.validate_technology_compatibility('mobile', 'expo', 'fastapi') is True
        assert validator.validate_technology_compatibility('api', None, 'fastapi') is True
        
        # Invalid combinations
        assert validator.validate_technology_compatibility('mobile', 'nextjs', 'fastapi') is False
        assert validator.validate_technology_compatibility('web', 'expo', 'fastapi') is False

    def test_validate_compliance_industry_match(self):
        """Test compliance and industry matching"""
        validator = ProjectValidator()
        
        # Valid matches
        assert validator.validate_compliance_industry_match('healthcare', ['hipaa']) is True
        assert validator.validate_compliance_industry_match('finance', ['sox', 'pci']) is True
        assert validator.validate_compliance_industry_match('ecommerce', ['pci', 'gdpr']) is True
        
        # Invalid matches
        assert validator.validate_compliance_industry_match('healthcare', ['pci']) is False
        assert validator.validate_compliance_industry_match('finance', ['hipaa']) is False

    def test_get_validation_errors(self):
        """Test getting validation error messages"""
        validator = ProjectValidator()
        
        errors = validator.get_validation_errors('name', 'empty')
        assert 'name' in errors.lower()
        assert 'empty' in errors.lower()
        
        errors = validator.get_validation_errors('industry', 'invalid')
        assert 'industry' in errors.lower()
        assert 'invalid' in errors.lower()

    def test_validate_config_with_optional_fields(self):
        """Test validation with optional fields"""
        validator = ProjectValidator()
        config = {
            'name': 'test-project',
            'industry': 'healthcare',
            'project_type': 'fullstack',
            'frontend': 'nextjs',
            'backend': 'fastapi',
            'database': 'postgres',
            'auth': 'auth0',
            'deploy': 'aws',
            'compliance': ['hipaa'],
            'features': ['patient-portal', 'appointment-scheduling'],
            'description': 'A test project',
            'version': '1.0.0'
        }
        
        is_valid, errors = validator.validate_config(config)
        
        assert is_valid is True
        assert errors == []

    def test_validate_config_minimal_valid(self):
        """Test validation with minimal valid configuration"""
        validator = ProjectValidator()
        config = {
            'name': 'test-project',
            'industry': 'healthcare',
            'project_type': 'web'
        }
        
        is_valid, errors = validator.validate_config(config)
        
        assert is_valid is True
        assert errors == []
