'''
49 Faça um algoritmo que leia 6 números inteiros e, ao final, exiba quantos deles são PARES e quantos são ÍMPARES.
'''

cont = 1
numero_par = 0
numero_impar = 0
while cont <= 6: 
    numero_atual = int(input("Digite um número: "))
    
    if numero_atual % 2 == 0:
        numero_par += 1
    else:
        numero_impar += 1
    cont+=1
print(f"Foram digitados {numero_par} números pares e {numero_impar} número impares.")
