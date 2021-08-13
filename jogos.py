import forca
import advinhacao

def escolha_jogo():
    print('*********************************')
    print('*******Escolha seu Jogo******** !')
    print('*********************************')

    print("(1) Adivinhação (2) Forca")

    jogo = int(input("Qual Jogo:"))

    if(jogo == 1):
        print("Bem vindo a Advinhação!")
        advinhacao.jogar()
    elif(jogo == 2):
        print("Bem vindo a Forca!")
        forca.jogar()

if(__name__ == "__main__"):
    escolha_jogo()

