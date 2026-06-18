-- =======================================================================
-- Project 2: Customer Churn Analysis
-- Description: SQL queries to analyze customer retention and churn drivers.
-- Database: Designed for standard SQL (PostgreSQL, SQL Server, SQLite)
-- =======================================================================

-- 1. Overall Churn Rate
SELECT 
    COUNT(CustomerID) AS TotalCustomers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS ChurnedCustomers,
    ROUND((SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0) / COUNT(CustomerID), 2) AS ChurnRatePercentage
FROM customer_data;

-- 2. Churn Rate by Contract Type
SELECT 
    Contract,
    COUNT(CustomerID) AS TotalCustomers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS ChurnedCustomers,
    ROUND((SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0) / COUNT(CustomerID), 2) AS ChurnRate
FROM customer_data
GROUP BY Contract
ORDER BY ChurnRate DESC;

-- 3. Average Tenure of Churned vs. Retained Customers
SELECT 
    Churn,
    ROUND(AVG(Tenure), 2) AS AverageTenureMonths,
    COUNT(CustomerID) AS CustomerCount
FROM customer_data
GROUP BY Churn;

-- 4. Churn by Monthly Charges (High vs Low)
WITH ChargeBuckets AS (
    SELECT 
        CustomerID,
        Churn,
        CASE 
            WHEN MonthlyCharges < 50 THEN 'Low (<$50)'
            WHEN MonthlyCharges BETWEEN 50 AND 100 THEN 'Medium ($50-$100)'
            ELSE 'High (>$100)'
        END AS ChargeSegment
    FROM customer_data
)
SELECT 
    ChargeSegment,
    COUNT(CustomerID) AS TotalCustomers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS ChurnedCustomers,
    ROUND((SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0) / COUNT(CustomerID), 2) AS ChurnRate
FROM ChargeBuckets
GROUP BY ChargeSegment
ORDER BY ChurnRate DESC;

-- 5. Impact of Senior Citizens and Dependents on Churn
SELECT 
    SeniorCitizen,
    Dependents,
    COUNT(CustomerID) AS TotalCustomers,
    ROUND((SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0) / COUNT(CustomerID), 2) AS ChurnRate
FROM customer_data
GROUP BY SeniorCitizen, Dependents
ORDER BY ChurnRate DESC;
