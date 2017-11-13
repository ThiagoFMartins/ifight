import sqlite3

conn = sqlite3.connect('ifight.db')

cursor = conn.cursor()

'''u_id = input("id:")'''
u_login = input("login:")
u_senha = input("senha:")
u_nome = input("nome:")
u_nascimento = input("nascimeno (aaaa/mm/dd):")
u_profissao = input("profissao:")

cursor.execute\
    ("""
     insert into ifight (id, login, senha, nome, nascimento, profissao)
     values (?, ?, ?, ?, ?, ?)
    """)

conn.commit()
print("ok")

conn.close()