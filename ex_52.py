'''
52 Crie um algoritmo que leia a idade de 10 pessoas e exiba:
a) A média de idade do grupo;
b) Quantas pessoas têm mais de 18 anos;
c) Quantas pessoas têm menos de 5 anos;
d) Qual foi a maior idade lida.
'''
pessoas_com_menos_de_5 = 0
pessoas_maiores_de_idade = 0
soma_idades = 0 
maior_idade = 0
cont = 1
while cont <= 10:
    idade_atual = int(input(f"Digite a idade da pessoa {cont}: "))
    if cont == 1:
        maior_idade = idade_atual
    if idade_atual >= 18:
        pessoas_maiores_de_idade += 1
    elif idade_atual < 5:
        pessoas_com_menos_de_5 += 1

    if maior_idade < idade_atual:
        maior_idade = idade_atual
    soma_idades += idade_atual
    cont+=1

media_idades = soma_idades / 10
print(f"- A média das idades é {media_idades:.2f} anos")
print(f"- Quantidade de pessoas acima dos 18 : {pessoas_maiores_de_idade}")
print(f"- Quantidade de pessoas menores de 5 anos: {pessoas_com_menos_de_5}")
print(f"- A maior idade lida foi: {maior_idade}")
        
