'''
Desenvolva um programa que sorteie 20 números entre 0 e 10 (usando 
random.randint()) e exiba:
a) Quais foram os números sorteados;
b) Quantos números estão acima de 5;
c) Quantos números são divisíveis por 3.
'''
import random

cont = 1
numeros_acima_de_5 = []
numeros_div_por_3 = []
numeros_sorteados = []

while cont <= 20: 
    numero_aleatorio = random.randint(0,10)
    numeros_sorteados.append(numero_aleatorio)
    if numero_aleatorio > 5:
        numeros_acima_de_5.append(numero_aleatorio)
    if numero_aleatorio % 3 == 0 and numero_aleatorio > 0:
        numeros_div_por_3.append(numero_aleatorio)
    cont += 1

exibir_numeros = "|".join(str(num) for num in numeros_sorteados)
exibir_numeros_acima_de_5 = "|".join(str(num) for num in numeros_acima_de_5)
exibir_numeros_div_por_3 = "|".join(str(num) for num in numeros_div_por_3)
print("Números sorteados: ")
print(exibir_numeros, "\n")
print(f"Numero estão acima de 5 = {exibir_numeros_acima_de_5} - Quantidade : {len(numeros_acima_de_5)}")
print(f"Numeros dívisiveis por 3 = {exibir_numeros_div_por_3} - Quantidade : {len(numeros_div_por_3)}")