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
        genero varchar(15) ,
        mensagem text
    )
""")

cursor.execute("""
    create table mensagem
        (mensagemPublica text,
         mensagemPrivada text
    )
""")

cursor.execute\
    ("""
    create table timeLine
        (mensagemPublica text,
         mensagemPrivada text
        )
""")

cursor.execute\
    ("""
  create table batePapo
   (mensagemPublica text,
    mensagemPrivada text
    )
""")

conn.commit()

print("Menu\n 1 - Criar rede social\n 2 - Inserir Usuário\n 3 - Adicionar Amigo\n 4 - Enviar Mensagem")
op_escolhida = int(input())
if op_escolhida == 1:
    print("Em produção")
elif op_escolhida == 2:
    print("Em produção")
elif op_escolhida == 3:
    print("Em produção")
elif op_escolhida == 4:
    print("Em produção")
    '''try:
        if op_escolhida == (op_escolhida*1):
            print("Número inválido")
    except ValueError:
        print("Tudo rasuavelmente bem")'''
conn.close()
