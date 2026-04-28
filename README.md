# Customer Intelligence & Revenue Analysis
🚀 End-to-end data pipeline: CSV → SQLite → SQL → Python → Reports


## 📊 Project Overview

This project analyzes customer data and revenue to generate business insights:

* Top clients by city
* Revenue share
* Monthly revenue trends
* Growth percentage (MoM)

## 💡 Business Value

This analysis can help:

* Identify top-performing customers
* Detect revenue drops early
* Support business decision-making
* Understand customer contribution by city


## ⚙️ Tech Stack

* Python (pandas, sqlite3)
* SQL (CTE, Window Functions, LAG)
* SQLite

## 📁 Data Pipeline

1. Load CSV data into SQLite
2. Run SQL analytics
3. Generate reports
4. Save results to CSV

## 📈 Key Insights

* Revenue fluctuates every 3–4 months
* Biggest drop: 2026-03
* Overall trend: stable after initial growth

## 📂 Outputs

* monthly_report.csv → monthly revenue + growth
* top_clients_report.csv → best clients by city

## ▶️ How to Run

```bash
python run_analysis.py
```

## 👨‍💻 Author

Grigor Hovhannisyan
