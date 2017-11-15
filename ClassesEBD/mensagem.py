import sqlite3

conn = sqlite3.connect('ifight.db')
cursor = conn.cursor()

class mensagem():
    def __init__(self,id,visibilidade,conteudoMensagem):
        self.id = id
        self.visibilidade = visibilidade
        self.conteudoMensagem = conteudoMensagem

    def listar(self):
        mensagens = []
        conn = sqlite3.connect('ifight.db')

        cursor = conn.cursor()

        cursor.execute("""
        select * tb_mensagem;
        """)
        for linha in cursor.fetchall():

            visibilidade = linha[1]
            conteudoMensagem = linha[2]
            mensagem = mensagem(visibilidade,conteudoMensagem)
            mensagens.append(mensagem)

        conn.close()

        return mensagens