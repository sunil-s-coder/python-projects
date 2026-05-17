import sqlite3

conn = sqlite3.connect("database/app.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

conn.commit()