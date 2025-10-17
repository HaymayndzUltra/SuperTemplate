"""
Unit tests for comprehensive validation
"""

import pytest
from unittest.mock import Mock, patch
from project_generator.core.validator import ProjectValidator


class TestComprehensiveValidation:
    """Test comprehensive validation functionality"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.validator = ProjectValidator()
        self.base_args = Mock(
            project_type='fullstack',
            frontend='nextjs',
            backend='django',
            database='postgres',
            auth='auth0',
            deploy='aws',
            industry='healthcare',
            compliance='hipaa',
            features=None
        )
    
    @patch('project_generator.core.validator.subprocess.run')
    @patch('project_generator.core.validator.which')
    def test_valid_fullstack_configuration(self, mock_which, mock_run):
        """Test valid fullstack configuration passes (mock system deps)"""
        # Simulate required CLIs present
        mock_which.side_effect = lambda cmd: f"/usr/bin/{cmd}"

        # Simulate modern Node and Python versions
        def _run_side_effect(args, **kwargs):
            cmd = args[0] if isinstance(args, (list, tuple)) else args
            if isinstance(cmd, (list, tuple)) and cmd and 'node' in cmd[0]:
                return Mock(returncode=0, stdout='v18.19.0')
            if isinstance(cmd, (list, tuple)) and cmd and 'python' in cmd[0]:
                return Mock(returncode=0, stdout='Python 3.11.0')
            return Mock(returncode=0, stdout='')

        mock_run.side_effect = _run_side_effect

        result = self.validator.validate_comprehensive(self.base_args)
        assert result['valid'] is True
        assert len(result['errors']) == 0
    
    def test_fullstack_requires_frontend_and_backend(self):
        """Test fullstack project type requires both frontend and backend"""
        args = Mock(
            project_type='fullstack',
            frontend='none',
            backend='django',
            database='postgres',
            auth='auth0',
            deploy='aws',
            industry='healthcare',
            compliance=None,
            features=None
        )
        
        result = self.validator.validate_comprehensive(args)
        assert result['valid'] == False
        assert any('requires a frontend framework' in error for error in result['errors'])
        
        args.frontend = 'nextjs'
        args.backend = 'none'
        
        result = self.validator.validate_comprehensive(args)
        assert result['valid'] == False
        assert any('requires a backend framework' in error for error in result['errors'])
    
    def test_api_project_excludes_frontend(self):
        """Test API project type should not have frontend"""
        args = Mock(
            project_type='api',
            frontend='nextjs',
            backend='django',
            database='postgres',
            auth='auth0',
            deploy='aws',
            industry='healthcare',
            compliance=None,
            features=None
        )
        
        result = self.validator.validate_comprehensive(args)
        assert result['valid'] == False
        assert any('should not have a frontend framework' in error for error in result['errors'])
    
    def test_realtime_feature_requires_database(self):
        """Test realtime feature requires database"""
        args = Mock(
            project_type='fullstack',
            frontend='nextjs',
            backend='django',
            database='none',
            auth='auth0',
            deploy='aws',
            industry='healthcare',
            compliance=None,
            features='realtime'
        )
        
        result = self.validator.validate_comprehensive(args)
        assert result['valid'] == False
        assert any('realtime' in error and 'database' in error for error in result['errors'])
    
    def test_offline_sync_feature_requires_frontend(self):
        """Test offline_sync feature requires frontend"""
        args = Mock(
            project_type='api',
            frontend='none',
            backend='django',
            database='postgres',
            auth='auth0',
            deploy='aws',
            industry='healthcare',
            compliance=None,
            features='offline_sync'
        )
        
        result = self.validator.validate_comprehensive(args)
        assert result['valid'] == False
        assert any('offline_sync' in error and 'frontend framework' in error for error in result['errors'])
    
    def test_file_upload_feature_requires_backend(self):
        """Test file_upload feature requires backend"""
        args = Mock(
            project_type='web',
            frontend='nextjs',
            backend='none',
            database='none',
            auth='none',
            deploy='vercel',
            industry='healthcare',
            compliance=None,
            features='file_upload'
        )
        
        result = self.validator.validate_comprehensive(args)
        assert result['valid'] == False
        assert any('file_upload' in error and 'backend framework' in error for error in result['errors'])
    
    def test_hipaa_compliance_requires_backend(self):
        """Test HIPAA compliance requires backend for audit logging"""
        args = Mock(
            project_type='web',
            frontend='nextjs',
            backend='none',
            database='none',
            auth='auth0',
            deploy='aws',
            industry='healthcare',
            compliance='hipaa',
            features=None
        )
        
        result = self.validator.validate_comprehensive(args)
        assert result['valid'] == False
        assert any('HIPAA' in error and 'audit logging' in error for error in result['errors'])
    
    def test_sox_compliance_requires_backend(self):
        """Test SOX compliance requires backend for audit trails"""
        args = Mock(
            project_type='web',
            frontend='nextjs',
            backend='none',
            database='none',
            auth='auth0',
            deploy='aws',
            industry='finance',
            compliance='sox',
            features=None
        )
        
        result = self.validator.validate_comprehensive(args)
        assert result['valid'] == False
        assert any('SOX' in error and 'audit trails' in error for error in result['errors'])
    
    def test_pci_compliance_requires_backend(self):
        """Test PCI compliance requires backend for secure payment processing"""
        args = Mock(
            project_type='web',
            frontend='nextjs',
            backend='none',
            database='none',
            auth='none',
            deploy='aws',
            industry='ecommerce',
            compliance='pci',
            features=None
        )
        
        result = self.validator.validate_comprehensive(args)
        assert result['valid'] == False
        assert any('PCI DSS' in error and 'secure payment processing' in error for error in result['errors'])
    
    @patch('project_generator.core.validator.which')
    def test_system_dependencies_docker_missing(self, mock_which):
        """Test system dependency validation fails when Docker is missing"""
        mock_which.side_effect = lambda cmd: None if cmd == 'docker' else '/usr/bin/' + cmd
        
        result = self.validator.validate_comprehensive(self.base_args)
        assert result['valid'] == False
        assert any('Docker is required' in error for error in result['errors'])
    
    @patch('project_generator.core.validator.which')
    def test_system_dependencies_node_missing_for_frontend(self, mock_which):
        """Test Node.js is required for frontend projects"""
        mock_which.side_effect = lambda cmd: None if cmd == 'node' else '/usr/bin/' + cmd
        
        result = self.validator.validate_comprehensive(self.base_args)
        assert result['valid'] == False
        assert any('Node.js 18+ is required' in error for error in result['errors'])
    
    @patch('project_generator.core.validator.which')
    @patch('project_generator.core.validator.subprocess.run')
    def test_system_dependencies_python_version_check(self, mock_run, mock_which):
        """Test Python version check warns for old versions"""
        mock_which.side_effect = lambda cmd: '/usr/bin/' + cmd if cmd != 'go' else None
        mock_run.return_value = Mock(returncode=0, stdout='Python 3.9.0')
        
        args = Mock(
            project_type='api',
            frontend='none',
            backend='django',
            database='postgres',
            auth='auth0',
            deploy='aws',
            industry='healthcare',
            compliance=None,
            features=None
        )
        
        result = self.validator.validate_comprehensive(args)
        assert any('Python 3.9.0 detected; Python 3.11+ recommended' in warning for warning in result['warnings'])
    
    @patch('project_generator.core.validator.subprocess.run')
    @patch('project_generator.core.validator.which')
    def test_multiple_features_validation(self, mock_which, mock_run):
        """Test validation with multiple features: should pass with at most warnings."""
        # Simulate required CLIs present
        mock_which.side_effect = lambda cmd: f"/usr/bin/{cmd}"

        # Simulate modern Node and Python versions
        def _run_side_effect(args, **kwargs):
            cmd = args[0] if isinstance(args, (list, tuple)) else args
            if isinstance(cmd, (list, tuple)) and cmd and 'node' in cmd[0]:
                return Mock(returncode=0, stdout='v18.19.0')
            if isinstance(cmd, (list, tuple)) and cmd and 'python' in cmd[0]:
                return Mock(returncode=0, stdout='Python 3.11.0')
            return Mock(returncode=0, stdout='')

        mock_run.side_effect = _run_side_effect

        args = Mock(
            project_type='fullstack',
            frontend='nextjs',
            backend='django',
            database='postgres',
            auth='auth0',
            deploy='aws',
            industry='healthcare',
            compliance=None,
            features='realtime,file_upload,analytics'
        )
        
        result = self.validator.validate_comprehensive(args)
        # Postgres makes 'realtime' emit a warning (recommended firebase/mongodb), but not an error
        assert result['valid'] is True
        assert all('requires' not in e for e in result['errors'])
    
    def test_incompatible_feature_combination(self):
        """Test incompatible feature combination"""
        args = Mock(
            project_type='api',
            frontend='none',
            backend='django',
            database='none',
            auth='none',
            deploy='aws',
            industry='healthcare',
            compliance=None,
            features='realtime,offline_sync,analytics'
        )
        
        result = self.validator.validate_comprehensive(args)
        assert result['valid'] == False
        # Should have errors for realtime (no database), offline_sync (no frontend), analytics (no frontend)
        assert len([e for e in result['errors'] if 'realtime' in e]) > 0
        assert len([e for e in result['errors'] if 'offline_sync' in e]) > 0
        assert len([e for e in result['errors'] if 'analytics' in e]) > 0


class TestFeatureValidation:
    """Test feature-specific validation logic"""
    
    def setup_method(self):
        self.validator = ProjectValidator()
    
    def test_push_notifications_warning_for_unsupported_frontend(self):
        """Test push notifications warns for unsupported frontend"""
        args = Mock(
            project_type='web',
            frontend='angular',
            backend='django',
            database='postgres',
            auth='auth0',
            deploy='aws',
            industry='healthcare',
            compliance=None,
            features='push_notifications'
        )
        
        result = self.validator.validate_comprehensive(args)
        assert any('push_notifications' in warning and 'mobile' in warning for warning in result['warnings'])
    
    def test_file_upload_vercel_warning(self):
        """Test file upload warns about Vercel limitations"""
        args = Mock(
            project_type='fullstack',
            frontend='nextjs',
            backend='django',
            database='postgres',
            auth='auth0',
            deploy='vercel',
            industry='healthcare',
            compliance=None,
            features='file_upload'
        )
        
        result = self.validator.validate_comprehensive(args)
        assert any('file_upload' in warning and 'Vercel' in warning for warning in result['warnings'])


if __name__ == '__main__':
    pytest.main([__file__])
