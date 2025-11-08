#!/usr/bin/env python3
"""
Data Volume Calculator for AI Data Strategy Planning

Calculates minimum data requirements based on AI use case complexity,
model type, and desired confidence levels.
"""

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime

class DataVolumeCalculator:
    """Calculate minimum data volume requirements for AI use cases"""
    
    def __init__(self):
        self.model_complexity_multipliers = {
            'simple_regression': 100,
            'classification': 500,
            'time_series': 1000,
            'nlp_classification': 1000,
            'computer_vision': 5000,
            'deep_learning': 10000,
            'reinforcement_learning': 50000
        }
        
        self.confidence_multipliers = {
            'low': 1.0,
            'medium': 2.0,
            'high': 5.0,
            'production': 10.0
        }
        
        self.feature_complexity_multipliers = {
            'low': 1.0,      # < 10 features
            'medium': 2.0,   # 10-50 features  
            'high': 5.0,     # 50-100 features
            'very_high': 10.0 # > 100 features
        }

    def calculate_base_samples(self, model_type: str, confidence_level: str) -> int:
        """Calculate base sample count for model type and confidence"""
        base = self.model_complexity_multipliers.get(model_type, 1000)
        confidence_mult = self.confidence_multipliers.get(confidence_level, 2.0)
        return int(base * confidence_mult)

    def adjust_for_features(self, base_samples: int, feature_count: int) -> int:
        """Adjust sample count based on feature complexity"""
        if feature_count < 10:
            complexity = 'low'
        elif feature_count <= 50:
            complexity = 'medium'
        elif feature_count <= 100:
            complexity = 'high'
        else:
            complexity = 'very_high'
            
        mult = self.feature_complexity_multipliers[complexity]
        return int(base_samples * mult)

    def calculate_class_balance_samples(self, base_samples: int, class_count: int) -> int:
        """Adjust samples for multi-class classification"""
        if class_count <= 2:
            return base_samples
        # Ensure minimum samples per class
        min_per_class = max(100, base_samples // 10)
        return base_samples + (class_count - 2) * min_per_class

    def calculate_time_series_samples(self, base_samples: int, time_horizon: str, frequency: str) -> Dict[str, Any]:
        """Calculate samples for time series data"""
        frequency_samples_per_day = {
            'hourly': 24,
            'daily': 1,
            'weekly': 1/7,
            'monthly': 1/30,
            'realtime': 1440  # per minute
        }
        
        time_horizon_days = {
            'week': 7,
            'month': 30,
            'quarter': 90,
            'year': 365,
            'multi_year': 1095
        }
        
        samples_needed = max(base_samples, 
                           time_horizon_days.get(time_horizon, 90) * 
                           frequency_samples_per_day.get(frequency, 1))
        
        return {
            'total_samples': int(samples_needed),
            'time_horizon_days': time_horizon_days.get(time_horizon, 90),
            'samples_per_day': frequency_samples_per_day.get(frequency, 1),
            'recommended_history': f"{time_horizon} at {frequency} frequency"
        }

    def calculate_cv_samples(self, base_samples: int, image_type: str, resolution: str) -> Dict[str, Any]:
        """Calculate samples for computer vision tasks"""
        resolution_multipliers = {
            'low_res': 1.0,      # < 224x224
            'medium_res': 2.0,   # 224x224 to 512x512
            'high_res': 5.0,     # > 512x512
            'ultra_hd': 10.0     # > 1920x1080
        }
        
        type_multipliers = {
            'classification': 1.0,
            'object_detection': 2.0,
            'segmentation': 3.0,
            'face_recognition': 5.0
        }
        
        res_mult = resolution_multipliers.get(resolution, 2.0)
        type_mult = type_multipliers.get(image_type, 1.0)
        
        total_samples = int(base_samples * res_mult * type_mult)
        
        return {
            'total_samples': total_samples,
            'resolution_factor': res_mult,
            'type_factor': type_mult,
            'recommended_augmentation': total_samples // 4  # 25% augmentation
        }

    def process_use_case(self, use_case: Dict[str, Any]) -> Dict[str, Any]:
        """Process a single use case and calculate data requirements"""
        uc_id = use_case.get('use_case_id', 'UC-UNKNOWN')
        model_type = use_case.get('model_type', 'classification')
        confidence_level = use_case.get('confidence_level', 'medium')
        feature_count = use_case.get('feature_count', 10)
        
        # Calculate base samples
        base_samples = self.calculate_base_samples(model_type, confidence_level)
        feature_adjusted = self.adjust_for_features(base_samples, feature_count)
        
        result = {
            'use_case_id': uc_id,
            'model_type': model_type,
            'confidence_level': confidence_level,
            'base_samples': base_samples,
            'feature_adjusted_samples': feature_adjusted,
            'final_min_samples': feature_adjusted
        }
        
        # Model-specific adjustments
        if model_type == 'classification':
            class_count = use_case.get('class_count', 2)
            result['final_min_samples'] = self.calculate_class_balance_samples(
                feature_adjusted, class_count)
            result['class_count'] = class_count
            
        elif model_type == 'time_series':
            time_horizon = use_case.get('time_horizon', 'quarter')
            frequency = use_case.get('frequency', 'daily')
            ts_result = self.calculate_time_series_samples(
                feature_adjusted, time_horizon, frequency)
            result.update(ts_result)
            
        elif model_type in ['computer_vision', 'deep_learning']:
            if 'image_type' in use_case:
                image_type = use_case.get('image_type', 'classification')
                resolution = use_case.get('resolution', 'medium_res')
                cv_result = self.calculate_cv_samples(
                    feature_adjusted, image_type, resolution)
                result.update(cv_result)
        
        # Add recommendations
        result['recommendations'] = self._generate_recommendations(result)
        
        return result

    def _generate_recommendations(self, result: Dict[str, Any]) -> List[str]:
        """Generate data collection recommendations"""
        recommendations = []
        
        if result['final_min_samples'] < 1000:
            recommendations.append("Consider data augmentation to increase effective sample size")
            
        if result['model_type'] == 'classification' and result.get('class_count', 2) > 10:
            recommendations.append("Multi-class problem: ensure balanced representation across classes")
            
        if result['confidence_level'] == 'production':
            recommendations.append("Production confidence: implement rigorous data validation and quality checks")
            
        return recommendations

    def process_use_cases(self, use_cases: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Process multiple use cases and generate comprehensive report"""
        results = []
        total_samples = 0
        
        for use_case in use_cases:
            try:
                result = self.process_use_case(use_case)
                results.append(result)
                total_samples += result['final_min_samples']
            except Exception as e:
                print(f"Error processing use case {use_case.get('use_case_id', 'unknown')}: {e}")
                continue
        
        # Generate summary
        summary = {
            'total_use_cases': len(use_cases),
            'processed_use_cases': len(results),
            'total_min_samples_required': total_samples,
            'average_samples_per_use_case': total_samples // len(results) if results else 0,
            'complexity_distribution': self._analyze_complexity(results)
        }
        
        return {
            'timestamp': datetime.now().isoformat(),
            'summary': summary,
            'use_case_requirements': results,
            'methodology': {
                'model_complexity_multipliers': self.model_complexity_multipliers,
                'confidence_multipliers': self.confidence_multipliers,
                'feature_complexity_multipliers': self.feature_complexity_multipliers
            }
        }

    def _analyze_complexity(self, results: List[Dict[str, Any]]) -> Dict[str, int]:
        """Analyze distribution of complexity across use cases"""
        distribution = {}
        for result in results:
            model_type = result['model_type']
            distribution[model_type] = distribution.get(model_type, 0) + 1
        return distribution

def main():
    parser = argparse.ArgumentParser(description='Calculate data volume requirements for AI use cases')
    parser.add_argument('--input', required=True, help='Input JSON file with use cases')
    parser.add_argument('--output', required=True, help='Output JSON file with volume calculations')
    parser.add_argument('--verbose', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    # Load use cases
    try:
        with open(args.input, 'r') as f:
            data = json.load(f)
        use_cases = data.get('use_cases', []) if isinstance(data, dict) else data
    except Exception as e:
        print(f"Error loading input file: {e}")
        sys.exit(1)
    
    if not use_cases:
        print("No use cases found in input file")
        sys.exit(1)
    
    # Calculate requirements
    calculator = DataVolumeCalculator()
    results = calculator.process_use_cases(use_cases)
    
    # Save results
    try:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
            
        if args.verbose:
            print(f"Processed {results['summary']['processed_use_cases']} use cases")
            print(f"Total minimum samples required: {results['summary']['total_min_samples_required']:,}")
            print(f"Results saved to: {args.output}")
            
    except Exception as e:
        print(f"Error saving results: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
