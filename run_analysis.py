import pandas as pd
import sqlite3

conn = sqlite3.connect("project.db")
print("Connected to database\n")

query = """
-- MONTHLY REVENUE ANALYSIS --
WITH monthly AS (
    SELECT
        strftime('%Y-%m', date) AS month,
        SUM(amount) AS monthly_revenue
    FROM customers
    GROUP BY month
),
lagged AS (
    SELECT
        month,
        monthly_revenue,
        LAG(monthly_revenue) OVER(ORDER BY month) AS perv_month
    FROM monthly
)
SELECT 
    month,
    monthly_revenue,
    perv_month,
    CASE
        WHEN perv_month IS NULL THEN NULL
        ELSE ROUND(
            (monthly_revenue - perv_month) * 100.0 / perv_month, 2)
    END AS growth_precent
FROM lagged
ORDER BY month;
"""
df = pd.read_sql_query(query, conn)
print(f"{df}\n")

df.to_csv("monthly_report.csv", index=False)
print("monthly_report.csv saved\n")

top_clients_query = """
-- CLIENT ANALYSIS --
WITH base AS (
        SELECT
            user_id,
            name,
            city,
            COALESCE(SUM(amount),0) AS total_amount
        FROM customers
        GROUP BY user_id, name, city
),
    ranked AS(
        SELECT 
            user_id,
            name,
            city,
            total_amount,
            SUM(total_amount) OVER() AS all_total,
            SUM(total_amount) OVER(PARTITION BY city) AS city_total,
            ROUND(total_amount * 100.0 / SUM(total_amount) OVER(PARTITION BY city), 2) AS city_share,
            ROUND(total_amount * 100.0 / SUM(total_amount) OVER(), 2) AS revenue_share,
            DENSE_RANK() OVER(
                PARTITION BY city
                ORDER BY  total_amount DESC
                ) AS rank
        FROM base

)
SELECT
    user_id,
    name,
    city,
    total_amount,
    all_total,
    city_total,
    city_share,
    revenue_share,
    rank
FROM ranked
WHERE rank <= 2
ORDER BY city;
"""
top_clients_df = pd.read_sql_query(top_clients_query, conn)
print(f"{top_clients_df}\n")

top_clients_df.to_csv("top_clients_report.csv",index=False)
print("Top clients report is saved\n")

conn.close()
print("Darabase connection closed\n")

print("All reports generatd successfully.")