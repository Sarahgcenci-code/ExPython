preço = float(input('Valor do produto: '))
print('Informe qual será a forma de pagamento: ')
print('Opção 1: Dinheiro/cheque')
print('Opção 2: Á vista no cartão')
print('Opção 3: 2x no cartão')
print('Opção 4: 3x ou mais no cartão')
opção = int(input('Opção escolhida: '))

if opção == 1:
    promo = preço - (preço * 10/100)
    print('O valor do produto será de: R${:.2f}'.format(promo))
elif opção == 2:
    promo = preço - (preço * 5/100)
    print('O valor do produto será de: R${:.2f}'.format(promo))
elif opção == 3:
    parcela= preço / 2
    print('Sua compra será parcelada x2 de R${:.2f}, cada parcela será de: {}'
          .format(preço,parcela))
elif opção == 4:
    total = preço + (preço * 20/100)
    totalparcelas = int(input('Quantas parcelas?'))
    parcela = total / totalparcelas
    print('Sua compra de R${:.2f} vai custar {:.2f}, parcelado em {} vezes'.format(preço,total,totalparcelas))
    print('Valor da parcela por mês: {}'.format(parcela))
else:
    print('Opção inválida.')
    print('A sua compra será de {}'.format(preço))