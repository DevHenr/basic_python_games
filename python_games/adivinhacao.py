import random


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")


    numero_secreto = random.randint(1, 30)
    total_de_tentativas = 0
    numero_de_vitorias = 0
    # rodada = 1

    print("Qual o nível de dificuldade?", end="\n\n")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5
        
    # while (rodada <= total_de_tentativas):
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 30: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 30:
            print ("Você deve digitar um número entre 1 e 10!")
            continue
        

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou and rodada <= 3):
            print("O número secreto era:", numero_secreto)
            print("Você acertou!", end="\n\n")
            numero_secreto = random.randint(1, 10)
            numero_de_vitorias = numero_de_vitorias + 1
        elif (acertou and rodada == 4):
            print("Você acertou!", end="\n\n")
            numero_de_vitorias = numero_de_vitorias + 1
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.", end="\n\n")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.", end="\n\n")

        # rodada = rodada + 1

    print("O número secreto era:", numero_secreto)
    print("O seu número de vitórias foi:", numero_de_vitorias, end="\n\n")
    print("Fim do jogo", end="\n\n")

if (__name__ == "__main__"):
    jogar()