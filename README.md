> If you encounter an error with the Jupyter Notebook on GitHub, please use the following links below:<br>
> [Survival Analysis Notebook](https://nbviewer.org/github/Agungvpzz/Survival-Analysis/blob/main/Survival%20Analysis.ipynb) <br>

# Telco-Churn-Analysis

## 1. Introduction
In this repository, I will conduct churn analysis using Python and Plotly for interactive data visualization. The analysis will include examining the correlation of all features with the target variable 'Churn,' assessing the composition of categorical features relative to churn, and evaluating the distribution of numerical features relative to churn. Furthermore, I will perform statistical analysis and predictive modeling using logistic regression and XGBoost algorithms.

## 2. Business Understanding
### A. Business Goals


### B. Objective of this analysis


### C. Key Questions to Answer


## 3. Data Understanding
The dataset can be explored and downloaded with the following link [telco-customer-churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn/data).

## 4. Methodology
### A. Exploratory Data Analysis (EDA)
1. Conduct a visual inspection of the churn composition using a pie chart.
2. Calculate the Pearson correlation coefficient between each feature and the churn feature to assess their individual relationships, and visualize the results using a bar chart.
3. Conduct chi-squared (χ²) tests to evaluate whether the distribution of churn values differs significantly across the unique categories of each categorical feature, and visualize the results using a bar chart.
4. Conduct Mann-Whitney U tests to determine whether the distribution of a numerical feature differs significantly between churned and non-churned groups, and visualize the results using a line chart.

### B. Predictive Analysis
1. Build predictive models using machine learning.
2. Assess model performance through various evaluation metrics: classification report, confusion matrix, TPR-FPR, ROC curves, and ROC area curve.


## 5. Data Preparation
### A. Data Cleaning for Exploratory Data Analysis (EDA)
- Decoding feature (for readability purposes)
- Encoding target value
- Replace inconsistency values

### B. Data Preprocessing for Modeling
- Encoding target value.
- Target mean Encoding for all categorical features.
- Scaling numerical features using standard scale


## 6. Exploratory Data Analysis

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
