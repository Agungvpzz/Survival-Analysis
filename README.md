> If you encounter an error with the Jupyter Notebook on GitHub, please use the following links below:<br>
> [Survival Analysis Notebook](https://nbviewer.org/github/Agungvpzz/Survival-Analysis/blob/main/Survival%20Analysis.ipynb) <br>

# Telco-Churn-Survival-Analysis

## 1. Introduction
In this repository, I will conduct survival analysis using Python, utilizing Plotly for interactive data visualization. The analysis will include exploratory data analysis, survival function estimation using the Kaplan-Meier method, and hazard modeling with the Cox Proportional Hazards model via CoxPHFitter from the lifelines package.

## 2. Business Understanding

### A. Business Goals
The primary goal of this analysis is to understand customer behavior over time and predict the likelihood of churn. By leveraging survival analysis techniques, businesses can gain insights into customer retention patterns, optimize engagement strategies, and enhance decision-making for long-term value.

### B. Objective of this analysis
1. Estimate survival probabilities to understand customer retention trends.
2. Identify key factors influencing customer churn using Cox Proportional Hazards modeling.
3. Provide actionable insights for customer segmentation and retention strategies.

### C. Key Questions to Answer
1. What is the estimated survival probability of customers over different time periods?
2. Which factors have the strongest impact on customer churn risk?
3. How can businesses optimize retention strategies based on survival analysis findings?

## 3. Data Understanding
- The dataset can be explored and downloaded with the following link [telco-customer-churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn/data).
- Learn more about the dataset through this link [Legend](https://community.ibm.com/community/user/blogs/steven-macko/2019/07/11/telco-customer-churn-1113)

## 4. Methodology
### A. Exploratory Data Analysis (EDA)
1. Visualizing churn composition using a pie chart.
2. Visualizing churn composition across categorical features using a stacked bar chart.
3. Visualizing churn distribution across tenure using a stacked bar chart.
4. Visualizing churn distribution across tenure under different conditions using multiple stacked bar charts.
5. Assessing the association between categorical features and churn using χ² tests.
6. Visualizing the Pearson correlation coefficient between churn and each feature using a bar chart.

### B. Survival Function Estimation using the Kaplan-Meier Method (Non-Parametric)
1. Visualizing the survival function curve and its confidence interval using a line chart.
2. Visualizing survival curves across the unique values of each categorical feature.

### C. Hazard Modeling with the Cox Proportional Hazards Model (Semi-Parametric)
1. **Data Pre-processing**
   - Drop features whose χ² p-values indicate no significant association with churn.
   - Apply ranked target mean encoding for all categorical features.
   - Split the data with `Surv.from_dataframe`, reserving 30 % for testing and stratifying on churn to keep class balance.
2. **Feature Engineering**
   - Transform continuous variables into quantile-based bins.
3. **Model Fitting**
   - Fit a Cox Proportional Hazards model using default hyper-parameters.
4. **Model Evaluation**
   - Examine the `CoxPHFitter` summary—coefficients, hazard ratios (exp(coef)), z-scores, p-values, and −log₂(p)—to judge covariate reliability.
   - Compute the standard concordance index to quantify the model’s ranking ability.
   - Compute the censored concordance index to incorporate censored observations.
   - Calculate the cumulative dynamic AUC to assess time-dependent predictive performance.
5. **Model Comparison**
   - Contrast results from the *lifelines* and *scikit-survival* implementations.  
   - Benchmark predictive performance across alternative feature sets.
6. **Model Visualisation**  
   - Plot coefficients with their 95 % confidence intervals (bar chart).
   - Plot covariate partial effects to show how within-group changes shift the survival curve (line chart).
   - Draw time-dependent ROC curves to illustrate accuracy over time.
   - Plot survival curves stratified by hazard-risk quartiles to display risk separation.
   - Overlay predicted vs. observed time-to-event curves to assess calibration.


## 5. Exploratory Data Analysis
### A. Churn Composition
<div align=center>

  ![Chrun Composition](https://github.com/user-attachments/assets/0e880dc6-daab-408c-9a00-8a0f7858b6c7)  
  The pie chart indicates that 26.5% (1869) of our customers have churned.
</div>


### B. Churn Composition Across Categorical Features
<div align=center>

   ![Churn Composition Across Categorical Features](https://github.com/user-attachments/assets/8ceb5b6e-d7af-459b-9272-0932a557c3a5)
</div>

- Sorted by chi-square (χ²) values, the bar chart highlights how churn composition varies across each categorical feature.
- As expected, the Contract feature reflects customers’ initial subscription agreements over specific time periods.
   - Although the monthly contract type has the highest churn rate, it still accounts for the largest share of active customers compared to other contract types.
- Other features, as shown in the chart, demonstrate significant differences in churn composition based on their `chi²` values—except for `Gender` and `PhoneService`, which show weak or negligible associations.

### C. Churn Distribution Across Tenure Periods
<div align=center>

   ![Churn Distribution Across Tenure Periods](https://github.com/user-attachments/assets/3b2767f2-638d-400b-8286-259eca0bca47)
</div>

- The bar chart reveals a sharp spike in churn (around 380 customers) early in the customer lifecycle. This suggests many users leave shortly after joining—possibly due to onboarding issues, unmet expectations, or a misalignment between product and customer needs.
- After this initial drop-off, churn steadily declines and stabilizes. This trend may indicate that customers who remain beyond the first few months are more likely to stay loyal, or that those who churn early differ significantly from long-term users.


### D. Churn Distribution Across Tenure Periods under Different Conditions
<div align=center>
Example Feature: Contract
   
   ![Churn Distribution Across Tenure Periods under Different Conditions](https://github.com/user-attachments/assets/0c741266-d483-463c-bc1d-62b3f2380212)
</div>

- The bar charts clearly illustrate how churn composition varies across customer tenure for each contract type.
- For `Month-to-month` contracts, the majority of churn occurs within the first year—particularly in the first month. Churn then drops sharply until month six, followed by a steady decline. Very few customers remain active beyond five years.
- The `One-year` contract displays a relatively uniform distribution of churn across tenure, suggesting consistent retention dynamics throughout the contract period.
- The `Two-year` contract displays a higher proportion of long-term customers, many of whom have remained active for over five years. This suggests strong loyalty among existing subscribers. However, the lower presence of newer users on this contract type may indicate a shift in preference toward more flexible, short-term plans—potentially challenging future retention

### E. Association Between Categorical Features and Churn using χ² tests
<div align=center>
   
   ![chi2 tests](https://github.com/user-attachments/assets/446d77a1-a64b-47dc-bf7a-3cd0f5a1db34)
</div>

- As shown in the table, Gender and PhoneService have high p-values, indicating no significant association with churn; therefore, we exclude them from the hazard modeling process.
- The remaining categorical features exhibit statistically significant p-values, supporting their inclusion in the model.


### F. Pearson Correlation Coefficient Between Churn and each Feature
<div align=center>
     
![Pearson Correlation Coefficient Between Churn and each Feature](https://github.com/user-attachments/assets/3319f680-85c4-4afb-8ded-8d5d85ce98ed)
</div>

- The bar chart shows that `MonthlyCharges` has a mild positive correlation (~0.20) with churn. This likely reflects pricing differences, as short-term contracts—linked to higher churn—often come with higher monthly costs.
- TotalCharges shows a negative correlation with churn, as higher spending typically reflects longer tenure—meaning these customers are still active and have not churned.
- Together, `MonthlyCharges`, `TotalCharges`, and `Contract` capture overlapping aspects of tenure and pricing. While not a direct case of data leakage, their interdependence warrants caution—especially with multicollinearity in modeling.

## 6. Survival Function Estimation

### A. Survival Function Curve
<div align=center>

![Survival Function Curve](https://github.com/user-attachments/assets/dd2e19fa-dd26-4305-bd81-3907c51dc596)
</div>

- The most significant drop in the curve occurs within the first month after customers engage, with a 5% decline. This suggests that many users are simply testing the service.
- After the first month, the curve continues to decline at a consistent pace each month, indicating a steady rate of churn.
- After 5 years (60 months of tenure), the survival function remains above 65%, indicating long-term retention stability.

### B. Survival Curves Across the Unique Values of each Categorical Feature

#### a. Socio-Demographic Features
<div align=center>
     
   ![Socio-Demographic Features](https://github.com/user-attachments/assets/bb91b34a-9782-4876-b537-c25a3128318e)
   ![Socio-Demographic Features Table](https://github.com/user-attachments/assets/52db90b9-b2bf-4106-b837-7f2d7c1e7741)
</div>

- The Partner feature shows a significant difference in survival probabilities.
- Among all socio-demographic features, only Gender did not reach statistical significance.
- Customers who have a partner, are not senior citizens, and live with dependents have the lowest churn rate, at only 13.75%.
- Customers who have no partner, are senior citizens, and have no dependents exhibit the highest churn rate, approaching 50%.

#### b. Product/Service Features
<div align=center>
     
   ![Service Features](https://github.com/user-attachments/assets/7ad66081-8b99-429d-b088-af1692fec09e)
   ![Service Features Table](https://github.com/user-attachments/assets/9ad999c4-811f-4b4c-9302-93d6f195f9fc)
</div>

- All product and service features, except PhoneService, show a significant p-value.
- Customers who subscribe to DSL internet service along with both OnlineBackup and OnlineSecurity have the lowest churn rate at 6.75%. However, when they do not subscribe to these services (OnlineBackup and OnlineSecurity), the churn rate increases significantly to 34.6%.
- Customers without internet service have a churn rate of 7.4%.
- Customers who subscribe only to Fiber Optic internet service, without OnlineBackup and OnlineSecurity, have the highest churn rate at 55.8%.

#### c. Payment Features
<div align=center>
     
   ![Payment Features](https://github.com/user-attachments/assets/e87d71e5-7986-4cb9-a973-9a4ff8f65a67)
   ![Payment Features Table](https://github.com/user-attachments/assets/216c63e3-22ef-4190-a12a-dd3a85952c00)
</div>

- Customers with a two-year contract generally have a churn rate of only 2.83%. Among them, those who use Mailed Check as their payment method and opt for manual (non-paperless) billing have the lowest churn rate at just 0.37%. Conversely, the highest churn rate within this group is 9.82% for customers who use Electronic Check with paperless billing.
- Customers who use Electronic Check as their payment method with paperless billing experience a churn rate that is twice as high across different contract types.
- 42% of customers with a monthly contract have churned, with the highest churn rate at 57.7% for those who use Electronic Check with paperless billing.


## 7. Hazard Modeling

### A. Model Evaluation
<div align=center>

   ![Model Evaluation](https://github.com/user-attachments/assets/2d6b81c7-e61e-4e22-b31a-5b894523c25e)
</div>

The survival model exhibits strong predictive performance with minimal overfitting, as shown by the following metrics:
- Concordance Index (C-Index) & C-IndexC (Censored):
    - Train: 0.9464
    - Test: 0.9414
    - High agreement between predicted and actual survival rankings, including censored cases.
- Cumulative Dynamic AUC:
    - Train: 0.973
    - Test: 0.9711
    - Excellent discriminatory ability in time-dependent survival probability estimation.
- The close alignment between train and test results highlights good generalization and model robustness for survival prediction.

### B. Model Comparison
<div align=center>
     
   ![Model Comparison](https://github.com/user-attachments/assets/2efd3932-352c-4444-a919-5e5998338121)
</div>

- CoxPHFitter, CoxPHSurvivalAnalysis: Include all columns.
- cph2, cphsk2: Exclude columns with an insignificant p-value (> 0.05).
- cph3, cphsk3: Exclude columns with an insignificant logp value (< 10).

### C. Model Visualization

#### a. Feature Coefficients
<div align=center>

   ![Feature Coefficients](https://github.com/user-attachments/assets/bf96841b-ab2a-4d19-a191-4bb557bbfafa)
</div>

- A positive coefficient indicates that the covariate increases the risk of churn (customers are more likely to leave sooner).
- A negative coefficient suggests that the covariate reduces the risk of churn (customers are more likely to stay longer).
- A coefficient near zero means the covariate has minimal impact on churn.

#### b. Time-Dependent ROC Curve
<div align=center>

   ![Time-Dependent ROC Curve](https://github.com/user-attachments/assets/0e5b9c52-1244-4a12-b58b-4569baf6f869)
</div>

- High initial AUCs: Both training and testing curves start high (~0.97), indicating strong early predictive performance.
- Stable Mid-range Performance (Tenure 5–40): The AUC remains very high (around 0.99), suggesting the model is performing exceptionally well in this middle range of time.
- Degradation Over Time (Post-40 Tenure): AUC values for both train and test begin to decline gradually, with a noticeable drop after around tenure 60. This could be due to fewer samples available at longer tenures, or that model generalization weakens over time.
- Train vs Test Consistency: The test curve closely follows the train curve, indicating good generalization and low overfitting.

#### c. Covariate Partial Effects
<div align=center>
Example Covariate: Contract
   
   ![Covariate Partial Effects](https://github.com/user-attachments/assets/349b8426-f7e5-4395-aaff-e31a1b957ec7)
</div>

- As shown in the line chart above, the survival curves differ significantly across contract types.

#### d. Survival Function Curve Based on Hazard Quartiles
<div align=center>

   ![Survival Function Curve Based on Hazard](https://github.com/user-attachments/assets/f9c9ffdb-c958-4da1-88df-75817a913bfa)
</div>

-The survival curves shows how clearly the hazard model separates customers by quartile-based risk levels.

#### e. Survival Function Curve for Time-to-Event Predictions
Example with the first 10 customers
<div align=center>

   ![Time-to-Event Predictions](https://github.com/user-attachments/assets/cab139fe-77c6-48b9-9d59-8b5e00eabc49)
</div>


## 8. Conclusion

### A. Survival Analysis
The survival curve shows three key retention patterns: early churn, steady decline, and long-term loyalty. The 5% drop in the first month suggests many users treat the service as a trial. Consistent month-to-month decline indicates predictable churn rather than sudden spikes. However, strong retention beyond five years (65% survival) highlights a loyal user base. These insights emphasize the need for early engagement strategies to reduce initial churn while sustaining long-term customer relationships.

### B. Hazard Predictive Modelin
The model demonstrates strong and consistent performance over most of the time range, with only slight degradation in later time periods. This is a good sign in survival modeling, especially for applications like churn prediction, patient risk modeling, or customer lifetime value analysis.


## 9. Recommendation
