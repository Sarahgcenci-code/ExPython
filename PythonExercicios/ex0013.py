preco = (float(input('Qual é o preço do produto?R$')))
novo = preco-(preco*5/100)

print('O produto com o valor R${}, com desconto é: R${}'.format(preco, novo))