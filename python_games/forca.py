import random



def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print("A seguinte palavra possui:", len(palavra_secreta), "Letras", end="\n\n")
    print(letras_acertadas, "\n\n")

    enforcou = False
    acertou = False
    erros = 0
    
    while (not acertou and not enforcou):

        chute = pede_chute()

        if(chute in palavra_secreta):
           marca_chute_corrteto(chute, letras_acertadas, palavra_secreta)
           print("A quantidade de vezes que a letra '{}' aparece é:".format(chute), palavra_secreta.count(chute))    
           print("Letra Certa!", end="\n\n")          
        else:
            erros += 1 
            desenha_forca(erros)
            print("Ops, você errou! Faltam {} tentativas.".format(7-erros), end="\n\n")

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas 
        print(letras_acertadas, "\n\n")   
       

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()
    print("A palavra secreta era: {}".format(palavra_secreta))    
    print("Fim de jogo!", end="\n\n")



def pede_chute():
    chute = input("Qual letra: ")
    chute = chute.strip().upper()
    return chute

def imprime_mensagem_abertura():
        print("*********************************")
        print("***Bem vindo ao jogo da Forca!***")
        print("*********************************", end="\n\n")
    
def carrega_palavra_secreta():
        arquivo = open('palavras.txt', encoding='utf-8', mode='r')
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
    
        arquivo.close()
   
        numero = random.randrange(0,len(palavras))
        palavra_secreta = palavras[numero].upper()
        
        return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def marca_chute_corrteto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ", end="\n\n")

def imprime_mensagem_perdedor():
    print("Puxa, você foi enforcado!")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ", end="\n\n")  


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()    

if(__name__ == "__main__"):
    jogar()