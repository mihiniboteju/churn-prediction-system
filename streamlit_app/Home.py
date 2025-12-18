import streamlit as st
import os

# Page configuration
st.set_page_config(
    page_title="Customer Churn Prediction System",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown(""" <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #FF4B4B;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-container {
        background-color: #F0F2F6;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .info-box {
        background-color: #E8F4F8;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #FF4B4B;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">Customer Churn Prediction System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">End-to-End Machine Learning Solution for Telecom Customer Retention</div>', unsafe_allow_html=True)

# Introduction
st.markdown("---")
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(""" ### Welcome!
    
    This interactive presentation showcases a **complete data science project** that predicts 
    customer churn for a telecommunications company. The project demonstrates the entire 
    machine learning pipeline from data exploration to deployment. **What You'll Discover:** - How data science solves real business problems
    - Interactive data visualizations and insights
    - Machine learning model performance and evaluation
    - Customer segmentation for targeted retention strategies
    - Live prediction tool you can try yourself
    """)

with col2:
    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.markdown(""" **Project Highlights:** - 7,043 customers analyzed
    - 37 engineered features
    - 3 ML models compared
    - 2 customer segments identified
    - Interactive prediction tool
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Key Metrics Dashboard
st.markdown("---")
st.markdown("### Model Performance at a Glance")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Overall Accuracy",
        value="80.41%",
        delta="Best performer: Logistic Regression" )

with col2:
    st.metric(
        label="Churn Detection Rate",
        value="53.21%",
        delta="Recall Score",
        help="Percentage of actual churners correctly identified" )

with col3:
    st.metric(
        label="Model Confidence",
        value="84.34%",
        delta="ROC-AUC Score",
        help="Area Under the Curve - measures model's ability to distinguish classes" )

with col4:
    st.metric(
        label="Churners Identified",
        value="199 / 374",
        delta="In test dataset",
        help="Successfully caught 199 out of 374 customers likely to churn" )

# Business Impact
st.markdown("---")
st.markdown("### Business Impact")

col1, col2 = st.columns(2)

with col1:
    st.markdown(""" **The Problem:** - Customer churn costs telecom companies **$1M-2M annually** - Acquiring new customers costs **5x more** than retaining existing ones
    - Only **26.5%** of customers churn, making prediction challenging
    """)

with col2:
    st.markdown(""" **The Solution:** - Predict which customers are likely to leave
    - Identify **2 distinct customer segments** for targeted campaigns
    - Prioritize retention efforts on high-risk customers
    - Achieve **80% accuracy** in predictions
    """)

# Navigation Guide
st.markdown("---")
st.markdown("### Navigate the Project")

st.markdown("""
Use the **sidebar** on the left to explore different sections of this project:

1. **Problem & Solution** - Understand the business challenge and our approach
2. **Data Story** - Explore the data through interactive visualizations
3. **Customer Segments** - Discover the 4 types of customers and retention strategies
4. **Model Performance** - Dive deep into model metrics and evaluation
5. **Try It Yourself** - Use the live prediction tool with your own inputs!
""")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem 0;'>
    <p><strong>Built with:</strong> Python • Scikit-learn • Pandas • Streamlit • Plotly</p>
    <p>Contact: mihiniboteju@gmail.com | <a href='https://github.com/mihiniboteju/churn-prediction-system'>GitHub Repository</a></p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## Project Overview")
    st.markdown(""" This project follows a **5-phase methodology**:
    
    1. Data Collection & Cleaning
    2. Exploratory Data Analysis
    3. Feature Engineering
    4. Customer Segmentation
    5. Predictive Modeling
    """)
    
    st.markdown("---")
    st.markdown("## Key Technologies")
    st.markdown(""" - **Python 3.11** - **Scikit-learn** (ML models)
    - **Pandas & NumPy** (data processing)
    - **Matplotlib & Seaborn** (visualization)
    - **Plotly** (interactive charts)
    - **Streamlit** (web app)
    """)
    
    st.markdown("---")
    st.info("Use the navigation above to explore different sections of the project!")
