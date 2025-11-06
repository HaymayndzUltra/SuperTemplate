#!/usr/bin/env python3
"""
Script: calculate_labeling_costs.py
Protocol: 07-ai-data-strategy-planning
Purpose: Estimate costs and timeline for data labeling
Author: AI Workflow System
Created: 2025-01-06
"""

import json
import logging
from typing import Dict, List, Optional, Any, Tuple
from pathlib import Path
from datetime import datetime, timedelta
from enum import Enum
import math

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LabelingApproach(Enum):
    """Data labeling approaches"""
    IN_HOUSE = "in_house"
    CROWDSOURCING = "crowdsourcing"
    SEMI_SUPERVISED = "semi_supervised"
    ACTIVE_LEARNING = "active_learning"
    WEAK_SUPERVISION = "weak_supervision"
    HYBRID = "hybrid"


class LabelCostCalculator:
    """Calculate costs and timeline for data labeling projects"""
    
    def __init__(self, workspace_path: str):
        self.workspace = Path(workspace_path)
        self.artifacts_dir = self.workspace / ".artifacts" / "protocol-07"
        self.artifacts_dir.mkdir(parents=True, exist_ok=True)
        
        # Cost parameters by labeling approach
        self.cost_parameters = {
            LabelingApproach.IN_HOUSE: {
                'cost_per_label': 0.25,
                'setup_cost': 5000,
                'tooling_cost': 2000,
                'quality_control_cost': 0.05,  # 5% of labeling cost
                'management_overhead': 0.15,   # 15% overhead
                'labels_per_person_per_day': 200,
                'setup_time_days': 5,
                'quality_score': 0.95
            },
            LabelingApproach.CROWDSOURCING: {
                'cost_per_label': 0.08,
                'setup_cost': 2000,
                'tooling_cost': 1000,
                'quality_control_cost': 0.20,  # 20% QC needed
                'management_overhead': 0.10,   # 10% overhead
                'labels_per_person_per_day': 500,
                'setup_time_days': 2,
                'quality_score': 0.85
            },
            LabelingApproach.SEMI_SUPERVISED: {
                'cost_per_label': 0.15,
                'setup_cost': 8000,
                'tooling_cost': 5000,
                'quality_control_cost': 0.10,  # 10% QC needed
                'management_overhead': 0.20,   # 20% overhead
                'labels_per_person_per_day': 300,
                'setup_time_days': 10,
                'quality_score': 0.90
            },
            LabelingApproach.ACTIVE_LEARNING: {
                'cost_per_label': 0.18,
                'setup_cost': 10000,
                'tooling_cost': 6000,
                'quality_control_cost': 0.08,  # 8% QC needed
                'management_overhead': 0.25,   # 25% overhead
                'labels_per_person_per_day': 250,
                'setup_time_days': 15,
                'quality_score': 0.92
            },
            LabelingApproach.WEAK_SUPERVISION: {
                'cost_per_label': 0.05,
                'setup_cost': 15000,
                'tooling_cost': 8000,
                'quality_control_cost': 0.15,  # 15% QC needed
                'management_overhead': 0.30,   # 30% overhead
                'labels_per_person_per_day': 1000,  # High throughput
                'setup_time_days': 20,
                'quality_score': 0.80
            },
            LabelingApproach.HYBRID: {
                'cost_per_label': 0.12,
                'setup_cost': 7000,
                'tooling_cost': 4000,
                'quality_control_cost': 0.12,  # 12% QC needed
                'management_overhead': 0.18,   # 18% overhead
                'labels_per_person_per_day': 400,
                'setup_time_days': 12,
                'quality_score': 0.88
            }
        }
        
        # Complexity multipliers
        self.complexity_multipliers = {
            'simple': 1.0,      # Basic classification
            'moderate': 1.5,    # Multi-class, basic NLP
            'complex': 2.5,     # Complex NLP, image classification
            'very_complex': 4.0 # Medical imaging, legal documents
        }
        
        # Quality requirements impact
        self.quality_impact = {
            'basic': {'cost_multiplier': 1.0, 'time_multiplier': 1.0},
            'standard': {'cost_multiplier': 1.2, 'time_multiplier': 1.3},
            'high': {'cost_multiplier': 1.5, 'time_multiplier': 1.8},
            'expert': {'cost_multiplier': 2.0, 'time_multiplier': 2.5}
        }
    
    def execute(self, **kwargs) -> Dict:
        """
        Calculate labeling costs and timeline
        
        Args:
            labeling_requirements: Number and complexity of labels needed
            labeling_approach: Type of labeling approach
            quality_requirements: Required label quality and validation level
            
        Returns:
            Dict: Cost analysis and timeline estimation
        """
        try:
            labeling_requirements = kwargs.get('labeling_requirements', {})
            labeling_approach = kwargs.get('labeling_approach', 'in_house')
            quality_requirements = kwargs.get('quality_requirements', 'standard')
            
            # Parse inputs
            total_labels = labeling_requirements.get('total_labels', 10000)
            complexity = labeling_requirements.get('complexity', 'moderate')
            domain_expertise = labeling_requirements.get('domain_expertise_required', False)
            
            # Convert string approach to enum
            approach_enum = LabelingApproach(labeling_approach)
            
            # Calculate base costs
            base_costs = self._calculate_base_costs(
                total_labels, approach_enum, complexity, quality_requirements
            )
            
            # Calculate timeline
            timeline = self._calculate_timeline(
                total_labels, approach_enum, complexity, quality_requirements
            )
            
            # Calculate resource requirements
            resources = self._calculate_resources(
                total_labels, approach_enum, timeline
            )
            
            # Perform cost-benefit analysis
            cost_benefit = self._analyze_cost_benefit(
                base_costs, approach_enum, quality_requirements
            )
            
            # Generate recommendations
            recommendations = self._generate_recommendations(
                base_costs, timeline, resources, approach_enum
            )
            
            # Create risk assessment
            risk_assessment = self._assess_risks(
                approach_enum, total_labels, complexity, domain_expertise
            )
            
            result = {
                "total_labels_needed": total_labels,
                "labeling_approach": labeling_approach,
                "cost_analysis": base_costs,
                "timeline": timeline,
                "resource_requirements": resources,
                "cost_benefit_analysis": cost_benefit,
                "recommendations": recommendations,
                "risk_assessment": risk_assessment,
                "quality_projection": self._project_quality(
                    approach_enum, quality_requirements
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
            logger.error(f"Labeling cost calculation failed: {e}")
            return {
                "status": "error",
                "error": str(e)
            }
    
    def _calculate_base_costs(self, total_labels: int, approach: LabelingApproach,
                            complexity: str, quality: str) -> Dict:
        """Calculate base labeling costs"""
        params = self.cost_parameters[approach]
        complexity_mult = self.complexity_multipliers.get(complexity, 1.5)
        quality_mult = self.quality_impact.get(quality, self.quality_impact['standard'])
        
        # Base labeling cost
        base_labeling_cost = total_labels * params['cost_per_label'] * complexity_mult
        
        # Quality control cost
        qc_cost = base_labeling_cost * params['quality_control_cost']
        
        # Management overhead
        overhead_cost = (base_labeling_cost + qc_cost) * params['management_overhead']
        
        # Setup and tooling costs
        setup_cost = params['setup_cost'] * quality_mult['cost_multiplier']
        tooling_cost = params['tooling_cost'] * quality_mult['cost_multiplier']
        
        # Total costs
        total_labeling_cost = base_labeling_cost + qc_cost + overhead_cost
        total_project_cost = total_labeling_cost + setup_cost + tooling_cost
        
        # Cost breakdown
        cost_breakdown = {
            'base_labeling': round(base_labeling_cost, 2),
            'quality_control': round(qc_cost, 2),
            'management_overhead': round(overhead_cost, 2),
            'setup_cost': round(setup_cost, 2),
            'tooling_cost': round(tooling_cost, 2),
            'total_labeling_cost': round(total_labeling_cost, 2),
            'total_project_cost': round(total_project_cost, 2)
        }
        
        # Cost per label
        effective_cost_per_label = total_project_cost / total_labels
        
        return {
            'cost_breakdown': cost_breakdown,
            'total_cost': round(total_project_cost, 2),
            'cost_per_label': round(effective_cost_per_label, 3),
            'cost_components': {
                'variable_costs': round(base_labeling_cost + qc_cost, 2),
                'fixed_costs': round(setup_cost + tooling_cost, 2),
                'overhead_costs': round(overhead_cost, 2)
            }
        }
    
    def _calculate_timeline(self, total_labels: int, approach: LabelingApproach,
                           complexity: str, quality: str) -> Dict:
        """Calculate project timeline"""
        params = self.cost_parameters[approach]
        complexity_mult = self.complexity_multipliers.get(complexity, 1.5)
        quality_mult = self.quality_impact.get(quality, self.quality_impact['standard'])
        
        # Setup time
        setup_days = params['setup_time_days'] * quality_mult['time_multiplier']
        
        # Labeling time (assuming parallel work)
        labels_per_day = params['labels_per_person_per_day'] / complexity_mult
        labeling_days = math.ceil(total_labels / labels_per_day)
        
        # Quality control time
        qc_days = math.ceil(labeling_days * 0.2)  # 20% of labeling time
        
        # Review and validation time
        review_days = math.ceil(labeling_days * 0.1)  # 10% review time
        
        # Buffer time (20% of total)
        buffer_days = math.ceil((setup_days + labeling_days + qc_days + review_days) * 0.2)
        
        # Total timeline
        total_days = setup_days + labeling_days + qc_days + review_days + buffer_days
        
        # Convert to business days (5 days/week)
        business_days = math.ceil(total_days * 5/7)
        
        # Convert to weeks and months
        weeks = math.ceil(business_days / 5)
        months = math.ceil(weeks / 4)
        
        return {
            'timeline_breakdown': {
                'setup_days': round(setup_days, 1),
                'labeling_days': round(labeling_days, 1),
                'quality_control_days': round(qc_days, 1),
                'review_days': round(review_days, 1),
                'buffer_days': round(buffer_days, 1)
            },
            'total_calendar_days': round(total_days, 1),
            'total_business_days': business_days,
            'estimated_weeks': weeks,
            'estimated_months': months,
            'key_milestones': {
                'project_start': 'Day 0',
                'setup_complete': f'Day {round(setup_days)}',
                'labeling_start': f'Day {round(setup_days)}',
                'labeling_complete': f'Day {round(setup_days + labeling_days)}',
                'quality_control_complete': f'Day {round(setup_days + labeling_days + qc_days)}',
                'project_complete': f'Day {total_days}'
            }
        }
    
    def _calculate_resources(self, total_labels: int, approach: LabelingApproach,
                            timeline: Dict) -> Dict:
        """Calculate resource requirements"""
        params = self.cost_parameters[approach]
        labeling_days = timeline['timeline_breakdown']['labeling_days']
        
        # Number of labelers needed
        labels_per_labeler_total = params['labels_per_person_per_day'] * labeling_days
        labelers_needed = max(1, math.ceil(total_labels / labels_per_labeler_total))
        
        # Reviewers (typically 1 per 3 labelers)
        reviewers_needed = max(1, math.ceil(labelers_needed / 3))
        
        # Project managers
        managers_needed = 1 if labelers_needed <= 5 else 2
        
        # Quality assurance specialists
        qa_specialists = max(1, math.ceil(labelers_needed / 10))
        
        # Technical support
        tech_support = 1 if labelers_needed <= 10 else 2
        
        # Total team size
        total_team = labelers_needed + reviewers_needed + managers_needed + qa_specialists + tech_support
        
        # Peak resources (during main labeling phase)
        peak_resources = {
            'labelers': labelers_needed,
            'reviewers': reviewers_needed,
            'managers': managers_needed,
            'qa_specialists': qa_specialists,
            'tech_support': tech_support,
            'total_team_size': total_team
        }
        
        # Resource timeline
        resource_timeline = {
            'setup_phase': {
                'duration_days': timeline['timeline_breakdown']['setup_days'],
                'team_size': managers_needed + tech_support,
                'description': 'Project setup, tool configuration, team training'
            },
            'labeling_phase': {
                'duration_days': labeling_days,
                'team_size': total_team,
                'description': 'Main labeling work with parallel quality control'
            },
            'review_phase': {
                'duration_days': timeline['timeline_breakdown']['review_days'],
                'team_size': reviewers_needed + managers_needed,
                'description': 'Final review and validation'
            }
        }
        
        return {
            'peak_resources': peak_resources,
            'resource_timeline': resource_timeline,
            'total_person_days': total_team * timeline['total_business_days'],
            'skill_requirements': self._get_skill_requirements(approach)
        }
    
    def _analyze_cost_benefit(self, costs: Dict, approach: LabelingApproach,
                            quality: str) -> Dict:
        """Analyze cost-benefit of different approaches"""
        total_cost = costs['total_cost']
        quality_score = self.cost_parameters[approach]['quality_score']
        
        # Compare with other approaches
        approach_comparisons = []
        for other_approach in LabelingApproach:
            if other_approach != approach:
                other_params = self.cost_parameters[other_approach]
                
                # Estimate cost for same quality
                cost_multiplier = quality_score / other_params['quality_score']
                estimated_cost = total_cost * cost_multiplier * 1.1  # 10% risk premium
                
                approach_comparisons.append({
                    'approach': other_approach.value,
                    'estimated_cost': round(estimated_cost, 2),
                    'quality_score': other_params['quality_score'],
                    'cost_difference': round(estimated_cost - total_cost, 2),
                    'quality_difference': round(other_params['quality_score'] - quality_score, 3)
                })
        
        # ROI calculation (simplified)
        estimated_value_per_label = 0.5  # Business value of each labeled data point
        total_value = costs['cost_breakdown']['base_labeling'] / 0.25 * estimated_value_per_label
        roi = (total_value - total_cost) / total_cost if total_cost > 0 else 0
        
        return {
            'current_approach': {
                'total_cost': total_cost,
                'quality_score': quality_score,
                'cost_per_label': costs['cost_per_label']
            },
            'alternative_approaches': approach_comparisons,
            'roi_analysis': {
                'estimated_total_value': round(total_value, 2),
                'total_cost': total_cost,
                'roi_percentage': round(roi * 100, 1),
                'payback_period_months': round(total_cost / (total_value / 12), 1) if total_value > 0 else 0
            },
            'cost_efficiency': {
                'cost_per_quality_point': round(total_cost / quality_score, 2),
                'quality_per_cost_dollar': round(quality_score / total_cost, 6)
            }
        }
    
    def _generate_recommendations(self, costs: Dict, timeline: Dict,
                                 resources: Dict, approach: LabelingApproach) -> List[str]:
        """Generate recommendations for labeling strategy"""
        recommendations = []
        
        # Cost-based recommendations
        if costs['total_cost'] > 50000:
            recommendations.append("Consider active learning to reduce total labeling costs by 40-60%")
        
        if costs['cost_per_label'] > 0.20:
            recommendations.append("Explore crowdsourcing for cost reduction on simple labeling tasks")
        
        # Timeline-based recommendations
        if timeline['estimated_months'] > 3:
            recommendations.append("Implement phased labeling approach to accelerate time-to-value")
        
        if timeline['estimated_months'] > 6:
            recommendations.append("Consider weak supervision for initial model training")
        
        # Resource-based recommendations
        if resources['peak_resources']['total_team_size'] > 10:
            recommendations.append("Implement team scaling strategy with gradual ramp-up")
        
        # Approach-specific recommendations
        if approach == LabelingApproach.IN_HOUSE:
            recommendations.append("Invest in labeling tools to improve efficiency")
        elif approach == LabelingApproach.CROWDSOURCING:
            recommendations.append("Implement robust quality control for crowdsourced labels")
        elif approach == LabelingApproach.ACTIVE_LEARNING:
            recommendations.append("Ensure ML team capacity for active learning iteration")
        elif approach == LabelingApproach.WEAK_SUPERVISION:
            recommendations.append("Allocate resources for weak supervision rule development")
        
        # Quality recommendations
        if resources['peak_resources']['qa_specialists'] < 2:
            recommendations.append("Consider additional QA specialists for high-quality requirements")
        
        # General recommendations
        recommendations.extend([
            "Implement pilot labeling phase before full-scale deployment",
            "Establish clear labeling guidelines and examples",
            "Set up continuous monitoring of label quality",
            "Plan for label iteration and improvement cycles"
        ])
        
        return recommendations
    
    def _assess_risks(self, approach: LabelingApproach, total_labels: int,
                     complexity: str, domain_expertise: bool) -> Dict:
        """Assess risks associated with labeling approach"""
        risks = {
            'high_risk': [],
            'medium_risk': [],
            'low_risk': [],
            'mitigation_strategies': []
        }
        
        # Approach-specific risks
        if approach == LabelingApproach.IN_HOUSE:
            if total_labels > 50000:
                risks['medium_risk'].append("Team capacity constraints for large volume")
            risks['low_risk'].append("Higher per-label cost vs alternatives")
            risks['mitigation_strategies'].append("Implement team scaling plan")
            
        elif approach == LabelingApproach.CROWDSOURCING:
            risks['high_risk'].append("Quality control challenges")
            risks['medium_risk'].append("Data privacy and security concerns")
            risks['mitigation_strategies'].extend([
                "Implement multi-level quality validation",
                "Use data anonymization techniques"
            ])
            
        elif approach == LabelingApproach.ACTIVE_LEARNING:
            risks['medium_risk'].append("Technical complexity of active learning implementation")
            risks['low_risk'].append("Dependency on ML team availability")
            risks['mitigation_strategies'].append("Ensure ML team expertise and availability")
            
        elif approach == LabelingApproach.WEAK_SUPERVISION:
            risks['high_risk'].append("Lower label quality may impact model performance")
            risks['medium_risk'].append("Complex rule development and maintenance")
            risks['mitigation_strategies'].extend([
                "Plan for human validation of weak labels",
                "Invest in rule testing and validation"
            ])
        
        # Complexity risks
        if complexity in ['complex', 'very_complex']:
            risks['medium_risk'].append("High complexity may increase error rates")
        
        # Domain expertise risks
        if domain_expertise:
            risks['medium_risk'].append("Limited availability of domain experts")
            risks['mitigation_strategies'].append("Develop expert training program")
        
        # Volume risks
        if total_labels > 100000:
            risks['medium_risk'].append("Large volume increases project complexity")
            risks['mitigation_strategies'].append("Implement project management best practices")
        
        return risks
    
    def _project_quality(self, approach: LabelingApproach, quality_level: str) -> Dict:
        """Project final label quality"""
        base_quality = self.cost_parameters[approach]['quality_score']
        quality_mult = self.quality_impact.get(quality_level, self.quality_impact['standard'])
        
        # Adjust quality based on requirements
        projected_quality = min(0.99, base_quality * (1 + (quality_mult['cost_multiplier'] - 1) * 0.1))
        
        return {
            'base_quality_score': base_quality,
            'projected_quality_score': round(projected_quality, 3),
            'quality_level': quality_level,
            'confidence_interval': {
                'lower': round(projected_quality - 0.05, 3),
                'upper': min(0.99, round(projected_quality + 0.05, 3))
            }
        }
    
    def _get_skill_requirements(self, approach: LabelingApproach) -> Dict:
        """Get skill requirements for labeling approach"""
        skill_requirements = {
            'technical_skills': [],
            'domain_skills': [],
            'management_skills': [],
            'tool_expertise': []
        }
        
        if approach == LabelingApproach.IN_HOUSE:
            skill_requirements['technical_skills'] = ['Data labeling tools', 'Quality control software']
            skill_requirements['management_skills'] = ['Project management', 'Team coordination']
            
        elif approach == LabelingApproach.CROWDSOURCING:
            skill_requirements['technical_skills'] = ['Crowdsourcing platforms', 'API integration']
            skill_requirements['management_skills'] = ['Vendor management', 'Quality assurance']
            
        elif approach == LabelingApproach.ACTIVE_LEARNING:
            skill_requirements['technical_skills'] = ['Machine learning', 'Python programming', 'Active learning frameworks']
            skill_requirements['domain_skills'] = ['Statistical analysis', 'Model evaluation']
            
        elif approach == LabelingApproach.WEAK_SUPERVISION:
            skill_requirements['technical_skills'] = ['Rule development', 'Data wrangling', 'Programming']
            skill_requirements['domain_skills'] = ['Domain expertise for rule creation']
        
        skill_requirements['tool_expertise'] = ['Labeling interfaces', 'Quality control tools', 'Project management software']
        
        return skill_requirements
    
    def _generate_evidence(self, result: Dict, inputs: Dict) -> None:
        """Generate evidence artifacts"""
        timestamp = datetime.now().isoformat()
        
        # Save detailed cost analysis
        cost_file = self.artifacts_dir / "labeling-cost-analysis.json"
        cost_data = {
            "timestamp": timestamp,
            "analysis_summary": {
                "total_labels": result['total_labels_needed'],
                "labeling_approach": result['labeling_approach'],
                "total_cost": result['cost_analysis']['total_cost'],
                "cost_per_label": result['cost_analysis']['cost_per_label'],
                "estimated_duration_days": result['timeline']['total_calendar_days'],
                "projected_quality": result['quality_projection']['projected_quality_score']
            },
            "detailed_costs": result['cost_analysis'],
            "timeline": result['timeline'],
            "resources": result['resource_requirements'],
            "cost_benefit": result['cost_benefit_analysis'],
            "recommendations": result['recommendations'],
            "risk_assessment": result['risk_assessment']
        }
        
        with open(cost_file, 'w') as f:
            json.dump(cost_data, f, indent=2)
        
        # Generate markdown cost report
        md_file = self.artifacts_dir / "labeling-cost-report.md"
        with open(md_file, 'w') as f:
            f.write("# Labeling Cost Analysis Report\n\n")
            f.write(f"**Generated**: {timestamp}\n\n")
            f.write("## Executive Summary\n")
            f.write(f"- **Total Labels Required**: {result['total_labels_needed']:,}\n")
            f.write(f"- **Labeling Approach**: {result['labeling_approach'].replace('_', ' ').title()}\n")
            f.write(f"- **Total Project Cost**: ${result['cost_analysis']['total_cost']:,.2f}\n")
            f.write(f"- **Cost Per Label**: ${result['cost_analysis']['cost_per_label']:.3f}\n")
            f.write(f"- **Estimated Duration**: {result['timeline']['estimated_months']} months\n")
            f.write(f"- **Projected Quality**: {result['quality_projection']['projected_quality_score']:.1%}\n\n")
            
            f.write("## Cost Breakdown\n")
            costs = result['cost_analysis']['cost_breakdown']
            f.write(f"- **Base Labeling**: ${costs['base_labeling']:,.2f}\n")
            f.write(f"- **Quality Control**: ${costs['quality_control']:,.2f}\n")
            f.write(f"- **Management Overhead**: ${costs['management_overhead']:,.2f}\n")
            f.write(f"- **Setup Cost**: ${costs['setup_cost']:,.2f}\n")
            f.write(f"- **Tooling Cost**: ${costs['tooling_cost']:,.2f}\n\n")
            
            f.write("## Resource Requirements\n")
            resources = result['resource_requirements']['peak_resources']
            f.write(f"- **Labelers**: {resources['labelers']}\n")
            f.write(f"- **Reviewers**: {resources['reviewers']}\n")
            f.write(f"- **Managers**: {resources['managers']}\n")
            f.write(f"- **QA Specialists**: {resources['qa_specialists']}\n")
            f.write(f"- **Total Team Size**: {resources['total_team_size']}\n\n")
            
            if result['recommendations']:
                f.write("## Key Recommendations\n")
                for rec in result['recommendations'][:5]:  # Top 5 recommendations
                    f.write(f"- {rec}\n")
                f.write("\n")
            
            f.write("## Timeline\n")
            timeline = result['timeline']['timeline_breakdown']
            f.write(f"- **Setup**: {timeline['setup_days']} days\n")
            f.write(f"- **Labeling**: {timeline['labeling_days']} days\n")
            f.write(f"- **Quality Control**: {timeline['quality_control_days']} days\n")
            f.write(f"- **Review**: {timeline['review_days']} days\n")
    
    def _list_artifacts(self) -> List[str]:
        """List generated artifacts"""
        artifacts = []
        for file in self.artifacts_dir.glob("*"):
            artifacts.append(str(file.relative_to(self.workspace)))
        return artifacts


def main():
    """CLI entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Calculate labeling costs for ML project")
    parser.add_argument("--workspace", required=True, help="Workspace path")
    parser.add_argument("--labeling-requirements", required=True, help="Labeling requirements (JSON)")
    parser.add_argument("--labeling-approach", default="in_house", help="Labeling approach")
    parser.add_argument("--quality-requirements", default="standard", help="Quality requirements")
    
    args = parser.parse_args()
    
    calculator = LabelCostCalculator(args.workspace)
    result = calculator.execute(
        labeling_requirements=json.loads(args.labeling_requirements),
        labeling_approach=args.labeling_approach,
        quality_requirements=args.quality_requirements
    )
    
    print(json.dumps(result, indent=2))
    
if __name__ == "__main__":
    main()
