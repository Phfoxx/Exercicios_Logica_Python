'''
15) Crie um programa que calcule o salário mensal de um funcionário com base no número de dias trabalhados, considerando uma carga horária de 8h/dia 
e um valor de R$25 por hora.
'''

#Definição de carga horária por dia
carga_horaria_dia = 8 

#Definição de salário por hora trabalhada
salario_hora_trabalhada = 15

#Solicitar a quantidade de dias trabalhados
quantidade_dias_trabalhados = int(input("Quantos dias foram trabalhados : "))

#Soma do salário 
salario_total = (carga_horaria_dia * salario_hora_trabalhada) * quantidade_dias_trabalhados

print(f"Salario Total: R${salario_total}")