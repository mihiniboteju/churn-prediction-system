import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

st.set_page_config(
    page_title="Data Story",
    page_icon="📊",
    layout="wide"
)

st.title("The Data Story: Uncovering Churn Patterns")
st.markdown("### Interactive exploration of 7,043 customer records")

# Load the original data
@st.cache_data
def load_data():
    data_path = os.path.join("..", "data", "raw", "telco_customer_churn.csv")
    try:
        df = pd.read_csv(data_path)
        # Clean TotalCharges
        df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
        df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)
        return df
    except FileNotFoundError:
        # Return sample data if file not found
        return None

df = load_data()

if df is None:
    st.warning("Data file not found. Showing representative insights from analysis.")
    # Create sample data for demonstration
    np.random.seed(42)
    n_samples = 7043
    
    # Generate sample data with proper distributions
    churn = np.random.choice(['No', 'Yes'], size=n_samples, p=[0.735, 0.265])
    tenure = np.random.randint(1, 73, size=n_samples)
    monthly_charges = np.random.uniform(18, 119, size=n_samples)
    contract = np.random.choice(['Month-to-month', 'One year', 'Two year'], size=n_samples, p=[0.55, 0.21, 0.24])
    internet = np.random.choice(['DSL', 'Fiber optic', 'No'], size=n_samples, p=[0.34, 0.44, 0.22])
    payment = np.random.choice(['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'], 
                                size=n_samples, p=[0.34, 0.23, 0.22, 0.21])
    
    df = pd.DataFrame({
        'Churn': churn,
        'tenure': tenure,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': tenure * monthly_charges + np.random.uniform(-100, 100, size=n_samples),
        'Contract': contract,
        'InternetService': internet,
        'PaymentMethod': payment
    })

st.markdown("---")

# Dataset Overview
st.markdown("## Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Customers", f"{len(df):,}")
    
with col2:
    churn_count = len(df[df['Churn'] == 'Yes'])
    st.metric("Churned", f"{churn_count:,}", f"{churn_count/len(df)*100:.1f}%")
    
with col3:
    retained_count = len(df[df['Churn'] == 'No'])
    st.metric("Retained", f"{retained_count:,}", f"{retained_count/len(df)*100:.1f}%")
    
with col4:
    if 'MonthlyCharges' in df.columns:
        avg_charges = df['MonthlyCharges'].mean()
        st.metric("Avg Monthly Charge", f"${avg_charges:.2f}")

st.markdown("---")

# Key Insight 1: Tenure Analysis
st.markdown("## Insight 1: Tenure Matters")

col1, col2 = st.columns([2, 1])

with col1:
    if 'tenure' in df.columns:
        # Create tenure distribution by churn
        fig = go.Figure()
        
        for churn_status in ['No', 'Yes']:
            data = df[df['Churn'] == churn_status]['tenure']
            fig.add_trace(go.Histogram(
                x=data,
                name='Retained' if churn_status == 'No' else 'Churned',
                opacity=0.7,
                marker_color='#2ECC71' if churn_status == 'No' else '#E74C3C'
            ))
        
        fig.update_layout(
            title="Tenure Distribution: Churned vs Retained Customers",
            xaxis_title="Tenure (months)",
            yaxis_title="Number of Customers",
            barmode='overlay',
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Tenure data visualization")

with col2:
    st.markdown(""" ### Key Findings **High Churn in Early Months:** - Customers with < 10 months tenure have highest churn
    - **Critical retention window**: First 6 months **Tenure Stability:** - After 12 months, churn rate drops significantly
    - Long-term customers (60+ months) rarely churn **Action Item:** - Focus onboarding & early engagement programs
    - Implement 6-month retention campaigns
    """)

# Key Insight 2: Contract Type Impact
st.markdown("---")
st.markdown("## Insight 2: Contract Type Drives Retention")

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown(""" ### Key Findings **Month-to-Month Contracts:** - Highest churn rate (**42%**)
    - Most flexible but least loyal
    - Represents immediate risk **One Year Contracts:** - Moderate churn rate (**11%**)
    - Good balance of commitment **Two Year Contracts:** - Lowest churn rate (**3%**)
    - Strong commitment indicator
    - Best retention strategy **Recommendation:** - Incentivize longer contracts
    - Offer discounts for commitments
    """)

with col2:
    if 'Contract' in df.columns:
        # Contract type vs Churn
        contract_churn = pd.crosstab(df['Contract'], df['Churn'], normalize='index') * 100
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Retained',
            x=contract_churn.index,
            y=contract_churn['No'],
            marker_color='#2ECC71',
            text=[f'{val:.1f}%' for val in contract_churn['No']],
            textposition='inside'
        ))
        fig.add_trace(go.Bar(
            name='Churned',
            x=contract_churn.index,
            y=contract_churn['Yes'],
            marker_color='#E74C3C',
            text=[f'{val:.1f}%' for val in contract_churn['Yes']],
            textposition='inside'
        ))
        
        fig.update_layout(
            title="Churn Rate by Contract Type",
            xaxis_title="Contract Type",
            yaxis_title="Percentage",
            barmode='stack',
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)

# Key Insight 3: Internet Service
st.markdown("---")
st.markdown("## Insight 3: Internet Service Impact")

if 'InternetService' in df.columns:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Internet service churn rates
        internet_churn = pd.crosstab(df['InternetService'], df['Churn'], normalize='index') * 100
        
        fig = px.bar(
            internet_churn,
            barmode='group',
            title="Churn Rate by Internet Service Type",
            labels={'value': 'Percentage (%)', 'InternetService': 'Internet Service'},
            color_discrete_map={'No': '#2ECC71', 'Yes': '#E74C3C'},
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown(""" ### Key Findings **Fiber Optic:** - **Highest churn rate** (~42%)
        - Despite faster speeds
        - Possibly due to higher cost **DSL:** - Moderate churn rate (~19%)
        - More stable customer base **No Internet:** - Lowest churn rate (~7%)
        - Basic service customers
        - Price-sensitive segment **Insight:** - Price sensitivity in fiber optic
        - Need better value proposition
        """)

# Key Insight 4: Charges Analysis
st.markdown("---")
st.markdown("## Insight 4: Price Sensitivity")

if 'MonthlyCharges' in df.columns and 'TotalCharges' in df.columns:
    col1, col2 = st.columns(2)
    
    with col1:
        # Monthly charges distribution
        fig = go.Figure()
        
        for churn_status in ['No', 'Yes']:
            data = df[df['Churn'] == churn_status]['MonthlyCharges']
            fig.add_trace(go.Box(
                y=data,
                name='Retained' if churn_status == 'No' else 'Churned',
                marker_color='#2ECC71' if churn_status == 'No' else '#E74C3C'
            ))
        
        fig.update_layout(
            title="Monthly Charges: Churned vs Retained",
            yaxis_title="Monthly Charges ($)",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Scatter plot: tenure vs monthly charges
        fig = px.scatter(
            df.sample(min(1000, len(df))),  # Sample for performance
            x='tenure',
            y='MonthlyCharges',
            color='Churn',
            title="Tenure vs Monthly Charges (Sample)",
            labels={'tenure': 'Tenure (months)', 'MonthlyCharges': 'Monthly Charges ($)'},
            color_discrete_map={'No': '#2ECC71', 'Yes': '#E74C3C'},
            opacity=0.6,
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)

    st.markdown(""" ### Key Findings on Pricing
    
    - **Churned customers** pay **higher monthly charges** on average ($74.44 vs $61.27)
    - **High charges + Low tenure** = Highest churn risk
    - **Sweet spot**: Moderate pricing ($50-70) with longer contracts
    - **Price sensitivity**: Customers paying $80+ have 2x churn rate
    """)

# Key Insight 5: Payment Method
st.markdown("---")
st.markdown("## Insight 5: Payment Method Correlation")

if 'PaymentMethod' in df.columns:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Payment method churn analysis
        payment_churn = pd.crosstab(df['PaymentMethod'], df['Churn'], normalize='index') * 100
        
        fig = px.bar(
            payment_churn,
            title="Churn Rate by Payment Method",
            labels={'value': 'Percentage (%)', 'PaymentMethod': 'Payment Method'},
            color_discrete_map={'No': '#2ECC71', 'Yes': '#E74C3C'},
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown(""" ### Key Findings **Electronic Check:** - **Highest churn rate** (~45%)
        - Less commitment signal
        - Easy to cancel **Automatic Payments:** - Lower churn rates (~15-18%)
        - Bank transfer, Credit card
        - Indicates stability **Recommendation:** - Incentivize automatic payments
        - Offer discounts for auto-pay
        - Reduce friction in payment
        """)

# Summary Insights
st.markdown("---")
st.markdown("## Summary: Key Churn Drivers")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(""" ### High Risk Factors
    
    1. **Short tenure** (< 6 months)
    2. **Month-to-month** contracts
    3. **Electronic check** payments
    4. **High monthly charges** ($80+)
    5. **Fiber optic** internet
    """)

with col2:
    st.markdown(""" ### 🟢 Retention Factors
    
    1. **Long tenure** (60+ months)
    2. **Two-year contracts** 3. **Automatic payments** 4. **Moderate pricing** ($50-70)
    5. **Bundle services** """)

with col3:
    st.markdown(""" ### Actionable Insights
    
    1. **Focus on first 6 months** 2. **Promote longer contracts** 3. **Incentivize auto-pay** 4. **Review fiber pricing** 5. **Target high-risk segments** """)

# Interactive Filter Section
st.markdown("---")
st.markdown("## Interactive Exploration")

with st.expander(" **Filter and Explore the Data Yourself**"):
    col1, col2 = st.columns(2)
    
    with col1:
        if 'Contract' in df.columns:
            contract_filter = st.multiselect(
                "Select Contract Type(s)",
                options=df['Contract'].unique(),
                default=df['Contract'].unique()
            )
    
    with col2:
        if 'InternetService' in df.columns:
            internet_filter = st.multiselect(
                "Select Internet Service(s)",
                options=df['InternetService'].unique(),
                default=df['InternetService'].unique()
            )
    
    # Filter data
    filtered_df = df.copy()
    if 'Contract' in df.columns:
        filtered_df = filtered_df[filtered_df['Contract'].isin(contract_filter)]
    if 'InternetService' in df.columns:
        filtered_df = filtered_df[filtered_df['InternetService'].isin(internet_filter)]
    
    # Show filtered metrics
    st.markdown("### Filtered Results")
    metric_col1, metric_col2, metric_col3 = st.columns(3)
    
    with metric_col1:
        st.metric("Customers", f"{len(filtered_df):,}")
    
    with metric_col2:
        churn_rate = (filtered_df['Churn'] == 'Yes').sum() / len(filtered_df) * 100
        st.metric("Churn Rate", f"{churn_rate:.1f}%")
    
    with metric_col3:
        if 'MonthlyCharges' in filtered_df.columns:
            avg_charge = filtered_df['MonthlyCharges'].mean()
            st.metric("Avg Monthly Charge", f"${avg_charge:.2f}")

# Navigation
st.markdown("---")
st.info(""" **Continue exploring:**
- **Customer Segments**: See how we grouped customers into 4 distinct segments
- **Model Performance**: Dive into the machine learning model evaluation
- **Try It Yourself**: Make your own churn predictions!
""")
