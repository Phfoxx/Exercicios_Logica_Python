'''
46) Escreva um programa que calcule e exiba o somatório de: 6 + 8 + 10 + ... +100.
'''
numero_final = 100
numero_atual = 6
soma_total = 0

while numero_atual <= numero_final:
    if numero_atual < numero_final:
        print(f"{numero_atual} + ", end="")
    
    else: 
        print(f"{numero_atual}", end="")
    soma_total = soma_total + numero_atual
    numero_atual += 2
print(f"\nA soma de todos os valores é {soma_total}")