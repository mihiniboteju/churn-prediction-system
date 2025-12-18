import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(
    page_title="Problem & Solution",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
st.markdown(""" <style>
    .big-number {
        font-size: 3rem;
        font-weight: bold;
        color: #FF4B4B;
    }
    .highlight-box {
        background-color: #FFF3CD;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #FF4B4B;
        margin: 1rem 0;
    }
    .solution-box {
        background-color: #D1ECF1;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #0C5460;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

st.title("The Problem & Our Solution")

# The Business Problem
st.markdown("---")
st.markdown("## The Business Challenge")

col1, col2 = st.columns([3, 2])

with col1:
    st.markdown(""" ### Customer Churn in Telecommunications **Customer churn** (also known as customer attrition) occurs when customers stop doing 
    business with a company. In the telecommunications industry, this is a critical issue that 
    directly impacts revenue and profitability. **Why is churn a problem?** - **Revenue Loss**: Each churned customer represents lost monthly recurring revenue
    - **High Acquisition Costs**: Acquiring new customers costs 5-7x more than retaining existing ones
    - **Competitive Market**: Customers can easily switch to competitors with better offers
    - **Predictability**: Without insights, companies can't proactively retain at-risk customers
    """)

with col2:
    # Churn distribution visualization
    churn_data = pd.DataFrame({
        'Status': ['Retained', 'Churned'],
        'Customers': [5172, 1871],
        'Percentage': [73.5, 26.5]
    })
    
    fig = go.Figure(data=[go.Pie(
        labels=churn_data['Status'],
        values=churn_data['Customers'],
        hole=0.4,
        marker_colors=['#2ECC71', '#E74C3C'],
        textinfo='label+percent',
        textfont_size=14
    )])
    
    fig.update_layout(
        title="Customer Distribution in Dataset",
        height=350,
        showlegend=True
    )
    
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("**Dataset**: 7,043 customers, 26.5% churn rate")

# Financial Impact
st.markdown("---")
st.markdown("## Financial Impact")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="highlight-box">', unsafe_allow_html=True)
    st.markdown("### Annual Revenue Loss")
    st.markdown('<p class="big-number">$1M - $2M</p>', unsafe_allow_html=True)
    st.markdown("Based on 1,871 churned customers with average monthly charges of $64.76")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="highlight-box">', unsafe_allow_html=True)
    st.markdown("### Cost to Acquire New Customer")
    st.markdown('<p class="big-number">5-7x</p>', unsafe_allow_html=True)
    st.markdown("More expensive than retaining existing customers")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="highlight-box">', unsafe_allow_html=True)
    st.markdown("### Churn Rate")
    st.markdown('<p class="big-number">26.5%</p>', unsafe_allow_html=True)
    st.markdown("More than 1 in 4 customers leave annually")
    st.markdown('</div>', unsafe_allow_html=True)

# Business Impact Calculation
st.markdown("---")
st.markdown("### Let's Calculate the Real Cost")

with st.expander(" **Click to see the detailed financial breakdown**"):
    calc_col1, calc_col2 = st.columns(2)
    
    with calc_col1:
        st.markdown(""" **Revenue Loss Calculation:** - Total Customers: 7,043
        - Churned Customers: 1,871 (26.5%)
        - Average Monthly Charge: $64.76
        - Annual Revenue per Customer: $777.12 **Annual Revenue Lost:** ```
        1,871 customers × $777.12 = $1,453,975
        ```
        """)
    
    with calc_col2:
        st.markdown(""" **Opportunity Cost:** - Customer Lifetime Value (CLV): ~$2,500
        - Total CLV Lost: $4,677,500
        - Acquisition Cost for Replacements: ~$700 per customer
        - Total Acquisition Costs: $1,309,700 **Total Business Impact:** ```
        Revenue Loss + Acquisition Costs = $2.76M annually
        ```
        """)

# The Solution
st.markdown("---")
st.markdown("## Our Machine Learning Solution")

st.markdown('<div class="solution-box">', unsafe_allow_html=True)
st.markdown("""
### How Predictive Analytics Solves This Problem

Instead of waiting for customers to churn, we built a **Machine Learning model** that:

1. **Predicts** which customers are likely to churn before they leave
2. **Identifies** key factors that drive churn behavior
3. **Segments** customers into distinct groups for targeted retention strategies
4. **Prioritizes** intervention efforts on high-risk, high-value customers
""")
st.markdown('</div>', unsafe_allow_html=True)

# Solution Approach
col1, col2 = st.columns(2)

with col1:
    st.markdown(""" ### Our 5-Phase Methodology **Phase 1: Data Collection & Cleaning** - Collected data on 7,043 customers
    - 21 features including demographics, services, and billing
    - Cleaned missing values and inconsistencies **Phase 2: Exploratory Data Analysis** - Identified patterns in churn behavior
    - Discovered key risk factors
    - Analyzed feature correlations **Phase 3: Feature Engineering** - Created 44 new features from existing data
    - Transformed categorical variables
    - Engineered interaction features
    - Total: 65 engineered features
    """)

with col2:
    st.markdown(""" ### Continued... **Phase 4: Customer Segmentation** - Applied K-Means clustering
    - Identified 2 distinct customer segments
    - Developed targeted retention strategies **Phase 5: Predictive Modeling** - Removed multicollinearity (VIF analysis)
    - Trained 3 ML models
    - Selected best model: **Logistic Regression** - Achieved **80.41% accuracy** """)

# Model Results Summary
st.markdown("---")
st.markdown("## Model Performance Summary")

# Create metrics display
metrics_col1, metrics_col2, metrics_col3, metrics_col4 = st.columns(4)

with metrics_col1:
    st.metric(
        label="Overall Accuracy",
        value="80.41%",
        help="Percentage of all predictions that were correct"
    )

with metrics_col2:
    st.metric(
        label="Recall (Sensitivity)",
        value="53.21%",
        help="Successfully identified 199 out of 374 actual churners"
    )

with metrics_col3:
    st.metric(
        label="ROC-AUC Score",
        value="84.34%",
        help="Excellent ability to distinguish churners from non-churners"
    )

with metrics_col4:
    st.metric(
        label="Precision",
        value="66.33%",
        help="When model predicts churn, it's correct 66% of the time"
    )

# Business Value
st.markdown("---")
st.markdown("## Business Value & ROI")

value_col1, value_col2 = st.columns(2)

with value_col1:
    st.markdown(""" ### What This Model Enables
    
    - **Proactive Retention**: Identify at-risk customers before they leave
    - **Cost Savings**: Reduce acquisition costs by retaining existing customers
    - **Targeted Campaigns**: Focus retention efforts on high-risk customers
    - **Revenue Protection**: Prevent up to $1.45M in annual revenue loss
    - **Data-Driven Decisions**: Replace guesswork with predictions
    """)

with value_col2:
    st.markdown(""" ### Potential ROI Calculation **Assumptions:** - Model identifies 199 churners correctly (53% recall)
    - Retention campaign cost: $50 per customer
    - Retention success rate: 30% **Results:** ```
    Customers Saved: 199 × 30% = 60 customers
    Revenue Saved: 60 × $777/year = $46,620
    Campaign Cost: 199 × $50 = $9,950
    Net Benefit: $36,670
    ROI: 268%
    ``` **With just 30% retention success, the model pays for itself 3.7x over!** """)

# Next Steps
st.markdown("---")
st.markdown("## Explore More")

st.info(""" **Continue your journey:**
- **Data Story**: See detailed exploratory analysis and patterns
- **Customer Segments**: Discover the 2 customer segments and retention strategies
- **Model Performance**: Deep dive into model metrics and evaluation
- **Try It Yourself**: Use the live prediction tool!
""")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p><strong>Key Insight:</strong> By predicting churn early, companies can implement targeted retention 
    strategies that are more cost-effective than acquiring new customers.</p>
</div>
""", unsafe_allow_html=True)
