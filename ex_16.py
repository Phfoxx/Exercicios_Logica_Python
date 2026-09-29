'''
16) [DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e há quantos
anos ele fuma. Considere que cada cigarro reduz 10 minutos de vida. Calcule o total de dias perdidos e exiba o resultado
'''
#CONSTANTES: Minutos perdidos e dias no ano
minutos_perdidos_por_cigarro = 10
dias_no_ano = 365 

#Solicitar a quantidade de cigarro é fumado por dia
quantidade_de_cigarros_por_dia = int(input("Quantos cigarros você fuma por dia ? \n"))

#Solicitar a quantidade de anos que o usúario fuma
anos_fumando = int(input("A quantos anos você fuma? "))

#Quantidade de cigarro fumados na vida
total_de_cigarros_fumados = quantidade_de_cigarros_por_dia * (dias_no_ano * anos_fumando)

#Conersão dos valores: 1- Calcular quantos minutos foram perdidos 2- transformar os minutos em horas 3- Transformar as horas em dias
minutos_perdidos = minutos_perdidos_por_cigarro * total_de_cigarros_fumados
horas_perdidas = minutos_perdidos / 60 
dias_perdidos = horas_perdidas / 24


print(f"Dias Perdidos: {dias_perdidos:.0f}")