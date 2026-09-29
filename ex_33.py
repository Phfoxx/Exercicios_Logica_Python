'''
33) Aprovação de Empréstimo: Escreva um programa para avaliar um empréstimo bancário. 
Pergunte o valor da casa, o salário do comprador e emquantos anos ele pretende pagar. Calcule a prestação mensal, sabendo que ela 
não pode exceder 30% do salário, caso contrário, o empréstimo será negado.
'''



import os
import platform

#Verificar o sistema operacional 
sistema = platform.system()

def limparTela():
    if sistema == "Windows":
        os.system("cls")
    else: 
        os.system("clear")

salario_comprador = float(input("Digite o seu salário: "))

valor_emprestimo = float(input("Digite o valor da casa: "))
anos_para_pagamento = int(input(f"Em quantos anos deseja pagar o valor de {valor_emprestimo:.2f}: "))

#Converter os anos em meses
meses_para_pagamento = anos_para_pagamento * 12 

prestacao_mensal = valor_emprestimo / meses_para_pagamento

limparTela()

if prestacao_mensal <= salario_comprador * 0.30:
    print("Empréstimo aprovado !!")
else:
    print("Empréstimo negado !!")