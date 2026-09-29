'''
12) Crie um script que aplique um desconto de 5% sobre o preço de um produto e
exiba o novo valor promocional.
'''
desconto = 0.05
preco_produto = float(input("Digite o valor do produto: "))
preco_com_desconto = preco_produto - (preco_produto * desconto )

print(f'\n VALOR ORIGINAL : R${preco_produto:.2f}\n VALOR COM DESCONTO: R${preco_com_desconto:.2f} ')