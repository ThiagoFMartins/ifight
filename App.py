import sqlite3

conn = sqlite3.connect('ifight.db')

cursor = conn.cursor()

cursor.execute ("""
    create table usuario (
        id integer not null primary key autoincrement,
        login varchar(100),
        senha varchar (50),
        nome varchar(150) not null,
        nascimento date,
        profissao varchar (50),
        publicacaoPublica text,
        publicacaoPrivada text
    )
""")

cursor.execute("""
    create table mensagem
        (mensagemPublica text,
         mensagemPrivada text
    )
""")

cursor.execute("""
    create table timeLine
        (mensagemPublica text,
        mensagemPrivada text
    )
""")

cursor.execute("""
  create table batePapo(
    mensagemPublica text,
    mensagemPrivada text
  )
""")

conn.commit()

print("tudo top")

conn.close()
