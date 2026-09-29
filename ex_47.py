'''
47) Desenvolva um aplicativo que calcule o resultado da expressão regressiva: 
500 + 450 + 400 + ... + 0.
'''

numero_atual = 500
numero_final = 0 
soma_total = 0 

while numero_atual >= numero_final:
    if numero_atual > numero_final:
        print(f"{numero_atual} + ", end="")
    else:
        print(numero_atual)
    soma_total += numero_atual
    numero_atual -= 50
print(f"A soma dos valores é {soma_total}")