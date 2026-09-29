'''
28) Desenvolva um programa que leia a largura e o comprimento de um terreno
retangular e calcule a sua área (m2). O programa deve classificar o terreno:
Abaixo de 100m2: TERRENO POPULAR
Entre 100m2 e 500m2: TERRENO MASTER
Acima de 500m2: TERRENO VIP
'''


print("** PARA O CÓDIO FUNCIONAR É NECESSARIO FORNECER A LARGURA E COMPRIMENTO DE UM TERRENO RETANGULAR.\n EX: \n-Largura = 30 \n-Comprimento = 40\n")
largura1 = float(input("Digite a Largura: "))
comprimento1 = float(input("Digite o Comprimento: "))

#Calcular a diagonal do retângulo. 
diagonal = ((largura1**2) + (comprimento1**2))** (1/2) #O **(1/2) server para calcular a raiz quadrada manualmente

#Verificar se é um retângulo
if largura1**2 + comprimento1**2 == diagonal**2: 
    #Calcular área
    area = comprimento1 * largura1
    if area < 100: 
        print(f"Seu terreno tem {area} metros quadrados.\nEle está classificado como: TERRENO POPULAR ")
    elif area <= 500: 
        print(f"Seu terreno tem {area} metros quadrados.\nEle está classificado como: TERRENO MASTER ")
    else: 
        print(f"Seu terreno tem {area} metros quadrados.\nEle está classificado como: TERRENO VIP")

else:
    print("Não é um retângulo !!")



