#!/usr/bin/env python3
"""
Validation script to verify completion of all 4 sessions.
Checks if all protocols and validators exist as specified in SESSION-PROMPTS.md
"""

import os
from pathlib import Path
from typing import Dict, List, Tuple

class SessionValidator:
    def __init__(self):
        self.base_path = Path("/home/haymayndz/SuperTemplate")
        self.protocols_path = self.base_path / "AI-project-workflow" / "protocols"
        self.validators_path = self.base_path / "validators-system"
        
        self.results = {
            'session_1': {'protocols': [], 'validators': [], 'complete': False},
            'session_2': {'protocols': [], 'validators': [], 'complete': False},
            'session_3': {'protocols': [], 'validators': [], 'complete': False},
            'session_4': {'protocols': [], 'validators': [], 'complete': False}
        }
    
    def validate_session_1(self) -> Dict:
        """Validate Session 1: Protocols 13-14"""
        print("\n🔍 Validating SESSION 1: Phase 3 Model Development")
        print("=" * 60)
        
        protocols = [
            "13-ai-algorithm-selection-baseline.md",
            "14-ai-model-validation-evaluation.md"
        ]
        
        validators = [
            "13-algorithm-selection/validate_algorithm_selection.py",
            "14-model-validation/validate_model_validation.py"
        ]
        
        return self._check_session(protocols, validators, 'session_1')
    
    def validate_session_2(self) -> Dict:
        """Validate Session 2: Protocols 15-17"""
        print("\n🔍 Validating SESSION 2: Phase 4 Testing & QA")
        print("=" * 60)
        
        protocols = [
            "15-ai-model-testing-edge-case-validation.md",
            "16-ai-bias-detection-fairness-audit.md",
            "17-ai-model-explainability-interpretability.md"
        ]
        
        validators = [
            "15-model-testing/validate_testing.py",
            "16-bias-fairness/validate_fairness.py",
            "17-explainability/validate_explainability.py"
        ]
        
        return self._check_session(protocols, validators, 'session_2')
    
    def validate_session_3(self) -> Dict:
        """Validate Session 3: Protocols 18-21"""
        print("\n🔍 Validating SESSION 3: Phase 5 MLOps & Deployment")
        print("=" * 60)
        
        protocols = [
            "18-ai-model-packaging-containerization.md",
            "19-ai-ml-pipeline-orchestration.md",
            "20-ai-model-deployment-serving.md",
            "21-ai-production-integration-api-development.md"
        ]
        
        validators = [
            "18-packaging/validate_packaging.py",
            "19-orchestration/validate_orchestration.py",
            "20-deployment/validate_deployment.py",
            "21-api-integration/validate_api.py"
        ]
        
        return self._check_session(protocols, validators, 'session_3')
    
    def validate_session_4(self) -> Dict:
        """Validate Session 4: Protocols 22-28"""
        print("\n🔍 Validating SESSION 4: Phase 6 Monitoring & Governance")
        print("=" * 60)
        
        protocols = [
            "22-ai-model-performance-monitoring.md",
            "23-ai-data-drift-concept-drift-detection.md",
            "24-ai-model-retraining-update-pipeline.md",
            "25-ai-incident-response-model-rollback.md",
            "26-ai-model-governance-audit-trail.md",
            "27-ai-documentation-knowledge-transfer.md",
            "28-ai-project-retrospective-continuous-improvement.md"
        ]
        
        validators = [
            "22-performance-monitoring/validate_monitoring.py",
            "23-drift-detection/validate_drift.py",
            "24-retraining/validate_retraining.py",
            "25-incident-response/validate_incident.py",
            "26-governance/validate_governance.py",
            "27-documentation/validate_docs.py",
            "28-retrospective/validate_retrospective.py"
        ]
        
        return self._check_session(protocols, validators, 'session_4')
    
    def _check_session(self, protocols: List[str], validators: List[str], session_key: str) -> Dict:
        """Check if all protocols and validators exist for a session"""
        
        protocol_results = []
        validator_results = []
        
        # Check protocols
        print("\n📄 Checking Protocols:")
        for protocol in protocols:
            protocol_path = self.protocols_path / protocol
            exists = protocol_path.exists()
            status = "✅" if exists else "❌"
            print(f"  {status} {protocol}")
            protocol_results.append({
                'file': protocol,
                'exists': exists,
                'path': str(protocol_path)
            })
        
        # Check validators
        print("\n🔧 Checking Validators:")
        for validator in validators:
            validator_path = self.validators_path / validator
            exists = validator_path.exists()
            status = "✅" if exists else "❌"
            print(f"  {status} {validator}")
            validator_results.append({
                'file': validator,
                'exists': exists,
                'path': str(validator_path)
            })
        
        # Calculate completion
        protocols_complete = all(p['exists'] for p in protocol_results)
        validators_complete = all(v['exists'] for v in validator_results)
        session_complete = protocols_complete and validators_complete
        
        self.results[session_key] = {
            'protocols': protocol_results,
            'validators': validator_results,
            'protocols_complete': protocols_complete,
            'validators_complete': validators_complete,
            'complete': session_complete
        }
        
        # Print summary
        protocols_count = sum(1 for p in protocol_results if p['exists'])
        validators_count = sum(1 for v in validator_results if v['exists'])
        
        print(f"\n📊 Session Summary:")
        print(f"  Protocols: {protocols_count}/{len(protocols)} {'✅' if protocols_complete else '❌'}")
        print(f"  Validators: {validators_count}/{len(validators)} {'✅' if validators_complete else '❌'}")
        print(f"  Status: {'✅ COMPLETE' if session_complete else '❌ INCOMPLETE'}")
        
        return self.results[session_key]
    
    def generate_missing_files_report(self) -> List[str]:
        """Generate list of missing files"""
        missing = []
        
        for session_key, session_data in self.results.items():
            for protocol in session_data.get('protocols', []):
                if not protocol['exists']:
                    missing.append(f"Protocol: {protocol['file']}")
            
            for validator in session_data.get('validators', []):
                if not validator['exists']:
                    missing.append(f"Validator: {validator['file']}")
        
        return missing
    
    def print_final_report(self):
        """Print final validation report"""
        print("\n" + "=" * 60)
        print("📋 FINAL VALIDATION REPORT")
        print("=" * 60)
        
        total_protocols = 0
        complete_protocols = 0
        total_validators = 0
        complete_validators = 0
        
        for session_key, session_data in self.results.items():
            session_num = session_key.split('_')[1]
            status = "✅ COMPLETE" if session_data['complete'] else "❌ INCOMPLETE"
            print(f"\nSession {session_num}: {status}")
            
            protocols = session_data.get('protocols', [])
            validators = session_data.get('validators', [])
            
            total_protocols += len(protocols)
            complete_protocols += sum(1 for p in protocols if p['exists'])
            
            total_validators += len(validators)
            complete_validators += sum(1 for v in validators if v['exists'])
        
        print(f"\n{'=' * 60}")
        print("📊 OVERALL STATISTICS")
        print(f"{'=' * 60}")
        print(f"Protocols: {complete_protocols}/{total_protocols} ({complete_protocols/total_protocols*100:.1f}%)")
        print(f"Validators: {complete_validators}/{total_validators} ({complete_validators/total_validators*100:.1f}%)")
        
        # Check if all complete
        all_complete = complete_protocols == total_protocols and complete_validators == total_validators
        
        if all_complete:
            print(f"\n{'🎉' * 20}")
            print("✅ ALL 4 SESSIONS COMPLETE!")
            print(f"{'🎉' * 20}")
        else:
            print(f"\n{'⚠️' * 20}")
            print("❌ INCOMPLETE - Missing files detected")
            print(f"{'⚠️' * 20}")
            
            missing = self.generate_missing_files_report()
            if missing:
                print(f"\n📝 Missing Files ({len(missing)}):")
                for item in missing:
                    print(f"  ❌ {item}")
        
        return all_complete
    
    def run_full_validation(self) -> bool:
        """Run validation for all sessions"""
        print("🚀 Starting Full Validation of All 4 Sessions")
        print("=" * 60)
        
        self.validate_session_1()
        self.validate_session_2()
        self.validate_session_3()
        self.validate_session_4()
        
        return self.print_final_report()


def main():
    validator = SessionValidator()
    all_complete = validator.run_full_validation()
    
    # Exit with appropriate code
    exit(0 if all_complete else 1)


if __name__ == "__main__":
    main()
