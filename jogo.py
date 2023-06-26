import random

print("********************************")
print("Bem-Vindo no jogo de advinhação!")
print("********************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 3

for rodada in range (1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu numero: ")
    print("Você digitou " , chute_str)
    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou!")
    else:
        if(maior):
            print("Você errou! 0 seu chute foi maior do que o número secreto.")
        elif(menor):
            print("Você errou! 0 seu chute foi menor do que o número secreto.")

    rodada = rodada + 1

print("Fim do jogo")
