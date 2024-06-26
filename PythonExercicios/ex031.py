distancia = int(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar a sua viagem de {}km.'.format(distancia))
if distancia<=200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O preço da sua viagem será R${:.2f}'.format(preco))

