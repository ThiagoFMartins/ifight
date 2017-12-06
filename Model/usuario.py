class usuario():
    def __init__(self,nome,email,senha,genero):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.genero = genero

    def __str__(self):
        return "Usuario <%s>" % (self.nome)

    def __repr__(self):
        return self.__str__()