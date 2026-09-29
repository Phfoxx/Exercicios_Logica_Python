'''
Desenvolva uma lógica que leia os coeficientes a, b e c de uma equação do
segundo grau e calcule o valor de Delta (Δ=b2−4ac).
'''
a = float(input('Digite o valor da coeficiente a: '))
b = float(input('Digite o valor da coeficiente b: '))
c = float(input('Digite o valor da coeficiente c: '))

delta = (b**2) - (4*a*c)

print(f'O valor de delta é {delta}')