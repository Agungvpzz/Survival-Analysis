> If you encounter an error with the Jupyter Notebook on GitHub, please use the following links below:<br>
> [Survival Analysis Notebook](https://nbviewer.org/github/Agungvpzz/Survival-Analysis/blob/main/Survival%20Analysis.ipynb) <br>

# Telco-Survival-Analysis

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
3. How do survival trends vary across customer segments?
4. Can predictive modeling improve the accuracy of churn risk estimation?
5. How can businesses optimize retention strategies based on survival analysis findings?

## 3. Data Understanding
The dataset can be explored and downloaded with the following link [telco-customer-churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn/data).

## 4. Methodology
### A. Exploratory Data Analysis (EDA)
1. Conduct a visual inspection of the churn composition using a pie chart and churn distribution across different tenure using a bar chart.
2. Calculate the Pearson correlation coefficient between each feature and the churn feature to assess their individual relationships, and visualize the results using a bar chart.
3. Conduct chi-squared (χ²) tests to evaluate whether the distribution of churn values differs significantly across the unique categories of each categorical feature.

### B. Survival Function Estimation using the Kaplan-Meier Method (Non-Parametric)
1. Plot survival function curve and its confidence interval using a line chart.
2. Plot survival function curve with mask based on each unique value of categorical features.

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
4. Model Evaluation
  - Standard concordance index: Measures how well the model ranks survival risks.
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

  ![image](https://github.com/Agungvpzz/Telco-Churn-Analysis/assets/48642326/aa82f4ce-f1a6-4ca2-8a6e-82fa95c342a6)
</div>

### Features Correlation Against Churn
Feature correlation in the following barplot informs us how each feature correlates to customer churn behaviour.
![corr_churn_features](https://github.com/Agungvpzz/Telco-Churn-Analysis/assets/48642326/cf57de7d-d9dc-4884-967a-89bcf009afcd)

Grouping features below allows for clear churn comparisons among unique values within each feature
![corr_churn_features_grouped](https://github.com/Agungvpzz/Telco-Churn-Analysis/assets/48642326/89748da4-5922-443f-8b67-fdab2e8af5f2)


### Comparison Across All Categorical Features in Relation to Churn
We can clearly compare each value across all categorical features with the help of this barplot below.
![compairson_across_categorical_features](https://github.com/Agungvpzz/Telco-Churn-Analysis/assets/48642326/139e8945-b03f-4cad-b43a-421310db135e)

### Churn Comparison Within Unique Values of Each Feature
- Each feature underwent chi-squared testing to evaluate churn comparisons among unique values
- The subplots are ordered in decreasing order of chi-squared values
- We can clearly identify churn value comparisons within unique values for each feature that significantly differ from other values.

#### Demographics Features Values Comparison by Churn
![categorical_features_demographics_by_churn](https://github.com/Agungvpzz/Telco-Churn-Analysis/assets/48642326/3d974671-eeb4-4128-ad21-66f6d6936805)
- As you can see above, only the 'Gender' feature does not have a significant p-value.
- Customers without dependents are likely to churn.
- Senior citizens tend to churn.
- Customers without partners tend to churn.
  

#### Payments Features Values Comparison by Churn
![categorical_features_payments_by_churn](https://github.com/Agungvpzz/Telco-Churn-Analysis/assets/48642326/be59ba31-fa1e-49f1-b88a-bc2bf88a5906)
- Customers who have contracts month-to-month are likely to churn.
- Customers with electronic check payment methods are likely to churn.
- Customers using paperless billing tend to churn.

#### Services Features Values Comparison by Churn
![categorical_features_services_by_churn](https://github.com/Agungvpzz/Telco-Churn-Analysis/assets/48642326/aeac8b1e-6778-4da5-a33d-a50ea9d5ff9d)
- Customers who don't subscribe to an additional online security service are likely to churn.
- Customers who don't subscribe to an additional tech support service are likely to churn.
- Customers who subscribe to fiber optic internet service tend to churn.
- Customers who don't subscribe to an additional online backup service are likely to churn.
- Customers who don't subscribe to an additional device protection service are likely to churn.
- Customers who didn't use their internet service to stream movies were likely to churn.
- Customers who didn't use their internet service to stream TV were likely to churn.
- Customers who subscribe to multiple telephone lines with the company tend to churn.
- Overall, customers who didn't subscribe to an internet service tend to be loyal.


## Model Development
### Model Performance Summary


### Model Evaluation and Interpretation

## 8. Conclusion

### Survival Analysis Report
The exploratory data analysis reveals several critical factors contributing to customer churn. Customers who are more likely to churn typically share the following characteristics:
- Payment Features:
  - Contract Type: Customers with a month-to-month contract are at a significantly higher risk of churning compared to those with longer-term commitments.
  - Payment methods: The electronic checks and paperless billing method, offer greater flexibility for customers. However, these methods have been identified as key drivers of customer churn.
- Demographic Characteristics:
    - Senior Citizens:
        - Older customers, specifically those identified as Senior Citizens, exhibit a higher likelihood of churning.
        - This may be due to factors such as changing service needs or financial considerations.
    - Marital and Family Status:
        - Single Customers (no partner) and have no dependents are more prone to churn.
        - This demographic might be more mobile and less tied down, making them more open to switching providers.
- Service Features:
  - There are several intriguing features with chi-squared scores exceeding 500, indicating significant differences in preferences between churned and non-churned customers. However, deeper analysis beyond the chi-squared tests is limited due to insufficient detailed information on the pricing of each service.
- Numerical Features:
  - The Tenure and TotalCharges variables are directly correlated with churn, making them consequence features rather than causal factors. As a result, analyzing these features provides limited value. On the other hand, higher MonthlyCharges are associated with an increased likelihood of customer churn.


### Hazard Predictive Modeling Report



## 9. Recommendation
