import random

print("********************************")
print("Bem-Vindo no jogo de advinhação!")
print("********************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 0
pontos = 1000

print("Qual nível de dificuldade?")
print("(1)Iniciante (2)Veterano (3) Capitão")

nivel = int(input("Define o nível: "))

if(nivel == 1):
    total_de_tentativas = 15
elif (nivel == 2 ):
    total_de_tentativas = 7
else:
    total_de_tentativas = 3


for rodada in range (1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite um número de 1 a 100: ")
    print("Você digitou " , chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    else:
        if(maior):
            print("Você errou! 0 seu chute foi maior do que o número secreto.")
        elif(menor):
            print("Você errou! 0 seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

print("Fim do jogo")
