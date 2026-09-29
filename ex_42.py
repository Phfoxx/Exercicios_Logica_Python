'''
42 Faça um algoritmo que solicite ao usuário um número inteiro positivo e mostre uma contagem de 1 até o valor digitado.
'''

numero_positivo = False
cont = 1
while numero_positivo == False:
    numero_usuario = int(input("Informe um número inteiro e positivo:" ))
    if numero_usuario < 0: 
        print("\n Informe um número positivo !! \n")
        continue
    else:
        print(f"Contagem até o número {numero_usuario}")
        while cont <= numero_usuario:
            print(cont, end=" ")
            cont+=1
        numero_positivo = True
