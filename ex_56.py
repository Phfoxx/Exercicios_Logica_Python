'''
56) Crie um programa que utilize um laço while para ler vários números inteiros pelo teclado. 
O programa deve somar todos os valores digitados e exibir o total apenas no final.

    Condição de parada: O programa deve ser interrompido quando o usuário digitar o número 1111 
    (este valor não deve entrar na soma)
'''

soma_numeros = 0 
saida = 0

while True:
    numero_atual = int(input("Digite um número inteiro: "))
    if numero_atual == 1111:
        break
    else:
        soma_numeros += numero_atual
    
print(f"A soma dos números digitados é {soma_numeros}")
