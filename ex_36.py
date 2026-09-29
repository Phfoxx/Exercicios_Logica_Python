'''
36) Programa de Vida Saudável: Um sistema de pontos por atividade física
funciona assim:
    Até 10h de atividade no mês: 2 pontos por hora
    De 10h até 20h no mês: 5 pontos por hora
    Acima de 20h no mês: 10 pontos por hora
Calcule o total de pontos e o prêmio em dinheiro, sabendo que cada ponto vale
R$0,05.
'''

print("--- PROGRAMA VIDA SAUDÁVEL ---")
print("Regras de pontos:\n - Até 10h de atividade no mês = 2 pontos por hora\n - De 10h até 20h no mês: 5 pontos por hora\n - Acima de 20h no mês: 10 pontos por hora")
print("(Cada ponto equivale a R$0.05)")
horas_de_atividade = int(input("-Informe quantas horas de exercicio fez no mês: "))
if horas_de_atividade <= 10:
    pontos_totais = horas_de_atividade * 2
elif horas_de_atividade <= 20:
    pontos_totais = horas_de_atividade * 5
else:
    pontos_totais = horas_de_atividade * 10

print(f"Você acumulou {pontos_totais} pontos e irá receber R${pontos_totais*0.05:.2f}")