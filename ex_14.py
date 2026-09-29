'''
14) Sistema de Locadora: Escreva um programa que pergunte a quantidade de Km percorridos e a quantidade de dias pelos quais um carro foi alugado. 
Calcule o preço total: R$90 por dia e R$0,20 por Km rodado.
'''

km_percorridos = float(input("Informe a quantidade de KM percorridos: "))
quantidade_de_dias = int(input("Informe a quantidade de dias que o carro ficou alugado: "))

#Calculo por KM (R$0,20 por km rodado)
calculoPorKm = km_percorridos * 0.20

#Calculo por dias (R$90,0 por dia)
calculoPorDia = quantidade_de_dias * 90 

#Calculo preço total
precoTotal = calculoPorDia + calculoPorKm

print(f"Preço do aluguel: R${precoTotal:.2f}")