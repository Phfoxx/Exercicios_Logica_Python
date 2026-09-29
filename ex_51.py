'''
51) Escreva um programa que leia o preço de 8 produtos e, ao final, informe qual foi o maior e o menor preço digitados
'''
cont = 1
menor_preco = 0
maior_preco = 0
while cont <= 8:
    preco_atual = float(input(f"Digite o valor do produto {cont}: "))
    if preco_atual > maior_preco:
        maior_preco = preco_atual
    if preco_atual <= menor_preco or menor_preco == 0:
        menor_preco = preco_atual
    cont += 1

print(f"O maior número digitado foi {maior_preco}\nO menor preço digitado foi {menor_preco}")