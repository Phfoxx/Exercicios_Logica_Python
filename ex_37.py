'''
37) Reajuste Salarial Complexo: Leia o salário atual, o gênero do funcionário e o
tempo de casa. Calcule o novo salário:
- Mulheres: < 15 anos (+5%) | 15 a 20 anos (+12%) | > 20 anos (+23%)
- Homens: < 20 anos (+3%) | 20 a 30 anos (+13%) | > 30 anos (+25%)
'''

print("--- CALCULADORA DE REAJUSTE SALARIAL ---")
salario_atual = float(input("Digite seu salarial atual: R$"))
genero = int(input("Informe seu gênerero\n[1] Mulher/ [2] Homem\n- "))
tempo_de_casa = int(input("Informe quantos anos tem de empresa - "))

if genero == 1: 
    if tempo_de_casa < 15:
        aumento_salarial = salario_atual * 0.05
    elif tempo_de_casa <= 20:
        aumento_salarial = salario_atual * 0.12
    else:
        aumento_salarial = salario_atual * 0.23
elif genero ==2:
    if tempo_de_casa < 20:
        aumento_salarial = salario_atual * 0.03
    elif tempo_de_casa <= 30:
        aumento_salarial = salario_atual * 0.13
    else:
        aumento_salarial = salario_atual * 0.25
else:
    print("Opção invalida")


novo_salario = salario_atual + aumento_salarial

print(f"Seu salário terá o aumento de R${aumento_salarial:.2f}\n NOVO SALARIO - R${novo_salario:.2f}")