'''
18) Crie um script que leia o ano de nascimento de uma pessoa, calcule a sua
idade atual e informe se ela já atingiu a idade mínima para votar (16 anos).
'''

ano_atual = 2026
ano_nascimento = int(input("Digite seu ano nascimentos: "))

idade_atual = ano_atual - ano_nascimento 

if idade_atual >= 18: 
    print(f"Olá, você tem {idade_atual} anos e já pode votar. ")
else: 
    print(f"Olá, você tem {idade_atual} anos e ainda não pode votar. ")