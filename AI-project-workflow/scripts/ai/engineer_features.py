#!/usr/bin/env python3
"""
Feature Engineering Script for Protocol 09
Creates and transforms features for ML model development
"""

import json
import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder, OneHotEncoder
from sklearn.feature_selection import SelectKBest, f_classif, f_regression, mutual_info_classif
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('feature_engineering.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class FeatureEngineer:
    """Engineers and selects features for ML model development"""
    
    def __init__(self, data_path: str, requirements_path: str, output_path: str):
        self.data_path = Path(data_path)
        self.requirements_path = Path(requirements_path)
        self.output_path = Path(output_path)
        self.output_path.mkdir(parents=True, exist_ok=True)
        self.engineering_log = []
        self.start_time = datetime.now()
        
        # Feature engineering configuration
        self.engineering_config = {
            'max_features_for_selection': 100,
            'correlation_threshold': 0.95,
            'variance_threshold': 0.01,
            'importance_threshold': 0.01,
            'pca_components': None,  # Will be determined dynamically
            'create_interaction_features': True,
            'create_polynomial_features': False,
            'max_polynomial_degree': 2
        }
    
    def load_cleaned_data(self) -> Optional[pd.DataFrame]:
        """Load cleaned data for feature engineering"""
        logger.info("Loading cleaned data for feature engineering")
        
        # Look for cleaned data files
        cleaned_files = list(self.data_path.glob("cleaned_*.csv"))
        cleaned_files.extend(list(self.data_path.glob("cleaned_*.json")))
        cleaned_files.extend(list(self.data_path.glob("cleaned_*.parquet")))
        
        if not cleaned_files:
            logger.error("No cleaned data files found")
            return None
        
        # Load the first cleaned file (in real implementation, might handle multiple)
        data_file = cleaned_files[0]
        logger.info(f"Loading data from {data_file}")
        
        try:
            if data_file.suffix == '.csv':
                df = pd.read_csv(data_file)
            elif data_file.suffix == '.json':
                df = pd.read_json(data_file)
            elif data_file.suffix == '.parquet':
                df = pd.read_parquet(data_file)
            else:
                logger.error(f"Unsupported file format: {data_file.suffix}")
                return None
            
            logger.info(f"Loaded data with shape: {df.shape}")
            return df
            
        except Exception as e:
            logger.error(f"Failed to load cleaned data: {e}")
            return None
    
    def load_requirements(self) -> Dict[str, Any]:
        """Load feature engineering requirements"""
        logger.info("Loading feature engineering requirements")
        
        try:
            if self.requirements_path.suffix == '.json':
                with open(self.requirements_path, 'r') as f:
                    return json.load(f)
            else:
                # Parse markdown requirements file
                return self._parse_markdown_requirements()
        except Exception as e:
            logger.error(f"Failed to load requirements: {e}")
            # Return default requirements
            return {
                'problem_type': 'classification',
                'target_column': 'target',
                'feature_engineering': {
                    'create_categorical_features': True,
                    'create_numerical_features': True,
                    'feature_selection': True,
                    'max_features': 50
                }
            }
    
    def _parse_markdown_requirements(self) -> Dict[str, Any]:
        """Parse markdown requirements file"""
        # Simple parsing - in real implementation would be more sophisticated
        return {
            'problem_type': 'classification',
            'target_column': 'target',
            'feature_engineering': {
                'create_categorical_features': True,
                'create_numerical_features': True,
                'feature_selection': True,
                'max_features': 50
            }
        }
    
    def analyze_data_types(self, df: pd.DataFrame) -> Dict[str, List[str]]:
        """Analyze and categorize data types"""
        logger.info("Analyzing data types for feature engineering")
        
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
        datetime_cols = df.select_dtypes(include=['datetime64']).columns.tolist()
        
        # Remove target column from feature lists if present
        target_col = self.load_requirements().get('target_column')
        if target_col:
            if target_col in numeric_cols:
                numeric_cols.remove(target_col)
            if target_col in categorical_cols:
                categorical_cols.remove(target_col)
            if target_col in datetime_cols:
                datetime_cols.remove(target_col)
        
        data_type_analysis = {
            'numeric_columns': numeric_cols,
            'categorical_columns': categorical_cols,
            'datetime_columns': datetime_cols,
            'total_features': len(numeric_cols) + len(categorical_cols) + len(datetime_cols)
        }
        
        logger.info(f"Data types analyzed: {len(numeric_cols)} numeric, {len(categorical_cols)} categorical, {len(datetime_cols)} datetime")
        return data_type_analysis
    
    def create_categorical_features(self, df: pd.DataFrame, categorical_cols: List[str]) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Create and encode categorical features"""
        logger.info("Creating categorical features")
        
        feature_creation_log = []
        df_encoded = df.copy()
        
        for col in categorical_cols:
            if col in df_encoded.columns:
                unique_count = df_encoded[col].nunique()
                
                if unique_count == 2:
                    # Binary encoding
                    le = LabelEncoder()
                    df_encoded[f"{col}_encoded"] = le.fit_transform(df_encoded[col].astype(str))
                    feature_creation_log.append(f"Binary encoded column '{col}'")
                    
                elif unique_count <= 10:
                    # One-hot encoding for low cardinality
                    dummies = pd.get_dummies(df_encoded[col], prefix=col, drop_first=True)
                    df_encoded = pd.concat([df_encoded, dummies], axis=1)
                    df_encoded = df_encoded.drop(columns=[col])
                    feature_creation_log.append(f"One-hot encoded column '{col}' ({unique_count} categories)")
                    
                else:
                    # Label encoding for high cardinality
                    le = LabelEncoder()
                    df_encoded[f"{col}_encoded"] = le.fit_transform(df_encoded[col].astype(str))
                    df_encoded = df_encoded.drop(columns=[col])
                    feature_creation_log.append(f"Label encoded column '{col}' ({unique_count} categories)")
        
        categorical_result = {
            'action': 'categorical_feature_creation',
            'original_categorical_columns': categorical_cols,
            'final_categorical_columns': [col for col in df_encoded.columns if col not in df.columns],
            'feature_creation_log': feature_creation_log
        }
        
        logger.info(f"Categorical feature creation completed: {len(feature_creation_log)} transformations")
        return df_encoded, categorical_result
    
    def create_numerical_features(self, df: pd.DataFrame, numeric_cols: List[str]) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Create numerical features through transformations and interactions"""
        logger.info("Creating numerical features")
        
        feature_creation_log = []
        df_transformed = df.copy()
        
        # Standard scaling for numerical features
        if numeric_cols:
            scaler = StandardScaler()
            df_transformed[[f"{col}_scaled" for col in numeric_cols]] = scaler.fit_transform(df_transformed[numeric_cols])
            feature_creation_log.append(f"Standard scaled {len(numeric_cols)} numerical columns")
        
        # Create interaction features if enabled
        if self.engineering_config['create_interaction_features'] and len(numeric_cols) >= 2:
            # Create interactions between top correlated features
            interaction_pairs = []
            for i, col1 in enumerate(numeric_cols[:5]):  # Limit to first 5 to avoid explosion
                for col2 in numeric_cols[i+1:5]:
                    interaction_name = f"{col1}_x_{col2}"
                    df_transformed[interaction_name] = df_transformed[col1] * df_transformed[col2]
                    interaction_pairs.append(interaction_name)
            
            if interaction_pairs:
                feature_creation_log.append(f"Created {len(interaction_pairs)} interaction features")
        
        # Create polynomial features if enabled (limited to avoid explosion)
        if self.engineering_config['create_polynomial_features'] and numeric_cols:
            poly_cols = numeric_cols[:3]  # Limit to first 3 columns
            for col in poly_cols:
                df_transformed[f"{col}_squared"] = df_transformed[col] ** 2
                df_transformed[f"{col}_cubed"] = df_transformed[col] ** 3
            
            feature_creation_log.append(f"Created polynomial features for {len(poly_cols)} columns")
        
        # Create ratio features
        if len(numeric_cols) >= 2:
            ratio_pairs = []
            for i, col1 in enumerate(numeric_cols[:3]):
                for col2 in numeric_cols[i+1:4]:
                    # Avoid division by zero
                    ratio_name = f"{col1}_div_{col2}"
                    df_transformed[ratio_name] = df_transformed[col1] / (df_transformed[col2] + 1e-8)
                    ratio_pairs.append(ratio_name)
            
            if ratio_pairs:
                feature_creation_log.append(f"Created {len(ratio_pairs)} ratio features")
        
        numerical_result = {
            'action': 'numerical_feature_creation',
            'original_numerical_columns': numeric_cols,
            'final_numerical_columns': [col for col in df_transformed.columns if col not in df.columns],
            'feature_creation_log': feature_creation_log
        }
        
        logger.info(f"Numerical feature creation completed: {len(feature_creation_log)} transformations")
        return df_transformed, numerical_result
    
    def select_features(self, df: pd.DataFrame, requirements: Dict[str, Any]) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Select most relevant features using various techniques"""
        logger.info("Performing feature selection")
        
        target_col = requirements.get('target_column')
        problem_type = requirements.get('problem_type', 'classification')
        
        if target_col not in df.columns:
            logger.warning(f"Target column '{target_col}' not found in data")
            return df, {'action': 'feature_selection', 'status': 'skipped', 'reason': 'target_column_not_found'}
        
        # Prepare features and target
        feature_cols = [col for col in df.columns if col != target_col]
        X = df[feature_cols]
        y = df[target_col]
        
        # Remove features with low variance
        variance_selector = SelectKBest(f_classif if problem_type == 'classification' else f_regression, k='all')
        variance_scores = variance_selector.fit(X, y).scores_
        
        # Remove highly correlated features
        correlation_matrix = X.corr().abs()
        upper_triangle = correlation_matrix.where(np.triu(np.ones(correlation_matrix.shape), k=1).astype(bool))
        high_corr_features = [column for column in upper_triangle.columns if any(upper_triangle[column] > self.engineering_config['correlation_threshold'])]
        
        if high_corr_features:
            X = X.drop(columns=high_corr_features)
            feature_cols = [col for col in feature_cols if col not in high_corr_features]
        
        # Select top features based on importance
        max_features = min(self.engineering_config['max_features_for_selection'], len(feature_cols))
        
        if problem_type == 'classification':
            selector = SelectKBest(f_classif, k=max_features)
        else:
            selector = SelectKBest(f_regression, k=max_features)
        
        X_selected = selector.fit_transform(X, y)
        selected_features = [feature_cols[i] for i in selector.get_support(indices=True)]
        
        # Create final dataframe with selected features and target
        df_selected = pd.DataFrame(X_selected, columns=selected_features)
        df_selected[target_col] = y.values
        
        # Calculate feature importance using Random Forest
        if problem_type == 'classification':
            rf = RandomForestClassifier(n_estimators=100, random_state=42)
        else:
            rf = RandomForestRegressor(n_estimators=100, random_state=42)
        
        rf.fit(X_selected, y)
        feature_importance = dict(zip(selected_features, rf.feature_importances_))
        
        selection_result = {
            'action': 'feature_selection',
            'original_feature_count': len(df.columns) - 1,  # Exclude target
            'selected_feature_count': len(selected_features),
            'features_removed': len(feature_cols) - len(selected_features),
            'selected_features': selected_features,
            'feature_importance': feature_importance,
            'high_correlation_features_removed': high_corr_features
        }
        
        logger.info(f"Feature selection completed: {len(selected_features)} features selected from {len(feature_cols)}")
        return df_selected, selection_result
    
    def validate_feature_quality(self, df: pd.DataFrame, requirements: Dict[str, Any]) -> Dict[str, Any]:
        """Validate quality of engineered features"""
        logger.info("Validating feature quality")
        
        target_col = requirements.get('target_column')
        problem_type = requirements.get('problem_type', 'classification')
        
        validation_results = {
            'feature_count': len(df.columns) - (1 if target_col in df.columns else 0),
            'missing_values': df.isnull().sum().sum(),
            'infinite_values': np.isinf(df.select_dtypes(include=[np.number])).sum().sum(),
            'data_types': df.dtypes.value_counts().to_dict(),
            'quality_score': 0.0,
            'validation_passed': False
        }
        
        # Calculate quality score based on various factors
        quality_factors = []
        
        # Missing value factor (lower is better)
        total_cells = df.shape[0] * df.shape[1]
        missing_ratio = validation_results['missing_values'] / total_cells if total_cells > 0 else 0
        missing_factor = max(0, 1 - missing_ratio * 10)  # Penalize heavily
        quality_factors.append(missing_factor)
        
        # Feature count factor (reasonable range is better)
        feature_count = validation_results['feature_count']
        if 10 <= feature_count <= 100:
            count_factor = 1.0
        elif feature_count < 10:
            count_factor = feature_count / 10
        else:
            count_factor = max(0, 1 - (feature_count - 100) / 100)
        quality_factors.append(count_factor)
        
        # Data type diversity factor
        type_diversity = len(validation_results['data_types'])
        diversity_factor = min(1.0, type_diversity / 3)  # Good to have some diversity
        quality_factors.append(diversity_factor)
        
        validation_results['quality_score'] = float(np.mean(quality_factors))
        validation_results['validation_passed'] = validation_results['quality_score'] >= 0.7
        
        logger.info(f"Feature validation completed: Quality Score = {validation_results['quality_score']:.3f}")
        return validation_results
    
    def execute_feature_engineering(self) -> Dict[str, Any]:
        """Execute complete feature engineering pipeline"""
        logger.info("Starting feature engineering execution")
        
        # Load data and requirements
        df = self.load_cleaned_data()
        if df is None:
            return {
                'engineering_summary': {
                    'status': 'failed',
                    'error': 'Could not load cleaned data'
                },
                'engineering_results': []
            }
        
        requirements = self.load_requirements()
        
        # Analyze data types
        data_type_analysis = self.analyze_data_types(df)
        
        engineering_results = []
        original_shape = df.shape
        
        # Create categorical features
        if data_type_analysis['categorical_columns']:
            df, categorical_result = self.create_categorical_features(df, data_type_analysis['categorical_columns'])
            engineering_results.append(categorical_result)
        
        # Create numerical features
        if data_type_analysis['numeric_columns']:
            df, numerical_result = self.create_numerical_features(df, data_type_analysis['numeric_columns'])
            engineering_results.append(numerical_result)
        
        # Feature selection
        df, selection_result = self.select_features(df, requirements)
        engineering_results.append(selection_result)
        
        # Validate feature quality
        quality_validation = self.validate_feature_quality(df, requirements)
        
        # Save engineered features
        output_file = self.output_path / f"engineered_features_{int(self.start_time.timestamp())}.csv"
        df.to_csv(output_file, index=False)
        
        # Calculate engineering effectiveness
        engineering_effectiveness = self.calculate_engineering_effectiveness(original_shape, df.shape, quality_validation)
        
        engineering_summary = {
            'status': 'completed',
            'original_shape': original_shape,
            'final_shape': list(df.shape),
            'feature_reduction': original_shape[1] - df.shape[1],
            'engineering_effectiveness': float(engineering_effectiveness),
            'quality_validation': quality_validation,
            'output_file': str(output_file),
            'execution_time_seconds': (datetime.now() - self.start_time).total_seconds(),
            'start_time': self.start_time.isoformat(),
            'end_time': datetime.now().isoformat()
        }
        
        engineering_report = {
            'engineering_summary': engineering_summary,
            'engineering_results': engineering_results,
            'data_type_analysis': data_type_analysis,
            'requirements': requirements,
            'engineering_config': self.engineering_config
        }
        
        logger.info(f"Feature engineering completed: {original_shape} -> {df.shape}, Effectiveness: {engineering_effectiveness:.3f}")
        return engineering_report
    
    def calculate_engineering_effectiveness(self, original_shape: Tuple[int, int], final_shape: Tuple[int, int], quality_validation: Dict[str, Any]) -> float:
        """Calculate overall feature engineering effectiveness"""
        try:
            factors = []
            
            # Feature optimization factor (not too many, not too few)
            original_features = original_shape[1] - 1  # Exclude target
            final_features = final_shape[1] - 1  # Exclude target
            
            if original_features > 0:
                if 10 <= final_features <= 100:
                    optimization_factor = 1.0
                elif final_features < 10:
                    optimization_factor = final_features / 10
                else:
                    optimization_factor = max(0, 1 - (final_features - 100) / original_features)
                factors.append(optimization_factor)
            
            # Quality score factor
            quality_factor = quality_validation.get('quality_score', 0)
            factors.append(quality_factor)
            
            # Data retention factor (keep most of the data)
            data_retention = final_shape[0] / max(original_shape[0], 1)
            factors.append(data_retention)
            
            effectiveness = np.mean(factors) if factors else 0.0
            return float(effectiveness)
            
        except Exception as e:
            logger.error(f"Failed to calculate engineering effectiveness: {e}")
            return 0.0
    
    def save_engineering_report(self, report: Dict[str, Any], report_path: str):
        """Save feature engineering report"""
        try:
            with open(report_path, 'w') as f:
                json.dump(report, f, indent=2, default=str)
            logger.info(f"Feature engineering report saved to {report_path}")
        except Exception as e:
            logger.error(f"Failed to save engineering report: {e}")

def main():
    """Main execution function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Engineer features for ML model development')
    parser.add_argument('--data', required=True, help='Path to cleaned data directory')
    parser.add_argument('--requirements', required=True, help='Path to data requirements file')
    parser.add_argument('--output', required=True, help='Output directory for engineered features')
    parser.add_argument('--report', help='Path to save engineering report')
    
    args = parser.parse_args()
    
    try:
        # Initialize feature engineer
        engineer = FeatureEngineer(args.data, args.requirements, args.output)
        
        # Execute feature engineering
        engineering_report = engineer.execute_feature_engineering()
        
        # Save engineering report
        report_path = args.report or Path(args.output) / 'feature_engineering_report.json'
        engineer.save_engineering_report(engineering_report, report_path)
        
        # Return success if engineering passed quality thresholds
        effectiveness = engineering_report['engineering_summary']['engineering_effectiveness']
        quality_passed = engineering_report['engineering_summary']['quality_validation']['validation_passed']
        
        if effectiveness >= 0.8 and quality_passed:
            logger.info("Feature engineering completed successfully")
            return 0
        else:
            logger.warning(f"Feature engineering completed with effectiveness: {effectiveness:.3f}, Quality: {quality_passed}")
            return 1
            
    except Exception as e:
        logger.error(f"Feature engineering failed: {e}")
        return 1

if __name__ == '__main__':
    sys.exit(main())
