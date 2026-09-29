'''
59) Crie um programa que leia o sexo e a idade de várias pessoas, perguntando
após cada cadastro se o usuário deseja continuar ou não. Ao final, exiba:
    a) Qual foi a maior idade lida.
    b) Quantos homens foram cadastrados.
    c) Qual é a idade da mulher mais jovem.
    d) Qual é a média de idade entre os homens.
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
continuar = 0
qtd_homens = 0 
maior_idade = 0 
idade_mulher_mais_jovem = 0

while continuar!=1 :
    limparTela()
    print(f"--- PESSOA {cont} ---")
    idade = int(input("- Idade :"))
    sexo = input("- Sexo [H/M]:").upper()
    if sexo == "H":
        if qtd_homens == 0: 
            soma_idade_homens = 0

        qtd_homens += 1
        soma_idade_homens += idade
    else:
        if idade_mulher_mais_jovem == 0:
            idade_mulher_mais_jovem = idade
        else:
            if idade_mulher_mais_jovem > idade:
                idade_mulher_mais_jovem = idade
    if maior_idade < idade:
        maior_idade = idade

    continuar = int(input("APERTE [1] PARA PARAR ou [2] PARA CONTINUAR \n-"))
    cont += 1 

media_idade_homens = soma_idade_homens / qtd_homens

print("--- RESULTADOS ---")
print(f"- Maior idade: {maior_idade}")
print(f"- Quantidade de homens: {qtd_homens}")
print(f"- A idade da mulher mais jovem: {idade_mulher_mais_jovem}")
print(f"- A média de idade dos homens: {media_idade_homens:.2f}")