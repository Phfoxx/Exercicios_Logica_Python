'''
20) Faça um programa que receba um número inteiro e utilize o operador de resto
da divisão ( % ) para determinar e exibir se o número é PAR ou ÍMPAR.
'''

print("------ PAR OU ÍMPAR ------")
numero = int(input("Digite um número: "))

if numero % 2 > 0: 
    print(f"O número {numero} é IMPAR")
else:
    print(f"O número {numero} é PAR")