"""
Integration tests for full project generation flow
"""

import pytest
import subprocess
import time
from pathlib import Path
from unittest.mock import patch, Mock


class TestProjectGenerationFlow:
    """Integration tests for complete project generation"""

    def test_healthcare_fullstack_generation(self, temp_dir: Path):
        """Test generating a complete healthcare fullstack project"""
        from project_generator.core.generator import ProjectGenerator
        
        config = {
            'name': 'healthcare-demo',
            'industry': 'healthcare',
            'project_type': 'fullstack',
            'frontend': 'nextjs',
            'backend': 'fastapi',
            'database': 'postgres',
            'auth': 'auth0',
            'deploy': 'aws',
            'compliance': ['hipaa'],
            'features': ['patient-portal', 'appointment-scheduling']
        }
        
        generator = ProjectGenerator(
            output_dir=temp_dir,
            template_dir=Path(__file__).parent.parent.parent.parent / 'template-packs'
        )
        
        generator.set_config(config)
        
        # Mock external dependencies
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(returncode=0, stdout=b'', stderr=b'')
            
            result = generator.generate_project()
            
            assert result is True
            
            # Verify project structure was created
            project_dir = temp_dir / 'healthcare-demo'
            assert project_dir.exists()
            assert (project_dir / 'frontend').exists()
            assert (project_dir / 'backend').exists()
            assert (project_dir / 'database').exists()
            assert (project_dir / 'docs').exists()
            assert (project_dir / 'README.md').exists()
            assert (project_dir / 'docker-compose.yml').exists()
            assert (project_dir / 'Makefile').exists()

    def test_finance_api_generation(self, temp_dir: Path):
        """Test generating a finance API project"""
        from project_generator.core.generator import ProjectGenerator
        
        config = {
            'name': 'finance-api',
            'industry': 'finance',
            'project_type': 'api',
            'backend': 'go',
            'database': 'postgres',
            'auth': 'cognito',
            'deploy': 'aws',
            'compliance': ['sox', 'pci'],
            'features': ['transaction-processing', 'audit-trail']
        }
        
        generator = ProjectGenerator(
            output_dir=temp_dir,
            template_dir=Path(__file__).parent.parent.parent.parent / 'template-packs'
        )
        
        generator.set_config(config)
        
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(returncode=0, stdout=b'', stderr=b'')
            
            result = generator.generate_project()
            
            assert result is True
            
            # Verify API-specific structure
            project_dir = temp_dir / 'finance-api'
            assert project_dir.exists()
            assert (project_dir / 'backend').exists()
            assert (project_dir / 'database').exists()
            assert not (project_dir / 'frontend').exists()  # API project shouldn't have frontend

    def test_ecommerce_mobile_generation(self, temp_dir: Path):
        """Test generating an e-commerce mobile project"""
        from project_generator.core.generator import ProjectGenerator
        
        config = {
            'name': 'ecommerce-mobile',
            'industry': 'ecommerce',
            'project_type': 'mobile',
            'frontend': 'expo',
            'backend': 'django',
            'database': 'mongodb',
            'auth': 'firebase',
            'deploy': 'gcp',
            'compliance': ['pci', 'gdpr'],
            'features': ['inventory', 'payment-processing']
        }
        
        generator = ProjectGenerator(
            output_dir=temp_dir,
            template_dir=Path(__file__).parent.parent.parent.parent / 'template-packs'
        )
        
        generator.set_config(config)
        
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(returncode=0, stdout=b'', stderr=b'')
            
            result = generator.generate_project()
            
            assert result is True
            
            # Verify mobile-specific structure
            project_dir = temp_dir / 'ecommerce-mobile'
            assert project_dir.exists()
            assert (project_dir / 'frontend').exists()
            assert (project_dir / 'backend').exists()
            assert (project_dir / 'database').exists()

    def test_generation_with_validation_failure(self, temp_dir: Path):
        """Test generation flow with validation failure"""
        from project_generator.core.generator import ProjectGenerator
        
        config = {
            'name': 'test-project',
            'industry': 'invalid-industry',  # Invalid industry
            'project_type': 'fullstack'
        }
        
        generator = ProjectGenerator(
            output_dir=temp_dir,
            template_dir=Path(__file__).parent.parent.parent.parent / 'template-packs'
        )
        
        generator.set_config(config)
        
        result = generator.generate_project()
        
        assert result is False
        assert not (temp_dir / 'test-project').exists()

    def test_generation_with_setup_failure(self, temp_dir: Path):
        """Test generation flow with setup script failure"""
        from project_generator.core.generator import ProjectGenerator
        
        config = {
            'name': 'test-project',
            'industry': 'healthcare',
            'project_type': 'fullstack',
            'frontend': 'nextjs',
            'backend': 'fastapi',
            'database': 'postgres'
        }
        
        generator = ProjectGenerator(
            output_dir=temp_dir,
            template_dir=Path(__file__).parent.parent.parent.parent / 'template-packs'
        )
        
        generator.set_config(config)
        
        # Mock setup script failure
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(returncode=1, stdout=b'', stderr=b'Setup failed')
            
            result = generator.generate_project()
            
            assert result is False

    def test_template_processing_integration(self, temp_dir: Path, sample_template_files: dict):
        """Test template processing with real template files"""
        from project_generator.core.generator import ProjectGenerator
        
        generator = ProjectGenerator(
            output_dir=temp_dir,
            template_dir=temp_dir / 'templates'
        )
        
        config = {
            'name': 'template-test',
            'industry': 'healthcare',
            'project_type': 'fullstack',
            'frontend': 'nextjs',
            'backend': 'fastapi',
            'database': 'postgres'
        }
        
        generator.set_config(config)
        
        # Test processing package.json template
        source_file = sample_template_files['package_json']
        target_file = temp_dir / 'processed_package.json'
        
        generator.process_template_file(source_file, target_file)
        
        assert target_file.exists()
        content = target_file.read_text()
        assert 'template-test' in content

    def test_docker_compose_generation_integration(self, temp_dir: Path):
        """Test Docker Compose generation with different configurations"""
        from project_generator.core.generator import ProjectGenerator
        
        generator = ProjectGenerator(
            output_dir=temp_dir,
            template_dir=Path(__file__).parent.parent.parent.parent / 'template-packs'
        )
        
        # Test with PostgreSQL
        config = {
            'name': 'postgres-test',
            'industry': 'healthcare',
            'project_type': 'fullstack',
            'database': 'postgres'
        }
        
        generator.set_config(config)
        project_dir = temp_dir / 'postgres-test'
        project_dir.mkdir()
        
        generator.generate_docker_compose(project_dir)
        
        docker_file = project_dir / 'docker-compose.yml'
        assert docker_file.exists()
        
        content = docker_file.read_text()
        assert 'postgres' in content
        assert 'postgres-test' in content

    def test_makefile_generation_integration(self, temp_dir: Path):
        """Test Makefile generation with different project types"""
        from project_generator.core.generator import ProjectGenerator
        
        generator = ProjectGenerator(
            output_dir=temp_dir,
            template_dir=Path(__file__).parent.parent.parent.parent / 'template-packs'
        )
        
        # Test fullstack project
        config = {
            'name': 'fullstack-test',
            'industry': 'healthcare',
            'project_type': 'fullstack',
            'frontend': 'nextjs',
            'backend': 'fastapi',
            'database': 'postgres'
        }
        
        generator.set_config(config)
        project_dir = temp_dir / 'fullstack-test'
        project_dir.mkdir()
        
        generator.generate_makefile(project_dir)
        
        makefile = project_dir / 'Makefile'
        assert makefile.exists()
        
        content = makefile.read_text()
        assert 'setup:' in content
        assert 'dev:' in content
        assert 'test:' in content
        assert 'build:' in content
        assert 'frontend' in content
        assert 'backend' in content

    def test_readme_generation_integration(self, temp_dir: Path):
        """Test README generation with different configurations"""
        from project_generator.core.generator import ProjectGenerator
        
        generator = ProjectGenerator(
            output_dir=temp_dir,
            template_dir=Path(__file__).parent.parent.parent.parent / 'template-packs'
        )
        
        # Test healthcare project
        config = {
            'name': 'healthcare-readme-test',
            'industry': 'healthcare',
            'project_type': 'fullstack',
            'frontend': 'nextjs',
            'backend': 'fastapi',
            'database': 'postgres',
            'compliance': ['hipaa'],
            'features': ['patient-portal']
        }
        
        generator.set_config(config)
        project_dir = temp_dir / 'healthcare-readme-test'
        project_dir.mkdir()
        
        generator.generate_readme(project_dir)
        
        readme_file = project_dir / 'README.md'
        assert readme_file.exists()
        
        content = readme_file.read_text()
        assert 'healthcare-readme-test' in content
        assert 'healthcare' in content
        assert 'Next.js' in content
        assert 'FastAPI' in content
        assert 'PostgreSQL' in content
        assert 'HIPAA' in content

    def test_cleanup_on_failure_integration(self, temp_dir: Path):
        """Test cleanup functionality when generation fails"""
        from project_generator.core.generator import ProjectGenerator
        
        generator = ProjectGenerator(
            output_dir=temp_dir,
            template_dir=Path(__file__).parent.parent.parent.parent / 'template-packs'
        )
        
        # Create a project directory with some files
        project_dir = temp_dir / 'cleanup-test'
        project_dir.mkdir()
        (project_dir / 'test_file.txt').write_text('test content')
        (project_dir / 'subdir').mkdir()
        (project_dir / 'subdir' / 'nested_file.txt').write_text('nested content')
        
        # Test cleanup
        generator.cleanup_on_failure(project_dir)
        
        # Directory should be completely removed
        assert not project_dir.exists()

    def test_health_check_urls_generation(self, temp_dir: Path):
        """Test health check URLs generation for different configurations"""
        from project_generator.core.generator import ProjectGenerator
        
        generator = ProjectGenerator(
            output_dir=temp_dir,
            template_dir=Path(__file__).parent.parent.parent.parent / 'template-packs'
        )
        
        # Test fullstack configuration
        config = {
            'name': 'health-check-test',
            'industry': 'healthcare',
            'project_type': 'fullstack',
            'frontend': 'nextjs',
            'backend': 'fastapi',
            'database': 'postgres'
        }
        
        generator.set_config(config)
        urls = generator.get_health_check_urls()
        
        assert 'frontend' in urls
        assert 'backend' in urls
        assert 'database' in urls
        assert urls['frontend'] == 'http://localhost:3000/api/health'
        assert urls['backend'] == 'http://localhost:8000/health'
        assert 'postgresql://' in urls['database']

    def test_template_variables_substitution(self, temp_dir: Path):
        """Test template variable substitution with complex configurations"""
        from project_generator.core.generator import ProjectGenerator
        
        generator = ProjectGenerator(
            output_dir=temp_dir,
            template_dir=Path(__file__).parent.parent.parent.parent / 'template-packs'
        )
        
        config = {
            'name': 'variable-test',
            'industry': 'finance',
            'project_type': 'api',
            'backend': 'go',
            'database': 'postgres',
            'auth': 'cognito',
            'deploy': 'aws',
            'compliance': ['sox', 'pci'],
            'features': ['transaction-processing', 'audit-trail']
        }
        
        generator.set_config(config)
        variables = generator.get_template_variables()
        
        assert variables['PROJECT_NAME'] == 'variable-test'
        assert variables['INDUSTRY'] == 'finance'
        assert variables['PROJECT_TYPE'] == 'api'
        assert variables['BACKEND'] == 'go'
        assert variables['DATABASE'] == 'postgres'
        assert variables['AUTH'] == 'cognito'
        assert variables['DEPLOY'] == 'aws'
        assert variables['COMPLIANCE'] == 'sox,pci'
        assert variables['FEATURES'] == 'transaction-processing,audit-trail'
