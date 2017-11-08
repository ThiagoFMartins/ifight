import sqlite3

class Usuario():
    def __init__(self, nome, email, senha, profissao, sexo, data_nasc):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.profissao = profissao
        self.sexo = sexo
        self.data_nasc = data_nasc

    def inserir(self):
        conn = sqlite3.connect('dinamics.db')
        cursor = conn.cursor()
        cursor.execute('''
          INSERT INTO TB_Usuario (nome, email, senha, profissao, sexo, data_nasc)
          VALUES (self.nome, self.email, self.senha, self.profissao,
           self.sexo, self.data_nasc)
        ''')
        conn.commit()
        conn.close()

    def listar(self):
        usuarios = []
        conn = sqlite3.connect('dinamics.db')
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM TB_Usuario;
        """)
        for linha in cursor.fetchall():
            nome = linha[1]
            email = linha[2]
            senha = linha[3]
            profissao = linha[4]
            sexo = linha[5]
            data_nasc = linha[6]
            usuario = Usuario(nome, email, senha, profissao, sexo, data_nasc)
            usuarios.append(usuario)

        conn.close()

        return usuarios

    def deletar(self, id):
        pass

    def atualizar(self, nome, email, senha, profissao, sexo, data_nasc):
        pass

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
