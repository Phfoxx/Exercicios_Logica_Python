'''
26) Escreva um algoritmo que leia dois números inteiros e compare-os, exibindo
uma das mensagens:
"O primeiro valor é o maior"
"O segundo valor é o maior"
"Não existe valor maior, os dois são iguais"
'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print("O primeiro número é maior")
elif n2 > n1:
    print("O segundo número é maior")
else:
    print("Os número são iguais ")