#!/usr/bin/env python3
"""
Script: generate_success_metrics.py
Protocol: 06-ai-use-case-definition
Purpose: Generate recommended success metrics based on problem type
Author: AI Workflow System
Created: 2025-01-06
"""

import json
import logging
from typing import Dict, List, Optional, Any
from pathlib import Path
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SuccessMetricsGenerator:
    """Generate success metrics for AI/ML projects based on problem type"""
    
    def __init__(self, workspace_path: str):
        self.workspace = Path(workspace_path)
        self.artifacts_dir = self.workspace / ".artifacts" / "protocol-06"
        self.artifacts_dir.mkdir(parents=True, exist_ok=True)
        
        # Metric definitions by problem type
        self.metric_definitions = {
            'classification': {
                'binary': {
                    'primary': 'f1_score',
                    'secondary': ['accuracy', 'precision', 'recall', 'auc_roc'],
                    'class_imbalance': ['balanced_accuracy', 'matthews_correlation'],
                    'thresholds': {
                        'f1_score': {'excellent': 0.9, 'good': 0.8, 'acceptable': 0.7},
                        'accuracy': {'excellent': 0.95, 'good': 0.9, 'acceptable': 0.85},
                        'precision': {'excellent': 0.9, 'good': 0.85, 'acceptable': 0.8},
                        'recall': {'excellent': 0.9, 'good': 0.85, 'acceptable': 0.8},
                        'auc_roc': {'excellent': 0.95, 'good': 0.9, 'acceptable': 0.85}
                    }
                },
                'multiclass': {
                    'primary': 'macro_f1',
                    'secondary': ['accuracy', 'weighted_f1', 'cohen_kappa'],
                    'per_class': ['precision_per_class', 'recall_per_class'],
                    'thresholds': {
                        'macro_f1': {'excellent': 0.85, 'good': 0.75, 'acceptable': 0.65},
                        'accuracy': {'excellent': 0.9, 'good': 0.85, 'acceptable': 0.8},
                        'weighted_f1': {'excellent': 0.85, 'good': 0.75, 'acceptable': 0.65}
                    }
                },
                'multilabel': {
                    'primary': 'hamming_loss',
                    'secondary': ['subset_accuracy', 'micro_f1', 'macro_f1'],
                    'ranking': ['coverage_error', 'label_ranking_loss'],
                    'thresholds': {
                        'hamming_loss': {'excellent': 0.05, 'good': 0.1, 'acceptable': 0.15},
                        'subset_accuracy': {'excellent': 0.8, 'good': 0.7, 'acceptable': 0.6}
                    }
                }
            },
            'regression': {
                'standard': {
                    'primary': 'rmse',
                    'secondary': ['mae', 'r2_score', 'mape'],
                    'robustness': ['median_absolute_error', 'max_error'],
                    'thresholds': {
                        'r2_score': {'excellent': 0.9, 'good': 0.8, 'acceptable': 0.7},
                        'mape': {'excellent': 0.05, 'good': 0.1, 'acceptable': 0.15}
                    }
                },
                'time_series': {
                    'primary': 'mape',
                    'secondary': ['rmse', 'mae', 'smape'],
                    'directional': ['directional_accuracy', 'sign_accuracy'],
                    'thresholds': {
                        'mape': {'excellent': 0.05, 'good': 0.1, 'acceptable': 0.2},
                        'directional_accuracy': {'excellent': 0.8, 'good': 0.7, 'acceptable': 0.6}
                    }
                }
            },
            'clustering': {
                'partitioning': {
                    'primary': 'silhouette_score',
                    'secondary': ['calinski_harabasz', 'davies_bouldin'],
                    'stability': ['adjusted_rand_index', 'normalized_mutual_info'],
                    'thresholds': {
                        'silhouette_score': {'excellent': 0.7, 'good': 0.5, 'acceptable': 0.3},
                        'davies_bouldin': {'excellent': 0.5, 'good': 1.0, 'acceptable': 1.5}
                    }
                }
            },
            'nlp': {
                'classification': {
                    'primary': 'f1_score',
                    'secondary': ['accuracy', 'precision', 'recall'],
                    'semantic': ['bleu_score', 'rouge_score'],
                    'thresholds': {
                        'f1_score': {'excellent': 0.85, 'good': 0.75, 'acceptable': 0.65}
                    }
                },
                'generation': {
                    'primary': 'perplexity',
                    'secondary': ['bleu_score', 'rouge_l', 'meteor'],
                    'human_eval': ['fluency', 'coherence', 'relevance'],
                    'thresholds': {
                        'perplexity': {'excellent': 20, 'good': 50, 'acceptable': 100},
                        'bleu_score': {'excellent': 0.6, 'good': 0.4, 'acceptable': 0.2}
                    }
                }
            },
            'computer_vision': {
                'detection': {
                    'primary': 'map',
                    'secondary': ['precision', 'recall', 'f1_score'],
                    'iou_based': ['map_50', 'map_75', 'map_50_95'],
                    'thresholds': {
                        'map': {'excellent': 0.7, 'good': 0.5, 'acceptable': 0.3},
                        'map_50': {'excellent': 0.8, 'good': 0.6, 'acceptable': 0.4}
                    }
                },
                'segmentation': {
                    'primary': 'mean_iou',
                    'secondary': ['pixel_accuracy', 'dice_coefficient'],
                    'per_class': ['iou_per_class', 'dice_per_class'],
                    'thresholds': {
                        'mean_iou': {'excellent': 0.7, 'good': 0.5, 'acceptable': 0.3},
                        'dice_coefficient': {'excellent': 0.8, 'good': 0.6, 'acceptable': 0.4}
                    }
                }
            }
        }
        
        # Business metric templates
        self.business_metrics = {
            'cost_reduction': {
                'unit': 'percentage',
                'direction': 'decrease',
                'typical_range': [10, 50]
            },
            'revenue_increase': {
                'unit': 'percentage',
                'direction': 'increase',
                'typical_range': [5, 30]
            },
            'processing_time': {
                'unit': 'percentage_reduction',
                'direction': 'decrease',
                'typical_range': [20, 80]
            },
            'accuracy_improvement': {
                'unit': 'percentage_points',
                'direction': 'increase',
                'typical_range': [5, 25]
            },
            'user_satisfaction': {
                'unit': 'nps_points',
                'direction': 'increase',
                'typical_range': [10, 40]
            },
            'operational_efficiency': {
                'unit': 'percentage',
                'direction': 'increase',
                'typical_range': [15, 60]
            }
        }
    
    def execute(self, **kwargs) -> Dict:
        """
        Generate success metrics based on problem type
        
        Args:
            problem_type: Classification type from problem classification
            business_goals: List of business objectives
            baseline_performance: Current performance data
            
        Returns:
            Dict: Recommended metrics with thresholds
        """
        try:
            problem_type = kwargs.get('problem_type', 'classification')
            subtype = kwargs.get('subtype', 'standard')
            business_goals = kwargs.get('business_goals', [])
            baseline_performance = kwargs.get('baseline_performance', {})
            industry_context = kwargs.get('industry_context', 'general')
            
            # Generate technical metrics
            technical_metrics = self._generate_technical_metrics(problem_type, subtype)
            
            # Generate business metrics
            business_metrics = self._generate_business_metrics(business_goals, industry_context)
            
            # Calculate thresholds based on baseline
            thresholds = self._calculate_thresholds(
                technical_metrics, baseline_performance, problem_type, subtype
            )
            
            # Generate monitoring strategy
            monitoring_strategy = self._generate_monitoring_strategy(
                technical_metrics, business_metrics
            )
            
            # Create evaluation framework
            evaluation_framework = self._create_evaluation_framework(
                technical_metrics, business_metrics, monitoring_strategy
            )
            
            result = {
                "technical_metrics": technical_metrics,
                "business_metrics": business_metrics,
                "thresholds": thresholds,
                "baseline": self._process_baseline(baseline_performance),
                "monitoring_strategy": monitoring_strategy,
                "evaluation_framework": evaluation_framework,
                "recommended_tools": self._recommend_tools(problem_type),
                "reporting_frequency": self._determine_reporting_frequency(business_goals)
            }
            
            # Generate evidence
            self._generate_evidence(result, kwargs)
            
            return {
                "status": "success",
                "result": result,
                "artifacts": self._list_artifacts()
            }
            
        except Exception as e:
            logger.error(f"Metrics generation failed: {e}")
            return {
                "status": "error",
                "error": str(e)
            }
    
    def _generate_technical_metrics(self, problem_type: str, subtype: str) -> Dict:
        """Generate technical metrics based on problem type"""
        # Map problem type to metric category
        if 'classification' in problem_type:
            category = 'classification'
        elif 'regression' in problem_type:
            category = 'regression'
        elif 'clustering' in problem_type:
            category = 'clustering'
        elif 'nlp' in problem_type:
            category = 'nlp'
            subtype = problem_type.split('_')[1] if '_' in problem_type else 'classification'
        elif 'vision' in problem_type or 'detection' in problem_type:
            category = 'computer_vision'
            subtype = 'detection' if 'detection' in problem_type else 'segmentation'
        else:
            # Default to classification
            category = 'classification'
            subtype = 'binary'
        
        # Get metrics for category and subtype
        if category in self.metric_definitions:
            if subtype in self.metric_definitions[category]:
                metrics_def = self.metric_definitions[category][subtype]
            else:
                # Use first available subtype as default
                metrics_def = list(self.metric_definitions[category].values())[0]
        else:
            # Fallback metrics
            metrics_def = {
                'primary': 'accuracy',
                'secondary': ['precision', 'recall'],
                'thresholds': {'accuracy': {'acceptable': 0.7, 'good': 0.85, 'excellent': 0.95}}
            }
        
        return {
            "primary": metrics_def.get('primary', 'accuracy'),
            "secondary": metrics_def.get('secondary', []),
            "additional": metrics_def.get('class_imbalance', []) + 
                         metrics_def.get('per_class', []) +
                         metrics_def.get('ranking', []) +
                         metrics_def.get('stability', []) +
                         metrics_def.get('semantic', []) +
                         metrics_def.get('iou_based', []),
            "category": category,
            "subtype": subtype
        }
    
    def _generate_business_metrics(self, business_goals: List[str], industry: str) -> Dict:
        """Generate business metrics based on goals"""
        selected_metrics = {}
        
        # Map common business goals to metrics
        goal_metric_map = {
            'reduce_cost': 'cost_reduction',
            'increase_revenue': 'revenue_increase',
            'improve_efficiency': 'operational_efficiency',
            'reduce_time': 'processing_time',
            'improve_satisfaction': 'user_satisfaction',
            'increase_accuracy': 'accuracy_improvement'
        }
        
        for goal in business_goals:
            goal_lower = goal.lower()
            for keyword, metric_name in goal_metric_map.items():
                if keyword in goal_lower:
                    if metric_name in self.business_metrics:
                        metric = self.business_metrics[metric_name].copy()
                        # Adjust ranges based on industry
                        metric['target'] = self._adjust_for_industry(
                            metric['typical_range'], industry
                        )
                        selected_metrics[metric_name] = metric
        
        # If no specific metrics identified, use defaults
        if not selected_metrics:
            selected_metrics = {
                'operational_efficiency': {
                    'unit': 'percentage',
                    'direction': 'increase',
                    'target': 25
                },
                'cost_reduction': {
                    'unit': 'percentage',
                    'direction': 'decrease',
                    'target': 20
                }
            }
        
        return selected_metrics
    
    def _calculate_thresholds(self, technical_metrics: Dict, baseline: Dict, 
                             problem_type: str, subtype: str) -> Dict:
        """Calculate performance thresholds"""
        thresholds = {}
        
        # Get predefined thresholds
        category = technical_metrics['category']
        subtype = technical_metrics['subtype']
        
        if category in self.metric_definitions:
            if subtype in self.metric_definitions[category]:
                predefined = self.metric_definitions[category][subtype].get('thresholds', {})
                
                # Adjust based on baseline if available
                for metric, levels in predefined.items():
                    if metric in baseline:
                        current = baseline[metric]
                        # Adjust thresholds relative to baseline
                        adjusted = {}
                        for level, value in levels.items():
                            if metric in ['hamming_loss', 'davies_bouldin', 'perplexity']:
                                # Lower is better metrics
                                adjusted[level] = min(value, current * 0.8)
                            else:
                                # Higher is better metrics
                                adjusted[level] = max(value, current * 1.2)
                        thresholds[metric] = adjusted
                    else:
                        thresholds[metric] = levels
        
        # Add minimum viable thresholds
        primary_metric = technical_metrics['primary']
        if primary_metric not in thresholds:
            thresholds[primary_metric] = {
                'minimum_viable': 0.7,
                'target': 0.85,
                'stretch': 0.95
            }
        
        return thresholds
    
    def _generate_monitoring_strategy(self, technical: Dict, business: Dict) -> Dict:
        """Generate monitoring strategy"""
        return {
            "evaluation_frequency": {
                "technical_metrics": "daily",
                "business_metrics": "weekly",
                "comprehensive_review": "monthly"
            },
            "alert_thresholds": {
                "performance_degradation": -0.05,  # 5% drop
                "data_drift_threshold": 0.1,
                "prediction_latency_ms": 100
            },
            "dashboards": {
                "technical": ["mlflow", "tensorboard", "grafana"],
                "business": ["tableau", "powerbi", "custom_dashboard"]
            },
            "logging": {
                "predictions": True,
                "confidence_scores": True,
                "feature_importance": True,
                "errors": True
            },
            "reporting": {
                "automated_reports": ["daily_summary", "weekly_trends", "monthly_analysis"],
                "stakeholder_updates": "bi-weekly",
                "incident_reports": "as_needed"
            }
        }
    
    def _create_evaluation_framework(self, technical: Dict, business: Dict, 
                                    monitoring: Dict) -> Dict:
        """Create comprehensive evaluation framework"""
        return {
            "evaluation_stages": {
                "offline": {
                    "metrics": [technical['primary']] + technical['secondary'],
                    "datasets": ["train", "validation", "test"],
                    "cross_validation": "5-fold"
                },
                "online": {
                    "metrics": [technical['primary']],
                    "ab_testing": True,
                    "canary_deployment": True,
                    "shadow_mode_duration": "2_weeks"
                },
                "production": {
                    "metrics": list(business.keys()),
                    "monitoring": monitoring['evaluation_frequency'],
                    "feedback_loop": True
                }
            },
            "success_criteria": {
                "technical": f"{technical['primary']} meets target threshold",
                "business": "All business metrics show positive trend",
                "user": "User acceptance rate > 80%",
                "operational": "System stability > 99.9%"
            },
            "failure_criteria": {
                "technical": f"{technical['primary']} below minimum viable",
                "business": "Negative ROI after 3 months",
                "user": "User complaints > 10%",
                "operational": "System downtime > 1%"
            }
        }
    
    def _process_baseline(self, baseline_performance: Dict) -> Dict:
        """Process and structure baseline performance data"""
        processed = {
            "current_performance": baseline_performance.get('current', {}),
            "human_benchmark": baseline_performance.get('human_level', None),
            "industry_standard": baseline_performance.get('industry_benchmark', None),
            "competitor_performance": baseline_performance.get('competitor', None),
            "historical_best": baseline_performance.get('historical_best', None)
        }
        
        # Remove None values
        return {k: v for k, v in processed.items() if v is not None}
    
    def _recommend_tools(self, problem_type: str) -> Dict:
        """Recommend tools for metrics tracking"""
        tools = {
            "experiment_tracking": ["MLflow", "Weights & Biases", "Neptune.ai"],
            "model_monitoring": ["Evidently AI", "WhyLabs", "Arize AI"],
            "visualization": ["TensorBoard", "Plotly", "Streamlit"],
            "testing": ["pytest", "Great Expectations", "Deepchecks"]
        }
        
        # Add specific tools based on problem type
        if 'nlp' in problem_type:
            tools["specialized"] = ["Hugging Face Evaluate", "NLTK", "spaCy"]
        elif 'vision' in problem_type:
            tools["specialized"] = ["FiftyOne", "Label Studio", "CVAT"]
        elif 'time_series' in problem_type:
            tools["specialized"] = ["Prophet", "Darts", "sktime"]
        
        return tools
    
    def _determine_reporting_frequency(self, business_goals: List[str]) -> str:
        """Determine appropriate reporting frequency"""
        if any('real-time' in goal.lower() or 'immediate' in goal.lower() 
               for goal in business_goals):
            return "real-time"
        elif any('daily' in goal.lower() for goal in business_goals):
            return "daily"
        elif any('weekly' in goal.lower() for goal in business_goals):
            return "weekly"
        else:
            return "weekly"  # Default
    
    def _adjust_for_industry(self, typical_range: List[int], industry: str) -> int:
        """Adjust metric targets based on industry"""
        industry_multipliers = {
            'finance': 1.2,  # Higher standards
            'healthcare': 1.3,  # Highest standards
            'retail': 0.9,  # Moderate standards
            'manufacturing': 1.0,  # Standard
            'general': 1.0
        }
        
        multiplier = industry_multipliers.get(industry.lower(), 1.0)
        avg_range = sum(typical_range) / len(typical_range)
        return int(avg_range * multiplier)
    
    def _generate_evidence(self, result: Dict, inputs: Dict) -> None:
        """Generate evidence artifacts"""
        timestamp = datetime.now().isoformat()
        
        # Save metrics configuration as YAML
        yaml_file = self.artifacts_dir / "success-metrics.yaml"
        yaml_content = f"""# Success Metrics Configuration
# Generated: {timestamp}
# Problem Type: {inputs.get('problem_type', 'unknown')}

metrics:
  technical:
    primary_metric: {result['technical_metrics']['primary']}
    secondary_metrics: {result['technical_metrics']['secondary']}
    evaluation_frequency: {result['monitoring_strategy']['evaluation_frequency']['technical_metrics']}
    
  business:"""
        
        for metric_name, metric_info in result['business_metrics'].items():
            yaml_content += f"""
    {metric_name}:
      unit: {metric_info['unit']}
      direction: {metric_info['direction']}
      target: {metric_info.get('target', 'TBD')}"""
        
        yaml_content += f"""

thresholds:"""
        for metric, levels in result['thresholds'].items():
            yaml_content += f"""
  {metric}:"""
            for level, value in levels.items():
                yaml_content += f"""
    {level}: {value}"""
        
        yaml_content += f"""

monitoring:
  dashboards: {result['monitoring_strategy']['dashboards']}
  alerts:
    performance_degradation: {result['monitoring_strategy']['alert_thresholds']['performance_degradation']}
    data_drift: {result['monitoring_strategy']['alert_thresholds']['data_drift_threshold']}
    
baseline:"""
        for key, value in result['baseline'].items():
            yaml_content += f"""
  {key}: {value}"""
        
        with open(yaml_file, 'w') as f:
            f.write(yaml_content)
        
        # Save detailed JSON report
        json_file = self.artifacts_dir / "metrics-detailed.json"
        with open(json_file, 'w') as f:
            json.dump(result, f, indent=2)
        
        # Generate markdown documentation
        md_file = self.artifacts_dir / "success-metrics-guide.md"
        with open(md_file, 'w') as f:
            f.write("# Success Metrics Guide\n\n")
            f.write(f"**Generated**: {timestamp}\n\n")
            f.write("## Technical Metrics\n\n")
            f.write(f"### Primary Metric: {result['technical_metrics']['primary']}\n")
            f.write("This is the main metric for evaluating model performance.\n\n")
            f.write("### Secondary Metrics\n")
            for metric in result['technical_metrics']['secondary']:
                f.write(f"- **{metric}**: Supporting metric for comprehensive evaluation\n")
            f.write("\n## Business Metrics\n\n")
            for name, info in result['business_metrics'].items():
                f.write(f"### {name.replace('_', ' ').title()}\n")
                f.write(f"- Target: {info.get('target', 'TBD')} {info['unit']}\n")
                f.write(f"- Direction: {info['direction']}\n\n")
            f.write("## Evaluation Framework\n\n")
            f.write(json.dumps(result['evaluation_framework'], indent=2))
    
    def _list_artifacts(self) -> List[str]:
        """List generated artifacts"""
        artifacts = []
        for file in self.artifacts_dir.glob("*"):
            artifacts.append(str(file.relative_to(self.workspace)))
        return artifacts


def main():
    """CLI entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Generate success metrics for AI project")
    parser.add_argument("--workspace", required=True, help="Workspace path")
    parser.add_argument("--problem-type", required=True, help="Problem type classification")
    parser.add_argument("--subtype", default="standard", help="Problem subtype")
    parser.add_argument("--business-goals", default="[]", help="Business goals (JSON array)")
    parser.add_argument("--baseline", default="{}", help="Baseline performance (JSON)")
    parser.add_argument("--industry", default="general", help="Industry context")
    
    args = parser.parse_args()
    
    generator = SuccessMetricsGenerator(args.workspace)
    result = generator.execute(
        problem_type=args.problem_type,
        subtype=args.subtype,
        business_goals=json.loads(args.business_goals),
        baseline_performance=json.loads(args.baseline),
        industry_context=args.industry
    )
    
    print(json.dumps(result, indent=2))
    
if __name__ == "__main__":
    main()
