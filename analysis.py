import sqlite3

DB_PATH = 'data/expenses.db'

def view_sorted_by_date():
    """Returns all expenses sorted by date."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM expenses ORDER BY date ASC")
    rows = cur.fetchall()
    conn.close()
    return rows

def view_total_by_category():
    """Returns total amount spent grouped by category."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    rows = cur.fetchall()
    conn.close()
    return rows
