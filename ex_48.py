'''
48 Crie um programa que use um laço para ler 7 números inteiros e, ao final,
mostre o somatório entre eles.
'''

soma_total = 0 
cont = 1 
numero_digitados = []
while cont <= 7: 
    numero_atual = int(input("Digite um número inteiro: "))
    numero_digitados.append(numero_atual)
    soma_total += numero_atual
    cont += 1

print("A soma dos números: ", end="")
resultado = " + ".join(str(num) for num in numero_digitados)
print(resultado)
print(f"É igual a {soma_total}")