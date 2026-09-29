'''
17) Escreva um programa que pergunte a velocidade de um carro. Se ultrapassar80 km/h, exiba uma mensagem dizendo que o usuário foi multado. O programa
deve calcular e exibir o valor da multa, cobrando R$5.00 por cada km acima do limite.
'''

limite_da_via = 80
velocidade_carro = float(input("Digite a velocidade do carro: "))
Velocidade_acima_do_limite = velocidade_carro - limite_da_via

if velocidade_carro > limite_da_via:
    valor_multa = Velocidade_acima_do_limite * 5 
    print(f"MULTA!! \nValor de R${valor_multa:.2f}")
else : 
    print("Não foi multado!")