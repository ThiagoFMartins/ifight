def criarRedeSocial():
    nome = str(input("Nome da Rede Social: "))

def exibirMenu():
    
    print("Menu\n
    1 - Escolher nome da rede social\n
    0 - Sair")
    
def main( args = [] ):
    
    exibirMenu()
    
    continuar = true
    
    while continuar:
        try:
    
            op_escolhida = int(input("Escolha uma das opções: "))
            if op_escolhida == 0 :
                continuar = false
            elif op_escolhida == 1:
                criarRedeSocial()
        
        except valueError:
            print("Erro")
