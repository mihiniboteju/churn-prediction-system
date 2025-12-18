import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
from pathlib import Path

st.set_page_config(
    page_title="Try It Yourself",
    page_icon="📊",
    layout="wide"
)

st.title("Try It Yourself: Churn Prediction")
st.markdown("### Test the model with your own customer scenarios")

# Load the model
@st.cache_resource
def load_model():
    model_path = Path(__file__).parents[2] / "models" / "best_churn_model.pkl"
    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model()

if model is None:
    st.error("Could not load the prediction model. Please check the model file.")
    st.stop()

st.markdown("---")
st.markdown("""
**How it works:** Adjust the customer characteristics below, and the model will predict 
the likelihood of churn. The model uses 37 carefully selected features to make predictions 
with **80.41% accuracy**.
""")

st.markdown("### Customer Profile")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### Demographics")
    gender = st.selectbox("Gender", ["Male", "Female"], key="gender")
    senior_citizen = st.selectbox("Senior Citizen", ["No", "Yes"], key="senior")
    partner = st.selectbox("Has Partner", ["No", "Yes"], key="partner")
    dependents = st.selectbox("Has Dependents", ["No", "Yes"], key="dependents")

with col2:
    st.markdown("#### Account Information")
    tenure = st.slider("Tenure (months)", 0, 72, 12, key="tenure")
    contract = st.selectbox("Contract Type", 
                           ["Month-to-month", "One year", "Two year"], 
                           key="contract")
    paperless_billing = st.selectbox("Paperless Billing", ["No", "Yes"], key="paperless")
    payment_method = st.selectbox("Payment Method", 
                                 ["Electronic check", "Mailed check", 
                                  "Bank transfer (automatic)", "Credit card (automatic)"],
                                 key="payment")

with col3:
    st.markdown("#### Services & Charges")
    phone_service = st.selectbox("Phone Service", ["No", "Yes"], key="phone")
    multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes"], key="lines")
    internet_service = st.selectbox("Internet Service", 
                                   ["No", "DSL", "Fiber optic"], 
                                   key="internet")
    monthly_charges = st.slider("Monthly Charges ($)", 18.0, 120.0, 65.0, 0.5, key="monthly")
    
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Security & Protection")
    online_security = st.selectbox("Online Security", ["No", "Yes"], key="security")
    online_backup = st.selectbox("Online Backup", ["No", "Yes"], key="backup")
    device_protection = st.selectbox("Device Protection", ["No", "Yes"], key="device")
    tech_support = st.selectbox("Tech Support", ["No", "Yes"], key="tech")

with col2:
    st.markdown("#### Entertainment")
    streaming_tv = st.selectbox("Streaming TV", ["No", "Yes"], key="tv")
    streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes"], key="movies")

# Create feature engineering function
def engineer_features(inputs):
    """
    Engineer features from raw inputs to match the model's expected 37 features in exact order
    """
    # Convert Yes/No to 1/0
    def to_binary(val):
        return 1 if val == "Yes" else 0
    
    # Calculate intermediate values
    is_fiber = 1 if inputs['internet_service'] == "Fiber optic" else 0
    is_dsl = 1 if inputs['internet_service'] == "DSL" else 0
    is_auto_payment = 1 if "automatic" in inputs['payment_method'] else 0
    is_electronic_check = 1 if inputs['payment_method'] == "Electronic check" else 0
    
    # Security bundle detection
    security_count = (to_binary(inputs['online_security']) + 
                     to_binary(inputs['online_backup']) + 
                     to_binary(inputs['device_protection']) +
                     to_binary(inputs['tech_support']))
    
    # Contract encoding
    contract_map = {"Month-to-month": 0, "One year": 1, "Two year": 2}
    contract_encoded = contract_map[inputs['contract']]
    
    # Price segment
    if inputs['monthly_charges'] < 35:
        price_segment = 0
    elif inputs['monthly_charges'] < 70:
        price_segment = 1
    else:
        price_segment = 2
    
    # Tenure group
    if inputs['tenure'] < 12:
        tenure_group = 0
    elif inputs['tenure'] < 36:
        tenure_group = 1
    else:
        tenure_group = 2
    
    # Build features dictionary in EXACT order the model expects
    features = {}
    
    # 1. contract_risk_score
    features['contract_risk_score'] = 2 - contract_encoded
    
    # 2. tenure_group_encoded
    features['tenure_group_encoded'] = tenure_group
    
    # 3. price_segment_encoded
    features['price_segment_encoded'] = price_segment
    
    # 4. TotalCharges_log
    features['TotalCharges_log'] = np.log1p(inputs['monthly_charges'] * inputs['tenure'])
    
    # 5-8. Basic demographics
    features['gender'] = 1 if inputs['gender'] == "Male" else 0
    features['SeniorCitizen'] = to_binary(inputs['senior_citizen'])
    features['Partner'] = to_binary(inputs['partner'])
    features['Dependents'] = to_binary(inputs['dependents'])
    
    # 9. PaperlessBilling
    features['PaperlessBilling'] = to_binary(inputs['paperless_billing'])
    
    # 10-11. Internet flags
    features['is_dsl'] = is_dsl
    
    # 12-13. Payment flags
    features['is_auto_payment'] = is_auto_payment
    features['is_electronic_check'] = is_electronic_check
    
    # 14-17. Service flags
    features['OnlineSecurity_binary'] = to_binary(inputs['online_security'])
    features['OnlineBackup_binary'] = to_binary(inputs['online_backup'])
    features['DeviceProtection_binary'] = to_binary(inputs['device_protection'])
    features['StreamingMovies_binary'] = to_binary(inputs['streaming_movies'])
    
    # 18. MultipleLines_binary
    features['MultipleLines_binary'] = to_binary(inputs['multiple_lines'])
    
    # 19-22. Security bundles
    has_internet = 1 if inputs['internet_service'] != "No" else 0
    features['has_security_bundle'] = 1 if security_count >= 3 else 0
    features['has_premium_protection'] = 1 if security_count == 4 else 0
    features['has_security_gap'] = 1 if (has_internet == 1 and security_count == 0) else 0
    features['has_partial_security'] = 1 if (security_count >= 1 and security_count <= 2) else 0
    
    # 23. is_heavy_streaming
    features['is_heavy_streaming'] = 1 if (to_binary(inputs['streaming_tv']) + 
                                           to_binary(inputs['streaming_movies']) == 2) else 0
    
    # 24. long_contract_loyal
    features['long_contract_loyal'] = 1 if (inputs['contract'] != "Month-to-month" and 
                                            inputs['tenure'] > 24) else 0
    
    # 25. fiber_mtm_risk
    features['fiber_mtm_risk'] = 1 if (is_fiber == 1 and 
                                        inputs['contract'] == "Month-to-month") else 0
    
    # 26. fiber_long_contract
    features['fiber_long_contract'] = 1 if (is_fiber == 1 and 
                                           inputs['contract'] == "Two year") else 0
    
    # 27. high_price_no_services
    features['high_price_no_services'] = 1 if (inputs['monthly_charges'] > 70 and 
                                               security_count == 0) else 0
    
    # 28. high_price_full_services
    features['high_price_full_services'] = 1 if (inputs['monthly_charges'] > 70 and 
                                                 security_count >= 2) else 0
    
    # 29. new_customer_high_price
    features['new_customer_high_price'] = 1 if (inputs['tenure'] < 6 and 
                                               inputs['monthly_charges'] > 70) else 0
    
    # 30. paperless_no_autopay
    features['paperless_no_autopay'] = 1 if (to_binary(inputs['paperless_billing']) == 1 and 
                                              is_auto_payment == 0) else 0
    
    # 31. senior_no_support
    features['senior_no_support'] = 1 if (to_binary(inputs['senior_citizen']) == 1 and 
                                          to_binary(inputs['tech_support']) == 0) else 0
    
    # 32. single_minimal_services
    features['single_minimal_services'] = 1 if (to_binary(inputs['partner']) == 0 and 
                                                to_binary(inputs['dependents']) == 0 and 
                                                security_count <= 1) else 0
    
    # 33. is_flight_risk
    features['is_flight_risk'] = 1 if (inputs['contract'] == "Month-to-month" and 
                                       is_electronic_check == 1) else 0
    
    # 34. is_value_at_risk
    features['is_value_at_risk'] = 1 if (inputs['monthly_charges'] > 70 and 
                                         is_fiber == 1 and 
                                         inputs['contract'] == "Month-to-month") else 0
    
    # 35. needs_retention
    features['needs_retention'] = 1 if (inputs['contract'] == "Month-to-month" and 
                                       inputs['tenure'] < 12) else 0
    
    # 36. upsell_opportunity
    features['upsell_opportunity'] = 1 if (inputs['tenure'] > 12 and 
                                          security_count < 2 and 
                                          inputs['monthly_charges'] < 70) else 0
    
    # 37. premium_retention_target
    features['premium_retention_target'] = 1 if (inputs['monthly_charges'] > 70 and 
                                                 inputs['tenure'] > 12) else 0
    
    # 38. cluster_label
    if inputs['tenure'] < 12 or inputs['monthly_charges'] > 80:
        features['cluster_label'] = 0  # High-risk cluster
    else:
        features['cluster_label'] = 1  # Stable cluster
    
    return features

# Prediction button
if st.button("Predict Churn Risk", type="primary", use_container_width=True):
    # Collect all inputs
    inputs = {
        'gender': gender,
        'senior_citizen': senior_citizen,
        'partner': partner,
        'dependents': dependents,
        'tenure': tenure,
        'contract': contract,
        'paperless_billing': paperless_billing,
        'payment_method': payment_method,
        'phone_service': phone_service,
        'multiple_lines': multiple_lines,
        'internet_service': internet_service,
        'monthly_charges': monthly_charges,
        'online_security': online_security,
        'online_backup': online_backup,
        'device_protection': device_protection,
        'tech_support': tech_support,
        'streaming_tv': streaming_tv,
        'streaming_movies': streaming_movies
    }
    
    # Engineer features
    features = engineer_features(inputs)
    
    # Create DataFrame with features in EXACT order model expects
    feature_order = [
        'contract_risk_score', 'tenure_group_encoded', 'price_segment_encoded', 'TotalCharges_log',
        'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PaperlessBilling', 'is_dsl',
        'is_auto_payment', 'is_electronic_check', 'OnlineSecurity_binary', 'OnlineBackup_binary',
        'DeviceProtection_binary', 'StreamingMovies_binary', 'MultipleLines_binary',
        'has_security_bundle', 'has_premium_protection', 'has_security_gap', 'has_partial_security',
        'is_heavy_streaming', 'long_contract_loyal', 'fiber_mtm_risk', 'fiber_long_contract',
        'high_price_no_services', 'high_price_full_services', 'new_customer_high_price',
        'paperless_no_autopay', 'senior_no_support', 'single_minimal_services', 'is_flight_risk',
        'is_value_at_risk', 'needs_retention', 'upsell_opportunity', 'premium_retention_target',
        'cluster_label'
    ]
    
    # Create feature values in correct order
    feature_values = [features[name] for name in feature_order]
    X = pd.DataFrame([feature_values], columns=feature_order)
    
    # Make prediction
    try:
        prediction = model.predict(X)[0]
        probability = model.predict_proba(X)[0]
        churn_probability = probability[1]
        
        st.markdown("---")
        st.markdown("## Prediction Results")
        
        # Display result with color coding
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            if prediction == 1:
                st.error("### HIGH CHURN RISK")
                st.markdown(f"#### Churn Probability: **{churn_probability*100:.1f}%**")
            else:
                st.success("### LOW CHURN RISK")
                st.markdown(f"#### Churn Probability: **{churn_probability*100:.1f}%**")
            
            # Risk gauge visualization
            import plotly.graph_objects as go
            
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=churn_probability * 100,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "Churn Risk Score"},
                gauge={
                    'axis': {'range': [None, 100]},
                    'bar': {'color': "darkred" if churn_probability > 0.5 else "green"},
                    'steps': [
                        {'range': [0, 30], 'color': "lightgreen"},
                        {'range': [30, 70], 'color': "yellow"},
                        {'range': [70, 100], 'color': "lightcoral"}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': 50
                    }
                }
            ))
            
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("---")
        
        # Interpretation
        st.markdown("### What This Means")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Key Risk Factors")
            risk_factors = []
            
            if contract == "Month-to-month":
                risk_factors.append("Month-to-month contract (highest churn rate)")
            if tenure < 12:
                risk_factors.append("New customer (< 12 months tenure)")
            if payment_method == "Electronic check":
                risk_factors.append("Electronic check payment (less reliable)")
            if internet_service == "Fiber optic" and contract == "Month-to-month":
                risk_factors.append("Fiber optic + month-to-month (high-risk combo)")
            if monthly_charges > 70:
                risk_factors.append("High monthly charges (price sensitivity)")
            
            security_count = sum([1 for s in [online_security, online_backup, device_protection, tech_support] 
                                 if s == "Yes"])
            if security_count == 0:
                risk_factors.append("No security/support services (low engagement)")
            
            if risk_factors:
                for factor in risk_factors:
                    st.markdown(f"- {factor}")
            else:
                st.markdown("- Good customer profile with minimal risk factors")
        
        with col2:
            st.markdown("#### Recommendations")
            
            if prediction == 1:
                st.markdown("""
                **Immediate Actions:**
                - Reach out proactively within 7 days
                - Offer contract upgrade incentives
                - Provide personalized service bundle discount
                - Assign dedicated customer success manager
                """)
            else:
                st.markdown("""
                **Retention Strategy:**
                - Continue excellent service
                - Offer loyalty rewards
                - Periodic check-ins
                - Upsell premium services when appropriate
                """)
        
        # Show feature importance
        with st.expander("View Feature Values (Advanced)"):
            feature_df = pd.DataFrame([features]).T
            feature_df.columns = ['Value']
            feature_df.index.name = 'Feature'
            st.dataframe(feature_df, use_container_width=True)
            
    except Exception as e:
        st.error(f"Error making prediction: {e}")
        st.write("Features shape:", X.shape)
        st.write("Expected features:", model.n_features_in_)

# Footer
st.markdown("---")
st.markdown("""
**How accurate is this?**  
Our model achieves **80.41% accuracy** overall, with an **84.34% ROC-AUC score**. However, 
it's important to note that the model catches **53.21% of actual churners** (recall). This means 
we successfully identify about **1 in 2 customers** who will churn, while correctly classifying 
8 out of 10 customers overall.

**Trade-off:** The model balances catching churners with avoiding false alarms. While we miss some 
churners, we minimize incorrectly flagging loyal customers, making retention campaigns more 
cost-effective and targeted.

Navigate to **Model Performance** to see detailed metrics, confusion matrix, and business impact analysis.
""")
