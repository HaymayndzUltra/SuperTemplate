#!/usr/bin/env python3
"""
Unit tests for Protocol 05b orchestration scripts.
"""
import json
import subprocess
import sys
from pathlib import Path
import pytest

# Get paths
TESTS_DIR = Path(__file__).parent
FIXTURES_DIR = TESTS_DIR / 'fixtures'
SCRIPTS_DIR = TESTS_DIR.parent.parent / 'scripts' / 'orchestration'
WORKSPACE_ROOT = TESTS_DIR.parent.parent

def run_script(script_name: str, args: list = None) -> tuple:
    """Run an orchestration script and return (exit_code, stdout, stderr)."""
    script_path = SCRIPTS_DIR / script_name
    cmd = [sys.executable, str(script_path)]
    if args:
        cmd.extend(args)
    
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=str(WORKSPACE_ROOT)
    )
    return result.returncode, result.stdout, result.stderr


class TestParseProjectBrief:
    """Tests for parse_project_brief.py"""
    
    def test_help_flag(self):
        """Test that --help works."""
        exit_code, stdout, stderr = run_script('parse_project_brief.py', ['--help'])
        assert exit_code == 0
        assert 'Parse PROJECT-BRIEF.md' in stdout
    
    def test_parse_sample_brief(self, tmp_path):
        """Test parsing sample project brief."""
        # Copy fixture to temp path
        brief_path = FIXTURES_DIR / 'sample-project-brief.md'
        output_path = tmp_path / 'parsed.json'
        
        exit_code, stdout, stderr = run_script('parse_project_brief.py', [
            '--input', str(brief_path),
            '--output', str(output_path),
            '--workspace', str(tmp_path)
        ])
        
        assert exit_code == 0
        assert output_path.exists()
        
        with open(output_path) as f:
            data = json.load(f)
        
        assert 'project_name' in data
        assert 'tech_stack' in data
        assert 'project_goals' in data


class TestClassifyProjectType:
    """Tests for classify_project_type.py"""
    
    def test_help_flag(self):
        """Test that --help works."""
        exit_code, stdout, stderr = run_script('classify_project_type.py', ['--help'])
        assert exit_code == 0
        assert 'Classify project type' in stdout
    
    def test_classification_with_sample(self, tmp_path):
        """Test classification with sample data."""
        # First parse the brief
        brief_path = FIXTURES_DIR / 'sample-project-brief.md'
        parsed_path = tmp_path / 'parsed.json'
        
        run_script('parse_project_brief.py', [
            '--input', str(brief_path),
            '--output', str(parsed_path),
            '--workspace', str(tmp_path)
        ])
        
        # Now classify
        output_path = tmp_path / 'classification.json'
        exit_code, stdout, stderr = run_script('classify_project_type.py', [
            '--brief', str(parsed_path),
            '--output', str(output_path),
            '--workspace', str(tmp_path)
        ])
        
        assert exit_code == 0
        assert output_path.exists()
        
        with open(output_path) as f:
            data = json.load(f)
        
        assert 'classification' in data
        assert 'confidence_score' in data
        assert data['confidence_score'] >= 0
        assert data['confidence_score'] <= 100


class TestDetectCharacteristics:
    """Tests for detect_characteristics.py"""
    
    def test_help_flag(self):
        """Test that --help works."""
        exit_code, stdout, stderr = run_script('detect_characteristics.py', ['--help'])
        assert exit_code == 0
        assert 'Detect project characteristics' in stdout


class TestBuildDependencyGraph:
    """Tests for build_dependency_graph.py"""
    
    def test_help_flag(self):
        """Test that --help works."""
        exit_code, stdout, stderr = run_script('build_dependency_graph.py', ['--help'])
        assert exit_code == 0
        assert 'Build protocol dependency graph' in stdout


class TestPackageEvidence:
    """Tests for package_evidence.py"""
    
    def test_help_flag(self):
        """Test that --help works."""
        exit_code, stdout, stderr = run_script('package_evidence.py', ['--help'])
        assert exit_code == 0
        assert 'Package Protocol 05b evidence' in stdout
    
    def test_package_empty_workspace(self, tmp_path):
        """Test packaging with empty workspace."""
        exit_code, stdout, stderr = run_script('package_evidence.py', [
            '--workspace', str(tmp_path)
        ])
        
        # Should succeed even with no artifacts
        assert exit_code == 0


class TestValidateProtocolEvidence:
    """Tests for validate_protocol_evidence.py"""
    
    def test_help_flag(self):
        """Test that --help works."""
        exit_code, stdout, stderr = run_script('validate_protocol_evidence.py', ['--help'])
        assert exit_code == 0
        assert 'Validate Protocol' in stdout


class TestValidateProjectBrief:
    """Tests for validate_project_brief.py"""
    
    def test_help_flag(self):
        """Test that --help works."""
        exit_code, stdout, stderr = run_script('validate_project_brief.py', ['--help'])
        assert exit_code == 0
        assert 'Validate PROJECT-BRIEF.md' in stdout
    
    def test_validate_sample_brief(self, tmp_path):
        """Test validating sample brief."""
        # Copy fixture
        brief_path = FIXTURES_DIR / 'sample-project-brief.md'
        target_path = tmp_path / 'PROJECT-BRIEF.md'
        target_path.write_text(brief_path.read_text())
        
        exit_code, stdout, stderr = run_script('validate_project_brief.py', [
            '--file', 'PROJECT-BRIEF.md',
            '--workspace', str(tmp_path)
        ])
        
        # Check output
        assert 'Validating PROJECT-BRIEF.md' in stdout


if __name__ == '__main__':
    pytest.main([__file__, '-v'])

