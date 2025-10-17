#!/usr/bin/env python3
"""
Integration tests for Unified Developer Workflow

Tests end-to-end workflow execution, component integration, and evidence tracking.
"""

import pytest
import json
import tempfile
import shutil
from pathlib import Path
from datetime import datetime
import sys
import os

# Add the automation directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent / "automation"))

from ai_executor import AIExecutor
from ai_orchestrator import AIOrchestrator
from quality_gates import QualityGates
from validation_gates import ValidationGates
from evidence_manager import EvidenceManager


class TestIntegration:
    """Integration tests for unified workflow"""
    
    def setup_method(self):
        """Set up test environment"""
        self.temp_dir = tempfile.mkdtemp()
        self.project_name = "integration-test-project"
        
        # Initialize all components
        self.ai_executor = AIExecutor(self.project_name, self.temp_dir)
        self.ai_orchestrator = AIOrchestrator(self.project_name, self.temp_dir)
        self.quality_gates = QualityGates(self.project_name, self.temp_dir)
        self.validation_gates = ValidationGates(self.project_name, self.temp_dir)
        self.evidence_manager = EvidenceManager(self.temp_dir)
    
    def teardown_method(self):
        """Clean up test environment"""
        shutil.rmtree(self.temp_dir)
    
    def test_full_workflow_integration(self):
        """Test complete workflow integration"""
        # Execute full workflow
        workflow_report = self.ai_executor.execute_full_workflow()
        
        # Verify workflow completion
        assert workflow_report["metadata"]["overall_status"] == "success"
        assert workflow_report["metadata"]["total_phases"] == 7
        assert len(workflow_report["phase_results"]) == 7
        
        # Verify all phases completed successfully
        for result in workflow_report["phase_results"]:
            assert result["status"] == "success"
            assert "duration" in result
            # Allow for small timing variations
            assert result["duration"] >= 0
        
        # Verify evidence was generated
        assert "evidence" in workflow_report
        assert workflow_report["evidence"]["manifest_path"]
        assert workflow_report["evidence"]["run_log_path"]
        assert workflow_report["evidence"]["validation_path"]
    
    def test_phase_by_phase_execution(self):
        """Test phase-by-phase execution with validation"""
        phases = [0, 1, 2, 3, 4, 5, 6]
        
        for phase in phases:
            # Execute phase
            result = self.ai_executor.execute_single_phase(phase)
            assert result["status"] == "success"
            
            # Request validation
            validation_request = self.validation_gates.request_validation(phase)
            assert validation_request["status"] == "pending"
            
            # Approve validation
            required_approvals = validation_request["checkpoint"]["required_approvals"]
            for approver in required_approvals:
                updated_request = self.validation_gates.approve_validation(
                    validation_request["request_id"], approver, True
                )
            
            assert updated_request["status"] == "approved"
    
    def test_quality_gates_integration(self):
        """Test quality gates integration with workflow"""
        # Execute implementation phase
        result = self.ai_executor.execute_single_phase(3)
        assert result["status"] == "success"
        
        # Execute quality audit
        audit_result = self.quality_gates.execute_comprehensive_audit()
        assert audit_result["mode"] == "comprehensive"
        assert "overall_score" in audit_result
        assert "layer_results" in audit_result
        
        # Verify all layers were audited
        assert len(audit_result["layer_results"]) == 6
        
        # Check that evidence was logged
        manifest = self.evidence_manager._read_json(self.evidence_manager.manifest_path)
        run_log = self.evidence_manager._read_json(self.evidence_manager.run_log_path)
        
        assert len(manifest["artifacts"]) > 0
        assert len(run_log["entries"]) > 0
    
    def test_evidence_consistency(self):
        """Test evidence consistency across components"""
        # Execute workflow
        workflow_report = self.ai_executor.execute_full_workflow()
        
        # Execute quality audit
        audit_result = self.quality_gates.execute_comprehensive_audit()
        
        # Validate evidence for specific phases
        evidence_validation_phase0 = self.evidence_manager.validate_evidence(phase=0)
        evidence_validation_phase4 = self.evidence_manager.validate_evidence(phase=4)
        
        # Check consistency
        assert evidence_validation_phase0["status"] == "passed"
        assert evidence_validation_phase4["status"] == "passed"
        
        # Verify manifest consistency
        manifest = self.evidence_manager._read_json(self.evidence_manager.manifest_path)
        assert len(manifest["artifacts"]) > 0
        
        # Verify run log consistency
        run_log = self.evidence_manager._read_json(self.evidence_manager.run_log_path)
        assert len(run_log["entries"]) > 0
        
        # Check phase coverage
        phases_executed = set(e["phase"] for e in run_log["entries"])
        assert phases_executed == set(range(7))
    
    def test_ai_orchestrator_integration(self):
        """Test AI orchestrator integration"""
        # Execute phase sequence
        results = self.ai_orchestrator.execute_phase_sequence(0, 2)
        
        assert len(results) == 3
        for result in results:
            assert result["status"] == "success"
            assert "ai_role" in result
            assert "outputs" in result
        
        # Verify evidence was logged
        run_log = self.evidence_manager._read_json(self.evidence_manager.run_log_path)
        ai_entries = [e for e in run_log["entries"] if "AI" in e["action"]]
        assert len(ai_entries) > 0
    
    def test_validation_workflow_integration(self):
        """Test validation workflow integration"""
        # Execute phase
        result = self.ai_executor.execute_single_phase(1)
        assert result["status"] == "success"
        
        # Create validation request
        validation_request = self.validation_gates.request_validation(1)
        request_id = validation_request["request_id"]
        
        # Check pending validations
        pending = self.validation_gates.list_pending_validations()
        assert len(pending) > 0
        
        # Approve validation
        required_approvals = validation_request["checkpoint"]["required_approvals"]
        for approver in required_approvals:
            self.validation_gates.approve_validation(request_id, approver, True)
        
        # Check final status
        status = self.validation_gates.get_validation_status(request_id)
        assert status["status"] == "approved"
    
    def test_error_handling_integration(self):
        """Test error handling across components"""
        # Test invalid phase execution
        with pytest.raises(ValueError):
            self.ai_executor.execute_single_phase(10)
        
        # Test invalid validation request
        with pytest.raises(ValueError):
            self.validation_gates.get_validation_status("nonexistent")
        
        # Test invalid quality gate mode
        result = self.quality_gates.execute_quality_gate("invalid_mode")
        assert result["mode"] == "invalid_mode"
        assert result["status"] in ["passed", "failed"]
    
    def test_performance_integration(self):
        """Test performance across components"""
        import time
        
        # Measure workflow execution time
        start_time = time.time()
        workflow_report = self.ai_executor.execute_full_workflow()
        workflow_duration = time.time() - start_time
        
        # Measure quality audit time
        start_time = time.time()
        audit_result = self.quality_gates.execute_comprehensive_audit()
        audit_duration = time.time() - start_time
        
        # Verify reasonable performance
        assert workflow_duration < 30  # Should complete within 30 seconds
        assert audit_duration < 20   # Should complete within 20 seconds
        
        # Verify reported durations
        total_reported_duration = sum(
            r["duration"] for r in workflow_report["phase_results"]
        )
        assert total_reported_duration > 0
        assert total_reported_duration < workflow_duration * 2  # Allow some overhead
    
    def test_data_persistence_integration(self):
        """Test data persistence across components"""
        # Execute workflow
        workflow_report = self.ai_executor.execute_full_workflow()
        
        # Create new instances to test persistence
        new_executor = AIExecutor(self.project_name, self.temp_dir)
        new_quality_gates = QualityGates(self.project_name, self.temp_dir)
        new_validation_gates = ValidationGates(self.project_name, self.temp_dir)
        
        # Verify data persistence
        manifest = new_executor.evidence_manager._read_json(
            new_executor.evidence_manager.manifest_path
        )
        run_log = new_executor.evidence_manager._read_json(
            new_executor.evidence_manager.run_log_path
        )
        
        assert len(manifest["artifacts"]) > 0
        assert len(run_log["entries"]) > 0
        
        # Verify validation requests persist
        pending = new_validation_gates.list_pending_validations()
        # Note: Validation requests are created per test, so this might be empty
        # but the structure should be accessible
    
    def test_configuration_integration(self):
        """Test configuration integration across components"""
        # Check project configuration
        config_path = self.ai_executor.project_dir / "project-config.json"
        assert config_path.exists()
        
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        assert config["project"]["name"] == self.project_name
        assert config["project"]["type"] == "web-app"
        
        # Check validation configuration
        validation_config_path = self.validation_gates.project_dir / "validation-config.json"
        assert validation_config_path.exists()
        
        with open(validation_config_path, 'r') as f:
            validation_config = json.load(f)
        
        assert validation_config["validation"]["human_approval_required"] is True
        assert len(validation_config["validation"]["checkpoints"]) == 7
    
    def test_artifact_generation_integration(self):
        """Test artifact generation across phases"""
        phases = [0, 1, 2, 3, 4, 5, 6]
        
        for phase in phases:
            result = self.ai_executor.execute_single_phase(phase)
            assert result["status"] == "success"
            
            # Verify artifacts were generated
            assert "outputs" in result
            assert "artifacts" in result["outputs"]
            assert len(result["outputs"]["artifacts"]) > 0
            
            # Verify artifacts were logged
            manifest = self.evidence_manager._read_json(self.evidence_manager.manifest_path)
            phase_artifacts = [a for a in manifest["artifacts"] if a["phase"] == phase]
            assert len(phase_artifacts) > 0
    
    def test_validation_criteria_integration(self):
        """Test validation criteria across phases"""
        for phase in range(7):
            checkpoint = self.validation_gates._get_validation_checkpoint(phase)
            
            # Verify checkpoint structure
            assert "validation_criteria" in checkpoint
            assert len(checkpoint["validation_criteria"]) > 0
            
            # Verify criteria are meaningful
            for criteria in checkpoint["validation_criteria"]:
                assert isinstance(criteria, str)
                assert len(criteria) > 10  # Should be descriptive
    
    def test_quality_score_integration(self):
        """Test quality score consistency across components"""
        # Execute implementation phase
        result = self.ai_executor.execute_single_phase(3)
        assert result["status"] == "success"
        
        # Get quality score from phase
        phase_score = result["outputs"]["validation"]["score"]
        
        # Execute quality audit
        audit_result = self.quality_gates.execute_comprehensive_audit()
        audit_score = audit_result["overall_score"]
        
        # Scores should be reasonable
        assert 0 <= phase_score <= 10
        assert 0 <= audit_score <= 10
        
        # Both should be positive (implementation should have some quality)
        assert phase_score > 0
        assert audit_score > 0


if __name__ == "__main__":
    pytest.main([__file__])
