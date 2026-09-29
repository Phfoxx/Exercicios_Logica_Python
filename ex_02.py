'''
Desenvolva um programa que receba o nome de uma pessoa através da
função input() e exiba uma mensagem de boas-vindas personalizada utilizando
f-strings.
'''
import os
nome = input("Digite seu nome: ")
os.system('clear')
print(f'Bem vindo {nome}')
