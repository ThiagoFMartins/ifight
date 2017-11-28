import sqlite3

conn = sqlite3.connect('ifight.db')
cursor = conn.cursor()

class usuario():
    def __init__(self,id,login,senha,nome,nascimento,profissao,genero,mensagem,amigos):
        self.id = id
        self.login = login
        self.senha = senha
        self.nome = nome
        self.nascimento = nascimento
        self.profissao = profissao
        self.genero = genero
        self.mensagem = mensagem
        self.amigos = amigos

    def inserir(self):
        conn = sqlite3.connect('ifight.db')
        cursor = conn.cursor()
        cursor.execute("""
        insert into tb_ususario(login,senha,nome,nascimento,profissao,genero,mensagem,amigos)
        values(self.login,self.senha,self.nome,self.nascimento,self.profissao,self.genero,self.mensagem,self.amigos)
        """)
        conn.commit()
        conn.close()

    def listar(self):
        usuarios = []
        conn = sqlite3.connect('ifight.db')

        cursor = conn.cursor()

        cursor.execute("""
        select * tb_ususario;
        """)
        for linha in cursor.fetchall():

            login = linha[1]
            senha = linha[2]
            nome = linha[3]
            nascimento = linha[4]
            profissao = linha[5]
            genero = linha[6]
            mensagem = linha[7]
            amigos = linha[8]
            usuario = usuario(login,senha,nome,nascimento,profissao,genero,mensagem,amigos)
            usuarios.append(usuario)

        conn.close()

        return usuarios

    def deletar(self, id):
        conn = sqlite3.connect("ifight.db")
        cursor = conn.cursor()

        cursor.execute(""""
                  DELETE FROM tb_usuario
                  WHERE id =?
              """, id)

        conn.commit()
        conn.close()

    def adicionarAmigo(self):
        amigos.inserir()