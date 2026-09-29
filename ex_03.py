'''
Crie um programa que leia o nome e o salário de um funcionário. No final, exiba
uma frase formatada. O salário deve ser tratado como um valor de ponto flutuante
( float ) e exibido com duas casas decimais.
'''

import os

nome_funcionario = input('Digite seu nome: ')
salario_funcionario = float(input('Digite seu salário: '))
os.system('clear')

print('--- INFORMAÇÕES FUNCIONARIOS ---')
print(f' FUNCIONARIO: {nome_funcionario}\n SALARIO: {salario_funcionario:.2f}')