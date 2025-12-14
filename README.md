# 📊 Customer Churn Prediction & Retention Analytics

> **End-to-end machine learning system for predicting customer churn in telecommunications**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange.svg)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-Ensemble-red.svg)](https://xgboost.readthedocs.io/)

---

## 🎯 Overview

A comprehensive **churn prediction system** that analyzes 7,043 telecom customers using 79 engineered features to predict churn with 80%+ accuracy. The system identifies at-risk customers and provides actionable retention strategies, with potential to reduce churn by 15-20% and retain $500K+ in annual revenue.

**Key Technologies:** Python, Scikit-learn, XGBoost, SHAP, Pandas, Matplotlib/Seaborn

---

## 🚀 Key Capabilities

- **Advanced Feature Engineering**: 79 features from 21 raw attributes including CLV metrics, risk flags, and 12 high-impact interactions
- **ML Pipeline**: Ensemble models (Random Forest, XGBoost) with Grid Search CV, SMOTE, and 80%+ prediction accuracy
- **Customer Segmentation**: K-Means clustering identifying 5 actionable segments (Flight Risk, Value at Risk, Upsell Opportunities)
- **Interpretability**: SHAP analysis and feature importance for explainable, business-friendly predictions
- **Revenue Impact**: Quantified $500K+ retention potential with 15-20% churn reduction through targeted strategies

---

## 📊 Dataset

- **Source**: Telecom customer database (7,043 customers)
- **Features**: 21 original → 79 engineered (Demographics, Services, Contract, Payment, CLV, Risk flags)
- **Target**: Binary classification (Churn: 26.5% rate)
- **Class Imbalance**: Addressed using SMOTE and class weighting

---

## 🔬 Methodology

### 1. Data Exploration & Feature Engineering
- Statistical profiling, correlation analysis, chi-square tests (Cramér's V)
- Created 32 advanced features:
  - **Service Engagement**: Total services, security bundles, entertainment counts
  - **CLV Metrics**: Projected 24m value, revenue per month, loyalty score
  - **Interaction Features**: Contract×Tenure, Price×Service, Demographics×Behavior
  - **Risk Flags**: Flight risk, value at risk, retention needs, upsell opportunities

### 2. Model Development
- **Algorithms**: Logistic Regression (baseline), Random Forest, XGBoost, Gradient Boosting
- **Optimization**: Grid Search CV for hyperparameter tuning, stratified train/test split (80/20)
- **Evaluation**: ROC-AUC, Precision-Recall, F1-Score (emphasis on Recall to minimize false negatives)
- **Interpretability**: SHAP values for feature contribution analysis

### 3. Customer Segmentation
- K-Means clustering (3-5 clusters with elbow method and silhouette analysis)
- Segment profiling by churn rate, revenue contribution, and behavioral patterns
- Mapped retention strategies to each segment

---

## 📈 Key Findings

### Top Churn Drivers
1. **Contract Type**: Month-to-month contracts → **60%+ churn** (vs. 11% for 2-year contracts)
2. **Customer Tenure**: New customers (0-12 months) → **48% churn rate**
3. **Internet Service**: Fiber optic + MTM contract → **42% churn**
4. **Payment Method**: Electronic check users → **45% churn**
5. **Service Engagement**: 0 add-on services → **42% churn** (vs. 12% for fully engaged)

### High-Risk Segments
- 🚨 **Flight Risk**: MTM + new customer + no security → **60%+ churn**
- 💰 **Value at Risk**: High CLV + risky profile → **Priority retention**
- ⚠️ **Fiber MTM Risk**: Fiber users without long contracts → **42% churn**
- 🎯 **Upsell Opportunity**: Long tenure + low services → **Growth potential**

---

## 🎯 Business Recommendations

### Retention Strategies
1. **Contract Incentives**: Offer 1-2 year upgrade discounts (targets 42% of MTM base)
2. **Onboarding Programs**: Enhanced support for 0-12 month customers (48% churn rate)
3. **Security Bundles**: Promote OnlineSecurity + OnlineBackup (27% churn reduction)
4. **Payment Migration**: Move e-check users to auto-pay methods (45% → 25% churn)
5. **Service Engagement**: Personalized upsell for low-engagement customers

### Expected ROI
- 📉 15-20% overall churn reduction
- 💵 $500K+ annual revenue retention
- 🎯 3x ROI on targeted campaigns vs. blanket offers

---

## 📁 Project Structure

```
churn-prediction-project/
├── data/
│   ├── raw/                          # Original dataset (7,043 × 21)
│   └── processed/                    # Engineered features (7,043 × 79)
│
├── notebooks/
│   ├── 01_project_setup.ipynb
│   ├── 02a_target_analysis.ipynb
│   ├── 02b_numerical_eda.ipynb
│   ├── 02c_categorical_eda.ipynb
│   ├── 03a_basic_transformations.ipynb
│   ├── 03b_advanced_features.ipynb
│   ├── 03c_model_preparation.ipynb
│   ├── 04_customer_segmentation.ipynb
│   └── 05_churn_prediction_modeling.ipynb
│
├── visualizations/figures/           # EDA plots and analysis charts
├── models/                           # Saved trained models
└── requirements.txt
```

---

## 🛠️ Technologies

**Core:** Python 3.8+, Pandas, NumPy, Scikit-learn, XGBoost  
**Visualization:** Matplotlib, Seaborn  
**ML Tools:** SMOTE (imbalanced-learn), SHAP, Jupyter Notebook

---

## 🚀 Getting Started

### Installation

```bash
# Clone repository
git clone https://github.com/mihiniboteju/churn-prediction-system.git
cd churn-prediction-project

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
```

### Usage Example

```python
import pandas as pd
import joblib

# Load model and data
model = joblib.load('models/churn_classifier_xgboost.pkl')
data = pd.read_csv('data/processed/features_advanced_engineered.csv')

# Predict churn probability
churn_prob = model.predict_proba(data)[:, 1]

# Identify high-risk customers (>70% probability)
high_risk = data[churn_prob > 0.7]
print(f"High-risk customers: {len(high_risk)}")
```

---

## 📝 Requirements

```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
scikit-learn>=1.0.0
xgboost>=1.5.0
imbalanced-learn>=0.9.0
shap>=0.40.0
jupyter>=1.0.0
```

---

## 👤 Author

**Mihini Boteju**

- GitHub: [@mihiniboteju](https://github.com/mihiniboteju)
- LinkedIn: [Connect with me](https://linkedin.com/in/mihiniboteju)

---

## 📄 License

This project is licensed under the MIT License.

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ for data science and machine learning

</div>
