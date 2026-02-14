import sqlite3

conn = sqlite3.connect("expenses.db")

cursor = conn.cursor()

print("Data base connected successfully")