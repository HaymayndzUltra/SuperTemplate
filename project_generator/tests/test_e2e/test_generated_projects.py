"""
End-to-end tests for generated projects
"""

import pytest
import subprocess
import time
import requests
from pathlib import Path
from unittest.mock import patch, Mock


class TestGeneratedProjects:
    """E2E tests for generated project functionality"""

    def test_generated_healthcare_project_structure(self, temp_dir: Path):
        """Test that generated healthcare project has correct structure"""
        from project_generator.core.generator import ProjectGenerator
        
        config = {
            'name': 'e2e-healthcare-test',
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
            template_dir=Path(__file__).parent.parent.parent.parent.parent / 'template-packs'
        )
        
        generator.set_config(config)
        
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(returncode=0, stdout=b'', stderr=b'')
            
            result = generator.generate_project()
            assert result is True
            
            project_dir = temp_dir / 'e2e-healthcare-test'
            
            # Verify main structure
            assert project_dir.exists()
            assert (project_dir / 'README.md').exists()
            assert (project_dir / 'docker-compose.yml').exists()
            assert (project_dir / 'Makefile').exists()
            assert (project_dir / '.gitignore').exists()
            
            # Verify frontend structure
            frontend_dir = project_dir / 'frontend'
            assert frontend_dir.exists()
            assert (frontend_dir / 'package.json').exists()
            assert (frontend_dir / 'next.config.js').exists()
            assert (frontend_dir / 'src').exists()
            assert (frontend_dir / 'public').exists()
            
            # Verify backend structure
            backend_dir = project_dir / 'backend'
            assert backend_dir.exists()
            assert (backend_dir / 'main.py').exists()
            assert (backend_dir / 'requirements.txt').exists()
            assert (backend_dir / 'app').exists()
            
            # Verify database structure
            database_dir = project_dir / 'database'
            assert database_dir.exists()
            assert (database_dir / 'docker-compose.yml').exists()
            assert (database_dir / 'init.sql').exists()
            
            # Verify docs structure
            docs_dir = project_dir / 'docs'
            assert docs_dir.exists()
            assert (docs_dir / 'API.md').exists()
            assert (docs_dir / 'DEVELOPMENT.md').exists()
            assert (docs_dir / 'DEPLOYMENT.md').exists()
            assert (docs_dir / 'COMPLIANCE.md').exists()

    def test_generated_project_docker_compose_validity(self, temp_dir: Path):
        """Test that generated docker-compose.yml is valid"""
        from project_generator.core.generator import ProjectGenerator
        
        config = {
            'name': 'docker-test',
            'industry': 'healthcare',
            'project_type': 'fullstack',
            'frontend': 'nextjs',
            'backend': 'fastapi',
            'database': 'postgres'
        }
        
        generator = ProjectGenerator(
            output_dir=temp_dir,
            template_dir=Path(__file__).parent.parent.parent.parent.parent / 'template-packs'
        )
        
        generator.set_config(config)
        
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(returncode=0, stdout=b'', stderr=b'')
            
            result = generator.generate_project()
            assert result is True
            
            project_dir = temp_dir / 'docker-test'
            docker_file = project_dir / 'docker-compose.yml'
            
            # Verify docker-compose.yml exists and has valid structure
            assert docker_file.exists()
            content = docker_file.read_text()
            
            # Check for required sections
            assert 'version:' in content
            assert 'services:' in content
            assert 'postgres:' in content
            assert 'nextjs:' in content
            assert 'fastapi:' in content
            
            # Check for health checks
            assert 'healthcheck:' in content
            
            # Check for volumes
            assert 'volumes:' in content

    def test_generated_project_makefile_commands(self, temp_dir: Path):
        """Test that generated Makefile has all required commands"""
        from project_generator.core.generator import ProjectGenerator
        
        config = {
            'name': 'makefile-test',
            'industry': 'healthcare',
            'project_type': 'fullstack',
            'frontend': 'nextjs',
            'backend': 'fastapi',
            'database': 'postgres'
        }
        
        generator = ProjectGenerator(
            output_dir=temp_dir,
            template_dir=Path(__file__).parent.parent.parent.parent.parent / 'template-packs'
        )
        
        generator.set_config(config)
        
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(returncode=0, stdout=b'', stderr=b'')
            
            result = generator.generate_project()
            assert result is True
            
            project_dir = temp_dir / 'makefile-test'
            makefile = project_dir / 'Makefile'
            
            assert makefile.exists()
            content = makefile.read_text()
            
            # Check for required commands
            required_commands = [
                'setup:',
                'dev:',
                'test:',
                'lint:',
                'build:',
                'deploy:',
                'clean:',
                'help:'
            ]
            
            for command in required_commands:
                assert command in content

    def test_generated_project_readme_content(self, temp_dir: Path):
        """Test that generated README has comprehensive content"""
        from project_generator.core.generator import ProjectGenerator
        
        config = {
            'name': 'readme-test',
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
            template_dir=Path(__file__).parent.parent.parent.parent.parent / 'template-packs'
        )
        
        generator.set_config(config)
        
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(returncode=0, stdout=b'', stderr=b'')
            
            result = generator.generate_project()
            assert result is True
            
            project_dir = temp_dir / 'readme-test'
            readme_file = project_dir / 'README.md'
            
            assert readme_file.exists()
            content = readme_file.read_text()
            
            # Check for required sections
            required_sections = [
                '# readme-test',
                '## Overview',
                '## Technology Stack',
                '## Features',
                '## Quick Start',
                '## Development',
                '## Testing',
                '## Deployment',
                '## Compliance'
            ]
            
            for section in required_sections:
                assert section in content

    def test_generated_project_compliance_documentation(self, temp_dir: Path):
        """Test that generated project has proper compliance documentation"""
        from project_generator.core.generator import ProjectGenerator
        
        config = {
            'name': 'compliance-test',
            'industry': 'healthcare',
            'project_type': 'fullstack',
            'frontend': 'nextjs',
            'backend': 'fastapi',
            'database': 'postgres',
            'compliance': ['hipaa']
        }
        
        generator = ProjectGenerator(
            output_dir=temp_dir,
            template_dir=Path(__file__).parent.parent.parent.parent.parent / 'template-packs'
        )
        
        generator.set_config(config)
        
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(returncode=0, stdout=b'', stderr=b'')
            
            result = generator.generate_project()
            assert result is True
            
            project_dir = temp_dir / 'compliance-test'
            compliance_doc = project_dir / 'docs' / 'COMPLIANCE.md'
            
            assert compliance_doc.exists()
            content = compliance_doc.read_text()
            
            # Check for HIPAA compliance content
            assert 'HIPAA' in content
            assert 'PHI' in content
            assert 'encryption' in content
            assert 'audit' in content

    def test_generated_project_api_documentation(self, temp_dir: Path):
        """Test that generated project has API documentation"""
        from project_generator.core.generator import ProjectGenerator
        
        config = {
            'name': 'api-docs-test',
            'industry': 'healthcare',
            'project_type': 'api',
            'backend': 'fastapi',
            'database': 'postgres'
        }
        
        generator = ProjectGenerator(
            output_dir=temp_dir,
            template_dir=Path(__file__).parent.parent.parent.parent.parent / 'template-packs'
        )
        
        generator.set_config(config)
        
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(returncode=0, stdout=b'', stderr=b'')
            
            result = generator.generate_project()
            assert result is True
            
            project_dir = temp_dir / 'api-docs-test'
            api_doc = project_dir / 'docs' / 'API.md'
            
            assert api_doc.exists()
            content = api_doc.read_text()
            
            # Check for API documentation content
            assert 'API' in content
            assert 'endpoints' in content
            assert 'authentication' in content

    def test_generated_project_development_documentation(self, temp_dir: Path):
        """Test that generated project has development documentation"""
        from project_generator.core.generator import ProjectGenerator
        
        config = {
            'name': 'dev-docs-test',
            'industry': 'healthcare',
            'project_type': 'fullstack',
            'frontend': 'nextjs',
            'backend': 'fastapi',
            'database': 'postgres'
        }
        
        generator = ProjectGenerator(
            output_dir=temp_dir,
            template_dir=Path(__file__).parent.parent.parent.parent.parent / 'template-packs'
        )
        
        generator.set_config(config)
        
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(returncode=0, stdout=b'', stderr=b'')
            
            result = generator.generate_project()
            assert result is True
            
            project_dir = temp_dir / 'dev-docs-test'
            dev_doc = project_dir / 'docs' / 'DEVELOPMENT.md'
            
            assert dev_doc.exists()
            content = dev_doc.read_text()
            
            # Check for development documentation content
            assert 'Development' in content
            assert 'setup' in content
            assert 'testing' in content

    def test_generated_project_deployment_documentation(self, temp_dir: Path):
        """Test that generated project has deployment documentation"""
        from project_generator.core.generator import ProjectGenerator
        
        config = {
            'name': 'deploy-docs-test',
            'industry': 'healthcare',
            'project_type': 'fullstack',
            'frontend': 'nextjs',
            'backend': 'fastapi',
            'database': 'postgres',
            'deploy': 'aws'
        }
        
        generator = ProjectGenerator(
            output_dir=temp_dir,
            template_dir=Path(__file__).parent.parent.parent.parent.parent / 'template-packs'
        )
        
        generator.set_config(config)
        
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(returncode=0, stdout=b'', stderr=b'')
            
            result = generator.generate_project()
            assert result is True
            
            project_dir = temp_dir / 'deploy-docs-test'
            deploy_doc = project_dir / 'docs' / 'DEPLOYMENT.md'
            
            assert deploy_doc.exists()
            content = deploy_doc.read_text()
            
            # Check for deployment documentation content
            assert 'Deployment' in content
            assert 'AWS' in content
            assert 'production' in content

    def test_generated_project_environment_configuration(self, temp_dir: Path):
        """Test that generated project has proper environment configuration"""
        from project_generator.core.generator import ProjectGenerator
        
        config = {
            'name': 'env-test',
            'industry': 'healthcare',
            'project_type': 'fullstack',
            'frontend': 'nextjs',
            'backend': 'fastapi',
            'database': 'postgres'
        }
        
        generator = ProjectGenerator(
            output_dir=temp_dir,
            template_dir=Path(__file__).parent.parent.parent.parent.parent / 'template-packs'
        )
        
        generator.set_config(config)
        
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(returncode=0, stdout=b'', stderr=b'')
            
            result = generator.generate_project()
            assert result is True
            
            project_dir = temp_dir / 'env-test'
            
            # Check for environment files
            assert (project_dir / '.env.example').exists()
            assert (project_dir / '.gitignore').exists()
            
            # Check .gitignore content
            gitignore_content = (project_dir / '.gitignore').read_text()
            assert '.env' in gitignore_content
            assert 'node_modules' in gitignore_content
            assert '__pycache__' in gitignore_content

    def test_generated_project_ci_cd_configuration(self, temp_dir: Path):
        """Test that generated project has CI/CD configuration"""
        from project_generator.core.generator import ProjectGenerator
        
        config = {
            'name': 'cicd-test',
            'industry': 'healthcare',
            'project_type': 'fullstack',
            'frontend': 'nextjs',
            'backend': 'fastapi',
            'database': 'postgres'
        }
        
        generator = ProjectGenerator(
            output_dir=temp_dir,
            template_dir=Path(__file__).parent.parent.parent.parent.parent / 'template-packs'
        )
        
        generator.set_config(config)
        
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(returncode=0, stdout=b'', stderr=b'')
            
            result = generator.generate_project()
            assert result is True
            
            project_dir = temp_dir / 'cicd-test'
            github_dir = project_dir / '.github' / 'workflows'
            
            # Check for GitHub Actions workflows
            assert github_dir.exists()
            assert (github_dir / 'ci-lint.yml').exists()
            assert (github_dir / 'ci-test.yml').exists()
            assert (github_dir / 'ci-security.yml').exists()
            assert (github_dir / 'ci-deploy.yml').exists()

    def test_generated_project_template_variable_substitution(self, temp_dir: Path):
        """Test that template variables are properly substituted in generated files"""
        from project_generator.core.generator import ProjectGenerator
        
        config = {
            'name': 'variable-substitution-test',
            'industry': 'finance',
            'project_type': 'api',
            'backend': 'go',
            'database': 'postgres',
            'compliance': ['sox', 'pci']
        }
        
        generator = ProjectGenerator(
            output_dir=temp_dir,
            template_dir=Path(__file__).parent.parent.parent.parent.parent / 'template-packs'
        )
        
        generator.set_config(config)
        
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(returncode=0, stdout=b'', stderr=b'')
            
            result = generator.generate_project()
            assert result is True
            
            project_dir = temp_dir / 'variable-substitution-test'
            
            # Check README for variable substitution
            readme_content = (project_dir / 'README.md').read_text()
            assert 'variable-substitution-test' in readme_content
            assert 'finance' in readme_content
            assert 'Go' in readme_content
            assert 'PostgreSQL' in readme_content
            
            # Check docker-compose for variable substitution
            docker_content = (project_dir / 'docker-compose.yml').read_text()
            assert 'variable-substitution-test' in docker_content
            
            # Check Makefile for variable substitution
            makefile_content = (project_dir / 'Makefile').read_text()
            assert 'variable-substitution-test' in makefile_content
