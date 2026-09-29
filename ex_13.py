'''
13) Faça um algoritmo que leia o salário de um funcionário e calcule o seu novo
salário com um aumento de 15%.
'''

salario = float(input("Digite seu salário: "))

#Porcentagem do aumento
porcentagem_aumento = 15

#Calculo aumento
novo_salario = ((porcentagem_aumento / 100) * salario) + salario

#Exibição do novo salário 
print(f"Novo salario com aumento de {porcentagem_aumento}% -> {novo_salario}")