import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

raw = c.execute('SELECT type FROM github')
raw.fetchall()
