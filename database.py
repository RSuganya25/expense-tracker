import sqlite3

def connect():
    conn = sqlite3.connect('data/expenses.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            date TEXT,
            category TEXT,
            amount REAL,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

