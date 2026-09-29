'''
34) O Índice de Massa Corpórea (IMC) é calculado pela expressão peso/altura2.
Crie um programa que leia o peso e a altura de uma pessoa e mostre sua
classificação:
Abaixo de 18.5: Abaixo do peso
Entre 18.5 e 25: Peso ideal
Entre 25 e 30: Sobrepeso
Entre 30 e 40: Obesidade
Acima de 40: Obesidade mórbida
'''

print("Calculador de IMC (Índice de Massa Corpórea)")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso/(altura**2)
situacao = ""

if imc < 18.5:
    situacao = "Abaixo do peso"
elif imc >= 18.5 and imc < 25:
    situacao = "Peso ideal"
elif imc >= 25 and imc < 30: 
    situacao = "Sobrepeso"
elif imc >= 30 and imc < 40:
    situacao = "Obesidade"
else:
    situacao = "Obesidade mórbida"

print(f"Seu IMC é {imc:.2f} e você está {situacao}")