'''
55) DESAFIO Melhore o jogo de adivinhação Ex 32. O computador sorteia umnúmero de 1 a 10, e o jogador tem 4 tentativas para acertar. O programa deveExercícios de Algoritmos7
avisar se o palpite foi correto ou se as tentativas acabaram.
'''
import random 
import os
import platform

#Verificar o sistema operacional 
sistema = platform.system()

def limparTela():
    if sistema == "Windows":
        os.system("cls")
    else: 
        os.system("clear")

def verificar_numero(a):
    if a > 10: 
        return False
    elif a <= 0:
        return False
    else:
        return True

numero_aleatorio = random.randint(1,10)
tentativas = 1
tentativa_limite = 4
print("---- JOGO DO NÚMERO SECRETO ----\n")

while tentativas <= tentativa_limite:
    print(f"TENTATIVA - {tentativas} DE {tentativa_limite}")
    print(" - Digite um número de 1 a 10 - \n")
    chute = int(input("Digite seu chute: "))
    limparTela()
    if not verificar_numero(chute):
        print("Número invalido")
        continue
    else: 
        if chute > numero_aleatorio:
            print("Seu chute foi MAIOR que o número secreto")
        elif chute < numero_aleatorio:
            print("Seu chute foi menor que o número secreto")
        else:
            print("Você acertou o número secreto !!")
            break
        tentativas = tentativas + 1
else: 
    limparTela()
    print(f"Infelizmente você não conseguiu acertar o numero secreto :(\nNúmero Secreto = {numero_aleatorio}")
    