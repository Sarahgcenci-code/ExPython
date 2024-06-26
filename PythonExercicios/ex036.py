valorcasa = float(input('Valor da casa: R$'))
salario = float(input('Qual é o salário do comprador: R$'))
ano = int(input('Quantos anos você irá pagar?'))

prestação = valorcasa / (ano*12)
minimo = salario * 30 / 100

if prestação > minimo:
    print('Para pagar a casa de {:.2f} em {} anos a '
          'prestação será de R${:.2f}'.format(valorcasa,ano,prestação))
    print('Empréstimo negado.')
elif prestação <= minimo:
    print('Para pagar a casa de R${:.2f} em {} anos a '
          'prestação será de R${:.2f}.'.format(valorcasa,ano,prestação))
    print('Empréstimo pode ser feito')
