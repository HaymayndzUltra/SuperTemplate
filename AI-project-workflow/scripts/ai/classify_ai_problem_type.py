#!/usr/bin/env python3
"""
Script: classify_ai_problem_type.py
Protocol: 06-ai-use-case-definition
Purpose: Automatically classify the AI problem type based on requirements
Author: AI Workflow System
Created: 2025-01-06
"""

import json
import logging
from typing import Dict, List, Optional
from pathlib import Path
import re

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AIProblemClassifier:
    """Main class for AI problem type classification"""
    
    def __init__(self, workspace_path: str):
        self.workspace = Path(workspace_path)
        self.artifacts_dir = self.workspace / ".artifacts" / "protocol-06"
        self.artifacts_dir.mkdir(parents=True, exist_ok=True)
        
        # Problem type patterns
        self.classification_keywords = [
            'classify', 'categorize', 'identify', 'predict class', 'label',
            'sentiment', 'detect', 'recognize', 'diagnose'
        ]
        self.regression_keywords = [
            'predict value', 'forecast', 'estimate', 'project', 'price',
            'score', 'rate', 'quantity', 'continuous'
        ]
        self.clustering_keywords = [
            'group', 'segment', 'cluster', 'organize', 'discover patterns',
            'similarity', 'cohort'
        ]
        self.nlp_keywords = [
            'text', 'language', 'translate', 'summarize', 'generate text',
            'chat', 'question answer', 'entity extraction'
        ]
        self.cv_keywords = [
            'image', 'video', 'visual', 'picture', 'detect object',
            'face', 'OCR', 'scene'
        ]
        self.rl_keywords = [
            'optimize', 'strategy', 'game', 'control', 'decision sequence',
            'reward', 'agent', 'environment'
        ]
        
    def execute(self, **kwargs) -> Dict:
        """
        Main execution method
        
        Args:
            problem_description: Text description of the problem
            data_characteristics: JSON with data properties
            business_constraints: List of constraints
            
        Returns:
            Dict: Classification results with confidence
        """
        try:
            problem_description = kwargs.get('problem_description', '')
            data_characteristics = kwargs.get('data_characteristics', {})
            business_constraints = kwargs.get('business_constraints', [])
            
            # Analyze the problem
            paradigm = self._determine_paradigm(problem_description, data_characteristics)
            problem_type = self._classify_problem_type(problem_description, paradigm)
            subtype = self._determine_subtype(problem_type, data_characteristics)
            confidence = self._calculate_confidence(problem_description, paradigm, problem_type)
            
            result = {
                "paradigm": paradigm,
                "problem_type": problem_type,
                "subtype": subtype,
                "confidence": confidence,
                "reasoning": self._generate_reasoning(paradigm, problem_type, subtype),
                "recommended_algorithms": self._suggest_algorithms(problem_type, subtype),
                "data_requirements": self._estimate_data_requirements(problem_type)
            }
            
            # Generate evidence
            self._generate_evidence(result)
            
            return {
                "status": "success",
                "result": result,
                "artifacts": self._list_artifacts()
            }
            
        except Exception as e:
            logger.error(f"Classification failed: {e}")
            return {
                "status": "error",
                "error": str(e)
            }
    
    def _determine_paradigm(self, description: str, data_chars: Dict) -> str:
        """Determine learning paradigm"""
        description_lower = description.lower()
        
        # Check for labeled data
        has_labels = data_chars.get('has_labels', False)
        has_feedback = data_chars.get('has_feedback', False)
        is_sequential = data_chars.get('is_sequential', False)
        
        if has_labels or any(kw in description_lower for kw in ['labeled', 'annotated', 'tagged']):
            return "supervised"
        elif has_feedback or any(kw in description_lower for kw in self.rl_keywords):
            return "reinforcement"
        elif any(kw in description_lower for kw in ['pattern', 'discover', 'explore', 'unsupervised']):
            return "unsupervised"
        elif 'semi-supervised' in description_lower or 'few labels' in description_lower:
            return "semi-supervised"
        else:
            # Default based on problem keywords
            if any(kw in description_lower for kw in self.classification_keywords + self.regression_keywords):
                return "supervised"
            return "unsupervised"
    
    def _classify_problem_type(self, description: str, paradigm: str) -> str:
        """Classify the specific problem type"""
        description_lower = description.lower()
        
        # Count keyword matches
        scores = {
            'classification': sum(1 for kw in self.classification_keywords if kw in description_lower),
            'regression': sum(1 for kw in self.regression_keywords if kw in description_lower),
            'clustering': sum(1 for kw in self.clustering_keywords if kw in description_lower),
            'nlp': sum(1 for kw in self.nlp_keywords if kw in description_lower),
            'computer_vision': sum(1 for kw in self.cv_keywords if kw in description_lower),
            'reinforcement_learning': sum(1 for kw in self.rl_keywords if kw in description_lower)
        }
        
        # Special cases
        if scores['nlp'] > 0:
            if 'classify' in description_lower or 'sentiment' in description_lower:
                return 'nlp_classification'
            elif 'generate' in description_lower or 'translate' in description_lower:
                return 'nlp_generation'
            return 'nlp'
            
        if scores['computer_vision'] > 0:
            if 'detect' in description_lower or 'identify' in description_lower:
                return 'object_detection'
            elif 'classify' in description_lower:
                return 'image_classification'
            return 'computer_vision'
        
        # General cases
        if paradigm == "supervised":
            if scores['classification'] > scores['regression']:
                return 'classification'
            elif scores['regression'] > 0:
                return 'regression'
        elif paradigm == "unsupervised":
            if scores['clustering'] > 0:
                return 'clustering'
            return 'dimensionality_reduction'
        elif paradigm == "reinforcement":
            return 'reinforcement_learning'
            
        return 'classification'  # Default
    
    def _determine_subtype(self, problem_type: str, data_chars: Dict) -> str:
        """Determine problem subtype"""
        if problem_type == 'classification':
            num_classes = data_chars.get('num_classes', 2)
            if num_classes == 2:
                return 'binary'
            elif num_classes > 2:
                return 'multiclass'
            elif data_chars.get('multi_label', False):
                return 'multilabel'
                
        elif problem_type == 'regression':
            if data_chars.get('is_time_series', False):
                return 'time_series'
            return 'standard'
            
        elif problem_type == 'clustering':
            if data_chars.get('hierarchical', False):
                return 'hierarchical'
            return 'partitioning'
            
        return 'standard'
    
    def _calculate_confidence(self, description: str, paradigm: str, problem_type: str) -> float:
        """Calculate classification confidence"""
        confidence = 0.5  # Base confidence
        
        # Increase confidence based on keyword matches
        description_lower = description.lower()
        
        # Check paradigm keywords
        if paradigm in description_lower:
            confidence += 0.2
            
        # Check problem type keywords
        type_keywords = {
            'classification': self.classification_keywords,
            'regression': self.regression_keywords,
            'clustering': self.clustering_keywords
        }
        
        for prob_type, keywords in type_keywords.items():
            if prob_type in problem_type:
                matches = sum(1 for kw in keywords if kw in description_lower)
                confidence += min(0.3, matches * 0.1)
                
        return min(0.95, confidence)
    
    def _generate_reasoning(self, paradigm: str, problem_type: str, subtype: str) -> str:
        """Generate explanation for classification"""
        reasoning = f"Based on the problem description analysis:\n"
        reasoning += f"1. Learning Paradigm: {paradigm} - "
        
        paradigm_reasons = {
            'supervised': "Labeled data is available for training",
            'unsupervised': "No labeled data, pattern discovery required",
            'reinforcement': "Sequential decision-making with feedback",
            'semi-supervised': "Limited labeled data available"
        }
        reasoning += paradigm_reasons.get(paradigm, "Default paradigm selected") + "\n"
        
        reasoning += f"2. Problem Type: {problem_type} - "
        type_reasons = {
            'classification': "Predicting discrete categories or classes",
            'regression': "Predicting continuous numerical values",
            'clustering': "Grouping similar data points",
            'nlp': "Processing and understanding natural language",
            'computer_vision': "Analyzing visual information",
            'reinforcement_learning': "Learning optimal actions through interaction"
        }
        reasoning += type_reasons.get(problem_type.split('_')[0], "Specific problem type identified") + "\n"
        
        reasoning += f"3. Subtype: {subtype} - Specific variant of the problem type"
        
        return reasoning
    
    def _suggest_algorithms(self, problem_type: str, subtype: str) -> List[str]:
        """Suggest appropriate algorithms"""
        algorithms = {
            'classification': {
                'binary': ['Logistic Regression', 'SVM', 'Random Forest', 'XGBoost', 'Neural Networks'],
                'multiclass': ['Random Forest', 'XGBoost', 'Neural Networks', 'SVM (OvR)', 'Naive Bayes'],
                'multilabel': ['Binary Relevance', 'Classifier Chains', 'ML-kNN', 'Neural Networks']
            },
            'regression': {
                'standard': ['Linear Regression', 'Random Forest', 'XGBoost', 'Neural Networks', 'SVR'],
                'time_series': ['ARIMA', 'LSTM', 'Prophet', 'XGBoost', 'Transformer']
            },
            'clustering': {
                'partitioning': ['K-Means', 'K-Medoids', 'Gaussian Mixture', 'DBSCAN'],
                'hierarchical': ['Agglomerative', 'Divisive', 'BIRCH']
            },
            'nlp_classification': ['BERT', 'RoBERTa', 'DistilBERT', 'FastText', 'CNN-Text'],
            'nlp_generation': ['GPT', 'T5', 'BART', 'Transformer'],
            'object_detection': ['YOLO', 'Faster R-CNN', 'SSD', 'RetinaNet'],
            'image_classification': ['ResNet', 'EfficientNet', 'Vision Transformer', 'ConvNeXT']
        }
        
        if problem_type in algorithms:
            if isinstance(algorithms[problem_type], dict):
                return algorithms[problem_type].get(subtype, algorithms[problem_type].get('standard', []))
            return algorithms[problem_type]
            
        return ['Neural Networks', 'Ensemble Methods', 'Traditional ML']
    
    def _estimate_data_requirements(self, problem_type: str) -> Dict:
        """Estimate data requirements for problem type"""
        requirements = {
            'classification': {
                'minimum_samples': 1000,
                'recommended_samples': 10000,
                'samples_per_class': 100,
                'features': '10-100'
            },
            'regression': {
                'minimum_samples': 500,
                'recommended_samples': 5000,
                'features': '5-50'
            },
            'clustering': {
                'minimum_samples': 100,
                'recommended_samples': 1000,
                'features': '2-100'
            },
            'nlp': {
                'minimum_samples': 5000,
                'recommended_samples': 50000,
                'text_length': '10-500 words'
            },
            'computer_vision': {
                'minimum_samples': 1000,
                'recommended_samples': 10000,
                'image_size': '224x224 minimum'
            }
        }
        
        base_type = problem_type.split('_')[0]
        return requirements.get(base_type, requirements['classification'])
    
    def _generate_evidence(self, result: Dict) -> None:
        """Generate evidence artifacts"""
        # Save classification result
        classification_file = self.artifacts_dir / "problem_classification.json"
        with open(classification_file, 'w') as f:
            json.dump(result, f, indent=2)
            
        # Save detailed report
        report_file = self.artifacts_dir / "classification_report.md"
        with open(report_file, 'w') as f:
            f.write("# AI Problem Classification Report\n\n")
            f.write(f"## Classification Results\n")
            f.write(f"- **Paradigm**: {result['paradigm']}\n")
            f.write(f"- **Problem Type**: {result['problem_type']}\n")
            f.write(f"- **Subtype**: {result['subtype']}\n")
            f.write(f"- **Confidence**: {result['confidence']:.2%}\n\n")
            f.write(f"## Reasoning\n{result['reasoning']}\n\n")
            f.write(f"## Recommended Algorithms\n")
            for algo in result['recommended_algorithms']:
                f.write(f"- {algo}\n")
    
    def _list_artifacts(self) -> List[str]:
        """List generated artifacts"""
        artifacts = []
        for file in self.artifacts_dir.glob("*"):
            artifacts.append(str(file.relative_to(self.workspace)))
        return artifacts


def main():
    """CLI entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Classify AI/ML problem type")
    parser.add_argument("--workspace", required=True, help="Workspace path")
    parser.add_argument("--description", required=True, help="Problem description")
    parser.add_argument("--data-chars", default="{}", help="Data characteristics (JSON)")
    parser.add_argument("--constraints", default="[]", help="Business constraints (JSON)")
    
    args = parser.parse_args()
    
    classifier = AIProblemClassifier(args.workspace)
    result = classifier.execute(
        problem_description=args.description,
        data_characteristics=json.loads(args.data_chars),
        business_constraints=json.loads(args.constraints)
    )
    
    print(json.dumps(result, indent=2))
    
if __name__ == "__main__":
    main()
