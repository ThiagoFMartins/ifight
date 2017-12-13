class usuario():
    def __init__(self,id,nome,email,senha,genero,nascimento,profissao):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.genero = genero
        self.nascimento = nascimento
        self.profissao = profissao

    def __str__(self):
        return "Usuario <%s>" % (self.nome)

    def __repr__(self):
        return self.__str__()