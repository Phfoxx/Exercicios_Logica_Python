'''
9) Faça um algoritmo que receba um valor em Reais (R$) e calcule quantos
Dólares (US$) a pessoa pode comprar.

Considere a taxa de câmbio fixa: US1.00=R3.45.
'''

print
valor_reais = float(input('Digite o valor em R$: '))
cambio = 3.45
valor_dolar = valor_reais / cambio

print(f'--- CONVERSÃO DE REAL PARA DOLAR ---')
print(f'    R${valor_reais:.2f} -> US${valor_dolar:.2f}')