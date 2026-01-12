import random
from datetime import datetime, timedelta
import psycopg2
from faker import Faker
import numpy as np

fake = Faker()

# ---------- DB CONFIG ----------
DB_CONFIG = {
    "host": "localhost",
    "database": "reco_db",
    "user": "shreyanshpathak",
    "password": "postgres",
    "port": 5432
}

NUM_USERS = 500
NUM_PRODUCTS = 200
NUM_INTERACTIONS = 20000
NUM_ORDERS = 3000

EVENT_TYPES = ["view", "click", "add_to_cart", "purchase"]
EVENT_WEIGHTS = [0.6, 0.2, 0.1, 0.1]  # more views than purchases

CATEGORIES = ["Electronics", "Fashion", "Home", "Beauty", "Sports", "Books"]

# ---------- CONNECT ----------
conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()

# ---------- USERS ----------
print("Inserting users...")
users = []
for _ in range(NUM_USERS):
    users.append((
        random.randint(18, 60),
        random.choice(["Male", "Female"]),
        fake.city(),
        fake.date_between(start_date="-2y", end_date="today")
    ))

cur.executemany("""
    INSERT INTO reco.users (age, gender, city, signup_date)
    VALUES (%s, %s, %s, %s)
""", users)

conn.commit()

# ---------- PRODUCTS ----------
print("Inserting products...")
products = []
for _ in range(NUM_PRODUCTS):
    products.append((
        fake.word().capitalize() + " " + fake.word().capitalize(),
        random.choice(CATEGORIES),
        round(random.uniform(5, 500), 2)
    ))

cur.executemany("""
    INSERT INTO reco.products (product_name, category, price)
    VALUES (%s, %s, %s)
""", products)

conn.commit()

# ---------- FETCH IDS ----------
cur.execute("SELECT user_id FROM reco.users;")
user_ids = [row[0] for row in cur.fetchall()]

cur.execute("SELECT product_id FROM reco.products;")
product_ids = [row[0] for row in cur.fetchall()]

# ---------- INTERACTIONS ----------
print("Inserting interactions...")
interactions = []

for _ in range(NUM_INTERACTIONS):
    user_id = random.choice(user_ids)
    product_id = random.choice(product_ids)
    event_type = random.choices(EVENT_TYPES, EVENT_WEIGHTS)[0]
    event_time = fake.date_time_between(start_date="-180d", end_date="now")

    interactions.append((
        user_id,
        product_id,
        event_type,
        event_time
    ))

cur.executemany("""
    INSERT INTO reco.interactions (user_id, product_id, event_type, event_time)
    VALUES (%s, %s, %s, %s)
""", interactions)

conn.commit()

# ---------- ORDERS ----------
print("Inserting orders...")
orders = []

for _ in range(NUM_ORDERS):
    user_id = random.choice(user_ids)
    order_date = fake.date_between(start_date="-180d", end_date="today")
    total_amount = round(random.uniform(20, 1000), 2)

    orders.append((
        user_id,
        order_date,
        total_amount
    ))

cur.executemany("""
    INSERT INTO reco.orders (user_id, order_date, total_amount)
    VALUES (%s, %s, %s)
""", orders)

conn.commit()

cur.close()
conn.close()

print("✅ Data generation completed successfully.")
