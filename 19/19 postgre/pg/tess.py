import psycopg2
from psycopg2 import OperationalError


params = {
    "host": "localhost",
    "port": 5432,
    "user": "your_username",
    "password": "your_password",
    "database": "your_database_name",
}


def check_database_status():
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        print(f"Connected to {db_version}")
    except OperationalError as e:
        print(f"The error '{e}' occurred.")

check_database_status()