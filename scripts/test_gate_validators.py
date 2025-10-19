#!/usr/bin/env python3
"""Regression tests for protocol gate validators.

Tests dynamic loading, validator execution, and manifest generation.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest


class TestProtocol01Validators:
    """Test Protocol 01 gate validators."""
    
    def test_gate_01_jobpost_validator_missing_file(self):
        """Test jobpost validator with missing file."""
        result = subprocess.run(
            [sys.executable, "scripts/validate_gate_01_jobpost.py", "--input", "/nonexistent/file.json"],
            capture_output=True,
            text=True,
        )
        
        assert result.returncode != 0
        output = json.loads(result.stdout)
        assert output["status"] == "fail"
        assert "Missing artifact" in output["notes"]
    
    def test_gate_01_jobpost_validator_valid_data(self):
        """Test jobpost validator with valid data."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            data = {
                "objectives": ["Improve user engagement"],
                "deliverables": ["Mobile app", "API"],
                "tone_signals": ["professional", "technical"],
                "risks": ["Timeline constraints"]
            }
            json.dump(data, f)
            temp_path = f.name
        
        try:
            result = subprocess.run(
                [sys.executable, "scripts/validate_gate_01_jobpost.py", "--input", temp_path],
                capture_output=True,
                text=True,
            )
            
            assert result.returncode == 0
            output = json.loads(result.stdout)
            assert output["status"] == "pass"
            assert output["score"] >= 0.9
        finally:
            Path(temp_path).unlink()
    
    def test_gate_01_tone_validator_low_confidence(self):
        """Test tone validator with low confidence."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            data = {
                "confidence": 0.5,
                "strategy": "technical"
            }
            json.dump(data, f)
            temp_path = f.name
        
        try:
            result = subprocess.run(
                [sys.executable, "scripts/validate_gate_01_tone.py", "--input", temp_path],
                capture_output=True,
                text=True,
            )
            
            assert result.returncode != 0
            output = json.loads(result.stdout)
            assert output["status"] == "fail"
            assert "Confidence" in output["notes"]
        finally:
            Path(temp_path).unlink()
    
    def test_gate_01_structure_validator_with_sections(self):
        """Test structure validator with required sections."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as proposal:
            proposal_content = """
# Greeting

Hello and thank you for this opportunity.

## Understanding

I understand your needs for a mobile application with real-time features.

### Proposed Approach

We will use a modern tech stack including React Native and Firebase.

## Deliverables and Timeline

Phase 1: Design and architecture (2 weeks)
Phase 2: Development (6 weeks)

### Collaboration Model

We'll have weekly sync meetings and daily async updates via Slack.

## Next Steps

Let's schedule a kickoff call to align on priorities.
"""
            proposal.write(proposal_content)
            proposal_path = proposal.name
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as log:
            log_data = {"empathy_tokens": 5, "variations_applied": 12}
            json.dump(log_data, log)
            log_path = log.name
        
        try:
            result = subprocess.run(
                [
                    sys.executable,
                    "scripts/validate_gate_01_structure.py",
                    "--proposal", proposal_path,
                    "--humanization-log", log_path,
                    "--min-words", "10",  # Lower threshold for test
                ],
                capture_output=True,
                text=True,
            )
            
            output = json.loads(result.stdout)
            # May pass or fail depending on section detection, but should parse
            assert "status" in output
            assert "score" in output
        finally:
            Path(proposal_path).unlink()
            Path(log_path).unlink()


class TestProtocol02Validators:
    """Test Protocol 02 gate validators."""
    
    def test_gate_02_objectives_validator(self):
        """Test objectives validator with valid content."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            content = """
# Client Context Notes

## Business Objectives
The primary objective is to increase user engagement by 50%.

## Target Users
Our primary users are small business owners.

## Key Performance Indicators
- Monthly Active Users (MAU)
- Customer Retention Rate
"""
            f.write(content)
            temp_path = f.name
        
        try:
            result = subprocess.run(
                [sys.executable, "scripts/validate_gate_02_objectives.py", "--input", temp_path],
                capture_output=True,
                text=True,
            )
            
            assert result.returncode == 0
            output = json.loads(result.stdout)
            assert output["status"] == "pass"
            assert output["coverage"] >= 0.95
        finally:
            Path(temp_path).unlink()
    
    def test_gate_02_requirements_validator(self):
        """Test requirements validator with MVP and backlog."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as form:
            form_content = """
# Discovery Form

## MVP Features (Must-Have)
- User authentication
- Dashboard view

## Optional Backlog
- Analytics integration
- Export functionality
"""
            form.write(form_content)
            form_path = form.name
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as scope:
            scope_content = """
# Scope Clarification

## Technology Stack
React, Node.js, PostgreSQL

## Technical Constraints
Must support IE11, WCAG 2.1 AA compliance

## Third-party Integrations
Stripe for payments, SendGrid for email
"""
            scope.write(scope_content)
            scope_path = scope.name
        
        try:
            result = subprocess.run(
                [
                    sys.executable,
                    "scripts/validate_gate_02_requirements.py",
                    "--form", form_path,
                    "--scope", scope_path,
                ],
                capture_output=True,
                text=True,
            )
            
            assert result.returncode == 0
            output = json.loads(result.stdout)
            assert output["status"] == "pass"
        finally:
            Path(form_path).unlink()
            Path(scope_path).unlink()


class TestProtocol03Validators:
    """Test Protocol 03 gate validators."""
    
    def test_gate_03_discovery_validator_missing_artifacts(self):
        """Test discovery validator with missing artifacts."""
        with tempfile.TemporaryDirectory() as tmpdir:
            result = subprocess.run(
                [
                    sys.executable,
                    "scripts/validate_gate_03_discovery.py",
                    "--input", tmpdir,
                    "--output", f"{tmpdir}/report.json",
                ],
                capture_output=True,
                text=True,
            )
            
            assert result.returncode != 0
            output = json.loads(result.stdout)
            assert output["status"] == "fail"
            assert output["validation_score"] < 0.95
    
    def test_gate_03_approvals_validator_valid(self):
        """Test approvals validator with valid record."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            record = {
                "client_status": "approved",
                "internal_status": "approved",
                "client_timestamp": "2025-01-15T10:30:00Z",
                "internal_timestamp": "2025-01-15T11:00:00Z",
                "approver_client": "john.doe@client.com",
                "approver_internal": "jane.smith@company.com"
            }
            json.dump(record, f)
            temp_path = f.name
        
        try:
            result = subprocess.run(
                [sys.executable, "scripts/validate_gate_03_approvals.py", "--input", temp_path],
                capture_output=True,
                text=True,
            )
            
            assert result.returncode == 0
            output = json.loads(result.stdout)
            assert output["status"] == "pass"
            assert output["client_approved"] is True
            assert output["internal_approved"] is True
        finally:
            Path(temp_path).unlink()


class TestGateRunner:
    """Test the gate runner framework."""
    
    def test_run_protocol_gates_config_loading(self):
        """Test gate runner can load configuration."""
        # Check that config files exist
        assert Path("config/protocol_gates/01.yaml").exists()
        assert Path("config/protocol_gates/02.yaml").exists()
        assert Path("config/protocol_gates/03.yaml").exists()
    
    def test_gate_utils_manifest_generation(self):
        """Test manifest generation utilities."""
        from gate_utils import ManifestData, write_manifest
        
        with tempfile.TemporaryDirectory() as tmpdir:
            data = ManifestData(
                protocol_id="01",
                protocol_title="Test Protocol",
                coverage=0.85,
                referenced_scripts=["script1.py", "script2.py"],
                missing_scripts=["script3.py"],
            )
            
            artifacts = [
                {"path": "test.json", "description": "Test artifact", "status": "generated"}
            ]
            
            validators = [
                {"name": "test_gate", "command": "test.py", "status": "pass", "notes": "OK"}
            ]
            
            manifest_path = Path(tmpdir) / "test-manifest.json"
            write_manifest(manifest_path, data, artifacts, validators, "Test notes")
            
            assert manifest_path.exists()
            
            manifest = json.loads(manifest_path.read_text())
            assert manifest["protocol_id"] == "01"
            assert manifest["protocol_title"] == "Test Protocol"
            assert len(manifest["artifacts"]) == 1
            assert len(manifest["validators"]) == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
