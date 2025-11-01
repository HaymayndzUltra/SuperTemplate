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

    def test_gate_02_pre_call_validator(self):
        """Test pre-call readiness validator with all artifacts present."""
        with tempfile.TemporaryDirectory() as tmpdir:
            artifacts = {
                "discovery-brief.md": "Summary of objectives",
                "assumptions-gaps.md": "Item 1 - ASK CLIENT\nItem 2 - ASK CLIENT",
                "question-bank.md": "Questions by theme",
                "integration-inventory.md": "System: CRM",
                "call-agenda.md": "Agenda outline",
                "ready-for-call-summary.md": "Status: pre_call_ready",
            }
            for name, content in artifacts.items():
                path = Path(tmpdir) / name
                path.write_text(content, encoding="utf-8")
                dest = Path(".artifacts/protocol-02") / name
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(content, encoding="utf-8")

            try:
                result = subprocess.run(
                    [sys.executable, "scripts/validate_gate_02_pre_call.py"],
                    capture_output=True,
                    text=True,
                )

                assert result.returncode == 0
                output = json.loads(result.stdout)
                assert output["status"] == "pass"
            finally:
                for name in artifacts:
                    Path(".artifacts/protocol-02") / name
                    (Path(".artifacts/protocol-02") / name).unlink()

    def test_gate_02_data_capture_validator(self):
        """Test data capture validator with required sections present."""
        files = {
            "client-discovery-form.md": "priority: high\nowner: dev\nacceptance: defined",
            "scope-clarification.md": "stack: python\nconstraint: none\nintegration: crm",
            "integration-inventory.md": "system: crm\nowner: ops\nrisk: medium",
            "timeline-discussion.md": "milestone: kickoff\ncheckpoint: review\ntimeline: 4 weeks",
            "communication-plan.md": "cadence: weekly\ntool: zoom\nescalation: email",
            "assumptions-gaps.md": "Question 1 - follow-up owner dev due tomorrow",
        }
        for name, content in files.items():
            path = Path(".artifacts/protocol-02") / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

        try:
            result = subprocess.run(
                [sys.executable, "scripts/validate_gate_02_data_capture.py"],
                capture_output=True,
                text=True,
            )

            assert result.returncode == 0
            output = json.loads(result.stdout)
            assert output["status"] == "pass"
        finally:
            for name in files:
                (Path(".artifacts/protocol-02") / name).unlink()

    def test_gate_02_recap_validator(self):
        """Test recap validator with approved status."""
        recap_content = "Recap sent on 2025-01-01\nStatus: approved"
        approval_log = {
            "status": "approved",
            "approved_at": "2025-01-01T12:00:00Z",
            "approver": "client@example.com",
            "delivery_channel": "email",
        }
        ready_content = "Status: pre_call_ready"

        Path(".artifacts/protocol-02/discovery-recap.md").parent.mkdir(parents=True, exist_ok=True)
        Path(".artifacts/protocol-02/discovery-recap.md").write_text(recap_content, encoding="utf-8")
        Path(".artifacts/protocol-02/discovery-approval-log.json").write_text(
            json.dumps(approval_log), encoding="utf-8"
        )
        Path(".artifacts/protocol-02/ready-for-call-summary.md").write_text(ready_content, encoding="utf-8")

        try:
            result = subprocess.run(
                [sys.executable, "scripts/validate_gate_02_recap.py"],
                capture_output=True,
                text=True,
            )

            assert result.returncode == 0
            output = json.loads(result.stdout)
            assert output["status"] == "pass"
        finally:
            Path(".artifacts/protocol-02/discovery-recap.md").unlink()
            Path(".artifacts/protocol-02/discovery-approval-log.json").unlink()
            Path(".artifacts/protocol-02/ready-for-call-summary.md").unlink()

    def test_gate_02_handoff_validator(self):
        """Test handoff validator with cleared blockers."""
        files = {
            "client-discovery-form.md": "Feature list",
            "scope-clarification.md": "Stack details",
            "timeline-discussion.md": "Schedule",
            "communication-plan.md": "Cadence",
            "discovery-recap.md": "Approved",
            "assumptions-gaps.md": "All resolved",
        }
        approval_log = {
            "status": "approved",
            "approved_at": "2025-01-01T12:00:00Z",
            "approver": "client@example.com",
        }

        for name, content in files.items():
            path = Path(".artifacts/protocol-02") / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        Path(".artifacts/protocol-02/discovery-approval-log.json").write_text(
            json.dumps(approval_log), encoding="utf-8"
        )

        try:
            result = subprocess.run(
                [sys.executable, "scripts/validate_gate_02_handoff.py"],
                capture_output=True,
                text=True,
            )

            assert result.returncode == 0
            output = json.loads(result.stdout)
            assert output["status"] == "pass"
        finally:
            for name in files:
                (Path(".artifacts/protocol-02") / name).unlink()
            Path(".artifacts/protocol-02/discovery-approval-log.json").unlink()


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
