import Mysql.connector
from Model.RedeSocial import RedeSocial
from DataBase.configDB import config

class RedeSocial():

    def criarRedeSocial():
        nome = str(input("Nome da Rede Social: "))

    def exibirMenu():

        print("Menu\n 1 - Escolher nome da rede social\n 0 - Sair")

    def inserirRedeSocial(redeSocial):

        idRedeSocial = 0
        query = "INSERT INTO ifight(nome) " \
                "VALUES(%s, %s)"
        VALUES = (redeSocial.nome)

        try:
            conn = Mysql.connector.connect(**config)
            cursor = conn.cursor()
            cursor.execute(query, VALUES)
            if cursor.lastrowid:
                idRedeSocial = cursor.lastrowid
            conn.commit()
        except Mysql.connector.Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()
        return idRedeSocial