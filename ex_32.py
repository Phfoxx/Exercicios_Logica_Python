'''
32 DESAFIO Desenvolva um jogo onde o computador "pensa" em um númerointeiro entre 1 e 5 e o jogador tenta adivinhar. 
O programa deve dizer se o jogadorvenceu ou perdeu.

Nota para os alunos: Use a biblioteca import random  e a função random.randint(1,5).
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
    if a > 5: 
        return False
    elif a <= 0:
        return False
    else:
        return True

numero_aleatorio = random.randint(1,5)
tentativas = 1
print("---- JOGO DO NÚMERO SECRETO ----\n")

while(tentativas <= 3):
    print(f"TENTATIVA - {tentativas} DE 3")
    print(" - Digite um número de 1 a 3 - \n")
    chute = int(input("Digite seu chute: "))
    limparTela()
    if verificar_numero(chute) == False:
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

    
    
