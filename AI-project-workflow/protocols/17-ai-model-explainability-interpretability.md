# Protocol 17: AI Model Explainability & Interpretability

## Metadata
```yaml
protocol_version: 1.0.0
created_date: 2025-01-07
category: testing_qa
phase: "Phase 4: AI Model Testing & Quality Assurance"
priority: critical
tags: [explainability, interpretability, shap, lime, transparency, xai]
triggers: [explainability, interpretability, model-transparency, xai]
```

## 1. Protocol Overview

**Purpose**: Provide comprehensive model explainability and interpretability through SHAP values, LIME explanations, feature importance analysis, and decision path visualization to ensure stakeholder trust and regulatory compliance.

**Critical Success Factors**:
- Global and local interpretability
- Stakeholder-appropriate explanations
- Regulatory compliance (GDPR Article 22)
- Actionable insights
- Continuous explanation monitoring

## 2. Explainability Workflow

### Step 1: Global Model Interpretability
**Duration**: 4-6 hours

**Activities**:
1. Feature importance calculation
2. Partial dependence plots
3. Global SHAP analysis
4. Model behavior documentation
5. Decision rule extraction

**Implementation**:
```python
# explainability/global_interpretability.py

import shap
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.inspection import partial_dependence, PartialDependenceDisplay

class GlobalInterpreter:
    
    def __init__(self, model, X_train, feature_names):
        """
        Initialize global interpreter.
        
        Args:
            model: Trained model
            X_train: Training data for background distribution
            feature_names: List of feature names
        """
        self.model = model
        self.X_train = X_train
        self.feature_names = feature_names
        self.explainer = None
        self.shap_values = None
    
    def calculate_feature_importance(self):
        """Calculate feature importance using multiple methods."""
        
        importance_scores = {}
        
        # Method 1: Model-specific importance (if available)
        if hasattr(self.model, 'feature_importances_'):
            importance_scores['model_native'] = dict(zip(
                self.feature_names,
                self.model.feature_importances_
            ))
        
        # Method 2: Permutation importance
        from sklearn.inspection import permutation_importance
        
        perm_importance = permutation_importance(
            self.model, self.X_train, 
            n_repeats=10, random_state=42
        )
        
        importance_scores['permutation'] = dict(zip(
            self.feature_names,
            perm_importance.importances_mean
        ))
        
        # Method 3: SHAP-based importance
        if self.shap_values is None:
            self._calculate_shap_values()
        
        shap_importance = np.abs(self.shap_values).mean(axis=0)
        importance_scores['shap'] = dict(zip(
            self.feature_names,
            shap_importance
        ))
        
        return importance_scores
    
    def _calculate_shap_values(self):
        """Calculate SHAP values for global interpretation."""
        
        # Select appropriate explainer based on model type
        if hasattr(self.model, 'predict_proba'):
            # Tree-based models
            try:
                self.explainer = shap.TreeExplainer(self.model)
            except:
                # Fallback to KernelExplainer
                self.explainer = shap.KernelExplainer(
                    self.model.predict_proba,
                    shap.sample(self.X_train, 100)
                )
        else:
            # Linear models or others
            self.explainer = shap.LinearExplainer(
                self.model, self.X_train
            )
        
        # Calculate SHAP values
        self.shap_values = self.explainer.shap_values(self.X_train)
        
        return self.shap_values
    
    def plot_global_shap_summary(self, save_path=None):
        """Create SHAP summary plot for global interpretation."""
        
        if self.shap_values is None:
            self._calculate_shap_values()
        
        plt.figure(figsize=(10, 8))
        shap.summary_plot(
            self.shap_values, 
            self.X_train,
            feature_names=self.feature_names,
            show=False
        )
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
        
        plt.close()
    
    def plot_feature_importance_comparison(self, save_path=None):
        """Compare feature importance across methods."""
        
        importance_scores = self.calculate_feature_importance()
        
        # Create comparison dataframe
        comparison_df = pd.DataFrame(importance_scores)
        comparison_df = comparison_df.sort_values('shap', ascending=False).head(15)
        
        # Normalize for comparison
        comparison_df_norm = comparison_df.div(comparison_df.max(axis=0), axis=1)
        
        # Plot
        fig, ax = plt.subplots(figsize=(12, 8))
        comparison_df_norm.plot(kind='barh', ax=ax)
        ax.set_xlabel('Normalized Importance Score')
        ax.set_ylabel('Feature')
        ax.set_title('Feature Importance Comparison Across Methods')
        ax.legend(title='Method')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
        
        return comparison_df
    
    def generate_partial_dependence_plots(self, features, save_path=None):
        """Generate partial dependence plots for key features."""
        
        fig, ax = plt.subplots(figsize=(14, 10))
        
        display = PartialDependenceDisplay.from_estimator(
            self.model,
            self.X_train,
            features=features,
            feature_names=self.feature_names,
            ax=ax
        )
        
        plt.suptitle('Partial Dependence Plots', fontsize=16)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
        
        return display
    
    def extract_decision_rules(self, max_depth=3):
        """Extract interpretable decision rules from tree-based models."""
        
        if not hasattr(self.model, 'tree_'):
            return "Decision rule extraction only available for tree-based models"
        
        from sklearn.tree import export_text
        
        rules = export_text(
            self.model,
            feature_names=self.feature_names,
            max_depth=max_depth
        )
        
        return rules
```

### Step 2: Local Instance Explanations (SHAP)
**Duration**: 4-6 hours

**Activities**:
1. Individual prediction explanations
2. SHAP force plots
3. SHAP waterfall charts
4. Decision path analysis
5. Counterfactual explanations

**Implementation**:
```python
# explainability/local_shap.py

import shap
import numpy as np
import matplotlib.pyplot as plt

class LocalSHAPExplainer:
    
    def __init__(self, model, X_background, feature_names):
        """
        Initialize local SHAP explainer.
        
        Args:
            model: Trained model
            X_background: Background dataset for SHAP
            feature_names: List of feature names
        """
        self.model = model
        self.feature_names = feature_names
        
        # Initialize SHAP explainer
        self.explainer = shap.Explainer(model, X_background)
    
    def explain_instance(self, instance):
        """Generate SHAP explanation for a single instance."""
        
        # Calculate SHAP values for instance
        shap_values = self.explainer(instance)
        
        explanation = {
            'prediction': self.model.predict(instance)[0],
            'base_value': self.explainer.expected_value,
            'shap_values': dict(zip(
                self.feature_names,
                shap_values.values[0]
            )),
            'feature_values': dict(zip(
                self.feature_names,
                instance[0]
            ))
        }
        
        return explanation
    
    def plot_force_plot(self, instance, save_path=None):
        """Create SHAP force plot for instance explanation."""
        
        shap_values = self.explainer(instance)
        
        # Create force plot
        shap.plots.force(
            self.explainer.expected_value,
            shap_values.values[0],
            instance[0],
            feature_names=self.feature_names,
            matplotlib=True,
            show=False
        )
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
        
        plt.close()
    
    def plot_waterfall(self, instance, save_path=None):
        """Create SHAP waterfall chart for instance."""
        
        shap_values = self.explainer(instance)
        
        plt.figure(figsize=(10, 8))
        shap.plots.waterfall(shap_values[0], show=False)
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
        
        plt.close()
    
    def plot_decision_plot(self, instances, save_path=None):
        """Create SHAP decision plot for multiple instances."""
        
        shap_values = self.explainer(instances)
        
        plt.figure(figsize=(10, 8))
        shap.decision_plot(
            self.explainer.expected_value,
            shap_values.values,
            instances,
            feature_names=self.feature_names,
            show=False
        )
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
        
        plt.close()
    
    def generate_counterfactual(self, instance, target_class):
        """Generate counterfactual explanation."""
        
        # Simple counterfactual: find minimal changes needed
        current_pred = self.model.predict(instance)[0]
        
        if current_pred == target_class:
            return "Instance already predicts target class"
        
        # Get SHAP values to identify most impactful features
        shap_values = self.explainer(instance)
        feature_impacts = dict(zip(
            self.feature_names,
            np.abs(shap_values.values[0])
        ))
        
        # Sort features by impact
        sorted_features = sorted(
            feature_impacts.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        counterfactual = {
            'original_prediction': current_pred,
            'target_prediction': target_class,
            'suggested_changes': []
        }
        
        # Suggest changes to top features
        for feature, impact in sorted_features[:5]:
            feature_idx = self.feature_names.index(feature)
            current_value = instance[0][feature_idx]
            shap_value = shap_values.values[0][feature_idx]
            
            # Suggest direction of change
            if shap_value > 0:
                suggestion = "decrease"
            else:
                suggestion = "increase"
            
            counterfactual['suggested_changes'].append({
                'feature': feature,
                'current_value': current_value,
                'suggestion': suggestion,
                'impact': impact
            })
        
        return counterfactual
```

### Step 3: Local Instance Explanations (LIME)
**Duration**: 4-6 hours

**Activities**:
1. LIME tabular explanations
2. LIME text explanations (if applicable)
3. LIME image explanations (if applicable)
4. Explanation stability analysis
5. Comparison with SHAP

**Implementation**:
```python
# explainability/local_lime.py

import lime
import lime.lime_tabular
import numpy as np
import matplotlib.pyplot as plt

class LocalLIMEExplainer:
    
    def __init__(self, model, X_train, feature_names, class_names=None):
        """
        Initialize LIME explainer.
        
        Args:
            model: Trained model
            X_train: Training data
            feature_names: List of feature names
            class_names: List of class names (for classification)
        """
        self.model = model
        self.feature_names = feature_names
        self.class_names = class_names or ['Class 0', 'Class 1']
        
        # Initialize LIME explainer
        self.explainer = lime.lime_tabular.LimeTabularExplainer(
            training_data=X_train,
            feature_names=feature_names,
            class_names=self.class_names,
            mode='classification' if hasattr(model, 'predict_proba') else 'regression'
        )
    
    def explain_instance(self, instance, num_features=10):
        """Generate LIME explanation for instance."""
        
        # Get prediction function
        if hasattr(self.model, 'predict_proba'):
            predict_fn = self.model.predict_proba
        else:
            predict_fn = self.model.predict
        
        # Generate explanation
        explanation = self.explainer.explain_instance(
            data_row=instance[0],
            predict_fn=predict_fn,
            num_features=num_features
        )
        
        return explanation
    
    def plot_explanation(self, instance, save_path=None):
        """Plot LIME explanation."""
        
        explanation = self.explain_instance(instance)
        
        fig = explanation.as_pyplot_figure()
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
        
        plt.close()
        
        return explanation
    
    def get_explanation_as_dict(self, instance):
        """Get LIME explanation as dictionary."""
        
        explanation = self.explain_instance(instance)
        
        explanation_dict = {
            'prediction': self.model.predict(instance)[0],
            'feature_contributions': dict(explanation.as_list()),
            'intercept': explanation.intercept[1] if hasattr(explanation, 'intercept') else None,
            'local_pred': explanation.local_pred[0] if hasattr(explanation, 'local_pred') else None
        }
        
        return explanation_dict
    
    def analyze_explanation_stability(self, instance, num_samples=10):
        """Analyze stability of LIME explanations."""
        
        explanations = []
        
        for _ in range(num_samples):
            exp = self.explain_instance(instance)
            explanations.append(dict(exp.as_list()))
        
        # Calculate stability metrics
        all_features = set()
        for exp in explanations:
            all_features.update(exp.keys())
        
        stability_scores = {}
        
        for feature in all_features:
            values = [exp.get(feature, 0) for exp in explanations]
            stability_scores[feature] = {
                'mean': np.mean(values),
                'std': np.std(values),
                'coefficient_of_variation': np.std(values) / (np.mean(values) + 1e-10)
            }
        
        return stability_scores
    
    def compare_with_shap(self, instance, shap_explainer):
        """Compare LIME and SHAP explanations."""
        
        # Get LIME explanation
        lime_exp = self.get_explanation_as_dict(instance)
        
        # Get SHAP explanation
        shap_exp = shap_explainer.explain_instance(instance)
        
        # Compare feature contributions
        comparison = {
            'lime_contributions': lime_exp['feature_contributions'],
            'shap_contributions': shap_exp['shap_values'],
            'correlation': self._calculate_correlation(
                lime_exp['feature_contributions'],
                shap_exp['shap_values']
            )
        }
        
        return comparison
    
    def _calculate_correlation(self, lime_values, shap_values):
        """Calculate correlation between LIME and SHAP."""
        
        # Align features
        common_features = set(lime_values.keys()) & set(shap_values.keys())
        
        lime_array = np.array([lime_values[f] for f in common_features])
        shap_array = np.array([shap_values[f] for f in common_features])
        
        correlation = np.corrcoef(lime_array, shap_array)[0, 1]
        
        return correlation
```

### Step 4: Feature Importance Visualization
**Duration**: 3-4 hours

**Activities**:
1. Create feature importance charts
2. Generate interaction plots
3. Visualize feature distributions
4. Create decision boundary plots
5. Generate explanation dashboards

**Implementation**:
```python
# explainability/visualizations.py

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class ExplainabilityVisualizer:
    
    def __init__(self, feature_names):
        self.feature_names = feature_names
    
    def plot_feature_importance_bar(self, importance_scores, top_n=15, save_path=None):
        """Create bar chart of feature importance."""
        
        # Sort by importance
        sorted_features = sorted(
            importance_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )[:top_n]
        
        features, scores = zip(*sorted_features)
        
        plt.figure(figsize=(10, 8))
        plt.barh(range(len(features)), scores, color='steelblue')
        plt.yticks(range(len(features)), features)
        plt.xlabel('Importance Score')
        plt.title(f'Top {top_n} Most Important Features')
        plt.gca().invert_yaxis()
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
        
        plt.close()
    
    def plot_shap_interaction(self, shap_interaction_values, feature_idx1, 
                             feature_idx2, X_data, save_path=None):
        """Plot SHAP interaction between two features."""
        
        plt.figure(figsize=(10, 8))
        
        shap.dependence_plot(
            (feature_idx1, feature_idx2),
            shap_interaction_values,
            X_data,
            feature_names=self.feature_names,
            show=False
        )
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
        
        plt.close()
    
    def create_interactive_dashboard(self, global_importance, local_explanations, 
                                    save_path='explainability-dashboard.html'):
        """Create interactive explainability dashboard."""
        
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=(
                'Global Feature Importance',
                'SHAP Summary',
                'Local Explanation Example',
                'Explanation Stability'
            ),
            specs=[
                [{'type': 'bar'}, {'type': 'scatter'}],
                [{'type': 'bar'}, {'type': 'scatter'}]
            ]
        )
        
        # Plot 1: Global importance
        sorted_features = sorted(
            global_importance.items(),
            key=lambda x: x[1],
            reverse=True
        )[:15]
        features, scores = zip(*sorted_features)
        
        fig.add_trace(
            go.Bar(x=list(scores), y=list(features), orientation='h',
                   marker_color='steelblue'),
            row=1, col=1
        )
        
        # Plot 2: SHAP summary (placeholder)
        fig.add_trace(
            go.Scatter(x=[1, 2, 3], y=[1, 2, 3], mode='markers'),
            row=1, col=2
        )
        
        # Plot 3: Local explanation
        if local_explanations:
            exp = local_explanations[0]
            features_local = list(exp['shap_values'].keys())[:10]
            values_local = [exp['shap_values'][f] for f in features_local]
            
            fig.add_trace(
                go.Bar(x=values_local, y=features_local, orientation='h',
                       marker_color='coral'),
                row=2, col=1
            )
        
        fig.update_layout(
            title_text="Model Explainability Dashboard",
            showlegend=False,
            height=900
        )
        
        fig.write_html(save_path)
        
        return fig
    
    def generate_interpretation_guide(self, model_type, save_path='interpretation-guide.md'):
        """Generate stakeholder-friendly interpretation guide."""
        
        guide = f"""# Model Interpretation Guide

## Understanding Model Predictions

### Model Type: {model_type}

## Key Concepts

### 1. Feature Importance
Feature importance tells us which input variables have the most influence on the model's predictions.

**How to read**: Higher values indicate more important features.

### 2. SHAP Values
SHAP (SHapley Additive exPlanations) values show how each feature contributes to a specific prediction.

**How to read**:
- Positive SHAP value → Feature pushes prediction higher
- Negative SHAP value → Feature pushes prediction lower
- Larger absolute value → Stronger influence

### 3. LIME Explanations
LIME (Local Interpretable Model-agnostic Explanations) provides local approximations of model behavior.

**How to read**:
- Shows which features were most important for a specific prediction
- Values indicate direction and magnitude of influence

## Interpreting Your Prediction

### Step 1: Check the Prediction
- Look at the final prediction value
- Compare to the baseline (average prediction)

### Step 2: Identify Key Features
- Review the top 5-10 features by importance
- Understand what each feature represents

### Step 3: Understand Feature Contributions
- Positive contributions increase the prediction
- Negative contributions decrease the prediction

### Step 4: Validate Reasonableness
- Do the important features make sense?
- Are the contributions aligned with domain knowledge?

## Common Questions

**Q: Why did the model make this prediction?**
A: Review the SHAP waterfall chart to see step-by-step how features contributed.

**Q: What would change the prediction?**
A: Look at the counterfactual explanation for suggested changes.

**Q: Is the model fair?**
A: Check the fairness audit report for demographic analysis.

## Regulatory Compliance

This explanation satisfies:
- GDPR Article 22 (Right to Explanation)
- EU AI Act transparency requirements
- ISO/IEC 42001 interpretability standards

## Contact

For questions about model explanations, contact: [Model Owner]
"""
        
        with open(save_path, 'w') as f:
            f.write(guide)
        
        return guide
```

### Step 5: Model Transparency Documentation
**Duration**: 4-5 hours

**Activities**:
1. Create model cards
2. Document model limitations
3. Generate explanation reports
4. Stakeholder communication materials
5. Regulatory compliance documentation

**Implementation**:
```python
# explainability/model_card.py

from dataclasses import dataclass
from typing import List, Dict
import json

@dataclass
class ModelCard:
    """Model card for transparency and documentation."""
    
    model_name: str
    model_version: str
    model_type: str
    intended_use: str
    training_data: Dict
    performance_metrics: Dict
    fairness_metrics: Dict
    limitations: List[str]
    ethical_considerations: List[str]
    explainability_methods: List[str]
    
    def to_markdown(self):
        """Generate model card as markdown."""
        
        card = f"""# Model Card: {self.model_name}

## Model Details
- **Version**: {self.model_version}
- **Type**: {self.model_type}
- **Last Updated**: {self.training_data.get('last_updated', 'N/A')}

## Intended Use
{self.intended_use}

## Training Data
- **Dataset**: {self.training_data.get('dataset_name', 'N/A')}
- **Size**: {self.training_data.get('size', 'N/A')} samples
- **Features**: {self.training_data.get('num_features', 'N/A')}
- **Time Period**: {self.training_data.get('time_period', 'N/A')}

## Performance Metrics
"""
        for metric, value in self.performance_metrics.items():
            card += f"- **{metric}**: {value}\n"
        
        card += f"""
## Fairness Metrics
"""
        for metric, value in self.fairness_metrics.items():
            card += f"- **{metric}**: {value}\n"
        
        card += f"""
## Limitations
"""
        for limitation in self.limitations:
            card += f"- {limitation}\n"
        
        card += f"""
## Ethical Considerations
"""
        for consideration in self.ethical_considerations:
            card += f"- {consideration}\n"
        
        card += f"""
## Explainability Methods
"""
        for method in self.explainability_methods:
            card += f"- {method}\n"
        
        return card
    
    def save(self, filepath):
        """Save model card to file."""
        with open(filepath, 'w') as f:
            f.write(self.to_markdown())
```

## 3. Quality Gates

### Gate 1: Explainability Coverage
- [ ] Global interpretability documented
- [ ] Local explanations available for all predictions
- [ ] SHAP values calculated and validated
- [ ] LIME explanations generated and tested

### Gate 2: Stakeholder Communication
- [ ] Interpretation guide created
- [ ] Model card completed
- [ ] Explanation dashboard deployed
- [ ] Stakeholder training conducted

### Gate 3: Regulatory Compliance
- [ ] GDPR Article 22 compliance verified
- [ ] EU AI Act transparency requirements met
- [ ] Documentation audit trail complete
- [ ] Legal team approval obtained

## 4. Deliverables

### Required Outputs
1. **Explainability Report** (`explainability-report.md`)
2. **SHAP Values** (`shap-values.pkl`)
3. **Interpretation Guide** (`interpretation-guide.md`)
4. **Model Card** (`model-card.md`)
5. **Explanation Dashboard** (`explainability-dashboard.html`)

### Evidence Package Structure
```
evidence/protocol-17-explainability/
├── reports/
│   ├── explainability-report.md
│   ├── interpretation-guide.md
│   └── model-card.md
├── artifacts/
│   ├── shap-values.pkl
│   ├── lime-explainer.pkl
│   └── feature-importance.json
├── visualizations/
│   ├── explainability-dashboard.html
│   ├── shap-summary.png
│   ├── feature-importance.png
│   └── partial-dependence.png
└── documentation/
    ├── stakeholder-guide.pdf
    └── regulatory-compliance.md
```

## 5. Success Criteria

- **Global Interpretability**: Feature importance documented and validated
- **Local Explanations**: SHAP and LIME available for all predictions
- **Stakeholder Understanding**: >80% comprehension in user testing
- **Regulatory Compliance**: All transparency requirements met
- **Documentation**: Complete audit trail with evidence
