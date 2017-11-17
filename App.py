import sqlite3
import datetime

conn = sqlite3.connect('ifight.db')
cursor = conn.cursor()

cursor.execute ("""
    create table usuario 
    (
        id integer not null primary key autoincrement,
        login varchar(100),
        senha varchar (50),
        nome varchar(150) not null,
        nascimento date,
        profissao varchar (50),
        genero varchar(15) ,
        mensagem text
    )
""")

conn.close()

conn = sqlite3.connect('ifight.db')
cursor = conn.cursor()

cursor.execute ("""
    create table amigo 
    (
        id integer not null primary key autoincrement,
        login varchar(100),
        senha varchar (50),
        nome varchar(150) not null,
        nascimento date,
        profissao varchar (50),
        genero varchar(15) ,
        mensagem text
    )
""")

'''conn = sqlite3.connect('ifight.db')

cursor = conn.cursor()

a_login = input("login:")
a_senha = input("senha:")
a_nome = input("nome:")
a_nascimento = input("nascimeno (aaaa/mm/dd):")
a_profissao = input("profissao:")
a_genero = input("Gênero:")

cursor.execute\
    ("""
     INSERT INTO amigo (login, senha, nome, nascimento, profissao,genero)
     VALUES (?, ?, ?, ?, ?, ?)
    """, (a_login,a_senha,a_nome,a_nascimento,a_profissao,a_genero))

conn.commit()

print("ok")

conn.close()'''

'''cursor.execute("""
    create table mensagem
    (
        id integer not null primary key autoincrement,
         conteudoMensagem text,
         visibilidade boolean
    )
""")

cursor.execute\
    ("""
    create table timeLine
        (
         id integer not null primary key autoincrement,
         mensagemPublica text,
         mensagemPrivada text
        )
""")

cursor.execute\
    ("""
  create table batePapo
   (
        id integer not null primary key autoincrement,
        mensagemPublica text,
        mensagemPrivada text
    )
""")

conn.commit()'''

print("Menu\n 1 - Criar rede social\n 2 - Inserir Usuário\n 3 - Adicionar Amigo\n 4 - Enviar Mensagem")
op_escolhida = int(input())
if op_escolhida == 1:
    print("Em produção")
elif op_escolhida == 2:
    conn = sqlite3.connect('ifight.db')

    cursor = conn.cursor()

    u_login = input("login:")
    u_senha = input("senha:")
    u_nome = input("nome:")
    u_nascimento = input("nascimeno (aaaa/mm/dd):")
    u_profissao = input("profissao:")
    u_genero = input("Gênero:")

    cursor.execute \
        ("""
         INSERT INTO usuario (login, senha, nome, nascimento, profissao,genero)
         VALUES (?, ?, ?, ?, ?, ?)
        """, (u_login, u_senha, u_nome, u_nascimento, u_profissao, u_genero))

    conn.commit()

    print("ok")

    conn.close()
elif op_escolhida == 3:
    conn = sqlite3.connect('ifight.db')

    cursor = conn.cursor()

    a_login = input("login:")
    a_senha = input("senha:")
    a_nome = input("nome:")
    a_nascimento = input("nascimeno (aaaa/mm/dd):")
    a_profissao = input("profissao:")
    a_genero = input("Gênero:")

    cursor.execute \
        ("""
         INSERT INTO amigo (login, senha, nome, nascimento, profissao,genero)
         VALUES (?, ?, ?, ?, ?, ?)
        """, (a_login, a_senha, a_nome, a_nascimento, a_profissao, a_genero))

    conn.commit()

    print("ok")

    conn.close()
elif op_escolhida == 4:
    print("Em produção")

conn.close()