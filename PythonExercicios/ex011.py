dinheiro = (float(input('Quanto você tem na carteira?R$')))
dolar= dinheiro / 5.10
euro = dinheiro/5.56
ARS = dinheiro/ 0.0058
print ('Com R${} você pode comprar US{:.2f}'.format(dinheiro,dolar))
print('Com R${} você pode comprar EUR{:.2f}'.format(dinheiro, euro))
print ('Com R${} você pode comprar ARS{:.2F}'.format(dinheiro, ARS))
