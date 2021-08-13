import random

def jogar():
    print('*********************************')
    print('Bem vindo ao jogo de advinhação !')
    print('*********************************')

    numero_secreto = random.randrange(0,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Escolha o nivel de dificuldade:", numero_secreto)
    print("(1) Facil (2) Medio (3) Dificil")

    nivel = int(input("Defina o nivel: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1,total_de_tentativas + 1) :
        print("Tentativa {} de {}".format(rodada,total_de_tentativas))
        chute_str = input("Digite um numero de 1 a 100:")
        print("Voce digitiou:", chute_str)
        chute_int = int(chute_str)

        acertou = numero_secreto == chute_int
        maior = chute_int > numero_secreto
        menor = chute_int < numero_secreto

        if(chute_int < 1 or chute_int >100):
            print("Valor errado digite um numero de 1 a 100!")
            continue

        if (acertou):
            print("Parabens voce acertou e fez {} !".format(pontos))
            break
        else:
            if(maior):
                print("Voce errou ! Seu numero é menor.")
            elif(menor):
                print("Voce errou ! Seu numero é maior. ")

                pontos_perdidos = abs(numero_secreto - chute_int)
                pontos = pontos - pontos_perdidos


    print("Fim do Jogo")

if(__name__ == "__main__"):
        jogar()