'''
60) Desenvolva um algoritmo que leia o nome, a idade e o sexo de várias pessoas. 
    O programa deve oferecer a opção de continuar ou parar após cada leitura. Ao final, apresente:
    a) O nome da pessoa mais velha.
    b) O nome da mulher mais jovem.
    c) A média de idade de todo o grupo.
    d) Quantos homens têm mais de 30 anos.
    e) Quantas mulheres têm menos de 18 anos.
'''

continuar = True
idade_pessoa_mais_velha = 0
idade_mulher_mais_jovem = 0

while continuar == True: 
    nome_atual = input("Digite seu nome: ")
    idade_atual = int(input("Digite sua idade"))
    sexo_atual = input("Digite seu sexo [M/H]: ").upper()


    #a) O nome da pessoa mais velha.
    if idade_pessoa_mais_velha == 0: 
        idade_pessoa_mais_velha = idade_atual
    else:
        if idade_atual > idade_pessoa_mais_velha:
            idade_pessoa_mais_velha = idade_atual

    #b) O nome da mulher mais jovem.
    if sexo_atual == 'M':
        if idade_mulher_mais_jovem == 0:
            idade_mulher_mais_jovem = idade_atual
        else:
            if idade_atual < idade_mulher_mais_jovem:
                idade_mulher_mais_jovem == idade_atual
    elif sexo_atual == "H":

    else:
        continue

    soma_idades += idade_atual 

    pergunta = int(input("Presione 1 para continuar."))
    