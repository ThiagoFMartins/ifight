import sqlite3

conn = sqlite3.connect('ifight.db')
cursor = conn.cursor()

class usuario():
    def __init__(self,id,login,senha,nome,nascimento,profissao,publicacaoPublica,publicacaoPrivada):
        self.id = id
        self.login = login
        self.senha = senha
        self.nome = nome
        self.nascimento = nascimento
        self.profissao = profissao
        self.publicacaoPublica = publicacaoPublica
        self.publicacaoPrivada = publicacaoPrivada

    def inserir(self):
        conn = sqlite3.connect('ifight.db')
        cursor = conn.cursor()
        cursor.execute("""
        insert into tb_ususario(login,senha,nome,nascimento,profissao,publicacaoPublica,publicacaoPrivada)
        values(self.login,self.senha,self.nome,self.nascimento,self.profissao,self.publicacaoPublica,self.publicacaoPrivada)
        """)
        conn.commit()
        conn.close()

    def listar(self):
        usuario = []
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
            publicacaoPublica = linha[6]
            publicacaoPrivada = linha[7]
            usuario = usuario(login,senha,nome,nascimento,profissao,publicacaoPublica,publicacaoPrivada)
            usuario.append(usuario)

        conn.close()

        return usuarios

    def deletar(self, id):
        pass


print("Menu\n 1 - Criar rede social\n 2 - Inserir Usuário\n 3 - Adicionar Amigo\n 4 - Enviar Mensagem")

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