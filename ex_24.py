'''
24) Desenvolva um programa que pergunte a distância que um passageiro deseja
percorrer em km. Calcule o preço da passagem usando uma condicional
composta:
    Para viagens de até 200 km: R$0.50 por km.
    Para viagens acima de 200 km: R$0.45 por km.
'''
distancia_percorrida = float(input("Digite a distância que deseja percorrer: "))
valor_ate_200 = 0.50
valor_acima_de_200 = 0.45

if distancia_percorrida <= 200: 
    valor_passagem = distancia_percorrida * valor_ate_200
else: 
    valor_passagem = distancia_percorrida * valor_acima_de_200

print(f"Para percorrer uma distancia de {distancia_percorrida}KM o valor será R${valor_passagem:.2f}")
