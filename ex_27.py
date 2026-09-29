'''
27) Crie um programa que leia duas notas de um aluno e calcule a sua média. Ao
final, exiba uma mensagem baseada na média atingida:
Média até 4.9: REPROVADO
Média entre 5.0 e 6.9: RECUPERAÇÃO
Média 7.0 ou superior: APROVADO
'''

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1 + nota2) / 2

if media < 5.0:
    print(f" Sua média foi {media:.2f}\n STATUS: REPROVADO")
elif media < 7:
    print(f" Sua média foi {media:.2f}\n STATUS: RECUPERAÇÃO")
else:
    print(f" Sua média foi {media:.2f}\n STATUS: APROVADO")