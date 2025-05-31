import sqlite3

def create_table():
    conn = sqlite3.connect('data/expenses.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_expense(date, category, amount, description):
    conn = sqlite3.connect('data/expenses.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
                (date, category, amount, description))
    conn.commit()
    conn.close()

def view_expenses():
    conn = sqlite3.connect('data/expenses.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM expenses")
    rows = cur.fetchall()
    conn.close()
    return rows

def update_expense(id, date, category, amount, description):
    conn = sqlite3.connect('data/expenses.db')
    cur = conn.cursor()
    cur.execute("UPDATE expenses SET date=?, category=?, amount=?, description=? WHERE id=?",
                (date, category, amount, description, id))
    conn.commit()
    conn.close()

def delete_expense(id):
    conn = sqlite3.connect('data/expenses.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM expenses WHERE id=?", (id,))
    conn.commit()
    conn.close()

