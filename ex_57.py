'''
    57 Desenvolva um aplicativo que leia o salário e o sexo de vários funcionários.
    Ao final, mostre o total de salários pagos aos homens e o total pago às mulheres.
        Controle de fluxo: A cada funcionário cadastrado, o programa deve perguntar:
        "Deseja continuar? S/N". O loop só para se a resposta for "N".
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


sair = False
total_salario_homens = 0
total_salario_mulheres = 0

while sair == False: 
    salario = float(input("Digite seu salário: "))
    sexo_valido = False
    while sexo_valido == False:
        sexo = input("Informe seu sexo[H/M]").upper()
        if sexo == "H":
            total_salario_homens += salario
            sexo_valido = True
        elif sexo == "M":
            total_salario_mulheres += salario
            sexo_valido = True
        else: 
            print("Sexo invalido !! Coloque apenas H (Homen) ou M (Mulher).")
            continue
    


    pergunta = input("Deseja continuar? S/N\n ->").upper()

    if pergunta == "N":
        sair = True

limparTela()
print("-- RESULTADOS --")
print(f"O salário total dos funcionarios homens é R${total_salario_homens:.2f}")
print(f"O salário total das funcionarias mulheres é RS{total_salario_mulheres:.2f}")

    