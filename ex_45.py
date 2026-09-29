'''
45 Refaça o exercício anterior de forma que ele funcione mesmo se o valor inicial
for maior que o valor final (fazendo uma contagem regressiva automática senecessário).
'''

valor_inicial = int(input("Digite o valor Inicial: "))
valor_final = int(input("Digite o valor final: "))
incremento = int(input("Digite o incremento de contagem: "))

#Proteger contra laços infinitos
if incremento <= 0:
    print("O incremento precisa ser um número positivo maior que zero!")
else:
    valor_atual = valor_inicial
    #Verificar qual número é maior
    if valor_inicial == valor_final:
        print("Os números são iguais !!")
    elif valor_atual < valor_final:
        while valor_atual <= valor_final:
            print(valor_atual, end=" ")
            valor_atual += incremento
    else:
        while valor_atual >= valor_final:
            print(valor_atual, end=" ")
            valor_atual -= incremento