n = input('Digite um número entre 0 a 9999: ')
s='000' + n
print('Unidade: {}'.format(s[-1]))
print('Dezena: {}'.format(s[-2]))
print('Centena: {}'.format(s[-3]))
print('Milhar: {}'.format(s[-4]))
