> If you encounter an error with the Jupyter Notebook on GitHub, please use the following links below:<br>
> [Survival Analysis Notebook](https://nbviewer.org/github/Agungvpzz/Survival-Analysis/blob/main/Survival%20Analysis.ipynb) <br>

# Telco-Churn-Survival-Analysis

## 1. Introduction
In this repository, I will conduct survival analysis using Python, utilizing Plotly for interactive data visualization. The analysis will include exploratory data analysis, survival function estimation using the Kaplan-Meier method, and hazard modeling with the Cox Proportional Hazards model via CoxPHFitter from the lifelines package. Additionally, I will improve the model's accuracy by integrating XGBoost predictions while ensuring that both survival target variables—Churn and Tenure—are fairly excluded.

## 2. Business Understanding

### A. Business Goals
The primary goal of this analysis is to understand customer behavior over time and predict the likelihood of churn. By leveraging survival analysis techniques, businesses can gain insights into customer retention patterns, optimize engagement strategies, and enhance decision-making for long-term value.

### B. Objective of this analysis
1. Estimate survival probabilities to understand customer retention trends.
2. Identify key factors influencing customer churn using Cox Proportional Hazards modeling.
3. Enhance predictive accuracy by integrating XGBoost while ensuring fair exclusion of target variables (Churn and Tenure).
4. Provide actionable insights for customer segmentation and retention strategies.

### C. Key Questions to Answer
1. What is the estimated survival probability of customers over different time periods?
2. Which factors have the strongest impact on customer churn risk?
3. Can predictive modeling improve the accuracy of churn risk estimation?
4. How can businesses optimize retention strategies based on survival analysis findings?

## 3. Data Understanding
- The dataset can be explored and downloaded with the following link [telco-customer-churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn/data).
- Explore more with the following link [Legend](https://community.ibm.com/community/user/blogs/steven-macko/2019/07/11/telco-customer-churn-1113)

## 4. Methodology
### A. Exploratory Data Analysis (EDA)
1. Visualizing churn composition using a pie chart and analyzing churn distribution across tenure with a bar chart.
3. Assessing feature relationships by calculating the Pearson correlation coefficient between each feature and churn, then visualizing the results with a bar chart.
4. Visualizing churn composition across unique values of all categorical features using a stacked bar chart.
5. Evaluating categorical feature impact using chi-squared (χ²) tests to determine whether churn distributions differ significantly across unique category values.

### B. Survival Function Estimation using the Kaplan-Meier Method (Non-Parametric)
1. Plotting the survival function curve along with its confidence interval using a line chart.
2. Segmenting survival curves by masking based on each unique categorical feature value.

### C. Hazard Modeling with the Cox Proportional Hazards Model (Semi-Parametric)
1. Data Preprocessing:
     - Drop insignificant features based on the p-value from the chi-squared test.
     - Apply custom encoding by combining one-hot encoding with manual feature selection to reduce variance among predictor features.
     - Split the dataset using Surv.from_dataframe, designed for survival analysis.
2. Feature Engineering:
    - Create new columns by transforming numerical features into quantiles.
    - Add a probability prediction column from XGBoost’s probability estimates.
3. Cox Proportional Hazards Model Fitting:
    - Train the model using the default configuration.
5. Model Evaluation
    - Standard concordance index: Measures how well the model ranks survival risks
    - Censored concordance index: Evaluates survival risk ranking while accounting for censored observations.
    - Cumulative Dynamic AUC: Assesses time-dependent prediction performance.
5. Model Comparison
    - Compare survival modeling frameworks: lifelines vs. scikit-survival.
    - Assess predictive performance across different feature sets.
6. Model Visualization
    - Plot Feature Coefficients: Displays the coefficient values for each covariate in the Cox Proportional Hazards model.
    - Plot Partial Effects on Outcome: Illustrates how within-group differences in covariate values influence the shape of the survival function.
    - Plot Time-Dependent ROC Curve: Evaluates the CoxPH model’s accuracy in predicting time to churn using a time-dependent AUC curve.
    - Plot Survival Function Curve Based on Hazard Quartiles: Assesses how well the model stratifies customers into risk groups (e.g., quartiles based on predicted hazard).
    - Plot Survival Function Curve for Time-to-Event Predictions: Compares the model’s predicted time-to-event outcomes against actual observations.


## 5. Exploratory Data Analysis

### Churn Compositions
<div align=center>

  ![image](https://github.com/user-attachments/assets/0e880dc6-daab-408c-9a00-8a0f7858b6c7)
  ![image](https://github.com/user-attachments/assets/c3151031-da88-47d5-9859-96a68777cde6)

</div>

### Comparison Across All Categorical Features in Relation to Churn
We can clearly compare each value across all categorical features with the help of this barplot below.
![compairson_across_categorical_features](https://github.com/Agungvpzz/Telco-Churn-Analysis/assets/48642326/139e8945-b03f-4cad-b43a-421310db135e)


### Features Correlation Against Churn
Feature correlation in the following barplot informs us how each feature correlates to customer churn behaviour.
![corr_churn_features](https://github.com/Agungvpzz/Telco-Churn-Analysis/assets/48642326/cf57de7d-d9dc-4884-967a-89bcf009afcd)

Grouping features below allows for clear churn comparisons among unique values within each feature
![corr_churn_features_grouped](https://github.com/Agungvpzz/Telco-Churn-Analysis/assets/48642326/89748da4-5922-443f-8b67-fdab2e8af5f2)


## Survival Function Estimation
### Survival Function Curve
![image](https://github.com/user-attachments/assets/dd2e19fa-dd26-4305-bd81-3907c51dc596)

### Segmenting survival curves by masking based on each unique categorical feature value.

#### All Features
![image](https://github.com/user-attachments/assets/2af3d3c1-46ed-4d2b-8904-d5154022c484)<br>
- Among all features, Contract feature has the highest Logrank score, that is 2352.9, with signifficant p-value.
- Only Gender and PhoneService features doesn't have significant p-value (p > 0.05), with logrank score less than 1

#### Socio-Demographic Features
<div align=center>
     
![image](https://github.com/user-attachments/assets/bb91b34a-9782-4876-b537-c25a3128318e)
![image](https://github.com/user-attachments/assets/52db90b9-b2bf-4106-b837-7f2d7c1e7741)
</div>

- The Partner feature shows a significant difference in survival probabilities.
- Among all socio-demographic features, only Gender did not reach statistical significance.
- Customers who have a partner, are not senior citizens, and live with dependents have the lowest churn rate, at only 13.75%.
- Customers who have no partner, are senior citizens, and have no dependents exhibit the highest churn rate, approaching 50%.

#### Product/Service Features
<div align=center>
     
![image](https://github.com/user-attachments/assets/7ad66081-8b99-429d-b088-af1692fec09e)
![image](https://github.com/user-attachments/assets/9ad999c4-811f-4b4c-9302-93d6f195f9fc)
</div>

- All product and service features, except PhoneService, show a significant p-value.
- Customers who subscribe to DSL internet service along with both OnlineBackup and OnlineSecurity have the lowest churn rate at 6.75%. However, when they do not subscribe to these services (OnlineBackup and OnlineSecurity), the churn rate increases significantly to 34.6%.
- Customers without internet service have a churn rate of 7.4%.
- Customers who subscribe only to Fiber Optic internet service, without OnlineBackup and OnlineSecurity, have the highest churn rate at 55.8%.

#### Payment Features
<div align=center>
     
![image](https://github.com/user-attachments/assets/e87d71e5-7986-4cb9-a973-9a4ff8f65a67)
![image](https://github.com/user-attachments/assets/216c63e3-22ef-4190-a12a-dd3a85952c00)
</div>

- Customers with a two-year contract generally have a churn rate of only 2.83%. Among them, those who use Mailed Check as their payment method and opt for manual (non-paperless) billing have the lowest churn rate at just 0.37%. Conversely, the highest churn rate within this group is 9.82% for customers who use Electronic Check with paperless billing.
- Customers who use Electronic Check as their payment method with paperless billing experience a churn rate that is twice as high across different contract types.
- 42% of customers with a monthly contract have churned, with the highest churn rate at 57.7% for those who use Electronic Check with paperless billing.


## Hazard Modeling
### Model Evaluation
![image](https://github.com/user-attachments/assets/583504c0-ffb3-4ed8-8c6c-813dd6941078)
<br>The survival model exhibits strong predictive performance with minimal overfitting, as shown by the following metrics:
- Concordance Index (C-Index) & C-IndexC (Censored):
    - Train: 0.9600
    - Test: 0.9508
    - High agreement between predicted and actual survival rankings, including censored cases.
- Cumulative Dynamic AUC:
    - Train: 0.9806
    - Test: 0.9771
    - Excellent discriminatory ability in time-dependent survival probability estimation.
- The close alignment between train and test results highlights good generalization and model robustness for survival prediction.

### Model Comparison
![image](https://github.com/user-attachments/assets/be3350ad-fc3b-47fa-876b-690ee1814af7)<br>
- CoxPHFitter, CoxPHSurvivalAnalysis: Include all columns.
- cph2, cphsk2: Exclude columns with an insignificant p-value (> 0.05).
- cph3, cphsk3: Exclude columns with an insignificant logp value (< 10).

### Model Visualization

#### Feature Coefficients: Displays the coefficient values for each covariate in the Cox Proportional Hazards model.
![image](https://github.com/user-attachments/assets/842e2407-118e-4f88-a989-9cd77eb003c8)<br>
- A positive coefficient indicates that the covariate increases the risk of churn (customers are more likely to leave sooner).
- A negative coefficient suggests that the covariate reduces the risk of churn (customers are more likely to stay longer).
- A coefficient near zero means the covariate has minimal impact on churn.

#### Plot Time-Dependent ROC Curve: Evaluates the CoxPH model’s accuracy in predicting time to churn using a time-dependent AUC curve.
![image](https://github.com/user-attachments/assets/49423dfa-8073-476c-b617-dbd6cfa0e3ee)

#### Plot Partial Effects on Outcome: Illustrates how within-group differences in covariate values influence the shape of the survival function.
Example with Contract Covariate
![image](https://github.com/user-attachments/assets/bc0c2856-e72b-4871-98e9-f56a8d3c8887)

#### Plot Survival Function Curve Based on Hazard Quartiles: Assesses how well the model stratifies customers into risk groups (e.g., quartiles based on predicted hazard).
![image](https://github.com/user-attachments/assets/f9c9ffdb-c958-4da1-88df-75817a913bfa)


#### Plot Survival Function Curve for Time-to-Event Predictions: Compares the model’s predicted time-to-event outcomes against actual observations.
Example with the first 10 customers
![image](https://github.com/user-attachments/assets/cab139fe-77c6-48b9-9d59-8b5e00eabc49)


## 8. Conclusion

### Survival Analysis
The survival function curve shows how different values within a feature depict the significant different curve among them. 

### Hazard Predictive Modeling



## 9. Recommendation
