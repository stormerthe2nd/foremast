import sqlite3

con = sqlite3.connect('login.db')

cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS emp(name TEXT,pass TEXT, bal INTEGER)")
cur.execute("SELECT * FROM  emp")
users = {}
for row in cur:
    users.update({row[0]: row[1]})
cur.execute("SELECT * FROM  emp")
users2 = {}
for row2 in cur:
    users2.update({row2[0]: row2[2]})

con.commit()
con.close()
