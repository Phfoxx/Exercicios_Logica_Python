'''
30) [DESAFIO] Refaça o algoritmo do triângulo (Ex 25), acrescentando a lógica
para mostrar que tipo de triângulo será formado:
EQUILÁTERO: todos os lados iguais
ISÓSCELES: dois lados iguais
ESCALENO: todos os lados diferentes
'''


comprimento1 = float(input("Digite o comprimento 1: "))
comprimento2 = float(input("Digite o comprimento 2: "))
comprimento3 = float(input("Digite o comprimento 3: "))

if comprimento1 + comprimento2 > comprimento3 and comprimento2 + comprimento3 > comprimento1 and comprimento1 + comprimento3 > comprimento2: 
    print("É possivel formar um triângulo! ")
    
    #Verificar se é equilátero(todos os lados são iguais)
    if comprimento1 == comprimento2 == comprimento3:
        print("É um triângulo equilátero !!")
    elif comprimento1 == comprimento2 or comprimento2 == comprimento3 or comprimento1 == comprimento3:
        print("É um triângulo isósceles !!")
    else:
        print("É um triângulo escaleno !!")
else: 
    print("Não é possível formar um triângulo! ")