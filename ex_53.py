'''
53 Faça um programa que leia a idade e o sexo de 5 pessoas e mostre:
a) Quantos homens foram cadastrados;
b) Quantas mulheres foram cadastradas;
c) A média de idade do grupo;
d) A média de idade dos homens;
e) Quantas mulheres têm mais de 20 anos.
'''
import os
import platform
#Verificar o sistema operacional 
sistema = platform.system()

def limparTela():
    if sistema == "Windows":
        os.system("cls")
    else: 
        os.system("clear")

cont = 1
contagem_de_pessoas = 5
contagem_homens = 0
contagem_mulheres = 0
soma_idade_grupo = 0
soma_idade_homens = 0
mulheres_acima_dos_20 = 0

while cont <= contagem_de_pessoas: 
    idade_atual = int(input("Informe sua idade: "))
    sexo_atual = input("Informe seu sexo \n[H] - Homens\n[M] - Mulheres").upper()
    if sexo_atual == "M":
        contagem_mulheres += 1
        if idade_atual > 20:
            mulheres_acima_dos_20 += 1
    elif sexo_atual == "H":
        contagem_homens += 1 
        soma_idade_homens += idade_atual
    else:
        print("ERROR - Sexo informado incorreto.\nDIGITE APENAS M(MULHERES) OU H(HOMENS)")
        continue
    soma_idade_grupo += idade_atual
    cont += 1

idade_media_grupo = soma_idade_grupo / contagem_de_pessoas
if contagem_homens > 0:
    idade_media_homens = soma_idade_homens / contagem_homens
else: 
    idade_media_homens = 0 

limparTela()
print("--- INFORMAÇÕES DE CADASTRO ---")
print(f"Homens Cadastrados - {contagem_homens}")
print(f"Mulheres Cadastradas - {contagem_mulheres}")
print(f"A idade média do grupo - {idade_media_grupo}")
print(f"A média de idade dos homens - {idade_media_homens}")
print(f"Mulheres acima dos 20 - {mulheres_acima_dos_20}")