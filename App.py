import mysql.connector
from mysql.connector import errorcode
from DataBase.configDB import *

def criarRedeSocial():
    nome = str(input("Nome da Rede Social: "))
    print("Rede Social %s criada com sucesso!"%nome)

def exibirMenu():
    print("""
            Menu\n
            1 - Criar rede social\n
            2 - Criar Usuário\n
            0 - Sair\n""")

def adicionarUsuario():

    try:
        conn = mysql.connector.connect(**config)
        print("Conexão Estabelecida")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with the user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE ifight(
                        id integer primary key autoincrement,
                        email varchar(100) not null,
                        senha varchar(50) not null, 
                        nome varchar(150), 
                        nascimento date, 
                        profissao varchar(50), 
                        genero varchar(15), 
                        mensagem text);''')

    a_email = input("email:")
    a_senha = input("senha:")
    a_nome = input("nome:")
    a_nascimento = int(input("seu nascimento:"))
#    a_diaNascimento = int(input("Dia do seu nascimento: "))
#    a_mesNascimento = int(input("Mes do seu nascimento: "))
#    a_anoNascimento = int(input("Ano do seu nascimento: "))
    a_profissao = input("profissao:")
    a_genero = input("Gênero:")

    cursor.execute('''INSERT INTO inventory ifight (login, senha, nome, nascimento, profissao,genero)
                        VALUES (?, ?, ?, ?, ?, ?)''',
                        ( a_email,a_senha,a_nome,a_nascimento,a_profissao,a_genero))
    print("Inserido", cursor.rowcount)

    conn.commit()
    cursor.close()
    conn.close()
    print("Tudo in ordi.")

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