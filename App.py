import mysql.connector
from Model.usuario import usuario
from Model.RedeSocial import RedeSocial
from DataBase.configDB import config


def criarRedeSocial():
    nome = str(input("Nome da Rede Social: "))


def exibirMenu():
    print("Menu\n 0 - Sair\n 1 - Escolher nome da rede social\n 2 - Criar Usuário")


def adicionarUsuario():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    DB_NAME = 'ifight'
    tables = {}
    create table ['ifight'] = ('''
        id integer not null primary key autoincrement,
        login varchar(100),
        senha varchar(50), 
        nome varchar(150) not null, 
        nascimento date, 
        profissao varchar(50), 
        genero varchar(15), 
        mensagem text
    ''')

    cursor = conn.cursor()
    a_login = input("login:")
    a_senha = input("senha:")
    a_nome = input("nome:")
    a_nascimento = input("nascimeno (aaaa/mm/dd):")
    a_profissao = input("profissao:")
    a_genero = input("Gênero:")
    cursor.execute \
        ("""
         INSERT INTO ifight (login, senha, nome, nascimento, profissao,genero)
         VALUES (?, ?, ?, ?, ?, ?)
        """, ( a_login, a_senha, a_nome, a_nascimento, a_profissao,a_genero))

def main(args=[]):
    continuar = True

    while continuar:

        exibirMenu()

        try:

            op_escolhida = int(input("Escolha uma das opções: "))
            if op_escolhida == 0:
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
