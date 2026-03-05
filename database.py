import sqlite3

conn = sqlite3.connect("cycles.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS cycles(
id INTEGER PRIMARY KEY AUTOINCREMENT,
last_period TEXT,
cycle_length INTEGER
)
""")

conn.commit()


def save_cycle(last_period, cycle_length):

    cursor.execute(
        "INSERT INTO cycles(last_period,cycle_length) VALUES (?,?)",
        (last_period, cycle_length)
    )

    conn.commit()


def get_latest():

    cursor.execute(
        "SELECT last_period,cycle_length FROM cycles ORDER BY id DESC LIMIT 1"
    )

    return cursor.fetchone()