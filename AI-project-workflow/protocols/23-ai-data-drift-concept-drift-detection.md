# Protocol 23: AI Data Drift & Concept Drift Detection

## Metadata
```yaml
protocol_version: 1.0.0
created_date: 2025-01-07
category: mlops_monitoring
phase: "Phase 6: Monitoring & Governance"
priority: critical
tags: [drift-detection, data-quality, model-monitoring, statistical-tests]
triggers: [production-monitoring, data-quality-check, model-degradation]
```

## 1. Protocol Overview

**Purpose**: Detect and respond to data drift (input distribution changes) and concept drift (relationship changes between features and target) to maintain model performance and reliability in production.

**Critical Success Factors**:
- Early drift detection (< 24 hours)
- Low false positive rate (< 5%)
- Automated alerting and root cause analysis
- Clear remediation workflows
- Minimal performance impact

## 2. Drift Detection Workflow

### Step 1: Drift Detection Strategy
**Duration**: 4-6 hours

**Drift Types**:
```python
# drift_detection/drift_types.py

from enum import Enum
from dataclasses import dataclass
from typing import List, Dict

class DriftType(Enum):
    DATA_DRIFT = "data_drift"  # Input distribution changes
    CONCEPT_DRIFT = "concept_drift"  # Target relationship changes
    PREDICTION_DRIFT = "prediction_drift"  # Output distribution changes
    LABEL_DRIFT = "label_drift"  # Ground truth distribution changes

@dataclass
class DriftConfig:
    feature_name: str
    drift_type: DriftType
    detection_method: str  # ks_test, chi_square, psi, wasserstein
    threshold: float
    window_size: int
    sensitivity: str  # low, medium, high
    
# Feature-specific configurations
DRIFT_CONFIGS = {
    'numerical_features': DriftConfig(
        feature_name='*',
        drift_type=DriftType.DATA_DRIFT,
        detection_method='ks_test',
        threshold=0.05,
        window_size=1000,
        sensitivity='medium'
    ),
    'categorical_features': DriftConfig(
        feature_name='*',
        drift_type=DriftType.DATA_DRIFT,
        detection_method='chi_square',
        threshold=0.05,
        window_size=1000,
        sensitivity='medium'
    ),
    'predictions': DriftConfig(
        feature_name='prediction',
        drift_type=DriftType.PREDICTION_DRIFT,
        detection_method='psi',
        threshold=0.1,
        window_size=500,
        sensitivity='high'
    )
}
```

**Statistical Tests Implementation**:
```python
# drift_detection/statistical_tests.py

import numpy as np
from scipy import stats
from typing import Tuple, Dict

class StatisticalDriftDetector:
    
    def kolmogorov_smirnov_test(self, 
                                reference: np.ndarray,
                                current: np.ndarray,
                                threshold: float = 0.05) -> Dict:
        """KS test for numerical features."""
        
        statistic, p_value = stats.ks_2samp(reference, current)
        
        drift_detected = p_value < threshold
        
        return {
            'test': 'kolmogorov_smirnov',
            'statistic': float(statistic),
            'p_value': float(p_value),
            'threshold': threshold,
            'drift_detected': drift_detected,
            'drift_magnitude': float(statistic)
        }
    
    def chi_square_test(self,
                       reference: np.ndarray,
                       current: np.ndarray,
                       threshold: float = 0.05) -> Dict:
        """Chi-square test for categorical features."""
        
        # Create contingency table
        ref_counts = np.bincount(reference)
        cur_counts = np.bincount(current, minlength=len(ref_counts))
        
        # Chi-square test
        statistic, p_value = stats.chisquare(cur_counts, ref_counts)
        
        drift_detected = p_value < threshold
        
        return {
            'test': 'chi_square',
            'statistic': float(statistic),
            'p_value': float(p_value),
            'threshold': threshold,
            'drift_detected': drift_detected,
            'drift_magnitude': float(statistic / len(ref_counts))
        }
    
    def population_stability_index(self,
                                  reference: np.ndarray,
                                  current: np.ndarray,
                                  bins: int = 10) -> Dict:
        """PSI calculation for drift detection."""
        
        # Create bins
        _, bin_edges = np.histogram(reference, bins=bins)
        
        # Calculate distributions
        ref_dist, _ = np.histogram(reference, bins=bin_edges)
        cur_dist, _ = np.histogram(current, bins=bin_edges)
        
        # Normalize
        ref_dist = ref_dist / len(reference)
        cur_dist = cur_dist / len(current)
        
        # Avoid division by zero
        ref_dist = np.where(ref_dist == 0, 0.0001, ref_dist)
        cur_dist = np.where(cur_dist == 0, 0.0001, cur_dist)
        
        # Calculate PSI
        psi = np.sum((cur_dist - ref_dist) * np.log(cur_dist / ref_dist))
        
        # PSI thresholds: <0.1 (no drift), 0.1-0.2 (moderate), >0.2 (significant)
        if psi < 0.1:
            severity = 'no_drift'
        elif psi < 0.2:
            severity = 'moderate_drift'
        else:
            severity = 'significant_drift'
        
        return {
            'test': 'psi',
            'psi_value': float(psi),
            'severity': severity,
            'drift_detected': psi > 0.1,
            'drift_magnitude': float(psi)
        }
    
    def wasserstein_distance(self,
                            reference: np.ndarray,
                            current: np.ndarray,
                            threshold: float = 0.1) -> Dict:
        """Wasserstein distance (Earth Mover's Distance)."""
        
        distance = stats.wasserstein_distance(reference, current)
        
        # Normalize by reference std
        ref_std = np.std(reference)
        normalized_distance = distance / ref_std if ref_std > 0 else distance
        
        drift_detected = normalized_distance > threshold
        
        return {
            'test': 'wasserstein',
            'distance': float(distance),
            'normalized_distance': float(normalized_distance),
            'threshold': threshold,
            'drift_detected': drift_detected,
            'drift_magnitude': float(normalized_distance)
        }
```

### Step 2: Drift Detection Automation
**Duration**: 6-8 hours

**Automated Drift Monitor**:
```python
# drift_detection/drift_monitor.py

import pandas as pd
from datetime import datetime, timedelta
from typing import Dict, List
import logging

class DriftMonitor:
    
    def __init__(self, reference_data: pd.DataFrame, config: Dict):
        self.reference_data = reference_data
        self.config = config
        self.detector = StatisticalDriftDetector()
        self.drift_history = []
        
    def monitor_batch(self, current_data: pd.DataFrame) -> Dict:
        """Monitor a batch of data for drift."""
        
        drift_results = {
            'timestamp': datetime.now().isoformat(),
            'batch_size': len(current_data),
            'features_checked': 0,
            'drifts_detected': 0,
            'feature_results': {}
        }
        
        # Check numerical features
        numerical_cols = current_data.select_dtypes(include=[np.number]).columns
        for col in numerical_cols:
            if col in self.reference_data.columns:
                result = self._check_numerical_drift(col, current_data[col])
                drift_results['feature_results'][col] = result
                drift_results['features_checked'] += 1
                if result['drift_detected']:
                    drift_results['drifts_detected'] += 1
        
        # Check categorical features
        categorical_cols = current_data.select_dtypes(include=['object', 'category']).columns
        for col in categorical_cols:
            if col in self.reference_data.columns:
                result = self._check_categorical_drift(col, current_data[col])
                drift_results['feature_results'][col] = result
                drift_results['features_checked'] += 1
                if result['drift_detected']:
                    drift_results['drifts_detected'] += 1
        
        # Store in history
        self.drift_history.append(drift_results)
        
        # Trigger alerts if needed
        if drift_results['drifts_detected'] > 0:
            self._trigger_drift_alert(drift_results)
        
        return drift_results
    
    def _check_numerical_drift(self, feature_name: str, current_values: pd.Series) -> Dict:
        """Check drift for numerical feature."""
        
        reference_values = self.reference_data[feature_name].dropna()
        current_values = current_values.dropna()
        
        # Run multiple tests
        ks_result = self.detector.kolmogorov_smirnov_test(
            reference_values.values,
            current_values.values
        )
        
        psi_result = self.detector.population_stability_index(
            reference_values.values,
            current_values.values
        )
        
        wasserstein_result = self.detector.wasserstein_distance(
            reference_values.values,
            current_values.values
        )
        
        # Aggregate results
        drift_detected = any([
            ks_result['drift_detected'],
            psi_result['drift_detected'],
            wasserstein_result['drift_detected']
        ])
        
        return {
            'feature_name': feature_name,
            'feature_type': 'numerical',
            'drift_detected': drift_detected,
            'tests': {
                'ks_test': ks_result,
                'psi': psi_result,
                'wasserstein': wasserstein_result
            },
            'statistics': {
                'reference_mean': float(reference_values.mean()),
                'current_mean': float(current_values.mean()),
                'reference_std': float(reference_values.std()),
                'current_std': float(current_values.std())
            }
        }
    
    def _check_categorical_drift(self, feature_name: str, current_values: pd.Series) -> Dict:
        """Check drift for categorical feature."""
        
        reference_values = self.reference_data[feature_name].dropna()
        current_values = current_values.dropna()
        
        # Encode categories
        all_categories = list(set(reference_values) | set(current_values))
        cat_to_idx = {cat: idx for idx, cat in enumerate(all_categories)}
        
        ref_encoded = reference_values.map(cat_to_idx).values
        cur_encoded = current_values.map(cat_to_idx).values
        
        # Chi-square test
        chi_result = self.detector.chi_square_test(ref_encoded, cur_encoded)
        
        # Distribution comparison
        ref_dist = reference_values.value_counts(normalize=True)
        cur_dist = current_values.value_counts(normalize=True)
        
        return {
            'feature_name': feature_name,
            'feature_type': 'categorical',
            'drift_detected': chi_result['drift_detected'],
            'tests': {
                'chi_square': chi_result
            },
            'statistics': {
                'reference_distribution': ref_dist.to_dict(),
                'current_distribution': cur_dist.to_dict(),
                'new_categories': list(set(current_values) - set(reference_values)),
                'missing_categories': list(set(reference_values) - set(current_values))
            }
        }
    
    def _trigger_drift_alert(self, drift_results: Dict):
        """Trigger alert when drift is detected."""
        
        alert_message = f"""
        🚨 Data Drift Detected
        
        Timestamp: {drift_results['timestamp']}
        Features Affected: {drift_results['drifts_detected']}/{drift_results['features_checked']}
        
        Drifted Features:
        {self._format_drifted_features(drift_results['feature_results'])}
        
        Action Required: Review drift report and consider model retraining
        """
        
        logging.warning(alert_message)
        # Send to alerting system (Slack, PagerDuty, etc.)
```

### Step 3: Concept Drift Detection
**Duration**: 5-6 hours

**Concept Drift Detector**:
```python
# drift_detection/concept_drift.py

from sklearn.metrics import accuracy_score, f1_score
import numpy as np

class ConceptDriftDetector:
    
    def __init__(self, model, window_size: int = 1000):
        self.model = model
        self.window_size = window_size
        self.performance_history = []
        
    def detect_concept_drift(self,
                            X_current: np.ndarray,
                            y_true: np.ndarray,
                            baseline_accuracy: float) -> Dict:
        """Detect concept drift using performance degradation."""
        
        # Get predictions
        y_pred = self.model.predict(X_current)
        
        # Calculate current performance
        current_accuracy = accuracy_score(y_true, y_pred)
        current_f1 = f1_score(y_true, y_pred, average='weighted')
        
        # Store in history
        self.performance_history.append({
            'timestamp': datetime.now(),
            'accuracy': current_accuracy,
            'f1_score': current_f1,
            'sample_size': len(y_true)
        })
        
        # Keep only recent history
        if len(self.performance_history) > self.window_size:
            self.performance_history = self.performance_history[-self.window_size:]
        
        # Detect drift
        accuracy_drop = baseline_accuracy - current_accuracy
        drift_detected = accuracy_drop > 0.05  # 5% threshold
        
        # Calculate trend
        if len(self.performance_history) >= 10:
            recent_accuracies = [h['accuracy'] for h in self.performance_history[-10:]]
            trend = np.polyfit(range(len(recent_accuracies)), recent_accuracies, 1)[0]
        else:
            trend = 0
        
        return {
            'drift_detected': drift_detected,
            'baseline_accuracy': baseline_accuracy,
            'current_accuracy': current_accuracy,
            'accuracy_drop': accuracy_drop,
            'current_f1': current_f1,
            'trend': 'declining' if trend < -0.01 else 'stable',
            'severity': self._calculate_severity(accuracy_drop)
        }
    
    def _calculate_severity(self, accuracy_drop: float) -> str:
        """Calculate drift severity."""
        if accuracy_drop < 0.05:
            return 'low'
        elif accuracy_drop < 0.10:
            return 'medium'
        elif accuracy_drop < 0.20:
            return 'high'
        else:
            return 'critical'
```

### Step 4: Root Cause Analysis
**Duration**: 4-5 hours

**Drift Root Cause Analyzer**:
```python
# drift_detection/root_cause_analysis.py

class DriftRootCauseAnalyzer:
    
    def analyze_drift_causes(self, drift_results: Dict, current_data: pd.DataFrame) -> Dict:
        """Perform root cause analysis for detected drift."""
        
        root_causes = {
            'timestamp': datetime.now().isoformat(),
            'analysis_type': 'automated',
            'findings': []
        }
        
        for feature, result in drift_results['feature_results'].items():
            if result['drift_detected']:
                cause = self._analyze_feature_drift(feature, result, current_data)
                root_causes['findings'].append(cause)
        
        return root_causes
    
    def _analyze_feature_drift(self, feature: str, result: Dict, data: pd.DataFrame) -> Dict:
        """Analyze drift for a specific feature."""
        
        analysis = {
            'feature': feature,
            'drift_type': result['feature_type'],
            'possible_causes': [],
            'recommendations': []
        }
        
        if result['feature_type'] == 'numerical':
            stats = result['statistics']
            
            # Check for mean shift
            mean_shift = abs(stats['current_mean'] - stats['reference_mean'])
            if mean_shift > stats['reference_std']:
                analysis['possible_causes'].append({
                    'cause': 'significant_mean_shift',
                    'description': f"Mean shifted by {mean_shift:.2f} (>{stats['reference_std']:.2f} std)",
                    'severity': 'high'
                })
                analysis['recommendations'].append("Investigate data source changes or upstream pipeline modifications")
            
            # Check for variance change
            variance_ratio = stats['current_std'] / stats['reference_std']
            if variance_ratio > 1.5 or variance_ratio < 0.5:
                analysis['possible_causes'].append({
                    'cause': 'variance_change',
                    'description': f"Variance changed by {variance_ratio:.2f}x",
                    'severity': 'medium'
                })
                analysis['recommendations'].append("Check for data quality issues or population changes")
        
        elif result['feature_type'] == 'categorical':
            stats = result['statistics']
            
            # Check for new categories
            if stats['new_categories']:
                analysis['possible_causes'].append({
                    'cause': 'new_categories',
                    'description': f"New categories detected: {stats['new_categories']}",
                    'severity': 'high'
                })
                analysis['recommendations'].append("Update model to handle new categories or filter them")
            
            # Check for missing categories
            if stats['missing_categories']:
                analysis['possible_causes'].append({
                    'cause': 'missing_categories',
                    'description': f"Categories no longer present: {stats['missing_categories']}",
                    'severity': 'medium'
                })
        
        return analysis
```

### Step 5: Drift Reporting & Alerting
**Duration**: 3-4 hours

**Drift Report Generator**:
```yaml
# drift_detection/drift-detection-config.yaml

drift_monitoring:
  enabled: true
  check_interval: 1h
  reference_window: 30d
  detection_window: 1d
  
  thresholds:
    psi:
      no_drift: 0.1
      moderate: 0.2
      significant: 0.3
    ks_test:
      p_value: 0.05
    chi_square:
      p_value: 0.05
  
  alerting:
    channels:
      - slack: "#ml-drift-alerts"
      - email: "ml-team@company.com"
    
    severity_routing:
      critical:
        - pagerduty
        - slack
        - email
      high:
        - slack
        - email
      medium:
        - slack
      low:
        - email
  
  reporting:
    daily_summary: true
    weekly_report: true
    auto_generate: true
    retention_days: 90
```

## 3. Quality Gates

### Gate 1: Detection Setup
- [ ] Reference data collected (minimum 30 days)
- [ ] All features configured for drift detection
- [ ] Statistical test thresholds calibrated
- [ ] Drift detection pipeline deployed
- [ ] Monitoring dashboard operational

### Gate 2: Alert Configuration
- [ ] Alert rules defined for all drift types
- [ ] Notification channels configured
- [ ] Alert severity levels calibrated
- [ ] False positive rate < 5%
- [ ] Runbooks created for each alert type

### Gate 3: Validation
- [ ] Drift detection tested with synthetic drift
- [ ] Root cause analysis validated
- [ ] Alert delivery confirmed
- [ ] Performance impact < 2% latency
- [ ] Documentation complete

## 4. Deliverables

### Required Outputs
1. **Drift Detection Configuration** (`drift-detection-config.yaml`)
2. **Drift Report** (`drift-report.md`)
3. **Alert History** (`alert-history.json`)
4. **Root Cause Analysis** (`root-cause-analysis.md`)
5. **Reference Data Snapshot** (`reference-data.parquet`)
6. **Drift Dashboard** (`drift-dashboard.json`)

### Evidence Package Structure
```
evidence/protocol-23-drift-detection/
├── configs/
│   └── drift-detection-config.yaml
├── reports/
│   ├── drift-report.md
│   ├── root-cause-analysis.md
│   └── weekly-drift-summary.md
├── data/
│   ├── reference-data.parquet
│   ├── drift-history.json
│   └── alert-history.json
├── scripts/
│   ├── statistical_tests.py
│   ├── drift_monitor.py
│   └── concept_drift.py
└── dashboards/
    └── drift-dashboard.json
```

## 5. Success Criteria

- **Detection Latency**: < 24 hours for significant drift
- **False Positive Rate**: < 5%
- **Coverage**: 100% of critical features monitored
- **Alert Response Time**: < 30 minutes
- **Root Cause Accuracy**: > 80% of alerts have actionable insights
