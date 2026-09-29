'''
1 DESAFIO Crie um jogo de JoKenPo Pedra-Papel-Tesoura).
Dica: Explore o uso de números para representar as opções ou stringsdiretamente.
'''

import os

def instrução():
    print("--- JoKenPo ---")
    print("Defina sua escolha:")
    print("[1] PEDRA\n[2] PAPEL \n[3] TESOURA")

def mostra_escolha(n1,n2):
    print(f"Jogador 1 : {n1}")
    print(f"Jogador 2 : {n2}")

instrução()
jogador1 = int(input("JOGADOR 1 - "))
os.system('clear')
instrução()
jogador2 = int(input("JOGADOR 2 - "))
os.system('clear')

if jogador1 == 1: 
    escolha1 = "PEDRA"
elif jogador1 == 2:
    escolha1 = "PAPEL"
else:
    escolha1 = "TESOURA"

if jogador2 == 1: 
    escolha2 = "PEDRA"
elif jogador2 == 2:
    escolha2= "PAPEL"
else:
    escolha2 = "TESOURA"

print("ESCOLHAS: ")

#Situações que o jogador 1 ganha
if (jogador1 == 1 and jogador2 == 3) or (jogador1 == 2 and jogador2 == 1) or (jogador1 == 3 and jogador2 == 2): 
    mostra_escolha(escolha1, escolha2)
    print("Jogador 1 GANHOU !!")
#Situações que o jogador 2 ganha
elif (jogador2 == 1 and jogador1 == 3) or (jogador2 == 2 and jogador1 == 1) or (jogador2 == 3 and jogador1 == 2):
    mostra_escolha(escolha1, escolha2)
    print("Jogador 2 GANHOU !!")
    
#Situações de empate
else:
    print("EMPATE")