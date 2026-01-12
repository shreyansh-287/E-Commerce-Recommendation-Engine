import psycopg2

DB_CONFIG = {
    "host": "localhost",
    "database": "reco_db",
    "user": "shreyanshpathak",
    "password": "postgres",
    "port": 5432
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)
