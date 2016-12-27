import sqlite3

def read_db(query):
	conn = sqlite3.connect('Portfolio.db')
	c = conn.cursor()
	c.execute(query)
	return c.fetchall()

q = """ SELECT DISTINCT category FROM projects """

lijst = read_db(q)
print lijst
lijst.sort()
print lijst

