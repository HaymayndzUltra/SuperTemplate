"""
Unit tests for ProjectGenerator core functionality
"""

import pytest
from pathlib import Path
from unittest.mock import Mock, patch, mock_open
from project_generator.core.generator import ProjectGenerator
from project_generator.core.validator import ProjectValidator


class TestProjectGenerator:
    """Test cases for ProjectGenerator class"""

    def test_initialization(self, temp_dir: Path):
        """Test ProjectGenerator initialization"""
        generator = ProjectGenerator(
            output_dir=temp_dir,
            template_dir=Path(__file__).parent.parent.parent / 'template-packs'
        )
        
        assert generator.output_dir == temp_dir
        assert generator.template_dir.exists()
        assert generator.project_name is None
        assert generator.config == {}

    def test_set_config(self, generator: ProjectGenerator, sample_config: dict):
        """Test setting project configuration"""
        generator.set_config(sample_config)
        
        assert generator.config == sample_config
        assert generator.project_name == 'test-project'

    def test_validate_config_valid(self, generator: ProjectGenerator, sample_config: dict):
        """Test configuration validation with valid config"""
        generator.set_config(sample_config)
        
        with patch.object(ProjectValidator, 'validate_config') as mock_validate:
            mock_validate.return_value = True, []
            result = generator.validate_config()
            
            assert result is True
            mock_validate.assert_called_once_with(sample_config)

    def test_validate_config_invalid(self, generator: ProjectGenerator):
        """Test configuration validation with invalid config"""
        invalid_config = {'name': 'test', 'industry': 'invalid'}
        generator.set_config(invalid_config)
        
        with patch.object(ProjectValidator, 'validate_config') as mock_validate:
            mock_validate.return_value = False, ['Invalid industry']
            result = generator.validate_config()
            
            assert result is False

    def test_get_template_path(self, generator: ProjectGenerator):
        """Test getting template path for different components"""
        # Test frontend template
        frontend_path = generator.get_template_path('frontend', 'nextjs')
        expected_path = generator.template_dir / 'frontend' / 'nextjs' / 'base'
        assert frontend_path == expected_path
        
        # Test backend template
        backend_path = generator.get_template_path('backend', 'fastapi')
        expected_path = generator.template_dir / 'backend' / 'fastapi' / 'base'
        assert backend_path == expected_path

    def test_get_template_path_nonexistent(self, generator: ProjectGenerator):
        """Test getting template path for nonexistent template"""
        with pytest.raises(FileNotFoundError):
            generator.get_template_path('frontend', 'nonexistent')

    @patch('shutil.copytree')
    def test_copy_template(self, mock_copytree, generator: ProjectGenerator, temp_dir: Path):
        """Test copying template files"""
        source_dir = Path('/fake/source')
        target_dir = temp_dir / 'test-project' / 'frontend'
        
        generator.copy_template(source_dir, target_dir)
        
        mock_copytree.assert_called_once_with(
            source_dir,
            target_dir,
            ignore=generator.ignore_patterns
        )

    @patch('pathlib.Path.write_text')
    def test_process_template_file(self, mock_write_text, generator: ProjectGenerator, temp_dir: Path):
        """Test processing template file with variable substitution"""
        template_content = "Hello {{PROJECT_NAME}}, welcome to {{INDUSTRY}}!"
        expected_content = "Hello test-project, welcome to healthcare!"
        
        generator.set_config({
            'name': 'test-project',
            'industry': 'healthcare'
        })
        
        source_file = temp_dir / 'template.txt'
        target_file = temp_dir / 'output.txt'
        source_file.write_text(template_content)
        
        generator.process_template_file(source_file, target_file)
        
        mock_write_text.assert_called_once_with(expected_content)

    def test_get_template_variables(self, generator: ProjectGenerator, sample_config: dict):
        """Test getting template variables from config"""
        generator.set_config(sample_config)
        variables = generator.get_template_variables()
        
        expected_variables = {
            'PROJECT_NAME': 'test-project',
            'INDUSTRY': 'healthcare',
            'PROJECT_TYPE': 'fullstack',
            'FRONTEND': 'nextjs',
            'BACKEND': 'fastapi',
            'DATABASE': 'postgres',
            'AUTH': 'auth0',
            'DEPLOY': 'aws',
            'COMPLIANCE': 'hipaa',
            'FEATURES': 'patient-portal,appointment-scheduling'
        }
        
        assert variables == expected_variables

    def test_create_project_structure(self, generator: ProjectGenerator, temp_dir: Path, sample_config: dict):
        """Test creating project directory structure"""
        generator.set_config(sample_config)
        project_dir = temp_dir / 'test-project'
        
        generator.create_project_structure(project_dir)
        
        # Check that main directories are created
        assert project_dir.exists()
        assert (project_dir / 'frontend').exists()
        assert (project_dir / 'backend').exists()
        assert (project_dir / 'database').exists()
        assert (project_dir / 'docs').exists()
        assert (project_dir / 'tests').exists()

    @patch('subprocess.run')
    def test_run_setup_script(self, mock_run, generator: ProjectGenerator, temp_dir: Path):
        """Test running setup script"""
        mock_run.return_value = Mock(returncode=0, stdout=b'Success', stderr=b'')
        
        project_dir = temp_dir / 'test-project'
        project_dir.mkdir()
        
        result = generator.run_setup_script(project_dir)
        
        assert result is True
        mock_run.assert_called_once()

    @patch('subprocess.run')
    def test_run_setup_script_failure(self, mock_run, generator: ProjectGenerator, temp_dir: Path):
        """Test running setup script with failure"""
        mock_run.return_value = Mock(returncode=1, stdout=b'', stderr=b'Error')
        
        project_dir = temp_dir / 'test-project'
        project_dir.mkdir()
        
        result = generator.run_setup_script(project_dir)
        
        assert result is False

    def test_generate_readme(self, generator: ProjectGenerator, temp_dir: Path, sample_config: dict):
        """Test generating README file"""
        generator.set_config(sample_config)
        project_dir = temp_dir / 'test-project'
        project_dir.mkdir()
        
        generator.generate_readme(project_dir)
        
        readme_file = project_dir / 'README.md'
        assert readme_file.exists()
        
        content = readme_file.read_text()
        assert 'test-project' in content
        assert 'healthcare' in content
        assert 'Next.js' in content
        assert 'FastAPI' in content

    def test_generate_docker_compose(self, generator: ProjectGenerator, temp_dir: Path, sample_config: dict):
        """Test generating docker-compose.yml file"""
        generator.set_config(sample_config)
        project_dir = temp_dir / 'test-project'
        project_dir.mkdir()
        
        generator.generate_docker_compose(project_dir)
        
        docker_file = project_dir / 'docker-compose.yml'
        assert docker_file.exists()
        
        content = docker_file.read_text()
        assert 'test-project' in content
        assert 'postgres' in content
        assert 'nextjs' in content

    def test_generate_makefile(self, generator: ProjectGenerator, temp_dir: Path, sample_config: dict):
        """Test generating Makefile"""
        generator.set_config(sample_config)
        project_dir = temp_dir / 'test-project'
        project_dir.mkdir()
        
        generator.generate_makefile(project_dir)
        
        makefile = project_dir / 'Makefile'
        assert makefile.exists()
        
        content = makefile.read_text()
        assert 'setup:' in content
        assert 'dev:' in content
        assert 'test:' in content
        assert 'build:' in content

    @patch('project_generator.core.generator.ProjectGenerator.copy_template')
    @patch('project_generator.core.generator.ProjectGenerator.process_template_file')
    def test_generate_project(self, mock_process_file, mock_copy_template, generator: ProjectGenerator, sample_config: dict):
        """Test full project generation"""
        generator.set_config(sample_config)
        
        with patch.object(generator, 'validate_config', return_value=True):
            with patch.object(generator, 'create_project_structure'):
                with patch.object(generator, 'run_setup_script', return_value=True):
                    result = generator.generate_project()
                    
                    assert result is True
                    mock_copy_template.assert_called()
                    mock_process_file.assert_called()

    def test_generate_project_validation_failure(self, generator: ProjectGenerator, sample_config: dict):
        """Test project generation with validation failure"""
        generator.set_config(sample_config)
        
        with patch.object(generator, 'validate_config', return_value=False):
            result = generator.generate_project()
            
            assert result is False

    def test_generate_project_setup_failure(self, generator: ProjectGenerator, sample_config: dict):
        """Test project generation with setup failure"""
        generator.set_config(sample_config)
        
        with patch.object(generator, 'validate_config', return_value=True):
            with patch.object(generator, 'create_project_structure'):
                with patch.object(generator, 'run_setup_script', return_value=False):
                    result = generator.generate_project()
                    
                    assert result is False

    def test_cleanup_on_failure(self, generator: ProjectGenerator, temp_dir: Path, sample_config: dict):
        """Test cleanup when project generation fails"""
        generator.set_config(sample_config)
        project_dir = temp_dir / 'test-project'
        project_dir.mkdir()
        
        # Create some files to test cleanup
        (project_dir / 'test_file.txt').write_text('test')
        
        generator.cleanup_on_failure(project_dir)
        
        # Directory should be removed
        assert not project_dir.exists()

    def test_include_selected_project_rules_outputs(self, generator: ProjectGenerator, temp_dir: Path):
        """Include project rules when requested, using fallbacks for missing sources."""
        generator.args.include_project_rules = True
        project_dir = temp_dir / generator.args.name
        rules_dir = project_dir / '.cursor' / 'rules' / 'project-rules'
        rules_dir.mkdir(parents=True, exist_ok=True)
        generator.project_root = project_dir

        generator._include_selected_project_rules(rules_dir)

        fe_map = {
            'nextjs': ['nextjs.mdc', 'nextjs-formatting.mdc', 'nextjs-rsc-and-client.mdc', 'typescript.mdc'],
            'angular': ['angular.mdc', 'typescript.mdc'],
            'expo': ['expo.mdc', 'react-native.mdc', 'typescript.mdc'],
            'nuxt': ['vue.mdc', 'typescript.mdc'],
        }
        be_map = {
            'fastapi': ['fastapi.mdc', 'python.mdc', 'rest-api.mdc', 'open-api.mdc'],
            'django': ['django.mdc', 'python.mdc', 'rest-api.mdc', 'open-api.mdc'],
            'nestjs': ['nodejs.mdc', 'typescript.mdc', 'rest-api.mdc', 'open-api.mdc'],
            'go': ['golang.mdc', 'nethttp.mdc', 'rest-api.mdc', 'open-api.mdc'],
        }
        db_addons: list[str] = []
        if generator.args.database.lower() == 'mongodb':
            db_addons.append('mongodb.mdc')
        elif generator.args.database.lower() == 'firebase':
            db_addons.append('firebase.mdc')

        expected = []
        expected += fe_map.get(generator.args.frontend, [])
        expected += be_map.get(generator.args.backend, [])
        expected += db_addons

        deduped: list[str] = []
        for name in expected:
            if name and name not in deduped:
                deduped.append(name)

        generated_files = sorted(p.name for p in rules_dir.glob('*.mdc'))
        assert generated_files, "No project rules were emitted"
        assert set(generated_files) == set(deduped)
        for name in deduped:
            assert (rules_dir / name).exists()

        recorded = {Path(entry).name for entry in generator._rules_selected_includes}
        assert set(deduped).issubset(recorded)

        rsc_rule = rules_dir / 'nextjs-rsc-and-client.mdc'
        assert rsc_rule.exists()
        assert 'SCOPE: project:test-project' in rsc_rule.read_text(encoding='utf-8')


    def test_get_ignore_patterns(self, generator: ProjectGenerator):
        """Test getting ignore patterns for template copying"""
        patterns = generator.get_ignore_patterns()
        
        assert '__pycache__' in patterns
        assert '*.pyc' in patterns
        assert '.git' in patterns
        assert 'node_modules' in patterns

    def test_validate_dependencies(self, generator: ProjectGenerator):
        """Test dependency validation"""
        with patch('shutil.which') as mock_which:
            mock_which.return_value = '/usr/bin/docker'
            
            result = generator.validate_dependencies()
            
            assert result is True
            mock_which.assert_called_with('docker')

    def test_validate_dependencies_missing(self, generator: ProjectGenerator):
        """Test dependency validation with missing dependencies"""
        with patch('shutil.which') as mock_which:
            mock_which.return_value = None
            
            result = generator.validate_dependencies()
            
            assert result is False

    def test_get_health_check_urls(self, generator: ProjectGenerator, sample_config: dict):
        """Test getting health check URLs for different configurations"""
        generator.set_config(sample_config)
        urls = generator.get_health_check_urls()
        
        assert 'frontend' in urls
        assert 'backend' in urls
        assert 'database' in urls
        assert urls['frontend'] == 'http://localhost:3000/api/health'
        assert urls['backend'] == 'http://localhost:8000/health'
        assert urls['database'] == 'postgresql://postgres:postgres@localhost:5432/test-project'
