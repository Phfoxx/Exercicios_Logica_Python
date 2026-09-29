'''
19) Desenvolva um algoritmo que leia o nome e duas notas de um aluno, calcule a
média e a exiba. Ao final, utilize uma estrutura condicional para verificar se a
média foi maior ou igual a 7.0. Se sim, mostre que o aluno teve um "Bom
Aproveitamento"; caso contrário, mostre "Abaixo da Média".
'''

nome = input("Digite seu nome: ")
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
media = (n1 + n2) / 2

print("------AVALIAÇÃO DE APROVEITAMENTO------")
print(f"ALUNO: {nome}")
print(f"MÉDIAS DE NOTAS: {media}")
if(media >= 7):
    print(f"APROVEITAMENTO: ACIMA DA MÉDIA")
else: 
    print(f"APROVEITAMENTO: ABAIXO DA MÉDIA")   