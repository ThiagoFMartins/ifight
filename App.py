from Model.usuario import usuario
from Model.RedeSocial import RedeSocial

def criarRedeSocial():
    nome = str(input("Nome da Rede Social: "))

def exibirMenu():
    
    print("Menu\n 1 - Escolher nome da rede social\n 0 - Sair")

def adicionarUsuario():
    pass
    
def main( args = [] ):
    
    continuar = True
    
    while continuar:

        exibirMenu()

        try:
    
            op_escolhida = int(input("Escolha uma das opções: "))
            if op_escolhida == 0 :
                continuar = False
            elif op_escolhida == 1:
                criarRedeSocial()
            else:
                print("Opção inválida")
        
        except ValueError:
            print("Erro")

if (__name__ == "__main__"):
    main()