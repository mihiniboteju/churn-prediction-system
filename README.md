# Customer Churn Prediction & Retention Analytics

> End-to-end machine learning system for predicting customer churn in telecommunications

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3.2-orange.svg)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.29.0-FF4B4B.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Live Demo:** [https://churn-insight-analytics.streamlit.app](https://churn-prediction-telcom.streamlit.app/) *(Coming Soon)*

---

## Overview

A comprehensive churn prediction system that analyzes 7,043 telecom customers to predict churn with **80.41% accuracy**. The system identifies at-risk customers, provides actionable retention strategies, and includes an interactive web application for real-time predictions.

### Key Highlights

- **80.41%** Accuracy with **84.34%** ROC-AUC
- Identified **2 distinct customer segments** (High-Risk 56.5%, Stable 43.5%)
- Potential to retain **$1M-2M** in annual revenue
- **Interactive Streamlit App** for live predictions and insights
- **37 optimized features** after VIF analysis

**Key Technologies:** Python, Scikit-learn, Streamlit, Plotly, Pandas, NumPy

---

## Features

### Machine Learning
- Advanced feature engineering: 79 features engineered from 21 raw attributes
- Optimized model: Logistic Regression with 37 features (post-VIF analysis)
- Performance metrics: 
  - Accuracy: 80.41%
  - Precision: 66.33%
  - Recall: 53.21%
  - F1-Score: 59.05%
  - ROC-AUC: 84.34%

### Customer Segmentation
- K-Means clustering: 2 actionable customer segments
  - **Segment 0 (High-Risk)**: 3,978 customers (56.5%), 29.7% churn rate
  - **Segment 1 (Stable)**: 3,065 customers (43.5%), 22.4% churn rate
- Segment-specific retention strategies tailored to each group

### Interactive Web Application
- 5 interactive pages: Home, Problem & Solution, Data Story, Customer Segments, Model Performance
- Live prediction tool with real-time churn risk assessment
- Interactive Plotly visualizations (gauges, charts, heatmaps)
- Business tools including ROI calculators and retention strategy recommendations

---

## Dataset

- **Source**: Telecom customer database (7,043 customers)
- **Features**: 21 original → 79 engineered → 37 optimized (after VIF)
- **Target**: Binary classification (Churn: 26.5% | Retained: 73.5%)
- **Train/Test Split**: 5,634 training, 1,409 test samples (stratified 80/20)
- **Categories**: Demographics, Services, Contract Terms, Payment Methods, Tenure, Charges

---

## Methodology

### Data Exploration & Feature Engineering
- Statistical profiling, correlation analysis, chi-square tests
- Created 79 advanced features including service engagement metrics, CLV projections, interaction features, and risk flags

### Model Development
- Trained and evaluated Logistic Regression, Random Forest, XGBoost, Gradient Boosting
- Applied VIF analysis to reduce multicollinearity (65 → 37 features)
- Used Grid Search CV for hyperparameter tuning with stratified train/test split
- Emphasized recall metric to minimize false negatives

### Customer Segmentation
- Applied K-Means clustering with elbow method and silhouette analysis
- Profiled segments by churn rate, revenue contribution, and behavioral patterns
- Developed targeted retention strategies for each segment

---

## Key Findings

### Model Performance
- **Best Model**: Logistic Regression (37 features)
- **Confusion Matrix**: TP=199, FP=126, FN=175, TN=909
- **Churners Identified**: 199 out of 374 actual churners (53.21% recall)
- **Prediction Confidence**: 66.33% precision
- **Overall Accuracy**: 80.41% (1,133 out of 1,409 correct predictions)

### Top Churn Drivers
1. Contract type: Month-to-month contracts show significantly higher churn
2. Customer tenure: Newer customers at higher risk
3. Internet service: Fiber optic users with specific patterns
4. Payment method: Electronic check correlation with churn
5. Service engagement: Lower add-on service adoption linked to churn

### Customer Segments
- **Segment 0 (High-Risk)**: 3,978 customers (56.5%), 29.7% churn rate
  - Lower tenure, lower monthly charges
  - Focus: First 90-day engagement, contract conversion
  
- **Segment 1 (Stable)**: 3,065 customers (43.5%), 22.4% churn rate
  - Higher tenure, higher monthly charges
  - Focus: Loyalty rewards, upselling opportunities

---

## Technologies

### Machine Learning & Data Science
- Python 3.12
- Scikit-learn 1.3.2
- Pandas 2.1.4
- NumPy 1.26.2

### Visualization & Web Application
- Streamlit 1.29.0
- Plotly 5.18.0
- Matplotlib 3.8.2
- Seaborn 0.13.0

### Development Tools
- Jupyter Notebook
- Git & GitHub
- VS Code

---

## Getting Started

### Prerequisites
- Python 3.12 or higher
- Git
- pip (Python package manager)

### Installation

```bash
# Clone repository
git clone https://github.com/mihiniboteju/churn-prediction-system.git
cd churn-prediction-project

# Create virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Streamlit App

```bash
# Navigate to streamlit app directory
cd streamlit_app

# Run the app
streamlit run Home.py
```

The app will open in your browser at `http://localhost:8501`

### Using the Model in Python

```python
import pandas as pd
import pickle

# Load the trained model
with open('models/best_churn_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load test data
X_test = pd.read_csv('data/processed/X_test_optimized.csv')

# Make predictions
predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)[:, 1]

# Identify high-risk customers (>70% churn probability)
high_risk_mask = probabilities > 0.7
high_risk_customers = X_test[high_risk_mask]
print(f"High-risk customers: {len(high_risk_customers)}")
```

### Exploring the Notebooks

```bash
# Launch Jupyter Notebook
jupyter notebook

# Navigate to notebooks/ directory and open any notebook
# Recommended order:
# 1. 01_project_setup.ipynb
# 2. 02a_target_analysis.ipynb
# 3. 04_customer_segmentation.ipynb
# 4. 05c_final_evaluation.ipynb
```

---

## Dependencies

### Core Project Requirements
```
pandas==2.1.4
numpy==1.26.2
matplotlib==3.8.2
seaborn==0.13.0
scikit-learn==1.3.2
jupyter>=1.0.0
```

### Streamlit App Requirements
```
streamlit==1.29.0
pandas==2.1.4
numpy==1.26.2
scikit-learn==1.3.2
plotly==5.18.0
matplotlib==3.8.2
seaborn==0.13.0
```

See `requirements.txt` and `streamlit_app/requirements.txt` for complete lists.

---

## Author

**Mihini Boteju**

- GitHub: [@mihiniboteju](https://github.com/mihiniboteju)
- LinkedIn: [Connect with me](https://www.linkedin.com/in/mihini-boteju)

---

## License

This project is licensed under the MIT License.

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ for data science and machine learning

</div>
