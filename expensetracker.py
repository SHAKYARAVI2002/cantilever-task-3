import sqlite3
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

conn = sqlite3.connect('expenses.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS expenses
             (id INTEGER PRIMARY KEY, date TEXT, category TEXT, amount REAL)''')

conn.commit()
conn.close()


class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title('Expense Tracker')
        # ... (rest of GUI setup)

def add_expense():
    date = date_entry.get()
    category = category_entry.get()
    amount = amount_entry.get()
    
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("INSERT INTO expenses (date, category, amount) VALUES (?, ?, ?)",
              (date, category, amount))
    conn.commit()
    conn.close()

def generate_report():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    data = c.fetchall()
    
    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]
    
    plt.bar(categories, amounts)
    plt.xlabel('Category')
    plt.ylabel('Total Amount')
    plt.title('Expense Report')
    plt.show()
