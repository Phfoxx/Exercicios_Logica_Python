'''
25) [DESAFIO] Crie um script que leia o comprimento de três segmentos de reta.
O programa deve analisar esses valores e dizer se é possível formar um triângulo
com eles.
    Regra matemática: Para formar um triângulo, a soma de dois lados deve ser
    sempre maior que o terceiro lado.
'''

comprimento1 = float(input("Digite o comprimento 1: "))
comprimento2 = float(input("Digite o comprimento 2: "))
comprimento3 = float(input("Digite o comprimento 3: "))

if comprimento1 + comprimento2 > comprimento3 and comprimento2 + comprimento3 > comprimento1 and comprimento1 + comprimento3 > comprimento2: 
    print("É possivel formar um triângulo! ")
else: 
    print("Não é possível formar um triângulo! ")