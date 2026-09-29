'''
22) Escreva um programa que leia o ano de nascimento de um rapaz e verifique sua situação em relação ao alistamento militar:
Se ele tiver menos de 18 anos, mostre quantos anos faltam para o alistamento. Se ele tiver mais de 18 anos, mostre quantos anos já se passaram do prazo.
'''
#Importar a biblioteca datetime para conseguir puxar o ano atual automaticamente
from datetime import date

#Constantes 
#Usa a biblioteca datetime para importar o ano atual direto do sistema operacional da máquina. 
ano_atual = date.today().year


print("VERIFICAÇÃO DE ALISTAMENTO")

ano_nascimento = int(input("Digite o seu ano de nascimento: "))
idade = ano_atual - ano_nascimento

#Verificar alistamento
if(idade < 18):
    print(f"\nNÃO PODE SE ALISTAR !! \nFaltam {18 - idade} anos, para poder se alistar.")
elif idade == 18:
    print('\nPODE SE ALISTAR !! \n Alistamento começa a partir desse ano.')

else: 
    print(f'\nPODE SE ALISTAR !! \nJá pode se alistar faz {idade - 18} ano(s)')