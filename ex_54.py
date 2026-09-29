'''
54 Desenvolva um aplicativo que leia o peso e a altura de 7 pessoas e exiba:
a) A média de altura do grupo;
b) Quantas pessoas pesam mais de 90kg;
c) Quantas pessoas com menos de 50kg medem menos de 1.60m;
d) Quantas pessoas com mais de 1.90m pesam mais de 100kg.
'''

cont = 1
contagem_limite = 7
pessoas_peso_acima_de_90 = 0
pessoas_magras_e_baixas = 0 
altas_maior_100_kg = 0
soma_alturas = 0 

while cont <= contagem_limite:
    peso = float(input("Informe seu peso: "))
    altura = float(input("Informe sua altura: "))

    soma_alturas += altura
    if peso > 90: 
        pessoas_peso_acima_de_90 += 1
        if peso > 100 and altura > 1.90:
            altas_maior_100_kg += 1
    elif peso < 50 and altura < 1.60: 
        pessoas_magras_e_baixas += 1
    cont += 1 

media_altura = soma_alturas / contagem_limite

print(f"A média de altura do grupo é {media_altura:.2f}")
print(f"Um total de {pessoas_peso_acima_de_90} pessoas pesam mais que 90 Kg")
print(f"Pessoas com menos de 50kg e que medem menos de 1.60m: {pessoas_magras_e_baixas}")
print(f"Pessoas com mais de 1.90m e que pesam mais de 100kg: {altas_maior_100_kg}")
