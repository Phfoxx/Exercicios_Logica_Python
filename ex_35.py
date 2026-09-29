'''
35) Aluguel de Carros: Uma locadora cobra R$90/dia por carros populares e
R$150/dia por carros de luxo. Além disso, há uma taxa por Km rodado:

Carros Populares: Até 100Km: R$0,20/Km | Acima de 100Km: R$0,10/Km
Carros de Luxo: Até 200Km: R$0,30/Km | Acima de 200Km: R$0,25/Km

Faça um programa que leia o tipo de carro, os dias de aluguel e os Km
percorridos, exibindo o preço final.
'''
import os
import platform
#Verificar o sistema operacional 
sistema = platform.system()

def limparTela():
    if sistema == "Windows":
        os.system("cls")
    else: 
        os.system("clear")

#Valor diárias
carro_popular = 90
carro_luxo = 150 

entrada_invalida = True

while entrada_invalida:
    print("Informe o tipo de carro:")
    tipo_de_carro = int(input("[1] Popular\n[2] Luxo\n->"))
    entrada_invalida = tipo_de_carro != 1 and tipo_de_carro != 2
    if entrada_invalida:
        limparTela()
        print("ENTRADA INVÁLIDA, DIGITE APENAS 1 OU 2!!")

dias_alugados = int(input("Informe os dias de alugel: "))
km_percorridos = float(input("Digite os Kms Percorridos: "))

if tipo_de_carro == 1:
    tipo_de_carro = "Popular"
    if km_percorridos <= 100:
        valor_total = dias_alugados * carro_popular + km_percorridos * 0.20
    else:
         valor_total = dias_alugados * carro_popular + km_percorridos * 0.10
else:
    tipo_de_carro = "Luxo"
    if km_percorridos <= 200:
        valor_total = dias_alugados * carro_luxo + km_percorridos * 0.30
    else:
         valor_total = dias_alugados * carro_luxo+ km_percorridos * 0.25

print("--- VALOR TOTAL---")
print(f"TIPO DE CARRO - {tipo_de_carro}\nDIAS ALUGADOS - {dias_alugados}\nKM PERCORRIDOS - {km_percorridos}")
print(F"VALOR - R${valor_total:.2f}")