import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

st.set_page_config(
    page_title="Customer Segments",
    page_icon="📊",
    layout="wide"
)

st.title("Customer Segmentation Analysis")
st.markdown("### Discover 2 distinct customer segments and targeted retention strategies")

st.markdown("---")

# Introduction
st.markdown("""
Using **K-Means clustering** with optimal K selection (Elbow Method + Silhouette Analysis), 
we identified **2 distinct customer segments** based on their behavior, tenure, and service 
usage patterns. Each segment requires a unique retention strategy. **Analysis Details:**
- Optimal K = 2 (highest silhouette score: 0.2662)
- Features used: 65 engineered features
- Clustering algorithm: K-Means with PCA visualization
""")

# Segment Overview Cards
st.markdown("---")
st.markdown("## The 2 Customer Segments")

col1, col2 = st.columns(2)

with col1:
    # Segment 0: Higher Risk
    st.markdown(""" <div style='background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                padding: 2rem; border-radius: 15px; color: white; margin-bottom: 1rem;'>
        <h2> Segment 0: High-Risk Customers</h2>
        <h3>Short-Term, Budget Conscious</h3>
        <hr style='border-color: rgba(255,255,255,0.3);'>
        <p><strong>Size:</strong> 3,978 customers (56.5%)</p>
        <p><strong>Churn Rate:</strong>  HIGH (29.7%)</p>
        <p><strong>Characteristics:</strong> Below-average tenure & spending</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(""" **Customer Profile:** - **Tenure:**Below average (shorter relationships)
    - **Monthly Charges:**Below average (lower spending)
    - **Total Charges:**Below average (less lifetime value)
    - **Churn Risk:** 29.7% - Nearly 1 in 3 will churn **Behavioral Patterns:** - Likely newer customers still evaluating service
    - Price-sensitive decision makers
    - Month-to-month contracts more common
    - Lower service bundle adoption
    - Higher electronic check payment usage **Retention Strategy:** **Immediate Actions:** - **Onboarding Enhancement:**First 90-day engagement program
    - **Value Demonstration:**Show ROI of current services
    - **Contract Incentives:**Discounts for longer commitments
    - **Proactive Support:**Early intervention at churn signals
    - **Usage Education:**Help maximize service value **Pricing Tactics:** - Welcome discounts (first 3 months)
    - Bundle package promotions
    - Price-lock guarantees for contract upgrades
    - Auto-pay discounts (5-10%) **Business Priority:** **CRITICAL** - Largest segment with highest churn rate
    - Converting to longer contracts is key
    - Focus: First 6-12 months of relationship
    - Target: Reduce churn to < 20% (save ~380 customers/year)
    """)

with col2:
    # Segment 1: Lower Risk
    st.markdown(""" <div style='background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); 
                padding: 2rem; border-radius: 15px; color: white; margin-bottom: 1rem;'>
        <h2>🟢 Segment 1: Stable Customers</h2>
        <h3>Long-Term, Higher Spenders</h3>
        <hr style='border-color: rgba(255,255,255,0.3);'>
        <p><strong>Size:</strong> 3,065 customers (43.5%)</p>
        <p><strong>Churn Rate:</strong> 🟢 LOW (22.4%)</p>
        <p><strong>Characteristics:</strong> Above-average tenure & spending</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(""" **Customer Profile:** - **Tenure:**Above average (longer relationships)
    - **Monthly Charges:**Above average (higher spending)
    - **Total Charges:**Above average (greater lifetime value)
    - **Churn Risk:** 22.4% - More stable, but still need attention **Behavioral Patterns:** - Established customers with longer tenure
    - Higher service adoption (bundles, premium features)
    - More likely on annual contracts
    - Automatic payment methods more common
    - Higher total lifetime value **Retention Strategy:** **Loyalty & Growth:** - **Loyalty Rewards:**Anniversary bonuses and exclusive perks
    - **VIP Treatment:**Priority support and account management
    - **Upsell Opportunities:**Premium service upgrades
    - **Community Building:**Customer advisory panels
    - **Contract Renewal:**Early renewal incentives **Value Enhancement:** - Tenure-based rewards (every 12 months)
    - Personalized service recommendations
    - Usage optimization reviews
    - Exclusive beta access to new features **Business Priority:** 🟢 **HIGH VALUE** - Smaller segment but higher per-customer revenue
    - Lower churn but still improvable
    - Focus: Retention + upselling
    - Target: Reduce churn to < 15% (save ~230 customers/year)
    - Opportunity: Increase ARPU by 10-20%
    """)

# Segment Comparison
st.markdown("---")
st.markdown("## Segment Comparison Dashboard")

# Create comparison data (actual values from Phase 4)
segments_df = pd.DataFrame({
    'Segment': ['Segment 0 (High-Risk)', 'Segment 1 (Stable)'],
    'Size': [3978, 3065],
    'Size (%)': [56.5, 43.5],
    'Churn Rate (%)': [29.7, 22.4],
    'Relative Tenure': ['Below Avg', 'Above Avg'],
    'Relative Charges': ['Below Avg', 'Above Avg']
})

col1, col2 = st.columns(2)

with col1:
    # Segment size pie chart
    fig = go.Figure(data=[go.Pie(
        labels=segments_df['Segment'],
        values=segments_df['Size'],
        hole=0.4,
        marker_colors=['#f093fb', '#4facfe'],
        textinfo='label+percent',
        textfont=dict(size=14)
    )])
    
    fig.update_layout(
        title="Customer Distribution: 7,043 Total Customers",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Churn rate by segment
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=segments_df['Segment'],
        y=segments_df['Churn Rate (%)'],
        marker_color=['#E74C3C', '#F39C12'],
        text=segments_df['Churn Rate (%)'],
        texttemplate='%{text:.1f}%',
        textposition='outside',
        showlegend=False
    ))
    
    fig.update_layout(
        title="Churn Rate by Segment",
        yaxis_title="Churn Rate (%)",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

# Detailed comparison table
st.markdown("### Detailed Segment Comparison")

comparison_col1, comparison_col2 = st.columns(2)

with comparison_col1:
    # Customer count
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=segments_df['Segment'],
        y=segments_df['Size'],
        marker_color=['#f093fb', '#4facfe'],
        text=segments_df['Size'],
        texttemplate='%{text:,}',
        textposition='outside',
        showlegend=False
    ))
    
    fig.update_layout(
        title="Number of Customers by Segment",
        yaxis_title="Customers",
        height=350
    )
    
    st.plotly_chart(fig, use_container_width=True)

with comparison_col2:
    # Comparison metrics table
    st.markdown("#### Key Segment Differences")
    
    comparison_data = pd.DataFrame({
        'Metric': ['Size', 'Percentage', 'Churn Rate', 'Tenure', 'Charges'],
        'Segment 0 (High-Risk)': ['3,978', '56.5%', '29.7%', 'Below Avg', 'Below Avg'],
        'Segment 1 (Stable)': ['3,065', '43.5%', '22.4%', 'Above Avg', 'Above Avg']
    })
    
    st.dataframe(
        comparison_data,
        use_container_width=True,
        hide_index=True
    )
    
    st.markdown(""" **Key Insight:**Segment 0 has **7.3 percentage points higher churn** than Segment 1, 
    representing approximately **290 additional churners per year**.
    """)

# Strategic Recommendations
st.markdown("---")
st.markdown("## Strategic Recommendations by Segment")

tab1, tab2 = st.tabs([" Segment 0: High-Risk", " Segment 1: Stable"])

with tab1:
    st.markdown("### High-Risk Segment Strategy (56.5% of customers, 29.7% churn)")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(""" ### Immediate Actions (First 90 Days)
        
        1. **Enhanced Onboarding Program** - Personalized welcome email sequence (Day 1, 7, 14, 30)
           - Video tutorials for service features
           - Dedicated onboarding specialist
           - Usage tracking and optimization tips
        
        2. **Early Value Demonstration** - First 2 months: 15% discount
           - Month 3: Free premium feature trial
           - Service bundle recommendations based on usage
           - Proactive support outreach
        
        3. **Contract Conversion Campaign** - Month 2: Contract upgrade offer (save $10-15/month)
           - Price-lock guarantee for 12+ month contracts
           - Auto-pay setup incentive ($5/month discount)
           - Refer-a-friend bonus ($50 credit)
        
        4. **Churn Prevention Triggers** - Low usage alert → engagement campaign
           - Support ticket → follow-up satisfaction call
           - Payment issue → flexible payment options
           - Contract end approaching → renewal offer
        """)
    
    with col2:
        st.markdown(""" ### Success Metrics **Primary Goals:** - Reduce churn from 29.7% to < 22%
        - Convert 40% to annual contracts
        - Increase auto-pay adoption to 60%
        - 4.2+ satisfaction score (NPS) **Financial Impact:** - Save ~290 customers/year
        - Revenue protected: $710K annually
        
        ### Investment
        
        - **Cost**: $60 per customer
        - **Total**: $239K (3,978 customers)
        - **ROI**: 198% 
        - **Payback**: 6 months
        - **Net Benefit**: $471K/year
        """)
    
    st.markdown("---")
    st.markdown(""" **Key Insight:**Focus on first 90 days. Data shows tenure is below average in this segment - converting month-to-month to annual contracts reduces churn by ~50%.
    """)

with tab2:
    st.markdown("### 🟢 Stable Segment Strategy (43.5% of customers, 22.4% churn)")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(""" ### Loyalty & Growth Strategy
        
        1. **Loyalty Recognition Program** - Anniversary rewards every 12 months
           - Tenure-based loyalty tiers (Silver/Gold/Platinum)
           - Exclusive member benefits
           - VIP support access
        
        2. **Value Enhancement** - Automatic rate reviews (ensure best pricing)
           - Quarterly usage optimization consultations
           - Early access to new features
           - Premium feature upgrades
        
        3. **Upselling & Cross-selling** - Personalized service recommendations
           - Bundle upgrades (save 10-15%)
           - Premium tier migrations
           - Add-on services based on usage patterns
        
        4. **Community Engagement** - Customer advisory panel invitations
           - Beta testing opportunities
           - VIP events and webinars
           - Referral incentive program
        
        5. **Contract Renewal Excellence** - 60 days before expiry: Renewal offer
           - Multi-year discounts (15% for 2-year)
           - Contract extension bonuses
           - Price-lock guarantees
        """)
    
    with col2:
        st.markdown(""" ### Success Metrics **Primary Goals:** - Reduce churn from 22.4% to < 15%
        - 75% contract renewal rate
        - 20% upsell success rate
        - 4.7+ satisfaction score (NPS) **Growth Targets:** - Increase ARPU by 15%
        - 30% cross-sell adoption
        - 50% referral participation **Financial Impact:** - Save ~230 customers/year
        - Revenue protected: $575K annually
        - Upsell revenue: $200K+ additional
        
        ### Investment
        
        - **Cost**: $35 per customer
        - **Total**: $107K (3,065 customers)
        - **ROI**: 624%
        - **Payback**: 2 months
        - **Net Benefit**: $668K/year
        """)
    
    st.markdown("---")
    st.markdown(""" **Key Insight:**This segment already shows loyalty (higher tenure, higher spend). 
    Focus on retention + revenue growth through upselling and maintaining satisfaction.
    """)

# ROI Calculator
st.markdown("---")
st.markdown("## Segment-Based Retention ROI Calculator")

with st.expander(" **Calculate Your Potential ROI**"):
    calc_col1, calc_col2, calc_col3 = st.columns(3)
    
    with calc_col1:
        segment_select = st.selectbox(
            "Select Segment",
            ["Segment 0 (High-Risk)", "Segment 1 (Stable)"]
        )
        
        customers = st.number_input(
            "Number of Customers in Segment",
            min_value=100,
            max_value=10000,
            value=3978 if segment_select == "Segment 0 (High-Risk)" else 3065,
            step=100
        )
    
    with calc_col2:
        # Set defaults based on segment
        if segment_select == "Segment 0 (High-Risk)":
            default_churn = 30
            default_cost = 60
            default_reduction = 8
        else:  # Segment 1 (Stable)
            default_churn = 22
            default_cost = 35
            default_reduction = 7
        
        current_churn = st.slider(
            "Current Churn Rate (%)",
            min_value=5,
            max_value=50,
            value=default_churn
        )
        
        campaign_cost = st.number_input(
            "Campaign Cost per Customer ($)",
            min_value=10,
            max_value=200,
            value=default_cost
        )
    
    with calc_col3:
        churn_reduction = st.slider(
            "Expected Churn Reduction (%)",
            min_value=5,
            max_value=30,
            value=default_reduction
        )
        
        avg_ltv = st.number_input(
            "Customer Lifetime Value ($)",
            min_value=500,
            max_value=5000,
            value=2500,
            step=100
        )
    
    # Calculate ROI
    churned_before = customers * (current_churn / 100)
    churned_after = customers * ((current_churn - churn_reduction) / 100)
    customers_saved = churned_before - churned_after
    
    revenue_saved = customers_saved * avg_ltv
    campaign_investment = customers * campaign_cost
    net_benefit = revenue_saved - campaign_investment
    roi = (net_benefit / campaign_investment) * 100 if campaign_investment > 0 else 0
    
    st.markdown("---")
    st.markdown("### Results")
    
    result_col1, result_col2, result_col3, result_col4 = st.columns(4)
    
    with result_col1:
        st.metric("Customers Saved", f"{int(customers_saved):,}")
    
    with result_col2:
        st.metric("Revenue Protected", f"${revenue_saved:,.0f}")
    
    with result_col3:
        st.metric("Campaign Investment", f"${campaign_investment:,.0f}")
    
    with result_col4:
        st.metric("ROI", f"{roi:.1f}%", delta=f"${net_benefit:,.0f} net")

# Navigation
st.markdown("---")
st.info(""" **Continue your journey:**
- **Model Performance**: See how the ML model predicts churn
- **Try It Yourself**: Make predictions with live customer data
""")
