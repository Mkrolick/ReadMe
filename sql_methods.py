import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

password = os.getenv("POSTGRES_PASSWORD")




def create_row(password, saver, victim, quote, table):
    conn = psycopg2.connect(f"dbname=postgres user=postgres password={password}")
    cur = conn.cursor()
    cur.execute(f"INSERT INTO {table} (saver, victim, quote) VALUES (%s, %s, %s)", (saver, victim, quote))
    conn.commit()
    cur.close()
    conn.close()

def bulk_create_rows(password, data, table):
    victims = data["victims"]
    quotes = data["quotes"]
    conn = psycopg2.connect(f"dbname=postgres user=postgres password={password}")
    for (victim, quote) in zip(victims, quotes):
        cur = conn.cursor()
        cur.execute(f"INSERT INTO {table} (victim, quote) VALUES (%s, %s)", (victim, quote))
        conn.commit()
        cur.close()
    conn.close()


def fetch_rows_by_saver(password, saver, victim):
    conn = psycopg2.connect(f"dbname=postgres user=postgres password={password}")
    cur = conn.cursor()
    cur.execute("SELECT * FROM discord_data WHERE saver = %s AND victim = %s", (saver, victim))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def delete_data(password):
    conn = psycopg2.connect(f"dbname=postgres user=postgres password={password}")
    cur = conn.cursor()
    cur.execute("DELETE * FROM discord_data")
    conn.commit()
    cur.close()
    conn.close()

def delete_data(password, id):
    conn = psycopg2.connect(f"dbname=postgres user=postgres password={password}")
    cur = conn.cursor()
    cur.execute("DELETE * FROM discord_data WHERE id = %s", (id,))
    conn.commit()
    cur.close()
    conn.close()