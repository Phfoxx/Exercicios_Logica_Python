'''
21) Desenvolva uma lógica que leia um ano qualquer e informe se ele é
BISSEXTO. 
Dica pedagógica: Lembre os alunos que um ano é bissexto se for divisível por 4
e não por 100, ou se for divisível por 400.
'''

print("------ BISSEXTO ? ------")
ano = int(input("DIGITE O ANO -> "))

bissexto = (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0)

if bissexto:
    print(f"O ano {ano} é um ano BISSEXTO")
else:
    print(f"O ano {ano} NÃO é ano BISSEXTO")