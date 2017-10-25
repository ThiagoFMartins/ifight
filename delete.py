import sqlite3

conn = sqlite3.connect('ifight.db')

cursor = conn.cursor()
id = 2

cursor.execute("""
delete from ifight
where id = ? """, (id,))

conn.commit()
print("ok")
conn.close()
