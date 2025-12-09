# Phase 2A: Data Preparation & Target Variable Analysis - Completion Report

**Date:** December 9, 2025  
**Project:** Customer Segmentation & Churn Prediction System  
**Phase:** 2A - Target Variable Analysis (Part of Comprehensive EDA)  
**Status:** ✅ COMPLETED

---

## Executive Summary

Phase 2A successfully completed the initial exploratory data analysis focusing on data preparation and target variable (Churn) analysis. The phase identified critical patterns in customer churn behavior, fixed data quality issues, and established baseline statistical comparisons between churned and retained customers.

**Key Achievement:** Fixed TotalCharges data type issue and created 2 professional visualizations revealing significant differences in tenure and pricing patterns between churned and retained customers.

---

## Objectives & Completion Status

| Objective | Status | Notes |
|-----------|--------|-------|
| Load and prepare data from Phase 1 | ✅ Complete | 7,043 customers loaded successfully |
| Fix TotalCharges data type issue | ✅ Complete | Converted to numeric, handled 11 empty values |
| Visualize churn distribution | ✅ Complete | Created bar chart + pie chart |
| Statistical comparison of groups | ✅ Complete | Analyzed tenure, charges differences |
| Create insights for feature engineering | ✅ Complete | Identified 3+ actionable patterns |

---

## Data Quality Improvements

### TotalCharges Data Type Fix

**Problem Identified:**
- TotalCharges stored as `object` type instead of numeric
- Caused by empty strings for new customers (tenure = 0)

**Solution Implemented:**
```python
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce').fillna(0)
```

**Impact:**
- 11 customers affected (0.16% of dataset)
- All affected customers had tenure = 0 months
- Logical to set TotalCharges = 0 for tenure = 0
- Successfully converted to float64 type

**Validation:**
- No remaining NULL values
- 11 zero values correspond to tenure = 0
- Mean: $2,283.30, Median: $1,397.47

---

## Target Variable Analysis

### Churn Distribution

**Overall Statistics:**
- **Total Customers:** 7,043
- **Churned:** 1,869 customers (26.54%)
- **Retained:** 5,174 customers (73.46%)
- **Class Imbalance Ratio:** 2.77:1 (Retained:Churned)

**Business Context:**
- ~1 in 4 customers leave the company
- Represents significant business problem
- Moderate class imbalance (not extreme, but needs handling)

### Visualizations Created

#### 1. Churn Distribution Chart
**File:** `visualizations/figures/01_churn_distribution.png`

**Components:**
- Bar chart showing absolute counts
- Pie chart showing percentages
- Color coding: Green (Retained), Red (Churned)

**Insights:**
- Clear visual representation of 3:1 ratio
- 26.5% churn rate is significant but manageable
- Sufficient samples in both classes for modeling

#### 2. Churn by Key Metrics (Box Plots)
**File:** `visualizations/figures/02_churn_by_metrics.png`

**Features Analyzed:**
1. Tenure (months)
2. Monthly Charges ($)
3. Total Charges ($)

**Key Observations:**
- All three metrics show distinct differences between groups
- Box plots reveal distribution shapes and outliers
- Mean lines (red dashed) highlight central tendency differences

---

## Statistical Comparison: Churners vs Non-Churners

### Numerical Features Summary

| Feature | Retained (Mean) | Churned (Mean) | Difference | % Difference |
|---------|----------------|----------------|------------|--------------|
| **Tenure** | 37.6 months | 17.9 months | -19.7 months | **-52.4%** ⚠️ |
| **Monthly Charges** | $61.27 | $74.44 | +$13.17 | **+21.5%** ⚠️ |
| **Total Charges** | $2,555.34 | $1,531.80 | -$1,023.54 | **-40.1%** ⚠️ |

### Critical Findings

#### 1. **Tenure Impact** (Strongest Signal)
- Churned customers have **52% lower tenure** on average
- Median churned tenure: ~10 months vs ~38 months for retained
- **Interpretation:** New customers are at highest risk
- **Action:** Focus retention efforts on first 12-18 months

#### 2. **Price Sensitivity**
- Churned customers pay **21.5% more monthly** on average
- Higher charges despite shorter tenure
- **Interpretation:** Price is a significant churn driver
- **Action:** Review pricing strategy for high-cost service bundles

#### 3. **Customer Lifetime Value**
- Churned customers have **40% lower total charges**
- Reflects combination of shorter tenure and timing
- **Interpretation:** Early churn = lost revenue potential
- **Action:** Early engagement and value demonstration critical

---

## Key Insights & Patterns

### 1. The "New Customer Churn Problem"
**Pattern:** Most churners are relatively new customers (< 18 months)

**Business Implications:**
- Onboarding process may need improvement
- First-year experience is critical
- Need proactive engagement in months 3-12

**Recommended Actions:**
- Implement 90-day check-in program
- Offer incentives at 6-month mark
- Monitor usage patterns in first 6 months

### 2. Price-Driven Churn
**Pattern:** Churners pay significantly more monthly despite shorter tenure

**Business Implications:**
- High-price customers are more likely to churn
- May indicate feature-price mismatch
- Competitors may offer better value

**Recommended Actions:**
- Review pricing of premium services
- Offer loyalty discounts for long-term contracts
- Bundle optimization to improve perceived value

### 3. Lost Revenue Opportunity
**Pattern:** $1,023 lower average total charges per churned customer

**Business Implications:**
- Each churned customer = ~$1,000 lost revenue
- 1,869 churners = ~$1.9M potential revenue loss
- Early churn prevention = exponential value

**Recommended Actions:**
- Calculate customer lifetime value (CLV)
- Determine optimal retention investment
- Prioritize high-value at-risk customers

---

## Modeling Implications

### 1. Class Imbalance Strategy
**Challenge:** 26.5% churn rate (moderate imbalance)

**Solutions to Implement:**
- ✅ Stratified train-test split
- ✅ `class_weight='balanced'` parameter in models
- ✅ SMOTE or undersampling if needed
- ✅ Focus on Recall and F1-score metrics

### 2. Feature Importance Predictions
**Expected Top Predictors:**
1. **Tenure** (strongest signal, -52% difference)
2. **MonthlyCharges** (price sensitivity indicator)
3. **TotalCharges** (customer value proxy)
4. Contract type (to be analyzed in Phase 2C)
5. Services bundle composition

### 3. Evaluation Metrics Priority
**Primary Metrics:**
1. **Recall** (minimize false negatives - missing churners costly)
2. **F1-Score** (balance precision and recall)
3. **ROC-AUC** (overall discrimination ability)

**Secondary Metrics:**
- Precision (avoid false alarms, but less critical)
- Accuracy (misleading due to imbalance)

---

## Files & Artifacts Created

### Notebooks
- ✅ `notebooks/02_eda_part1_target_analysis.ipynb` - Complete analysis notebook

### Visualizations
- ✅ `visualizations/figures/01_churn_distribution.png` - Bar + Pie chart
- ✅ `visualizations/figures/02_churn_by_metrics.png` - Box plots comparison

### Data Files
- ✅ `data/processed/phase2a_summary.csv` - Statistical summary table

### Documentation
- ✅ `documentation/phase_reports/phase2a_target_analysis.md` - This report

---

## Next Steps: Phase 2B - Numerical Features Analysis

### Objectives for Phase 2B

1. **Deep Dive into Tenure:**
   - Distribution analysis (histogram with KDE)
   - Identify churn "danger zones" (e.g., months 1-6, 7-12, etc.)
   - Tenure segmentation for targeted strategies

2. **Monthly Charges Analysis:**
   - Price distribution by churn status
   - Identify high-risk price points
   - Correlation with service types

3. **Total Charges vs Tenure:**
   - Scatter plot with churn color coding
   - Identify unusual patterns (high tenure + low charges, etc.)
   - Customer value segmentation

4. **Correlation Heatmap:**
   - Numerical feature correlations
   - Identify multicollinearity risks
   - Feature selection preparation

### Expected Deliverables

- 3+ professional visualizations
- Tenure-based churn risk segments
- Price sensitivity analysis
- Feature correlation insights
- Phase 2B documentation report

---

## Recommendations Summary

### Immediate Actions (Business)
1. 🎯 **Launch new customer engagement program** - Focus on first 6 months
2. 💰 **Review pricing strategy** - Analyze high-cost service bundles
3. 📊 **Implement churn monitoring** - Track tenure-based risk scores

### Immediate Actions (Modeling)
1. 🔧 **Prepare stratified sampling** - For train-test split
2. 📈 **Create tenure bins** - For categorical feature engineering
3. 🧪 **Design feature interactions** - Tenure × MonthlyCharges, etc.

### Long-term Strategy
1. 📱 **Predictive churn scoring** - Deploy model for real-time monitoring
2. 🎁 **Personalized retention offers** - Based on churn risk + customer value
3. 📊 **Continuous monitoring** - Track churn rate trends and model performance

---

## Technical Notes

### Code Quality
- All code follows PEP 8 standards
- Professional visualizations with proper labels
- Reproducible analysis (random seed = 42)
- Clean, commented code for portfolio presentation

### Performance
- Memory usage: ~2 MB (efficient)
- Processing time: < 30 seconds
- All visualizations saved at 300 DPI (publication quality)

### Reproducibility
- Fixed random seed (42)
- Explicit file paths
- Version-controlled code
- Documented all transformations

---

## Success Metrics: Phase 2A

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Data quality issues fixed | 1+ | 1 (TotalCharges) | ✅ |
| Visualizations created | 2 | 2 | ✅ |
| Statistical comparisons | 3 features | 3 features | ✅ |
| Insights documented | 3+ | 5+ | ✅ Exceeded |
| Code quality | Professional | Professional | ✅ |

---

## Conclusion

Phase 2A successfully established the foundation for comprehensive EDA by:
1. ✅ Resolving critical data quality issues
2. ✅ Quantifying the churn problem (26.5% rate)
3. ✅ Identifying tenure as the strongest predictor
4. ✅ Revealing price sensitivity patterns
5. ✅ Creating professional, publication-quality visualizations

**The analysis reveals a clear "new customer churn problem" with price sensitivity as a secondary factor. These insights will directly inform feature engineering and modeling strategies in subsequent phases.**

---

**Status:** ✅ PHASE 2A COMPLETE  
**Next Phase:** 2B - Numerical Features Analysis  
**Estimated Duration:** 30-45 minutes  
**Dependencies:** None (Phase 2A complete)

---

**Report Generated:** December 9, 2025  
**Analyst:** Mihini Boteju  
**Project:** Customer Churn Prediction System
