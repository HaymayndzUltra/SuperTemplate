#!/usr/bin/env python3
"""
Data Cleaning Script for Protocol 09
Cleans and transforms collected data to meet ML-readiness standards
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
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer, KNNImputer

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('data_cleaning.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class DataCleaner:
    """Cleans and transforms data for ML readiness"""
    
    def __init__(self, input_path: str, output_path: str):
        self.input_path = Path(input_path)
        self.output_path = Path(output_path)
        self.output_path.mkdir(parents=True, exist_ok=True)
        self.cleaning_log = []
        self.start_time = datetime.now()
        
        # Cleaning configuration
        self.cleaning_config = {
            'missing_value_threshold': 0.05,  # Remove columns with >5% missing
            'duplicate_threshold': 0.02,      # Flag datasets with >2% duplicates
            'outlier_threshold': 3.0,         # Z-score threshold for outliers
            'min_unique_values': 2,           # Minimum unique values for categorical
            'max_unique_values': 50           # Maximum unique values for categorical
        }
    
    def discover_data_files(self) -> List[Path]:
        """Discover all data files in input directory"""
        data_files = []
        
        # Look for common data file extensions
        extensions = ['.csv', '.json', '.parquet', '.xlsx', '.tsv']
        
        for ext in extensions:
            data_files.extend(self.input_path.glob(f"*{ext}"))
            data_files.extend(self.input_path.glob(f"**/*{ext}"))
        
        logger.info(f"Discovered {len(data_files)} data files for cleaning")
        return data_files
    
    def load_data_file(self, file_path: Path) -> Optional[pd.DataFrame]:
        """Load data file based on extension"""
        try:
            if file_path.suffix == '.csv':
                return pd.read_csv(file_path)
            elif file_path.suffix == '.json':
                return pd.read_json(file_path)
            elif file_path.suffix == '.parquet':
                return pd.read_parquet(file_path)
            elif file_path.suffix in ['.xlsx', '.xls']:
                return pd.read_excel(file_path)
            elif file_path.suffix == '.tsv':
                return pd.read_csv(file_path, sep='\t')
            else:
                logger.warning(f"Unsupported file format: {file_path.suffix}")
                return None
        except Exception as e:
            logger.error(f"Failed to load {file_path}: {e}")
            return None
    
    def analyze_data_quality(self, df: pd.DataFrame, file_path: Path) -> Dict[str, Any]:
        """Analyze data quality before cleaning"""
        logger.info(f"Analyzing data quality for {file_path.name}")
        
        quality_analysis = {
            'original_shape': list(df.shape),
            'missing_values': {},
            'data_types': df.dtypes.to_dict(),
            'duplicates': int(df.duplicated().sum()),
            'duplicate_percentage': float((df.duplicated().sum() / len(df)) * 100) if len(df) > 0 else 0,
            'memory_usage_mb': float(df.memory_usage(deep=True).sum() / (1024 * 1024))
        }
        
        # Analyze missing values by column
        for col in df.columns:
            missing_count = df[col].isnull().sum()
            missing_percentage = (missing_count / len(df)) * 100 if len(df) > 0 else 0
            quality_analysis['missing_values'][col] = {
                'count': int(missing_count),
                'percentage': float(missing_percentage)
            }
        
        return quality_analysis
    
    def handle_missing_values(self, df: pd.DataFrame, file_path: Path) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Handle missing values in the dataset"""
        logger.info(f"Handling missing values for {file_path.name}")
        
        cleaning_actions = []
        original_shape = df.shape
        
        # Remove columns with too many missing values
        cols_to_drop = []
        for col in df.columns:
            missing_percentage = (df[col].isnull().sum() / len(df)) * 100 if len(df) > 0 else 0
            if missing_percentage > self.cleaning_config['missing_value_threshold'] * 100:
                cols_to_drop.append(col)
        
        if cols_to_drop:
            df = df.drop(columns=cols_to_drop)
            cleaning_actions.append(f"Dropped {len(cols_to_drop)} columns with >{self.cleaning_config['missing_value_threshold']*100}% missing values")
        
        # Impute remaining missing values
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        categorical_cols = df.select_dtypes(include=['object']).columns
        
        # Numeric imputation using median
        if len(numeric_cols) > 0:
            imputer = SimpleImputer(strategy='median')
            df[numeric_cols] = imputer.fit_transform(df[numeric_cols])
            cleaning_actions.append(f"Imputed {len(numeric_cols)} numeric columns with median values")
        
        # Categorical imputation using mode
        if len(categorical_cols) > 0:
            for col in categorical_cols:
                mode_value = df[col].mode()
                if len(mode_value) > 0:
                    df[col] = df[col].fillna(mode_value[0])
            cleaning_actions.append(f"Imputed {len(categorical_cols)} categorical columns with mode values")
        
        missing_result = {
            'action': 'missing_value_handling',
            'original_shape': original_shape,
            'final_shape': list(df.shape),
            'columns_dropped': cols_to_drop,
            'numeric_columns_imputed': list(numeric_cols),
            'categorical_columns_imputed': list(categorical_cols),
            'cleaning_actions': cleaning_actions
        }
        
        logger.info(f"Missing value handling completed: {original_shape} -> {df.shape}")
        return df, missing_result
    
    def handle_duplicates(self, df: pd.DataFrame, file_path: Path) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Handle duplicate rows"""
        logger.info(f"Handling duplicates for {file_path.name}")
        
        original_shape = df.shape
        duplicate_count = df.duplicated().sum()
        
        if duplicate_count > 0:
            df = df.drop_duplicates()
            cleaning_actions = [f"Removed {duplicate_count} duplicate rows"]
        else:
            cleaning_actions = ["No duplicates found"]
        
        duplicate_result = {
            'action': 'duplicate_handling',
            'original_shape': original_shape,
            'final_shape': list(df.shape),
            'duplicates_removed': int(duplicate_count),
            'cleaning_actions': cleaning_actions
        }
        
        logger.info(f"Duplicate handling completed: {original_shape} -> {df.shape}")
        return df, duplicate_result
    
    def handle_outliers(self, df: pd.DataFrame, file_path: Path) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Handle outliers in numeric columns"""
        logger.info(f"Handling outliers for {file_path.name}")
        
        cleaning_actions = []
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        outlier_info = {}
        
        for col in numeric_cols:
            # Calculate Z-scores
            z_scores = np.abs((df[col] - df[col].mean()) / df[col].std())
            outliers = z_scores > self.cleaning_config['outlier_threshold']
            outlier_count = outliers.sum()
            
            if outlier_count > 0:
                # Cap outliers at threshold
                upper_bound = df[col].mean() + self.cleaning_config['outlier_threshold'] * df[col].std()
                lower_bound = df[col].mean() - self.cleaning_config['outlier_threshold'] * df[col].std()
                
                df[col] = np.where(df[col] > upper_bound, upper_bound, df[col])
                df[col] = np.where(df[col] < lower_bound, lower_bound, df[col])
                
                outlier_info[col] = {
                    'outliers_capped': int(outlier_count),
                    'upper_bound': float(upper_bound),
                    'lower_bound': float(lower_bound)
                }
                cleaning_actions.append(f"Capped {outlier_count} outliers in column '{col}'")
        
        outlier_result = {
            'action': 'outlier_handling',
            'numeric_columns_processed': list(numeric_cols),
            'outlier_info': outlier_info,
            'cleaning_actions': cleaning_actions
        }
        
        logger.info(f"Outlier handling completed for {len(numeric_cols)} numeric columns")
        return df, outlier_result
    
    def standardize_data_types(self, df: pd.DataFrame, file_path: Path) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Standardize and optimize data types"""
        logger.info(f"Standardizing data types for {file_path.name}")
        
        cleaning_actions = []
        type_conversions = {}
        
        for col in df.columns:
            original_type = str(df[col].dtype)
            
            # Convert object columns with numeric-like data to numeric
            if df[col].dtype == 'object':
                # Try to convert to numeric
                try:
                    numeric_converted = pd.to_numeric(df[col], errors='coerce')
                    if not numeric_converted.isna().all():
                        df[col] = numeric_converted
                        type_conversions[col] = {'from': original_type, 'to': 'numeric'}
                        cleaning_actions.append(f"Converted column '{col}' from {original_type} to numeric")
                except:
                    pass
            
            # Optimize numeric types
            if df[col].dtype in ['int64', 'float64']:
                if df[col].dtype == 'int64':
                    # Try to downcast to smaller integer types
                    if df[col].min() >= 0 and df[col].max() <= 255:
                        df[col] = df[col].astype('uint8')
                        type_conversions[col] = {'from': original_type, 'to': 'uint8'}
                    elif df[col].min() >= -128 and df[col].max() <= 127:
                        df[col] = df[col].astype('int8')
                        type_conversions[col] = {'from': original_type, 'to': 'int8'}
                elif df[col].dtype == 'float64':
                    # Try to convert to float32
                    df[col] = df[col].astype('float32')
                    type_conversions[col] = {'from': original_type, 'to': 'float32'}
        
        # Convert categorical columns to category dtype
        categorical_cols = df.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            unique_count = df[col].nunique()
            if unique_count <= self.cleaning_config['max_unique_values']:
                df[col] = df[col].astype('category')
                type_conversions[col] = {'from': str(df[col].dtype), 'to': 'category'}
                cleaning_actions.append(f"Converted column '{col}' to category dtype")
        
        type_result = {
            'action': 'data_type_standardization',
            'type_conversions': type_conversions,
            'cleaning_actions': cleaning_actions,
            'final_memory_usage_mb': float(df.memory_usage(deep=True).sum() / (1024 * 1024))
        }
        
        logger.info(f"Data type standardization completed: {len(type_conversions)} conversions")
        return df, type_result
    
    def clean_file(self, file_path: Path) -> Dict[str, Any]:
        """Clean a single data file"""
        logger.info(f"Cleaning file: {file_path}")
        
        try:
            # Load data
            df = self.load_data_file(file_path)
            if df is None:
                return {
                    'file_path': str(file_path),
                    'cleaning_status': 'failed',
                    'error': 'Could not load file'
                }
            
            # Analyze original quality
            original_quality = self.analyze_data_quality(df, file_path)
            
            # Apply cleaning steps
            cleaning_results = []
            
            # Handle missing values
            df, missing_result = self.handle_missing_values(df, file_path)
            cleaning_results.append(missing_result)
            
            # Handle duplicates
            df, duplicate_result = self.handle_duplicates(df, file_path)
            cleaning_results.append(duplicate_result)
            
            # Handle outliers
            df, outlier_result = self.handle_outliers(df, file_path)
            cleaning_results.append(outlier_result)
            
            # Standardize data types
            df, type_result = self.standardize_data_types(df, file_path)
            cleaning_results.append(type_result)
            
            # Save cleaned data
            output_file = self.output_path / f"cleaned_{file_path.name}"
            if file_path.suffix == '.csv':
                df.to_csv(output_file, index=False)
            elif file_path.suffix == '.json':
                df.to_json(output_file, orient='records', indent=2)
            elif file_path.suffix == '.parquet':
                df.to_parquet(output_file, index=False)
            else:
                # Default to CSV
                df.to_csv(output_file.with_suffix('.csv'), index=False)
                output_file = output_file.with_suffix('.csv')
            
            # Calculate cleaning effectiveness
            cleaning_effectiveness = self.calculate_cleaning_effectiveness(original_quality, df)
            
            file_cleaning_result = {
                'file_path': str(file_path),
                'cleaning_status': 'completed',
                'original_quality': original_quality,
                'cleaning_results': cleaning_results,
                'final_shape': list(df.shape),
                'cleaning_effectiveness': cleaning_effectiveness,
                'output_file': str(output_file),
                'cleaning_timestamp': datetime.now().isoformat()
            }
            
            logger.info(f"File cleaning completed: {file_path.name} - Effectiveness: {cleaning_effectiveness:.3f}")
            return file_cleaning_result
            
        except Exception as e:
            logger.error(f"File cleaning failed for {file_path}: {e}")
            return {
                'file_path': str(file_path),
                'cleaning_status': 'failed',
                'error': str(e),
                'cleaning_timestamp': datetime.now().isoformat()
            }
    
    def calculate_cleaning_effectiveness(self, original_quality: Dict[str, Any], cleaned_df: pd.DataFrame) -> float:
        """Calculate overall cleaning effectiveness score"""
        try:
            # Factors contributing to effectiveness
            factors = []
            
            # Missing value improvement
            original_missing = sum(info['percentage'] for info in original_quality['missing_values'].values())
            current_missing = (cleaned_df.isnull().sum().sum() / (cleaned_df.shape[0] * cleaned_df.shape[1])) * 100 if cleaned_df.shape[0] > 0 else 0
            missing_improvement = max(0, (original_missing - current_missing) / max(original_missing, 1))
            factors.append(missing_improvement)
            
            # Duplicate removal
            original_duplicates = original_quality['duplicate_percentage']
            current_duplicates = (cleaned_df.duplicated().sum() / len(cleaned_df)) * 100 if len(cleaned_df) > 0 else 0
            duplicate_improvement = max(0, (original_duplicates - current_duplicates) / max(original_duplicates, 1))
            factors.append(duplicate_improvement)
            
            # Data retention (we want to keep as much data as possible)
            original_rows = original_quality['original_shape'][0]
            current_rows = cleaned_df.shape[0]
            data_retention = current_rows / max(original_rows, 1)
            factors.append(data_retention)
            
            # Overall effectiveness is the average of factors
            effectiveness = np.mean(factors) if factors else 0.0
            return float(effectiveness)
            
        except Exception as e:
            logger.error(f"Failed to calculate cleaning effectiveness: {e}")
            return 0.0
    
    def execute_cleaning(self) -> Dict[str, Any]:
        """Execute cleaning for all discovered data files"""
        logger.info("Starting data cleaning execution")
        
        # Discover data files
        data_files = self.discover_data_files()
        
        if not data_files:
            logger.warning("No data files found for cleaning")
            return {
                'cleaning_summary': {
                    'total_files': 0,
                    'cleaned_files': 0,
                    'failed_files': 0,
                    'overall_effectiveness': 0.0,
                    'cleaning_passed': False
                },
                'file_cleaning_results': []
            }
        
        # Clean each file
        file_cleaning_results = []
        for file_path in data_files:
            cleaning_result = self.clean_file(file_path)
            file_cleaning_results.append(cleaning_result)
            self.cleaning_log.append(cleaning_result)
        
        # Calculate cleaning summary
        total_files = len(file_cleaning_results)
        cleaned_files = sum(1 for r in file_cleaning_results if r.get('cleaning_status') == 'completed')
        failed_files = total_files - cleaned_files
        
        # Calculate overall cleaning effectiveness
        effectiveness_scores = [r.get('cleaning_effectiveness', 0) for r in file_cleaning_results if 'cleaning_effectiveness' in r]
        overall_effectiveness = np.mean(effectiveness_scores) if effectiveness_scores else 0.0
        
        cleaning_summary = {
            'cleaning_summary': {
                'total_files': int(total_files),
                'cleaned_files': int(cleaned_files),
                'failed_files': int(failed_files),
                'success_rate': float(cleaned_files / total_files) if total_files > 0 else 0.0,
                'overall_effectiveness': float(overall_effectiveness),
                'effectiveness_threshold': 0.8,  # 80% effectiveness threshold
                'cleaning_passed': overall_effectiveness >= 0.8 and cleaned_files == total_files,
                'execution_time_seconds': (datetime.now() - self.start_time).total_seconds(),
                'start_time': self.start_time.isoformat(),
                'end_time': datetime.now().isoformat()
            },
            'file_cleaning_results': file_cleaning_results,
            'cleaning_config': self.cleaning_config
        }
        
        logger.info(f"Cleaning completed: {cleaned_files}/{total_files} files, Overall Effectiveness: {overall_effectiveness:.3f}")
        return cleaning_summary
    
    def save_cleaning_log(self, log_path: str):
        """Save cleaning log to specified path"""
        try:
            with open(log_path, 'w') as f:
                json.dump(self.cleaning_log, f, indent=2, default=str)
            logger.info(f"Cleaning log saved to {log_path}")
        except Exception as e:
            logger.error(f"Failed to save cleaning log: {e}")

def main():
    """Main execution function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Clean and transform collected data')
    parser.add_argument('--input', required=True, help='Input directory containing collected data')
    parser.add_argument('--output', required=True, help='Output directory for cleaned data')
    parser.add_argument('--log', help='Path to save cleaning log')
    
    args = parser.parse_args()
    
    try:
        # Initialize data cleaner
        cleaner = DataCleaner(args.input, args.output)
        
        # Execute cleaning
        cleaning_report = cleaner.execute_cleaning()
        
        # Save cleaning log if specified
        if args.log:
            cleaner.save_cleaning_log(args.log)
        
        # Save cleaning report
        report_file = Path(args.output) / 'cleaning_report.json'
        with open(report_file, 'w') as f:
            json.dump(cleaning_report, f, indent=2, default=str)
        
        logger.info(f"Cleaning report saved to {report_file}")
        
        # Return success if cleaning passed effectiveness threshold
        if cleaning_report['cleaning_summary']['cleaning_passed']:
            logger.info("Data cleaning completed successfully")
            return 0
        else:
            logger.warning(f"Data cleaning completed with effectiveness: {cleaning_report['cleaning_summary']['overall_effectiveness']:.3f}")
            return 1
            
    except Exception as e:
        logger.error(f"Data cleaning failed: {e}")
        return 1

if __name__ == '__main__':
    sys.exit(main())
