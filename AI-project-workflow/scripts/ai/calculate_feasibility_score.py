#!/usr/bin/env python3
"""
Script: calculate_feasibility_score.py
Protocol: 06-ai-use-case-definition
Purpose: Calculate the Problem-AI Fit Score for feasibility assessment
Author: AI Workflow System
Created: 2025-01-06
"""

import json
import logging
from typing import Dict, List, Optional
from pathlib import Path
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FeasibilityScoreCalculator:
    """Calculate Problem-AI Fit Score for AI project feasibility"""
    
    def __init__(self, workspace_path: str):
        self.workspace = Path(workspace_path)
        self.artifacts_dir = self.workspace / ".artifacts" / "protocol-06"
        self.artifacts_dir.mkdir(parents=True, exist_ok=True)
        
        # Scoring weights
        self.weights = {
            'data': 0.30,
            'technical': 0.25,
            'business': 0.25,
            'complexity': 0.20
        }
        
        # Risk thresholds
        self.risk_thresholds = {
            'high': 0.6,
            'medium': 0.8,
            'low': 0.9
        }
        
    def execute(self, **kwargs) -> Dict:
        """
        Calculate feasibility score
        
        Args:
            data_assessment: JSON with data scores
            technical_assessment: JSON with technical scores
            business_assessment: JSON with business scores
            complexity_assessment: JSON with complexity scores
            
        Returns:
            Dict: Feasibility scores and recommendation
        """
        try:
            # Extract assessments
            data_assessment = kwargs.get('data_assessment', {})
            technical_assessment = kwargs.get('technical_assessment', {})
            business_assessment = kwargs.get('business_assessment', {})
            complexity_assessment = kwargs.get('complexity_assessment', {})
            
            # Calculate individual scores
            data_score = self._calculate_data_score(data_assessment)
            technical_score = self._calculate_technical_score(technical_assessment)
            business_score = self._calculate_business_score(business_assessment)
            complexity_score = self._calculate_complexity_score(complexity_assessment)
            
            # Calculate overall score
            overall_score = (
                data_score * self.weights['data'] +
                technical_score * self.weights['technical'] +
                business_score * self.weights['business'] +
                complexity_score * self.weights['complexity']
            )
            
            # Generate recommendation
            recommendation = self._generate_recommendation(overall_score)
            
            # Identify risk factors
            risk_factors = self._identify_risks(
                data_score, technical_score, business_score, complexity_score
            )
            
            # Suggest mitigation strategies
            mitigation_strategies = self._suggest_mitigations(risk_factors)
            
            result = {
                "overall_score": round(overall_score, 3),
                "data_score": round(data_score, 3),
                "technical_score": round(technical_score, 3),
                "business_score": round(business_score, 3),
                "complexity_score": round(complexity_score, 3),
                "recommendation": recommendation,
                "risk_factors": risk_factors,
                "mitigation_strategies": mitigation_strategies,
                "confidence_level": self._calculate_confidence(overall_score),
                "detailed_assessment": self._create_detailed_assessment(
                    data_assessment, technical_assessment, 
                    business_assessment, complexity_assessment
                )
            }
            
            # Generate evidence
            self._generate_evidence(result, kwargs)
            
            return {
                "status": "success",
                "result": result,
                "artifacts": self._list_artifacts()
            }
            
        except Exception as e:
            logger.error(f"Feasibility calculation failed: {e}")
            return {
                "status": "error",
                "error": str(e)
            }
    
    def _calculate_data_score(self, assessment: Dict) -> float:
        """Calculate data feasibility score"""
        score = 0.0
        
        # Data availability (40% of data score)
        availability = assessment.get('availability', 'low')
        availability_scores = {'high': 1.0, 'medium': 0.7, 'low': 0.3}
        score += availability_scores.get(availability, 0.3) * 0.4
        
        # Data quality (30% of data score)
        quality = assessment.get('quality', 'low')
        quality_scores = {'high': 1.0, 'medium': 0.6, 'low': 0.2}
        score += quality_scores.get(quality, 0.2) * 0.3
        
        # Data volume (20% of data score)
        volume = assessment.get('volume', 'insufficient')
        volume_scores = {'abundant': 1.0, 'sufficient': 0.8, 'minimal': 0.5, 'insufficient': 0.2}
        score += volume_scores.get(volume, 0.2) * 0.2
        
        # Data privacy/compliance (10% of data score)
        compliance = assessment.get('compliance_ready', False)
        score += (1.0 if compliance else 0.5) * 0.1
        
        return min(1.0, score)
    
    def _calculate_technical_score(self, assessment: Dict) -> float:
        """Calculate technical feasibility score"""
        score = 0.0
        
        # Computational resources (30% of technical score)
        resources = assessment.get('resources', 'limited')
        resource_scores = {'abundant': 1.0, 'adequate': 0.8, 'limited': 0.4, 'insufficient': 0.1}
        score += resource_scores.get(resources, 0.4) * 0.3
        
        # Team expertise (35% of technical score)
        expertise = assessment.get('expertise', 'none')
        expertise_scores = {'expert': 1.0, 'experienced': 0.8, 'moderate': 0.5, 'beginner': 0.3, 'none': 0.1}
        score += expertise_scores.get(expertise, 0.1) * 0.35
        
        # Integration complexity (20% of technical score)
        integration = assessment.get('integration_complexity', 'high')
        integration_scores = {'low': 1.0, 'medium': 0.7, 'high': 0.4, 'very_high': 0.1}
        score += integration_scores.get(integration, 0.4) * 0.2
        
        # Technology maturity (15% of technical score)
        maturity = assessment.get('tech_maturity', 'experimental')
        maturity_scores = {'production': 1.0, 'stable': 0.8, 'beta': 0.5, 'experimental': 0.2}
        score += maturity_scores.get(maturity, 0.2) * 0.15
        
        return min(1.0, score)
    
    def _calculate_business_score(self, assessment: Dict) -> float:
        """Calculate business feasibility score"""
        score = 0.0
        
        # ROI potential (35% of business score)
        roi = assessment.get('roi_potential', 'negative')
        roi_scores = {'high': 1.0, 'positive': 0.8, 'neutral': 0.5, 'negative': 0.2}
        score += roi_scores.get(roi, 0.2) * 0.35
        
        # Timeline alignment (25% of business score)
        timeline = assessment.get('timeline_fit', 'poor')
        timeline_scores = {'perfect': 1.0, 'good': 0.8, 'acceptable': 0.6, 'tight': 0.4, 'poor': 0.2}
        score += timeline_scores.get(timeline, 0.2) * 0.25
        
        # Budget availability (25% of business score)
        budget = assessment.get('budget_status', 'insufficient')
        budget_scores = {'abundant': 1.0, 'sufficient': 0.8, 'tight': 0.5, 'insufficient': 0.2}
        score += budget_scores.get(budget, 0.2) * 0.25
        
        # Stakeholder buy-in (15% of business score)
        stakeholder = assessment.get('stakeholder_support', 'low')
        stakeholder_scores = {'strong': 1.0, 'moderate': 0.7, 'weak': 0.4, 'low': 0.2}
        score += stakeholder_scores.get(stakeholder, 0.2) * 0.15
        
        return min(1.0, score)
    
    def _calculate_complexity_score(self, assessment: Dict) -> float:
        """Calculate problem complexity score (inverse - lower complexity = higher score)"""
        score = 1.0  # Start with perfect score
        
        # Problem complexity (40% weight)
        problem_complexity = assessment.get('problem_complexity', 'high')
        complexity_penalties = {'low': 0.0, 'medium': 0.2, 'high': 0.4, 'very_high': 0.6}
        score -= complexity_penalties.get(problem_complexity, 0.4) * 0.4
        
        # Data complexity (25% weight)
        data_complexity = assessment.get('data_complexity', 'high')
        score -= complexity_penalties.get(data_complexity, 0.4) * 0.25
        
        # Solution complexity (25% weight)
        solution_complexity = assessment.get('solution_complexity', 'high')
        score -= complexity_penalties.get(solution_complexity, 0.4) * 0.25
        
        # Uncertainty level (10% weight)
        uncertainty = assessment.get('uncertainty', 'high')
        uncertainty_penalties = {'low': 0.0, 'medium': 0.3, 'high': 0.6, 'very_high': 0.9}
        score -= uncertainty_penalties.get(uncertainty, 0.6) * 0.1
        
        return max(0.0, score)
    
    def _generate_recommendation(self, score: float) -> str:
        """Generate recommendation based on score"""
        if score >= 0.9:
            return "strongly_proceed"
        elif score >= 0.8:
            return "proceed"
        elif score >= 0.7:
            return "proceed_with_caution"
        elif score >= 0.6:
            return "reconsider"
        else:
            return "reject"
    
    def _identify_risks(self, data: float, technical: float, business: float, complexity: float) -> List[str]:
        """Identify risk factors based on scores"""
        risks = []
        
        # Data risks
        if data < 0.6:
            risks.append("critical_data_insufficiency")
        elif data < 0.8:
            risks.append("data_quality_concerns")
            
        # Technical risks
        if technical < 0.5:
            risks.append("severe_technical_limitations")
        elif technical < 0.7:
            risks.append("technical_capability_gaps")
            
        # Business risks
        if business < 0.5:
            risks.append("poor_business_case")
        elif business < 0.7:
            risks.append("business_alignment_issues")
            
        # Complexity risks
        if complexity < 0.5:
            risks.append("excessive_complexity")
        elif complexity < 0.7:
            risks.append("high_implementation_difficulty")
            
        # Combined risks
        if data < 0.7 and technical < 0.7:
            risks.append("compound_data_technical_risk")
            
        if business < 0.7 and complexity < 0.7:
            risks.append("business_complexity_mismatch")
            
        return risks
    
    def _suggest_mitigations(self, risks: List[str]) -> Dict[str, str]:
        """Suggest mitigation strategies for identified risks"""
        mitigations = {}
        
        mitigation_map = {
            "critical_data_insufficiency": "Invest in data collection or consider synthetic data generation",
            "data_quality_concerns": "Implement data cleaning pipeline and quality assurance processes",
            "severe_technical_limitations": "Consider cloud resources or external expertise",
            "technical_capability_gaps": "Provide team training or hire specialized talent",
            "poor_business_case": "Refine scope to improve ROI or consider pilot project",
            "business_alignment_issues": "Conduct stakeholder workshops to align expectations",
            "excessive_complexity": "Simplify approach or break into phases",
            "high_implementation_difficulty": "Consider proof-of-concept before full implementation",
            "compound_data_technical_risk": "Address data issues first, then scale technical resources",
            "business_complexity_mismatch": "Adjust timeline and budget to match complexity"
        }
        
        for risk in risks:
            if risk in mitigation_map:
                mitigations[risk] = mitigation_map[risk]
                
        return mitigations
    
    def _calculate_confidence(self, score: float) -> str:
        """Calculate confidence level in the assessment"""
        if score >= 0.85:
            return "high"
        elif score >= 0.70:
            return "medium"
        else:
            return "low"
    
    def _create_detailed_assessment(self, data: Dict, technical: Dict, 
                                   business: Dict, complexity: Dict) -> Dict:
        """Create detailed assessment breakdown"""
        return {
            "data_assessment": {
                "strengths": self._identify_strengths(data),
                "weaknesses": self._identify_weaknesses(data),
                "details": data
            },
            "technical_assessment": {
                "strengths": self._identify_strengths(technical),
                "weaknesses": self._identify_weaknesses(technical),
                "details": technical
            },
            "business_assessment": {
                "strengths": self._identify_strengths(business),
                "weaknesses": self._identify_weaknesses(business),
                "details": business
            },
            "complexity_assessment": {
                "manageable_aspects": self._identify_manageable(complexity),
                "challenging_aspects": self._identify_challenging(complexity),
                "details": complexity
            }
        }
    
    def _identify_strengths(self, assessment: Dict) -> List[str]:
        """Identify strengths in assessment"""
        strengths = []
        positive_indicators = {
            'availability': 'high',
            'quality': 'high',
            'volume': 'abundant',
            'resources': 'abundant',
            'expertise': 'expert',
            'roi_potential': 'high',
            'stakeholder_support': 'strong'
        }
        
        for key, value in assessment.items():
            if key in positive_indicators and value == positive_indicators[key]:
                strengths.append(key)
                
        return strengths
    
    def _identify_weaknesses(self, assessment: Dict) -> List[str]:
        """Identify weaknesses in assessment"""
        weaknesses = []
        negative_indicators = {
            'availability': 'low',
            'quality': 'low',
            'volume': 'insufficient',
            'resources': 'insufficient',
            'expertise': 'none',
            'roi_potential': 'negative',
            'stakeholder_support': 'low'
        }
        
        for key, value in assessment.items():
            if key in negative_indicators and value == negative_indicators[key]:
                weaknesses.append(key)
                
        return weaknesses
    
    def _identify_manageable(self, complexity: Dict) -> List[str]:
        """Identify manageable complexity aspects"""
        manageable = []
        for key, value in complexity.items():
            if value in ['low', 'medium']:
                manageable.append(key)
        return manageable
    
    def _identify_challenging(self, complexity: Dict) -> List[str]:
        """Identify challenging complexity aspects"""
        challenging = []
        for key, value in complexity.items():
            if value in ['high', 'very_high']:
                challenging.append(key)
        return challenging
    
    def _generate_evidence(self, result: Dict, inputs: Dict) -> None:
        """Generate evidence artifacts"""
        timestamp = datetime.now().isoformat()
        
        # Save feasibility report
        report_file = self.artifacts_dir / "feasibility-report.json"
        report_data = {
            "timestamp": timestamp,
            "problem_id": inputs.get('problem_id', 'unknown'),
            "scores": {
                "overall": result['overall_score'],
                "data": result['data_score'],
                "technical": result['technical_score'],
                "business": result['business_score'],
                "complexity": result['complexity_score']
            },
            "assessment_details": result['detailed_assessment'],
            "recommendation": result['recommendation'],
            "risks": result['risk_factors'],
            "mitigations": result['mitigation_strategies']
        }
        
        with open(report_file, 'w') as f:
            json.dump(report_data, f, indent=2)
        
        # Generate markdown report
        md_report = self.artifacts_dir / "feasibility-analysis.md"
        with open(md_report, 'w') as f:
            f.write("# AI Project Feasibility Analysis\n\n")
            f.write(f"**Generated**: {timestamp}\n\n")
            f.write("## Executive Summary\n")
            f.write(f"- **Overall Score**: {result['overall_score']:.2f}/1.00\n")
            f.write(f"- **Recommendation**: {result['recommendation'].replace('_', ' ').title()}\n")
            f.write(f"- **Confidence Level**: {result['confidence_level'].title()}\n\n")
            
            f.write("## Score Breakdown\n")
            f.write(f"- Data Feasibility: {result['data_score']:.2f}\n")
            f.write(f"- Technical Feasibility: {result['technical_score']:.2f}\n")
            f.write(f"- Business Feasibility: {result['business_score']:.2f}\n")
            f.write(f"- Complexity Score: {result['complexity_score']:.2f}\n\n")
            
            if result['risk_factors']:
                f.write("## Risk Factors\n")
                for risk in result['risk_factors']:
                    mitigation = result['mitigation_strategies'].get(risk, "No specific mitigation identified")
                    f.write(f"- **{risk.replace('_', ' ').title()}**\n")
                    f.write(f"  - Mitigation: {mitigation}\n")
    
    def _list_artifacts(self) -> List[str]:
        """List generated artifacts"""
        artifacts = []
        for file in self.artifacts_dir.glob("*"):
            artifacts.append(str(file.relative_to(self.workspace)))
        return artifacts


def main():
    """CLI entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Calculate AI project feasibility score")
    parser.add_argument("--workspace", required=True, help="Workspace path")
    parser.add_argument("--data-assessment", default="{}", help="Data assessment (JSON)")
    parser.add_argument("--technical-assessment", default="{}", help="Technical assessment (JSON)")
    parser.add_argument("--business-assessment", default="{}", help="Business assessment (JSON)")
    parser.add_argument("--complexity-assessment", default="{}", help="Complexity assessment (JSON)")
    parser.add_argument("--problem-id", default="unknown", help="Problem identifier")
    
    args = parser.parse_args()
    
    calculator = FeasibilityScoreCalculator(args.workspace)
    result = calculator.execute(
        data_assessment=json.loads(args.data_assessment),
        technical_assessment=json.loads(args.technical_assessment),
        business_assessment=json.loads(args.business_assessment),
        complexity_assessment=json.loads(args.complexity_assessment),
        problem_id=args.problem_id
    )
    
    print(json.dumps(result, indent=2))
    
if __name__ == "__main__":
    main()
