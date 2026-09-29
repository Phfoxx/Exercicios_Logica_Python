'''
44 Crie um script que peça o valor inicial, o valor final e o incremento de uma contagem. O programa deve exibir todos os valores no intervalo.
'''
valor_inicial = int(input("Digite o valor Inicial: "))
valor_final = int(input("Digite o valor final: "))
cont = int(input("Digite o incremento de contagem: "))

#Proteger contra laços infinitos
if cont <= 0:
    print("O incremento precisa ser um número positivo maior que zero!")
else:
    #Verificar qual número é maior
    if valor_inicial == valor_final:
        print("Os números são iguais !!")
    elif valor_inicial <= valor_final:
        while valor_inicial <= valor_final:
            print(valor_inicial, end=" ")
            valor_inicial += cont
    else:
        while valor_inicial >= valor_final:
            print(valor_inicial, end=" ")
            valor_inicial -= cont
