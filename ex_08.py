'''
Escreva um programa que leia uma distância em metros e a converta para as
demais unidades de medida (quilômetros, hectômetros, decâmetros, decímetros,
centímetros e milímetros), exibindo cada uma em uma nova linha.
'''
distancia_metros = float(input('Digite a distância de São Paulo a Minas Gerais: '))
distancia_quilometros = distancia_metros / 1000 
distancia_hectometros = distancia_metros / 100
distancia_decametros = distancia_metros / 10
distancia_decimetros = distancia_metros * 10 
distancia_centimetros = distancia_metros * 100
distancia_milimetros = distancia_metros * 1000

print("---CONVERSÃO PARA QUILOMETROS---")
print(f"{distancia_metros}metros -> {distancia_quilometros}Km")
print("---CONVERSÃO PARA HECTÔMETROS---")
print(f"{distancia_metros}metros -> {distancia_hectometros}Hm")
print("---CONVERSÃO PARA DECÂMETROS---")
print(f"{distancia_metros}metros -> {distancia_decametros}Dam")
print("---CONVERSÃO PARA DECÍMETROS---")
print(f"{distancia_metros}metros -> {distancia_decimetros}Dm")
print("---CONVERSÃO PARA CENTÍMETROS---")
print(f"{distancia_metros}metros -> {distancia_centimetros}Cm")
print("---CONVERSÃO PARA MILÍMETROS---")
print(f"{distancia_metros}metros -> {distancia_milimetros}Mm")
