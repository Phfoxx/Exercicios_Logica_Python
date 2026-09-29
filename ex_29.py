'''
29) Escreva um programa que leia o nome, o salário e o tempo de empresa (em
anos) de um funcionário. Calcule o reajuste salarial conforme a tabela:
    Até 3 anos de empresa: aumento de 3%
    Entre 3 e 10 anos: aumento de 12.5%
    10 anos ou mais: aumento de 20%
'''

nome = input("Infome seu nome: ")
salario = float(input("Informe seu salário: "))
tempo_empresa = int(input("Informe quantos anos está na empresa: "))

if tempo_empresa <= 3:
    valor_aumento= 0.03 * salario
elif tempo_empresa < 10:    
    valor_aumento = 0.125 * salario
else:
    valor_aumento = 0.20 * salario

print(f"Olá {nome}\nSeu novo salário é R$ {(salario + valor_aumento):.2f} ")
