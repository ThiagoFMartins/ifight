import mysql.connector
from DataBase.configDB import *

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

def criarRedeSocial():
    nome = str(input("Nome da Rede Social: "))
    print("Rede Social %s criada com sucesso!"%nome)

def exibirMenu():
    print(""""Menu\n 
            1 - Criar rede social\n 
            2 - Criar Usuário\n
            0 - Sair\n """)

def adicionarUsuario():

    cursor.execute('''CREATE TABLE ifight(
        id integer primary key autoincrement,
        login varchar(100),
        senha varchar(50), 
        nome varchar(150) not null, 
        nascimento date, 
        profissao varchar(50), 
        genero varchar(15), 
        mensagem text
    );'''
                   )

    a_login = input("login:")
    a_senha = input("senha:")
    a_nome = input("nome:")
    a_nascimento = input("nascimeno (aaaa/mm/dd):")
    a_profissao = input("profissao:")
    a_genero = input("Gênero:")
    cursor.execute ("""
         INSERT INTO ifight (login, senha, nome, nascimento, profissao,genero)
         VALUES (?, ?, ?, ?, ?, ?)
        """, ( a_login, a_senha, a_nome, a_nascimento, a_profissao,a_genero))

def main(args=[]):
    continuar = True

    while (continuar):

        exibirMenu()

        try:

            op_escolhida = int(input("Escolha uma das opções: "))
            if op_escolhida == 0:
                print("Saindo...")
                continuar = False
            elif op_escolhida == 1:
                criarRedeSocial()
            elif op_escolhida == 2:
                adicionarUsuario()
            else:
                print("Opção inválida")

        except ValueError:
            print("Erro")


if (__name__ == "__main__"):
    main()