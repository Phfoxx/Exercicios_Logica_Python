'''
43 Desenvolva um algoritmo que mostre uma contagem regressiva de 30 até 1.
No entanto, se o número for divisível por 4, ele deve aparecer entre colchetes.
Ex: 30 29 [28] 27 ...
'''
cont = 30

while cont >= 1: 
    if cont % 4 == 0:
        print(f"[{cont}]", end=" ")
    else:
        print(cont, end=" ")
    cont -= 1