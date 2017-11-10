import sqlite3

conn = sqlite3.connect('ifight.db')

cursor = conn.cursor()

novo_nome = "zefinha"
novo_profissao = "professor"

cursor.execute("""
UPDATE ifight
 SET nome = ?, profissao = ?
 """, (novo_nome, novo_profissao)
)

conn.commit()
print("ok")
conn.close()