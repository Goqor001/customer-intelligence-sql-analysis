import pandas as pd
import sqlite3

def load_data():
    path = "customer_data_clean.csv"

    df = pd.read_csv(path)

    conn = sqlite3.connect("project.db")

    df.to_sql("customers", conn, if_exists="replace", index=False)

    print("Data loaded to SQLite")
    
    conn.close()

load_data()