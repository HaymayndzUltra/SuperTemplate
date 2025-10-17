#!/usr/bin/env python3
"""
Test suite for Validation Gates

Tests human validation checkpoints, approval workflows, and evidence tracking.
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

from validation_gates import ValidationGates


class TestValidationGates:
    """Test cases for ValidationGates"""
    
    def setup_method(self):
        """Set up test environment"""
        self.temp_dir = tempfile.mkdtemp()
        self.project_name = "test-project"
        self.validation_gates = ValidationGates(self.project_name, self.temp_dir)
    
    def teardown_method(self):
        """Clean up test environment"""
        shutil.rmtree(self.temp_dir)
    
    def test_initialization(self):
        """Test ValidationGates initialization"""
        assert self.validation_gates.project_name == self.project_name
        assert self.validation_gates.project_dir.exists()
        assert self.validation_gates.evidence_manager is not None
        assert self.validation_gates.config is not None
    
    def test_validation_config_creation(self):
        """Test validation configuration creation"""
        config_path = self.validation_gates.project_dir / "validation-config.json"
        assert config_path.exists()
        
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        assert config["validation"]["human_approval_required"] is True
        assert "checkpoints" in config["validation"]
        assert len(config["validation"]["checkpoints"]) == 7
    
    def test_get_validation_checkpoint(self):
        """Test validation checkpoint retrieval"""
        checkpoint = self.validation_gates._get_validation_checkpoint(0)
        
        assert "name" in checkpoint
        assert "title" in checkpoint
        assert "description" in checkpoint
        assert "required_approvals" in checkpoint
        assert "artifacts" in checkpoint
        assert "validation_criteria" in checkpoint
        
        assert checkpoint["name"] == "phase_0_completion"
        assert len(checkpoint["required_approvals"]) > 0
        assert len(checkpoint["validation_criteria"]) > 0
    
    def test_create_validation_request(self):
        """Test validation request creation"""
        context = {"test": "value"}
        request = self.validation_gates._create_validation_request(0, context)
        
        assert "phase" in request
        assert "checkpoint" in request
        assert "context" in request
        assert "request_id" in request
        assert "created_at" in request
        assert "status" in request
        assert "approvals" in request
        assert "comments" in request
        
        assert request["phase"] == 0
        assert request["status"] == "pending"
        assert request["context"] == context
    
    def test_save_and_load_validation_request(self):
        """Test validation request save and load"""
        context = {"test": "value"}
        request = self.validation_gates._create_validation_request(0, context)
        
        # Save request
        self.validation_gates._save_validation_request(request)
        
        # Load request
        loaded_request = self.validation_gates._load_validation_request(request["request_id"])
        
        assert loaded_request is not None
        assert loaded_request["request_id"] == request["request_id"]
        assert loaded_request["phase"] == request["phase"]
        assert loaded_request["status"] == request["status"]
    
    def test_request_validation(self):
        """Test validation request creation"""
        context = {"test": "value"}
        request = self.validation_gates.request_validation(0, context)
        
        assert request["phase"] == 0
        assert request["status"] == "pending"
        assert request["context"] == context
        
        # Check that request was saved
        loaded_request = self.validation_gates._load_validation_request(request["request_id"])
        assert loaded_request is not None
    
    def test_approve_validation(self):
        """Test validation approval"""
        # Create validation request
        request = self.validation_gates.request_validation(0)
        request_id = request["request_id"]
        
        # Approve validation
        updated_request = self.validation_gates.approve_validation(
            request_id, "test_approver", True, "Test approval"
        )
        
        assert updated_request["status"] == "pending"  # Still pending until all approvals
        assert "test_approver" in updated_request["approvals"]
        assert updated_request["approvals"]["test_approver"]["approved"] is True
        assert updated_request["approvals"]["test_approver"]["comments"] == "Test approval"
    
    def test_approve_validation_complete(self):
        """Test validation approval completion"""
        # Create validation request
        request = self.validation_gates.request_validation(0)
        request_id = request["request_id"]
        
        # Get required approvers
        required_approvals = request["checkpoint"]["required_approvals"]
        
        # Approve with all required approvers
        for approver in required_approvals:
            updated_request = self.validation_gates.approve_validation(
                request_id, approver, True, f"Approval from {approver}"
            )
        
        # Check final status
        assert updated_request["status"] == "approved"
        assert "completed_at" in updated_request
    
    def test_reject_validation(self):
        """Test validation rejection"""
        # Create validation request
        request = self.validation_gates.request_validation(0)
        request_id = request["request_id"]
        
        # Reject validation
        updated_request = self.validation_gates.approve_validation(
            request_id, "test_approver", False, "Test rejection"
        )
        
        assert updated_request["status"] == "pending"  # Still pending until all approvals
        assert updated_request["approvals"]["test_approver"]["approved"] is False
        assert updated_request["approvals"]["test_approver"]["comments"] == "Test rejection"
    
    def test_get_validation_status(self):
        """Test validation status retrieval"""
        # Create validation request
        request = self.validation_gates.request_validation(0)
        request_id = request["request_id"]
        
        # Get status
        status = self.validation_gates.get_validation_status(request_id)
        
        assert "request_id" in status
        assert "phase" in status
        assert "status" in status
        assert "required_approvals" in status
        assert "received_approvals" in status
        assert "pending_approvals" in status
        assert "approval_details" in status
        assert "comments" in status
        
        assert status["request_id"] == request_id
        assert status["phase"] == 0
        assert status["status"] == "pending"
    
    def test_list_pending_validations(self):
        """Test pending validations listing"""
        # Create multiple validation requests
        request1 = self.validation_gates.request_validation(0)
        request2 = self.validation_gates.request_validation(1)
        
        # List pending validations
        pending = self.validation_gates.list_pending_validations()
        
        assert len(pending) >= 2
        
        # Check structure
        for req in pending:
            assert "request_id" in req
            assert "phase" in req
            assert "checkpoint" in req
            assert "created_at" in req
            assert "required_approvals" in req
            assert "received_approvals" in req
    
    def test_validation_request_not_found(self):
        """Test validation request not found error"""
        with pytest.raises(ValueError):
            self.validation_gates.get_validation_status("nonexistent_request_id")
    
    def test_approve_nonexistent_request(self):
        """Test approval of nonexistent request"""
        with pytest.raises(ValueError):
            self.validation_gates.approve_validation(
                "nonexistent_request_id", "approver", True
            )
    
    def test_approve_completed_request(self):
        """Test approval of completed request"""
        # Create and complete validation request
        request = self.validation_gates.request_validation(0)
        request_id = request["request_id"]
        
        # Complete the request
        required_approvals = request["checkpoint"]["required_approvals"]
        for approver in required_approvals:
            self.validation_gates.approve_validation(request_id, approver, True)
        
        # Try to approve again
        with pytest.raises(ValueError):
            self.validation_gates.approve_validation(request_id, "extra_approver", True)
    
    def test_evidence_logging(self):
        """Test evidence logging during validation"""
        # Create validation request
        request = self.validation_gates.request_validation(0)
        
        # Check that evidence was logged
        run_log = self.validation_gates.evidence_manager._read_json(
            self.validation_gates.evidence_manager.run_log_path
        )
        
        assert len(run_log["entries"]) > 0
        
        # Verify validation evidence
        validation_entries = [e for e in run_log["entries"] if "Validation" in e["action"]]
        assert len(validation_entries) > 0
    
    def test_validation_checkpoints_all_phases(self):
        """Test validation checkpoints for all phases"""
        for phase in range(7):
            checkpoint = self.validation_gates._get_validation_checkpoint(phase)
            
            assert "name" in checkpoint
            assert "title" in checkpoint
            assert "description" in checkpoint
            assert "required_approvals" in checkpoint
            assert "artifacts" in checkpoint
            assert "validation_criteria" in checkpoint
            
            assert checkpoint["name"] in [f"phase_{phase}_completion", f"phase_{phase}_approval", f"phase_{phase}_confirmation", f"phase_{phase}_review", f"phase_{phase}_audit_results", f"phase_{phase}_retrospective", f"phase_{phase}_operations_readiness", f"phase_{phase}_validation"]
            assert len(checkpoint["required_approvals"]) > 0
            assert len(checkpoint["validation_criteria"]) > 0
    
    def test_validation_request_structure(self):
        """Test validation request structure"""
        request = self.validation_gates.request_validation(0)
        
        # Check required fields
        required_fields = [
            "phase", "checkpoint", "context", "request_id", 
            "created_at", "status", "approvals", "comments"
        ]
        
        for field in required_fields:
            assert field in request
        
        # Check checkpoint structure
        checkpoint = request["checkpoint"]
        checkpoint_fields = [
            "name", "title", "description", "required_approvals",
            "artifacts", "validation_criteria"
        ]
        
        for field in checkpoint_fields:
            assert field in checkpoint
        
        # Check initial state
        assert request["status"] == "pending"
        assert len(request["approvals"]) == 0
        assert len(request["comments"]) == 0


if __name__ == "__main__":
    pytest.main([__file__])
