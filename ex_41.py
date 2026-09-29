'''
41 Desenvolva um programa que mostre uma contagem decrescente de 5 em 5 
100 95 90 85 ... 0 Acabou!
'''

cont = 100

while cont >= 0: 
    print(cont, end=" ")
    cont -= 5 
print("Acabou !!")