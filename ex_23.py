'''
Promoção Dia da Mulher: Crie um algoritmo que leia o nome, o sexo (M ou F)
e o valor das compras de um cliente. O programa deve calcular o preço com
desconto:
    Se for Homem, o desconto é de 5%.
    Se for Mulher, o desconto é de 13%.
'''

nome = input("Digire seu nome: ")
sexo = input("Informe seu sexo (M/F): ").upper()
valor_compras = float(input("Informe o valor total da compra: "))
erro = False

if sexo == "M": 
    desconto = (valor_compras * 0.05)
elif sexo == "F": 
    desconto = (valor_compras * 0.13)
else: 
    erro = True

valor_com_desconto = valor_compras - desconto

if erro:
    print("Sexo informado INVALIDO")
else:
    print(f'\nOlá {nome}, bem vindo a loja!!')
    print(f'Aplicando o desconto de R${desconto:.2f} o valor total é R${valor_com_desconto:.2f}')