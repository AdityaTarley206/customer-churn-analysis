# Customer Churn Analysis

## Objective
To analyze a telecom customer dataset containing over 20,000 records, identify the primary drivers of customer churn, and provide actionable, data-driven recommendations to improve customer retention.

## Methodology
1. **Data Engineering:** Developed a Python script to generate a highly realistic dataset of 21,500 telecom customers, including demographic information, contract types, tenure, and payment methods. Intentionally injected missing values and logical noise to simulate real-world data issues.
2. **Exploratory Data Analysis (EDA):** Built a Jupyter Notebook to clean the data, handle missing values, and perform EDA using Pandas, Matplotlib, and Seaborn.
3. **SQL Analytics:** Wrote comprehensive SQL queries to calculate overall churn rates, group customers into charge buckets, and analyze retention across different demographic segments.

## Files
- `customer_data.csv`: The raw dataset.
- `Churn_EDA.ipynb`: Jupyter Notebook containing data cleaning, visualizations, and EDA.
- `churn_analysis.sql`: SQL queries for calculating churn metrics.
- `generate_churn_data.py`: The data generation script.

## Key Recommendations
- **Contract Incentives:** Month-to-month contracts exhibit the highest churn rates. The company should offer aggressive discounts to incentivize 1-year or 2-year contract upgrades.
- **Onboarding Experience:** The highest volume of churn occurs in the first 6 months (low tenure). Implementing a stronger onboarding process and early customer check-ins is critical.
