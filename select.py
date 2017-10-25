import sqlite3

conn = sqlite3.connect('ifight.db')

cursor = conn.cursor()
cursor.execute("""
select * from ifght;
""")

for linha in cursor.fetchall():
    print("linha")

conn.close()
