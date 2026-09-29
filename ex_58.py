'''
58) Faça um algoritmo que leia a idade de vários alunos de uma turma. O programa deve parar imediatamente quando a idade 999
    for digitada. No final, exiba:
        Quantos alunos existem na turma.
        Qual é a média de idade do grupo (desconsiderando o 999.
'''

qtd_alunos = 0 
soma_idade_alunos = 0 
cont = 1

while True:
    idade_aluno = int(input(f"Digite a idade do aluno {cont}: "))
    if idade_aluno == 999:
        break
    else:
        soma_idade_alunos += idade_aluno
        qtd_alunos += 1
    cont += 1 
media_alunos = soma_idade_alunos / qtd_alunos
print(f"Quantidade de alunos: {qtd_alunos}\nMédia de idade dos alunos: {media_alunos:.2f}")