import mysql.connector
from model.RedeSocial import RedeSocial
from database.configDB import config

class RedeSocialDAO():

    def inserirRedeSocial(redeSocial: RedeSocial):

        
        idRedeSocial = 0
       
        query = "INSERT INTO redesocial(nome, descricao) " \
                "VALUES(%s, %s)"
      
        values = (redeSocial.nome, redeSocial.descricao)

        try:
           
            conn = mysql.connector.connect(**config) 
           
            cursor = conn.cursor()
            cursor.execute(query, values)
           
            if cursor.lastrowid:
                idRedeSocial = cursor.lastrowid
           
            conn.commit()
        except mysql.connector.Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()
       
        return idRedeSocial
