'''
Crie um programa que calcule a área de uma parede (base x altura) e a
quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta
cobre 2m2.
'''


rendimento_litro = 2
base = float(input('Informe a base da parede (m):  '))
altura = float(input('Informe a altura da parede (m): '))
area = base * altura
litros_necessarios = area / rendimento_litro

print(f'A área da parede é {area}m')
print(f'É necessario {litros_necessarios:.2f} litros de tinta para pintar a parede.')