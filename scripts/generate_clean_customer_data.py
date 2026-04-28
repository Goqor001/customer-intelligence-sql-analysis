import pandas as pd
import random
from datetime import datetime, timedelta

names = [
    "Anna", "Arman", "Karen", "Gor", "Anahit",
    "Lilit", "Hayk", "Narek", "Mariam", "Sona",
    "David", "Tigran", "Artur", "Ani", "Ruben",
    "Levon", "Mane", "Vardan", "Suren", "Aram"
]

cities = ["Yerevan", "Gyumri", "Vanadzor"]

products = ["Laptop", "Phone", "Headphones", "TV", "Tablet", "Watch"]

categories = {
    "Laptop": "Electronics",
    "Phone": "Electronics",
    "Headphones": "Accessories",
    "TV": "Electronics",
    "Tablet": "Electronics",
    "Watch": "Accessories"
}

# 1. Create users table
users = []

for user_id in range(1, 21):
    name = names[user_id - 1]
    city = random.choice(cities)
    age = random.randint(18, 60)
    income = random.randint(300, 3000)

    users.append({
        "user_id": user_id,
        "name": name,
        "city": city,
        "age": age,
        "income": income
    })

users_df = pd.DataFrame(users)

# 2. Create orders table
orders = []
order_id = 1

for _ in range(300):
    user = random.choice(users)

    product = random.choice(products)
    category = categories[product]
    amount = random.randint(50, 1000)

    days_ago = random.randint(0, 365)
    date = (datetime.now() - timedelta(days=days_ago)).strftime("%Y-%m-%d")

    orders.append({
        "order_id": order_id,
        "user_id": user["user_id"],
        "product": product,
        "category": category,
        "amount": amount,
        "date": date
    })

    order_id += 1

orders_df = pd.DataFrame(orders)

# 3. Merge users + orders for simple analysis
customer_data = orders_df.merge(users_df, on="user_id", how="left")

customer_data = customer_data[
    [
        "user_id", "name", "city", "age", "income",
        "order_id", "product", "category", "amount", "date"
    ]
]

users_df.to_csv("users.csv", index=False)
orders_df.to_csv("orders.csv", index=False)
customer_data.to_csv("customer_data_clean.csv", index=False)

print("Created:")
print("users.csv")
print("orders.csv")
print("customer_data_clean.csv")