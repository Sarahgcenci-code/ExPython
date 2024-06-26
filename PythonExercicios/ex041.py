'''Exercício Python 041:
A Confederação Nacional de Natação precisa de um
programa que leia o ano de nascimento de um atleta e
mostre sua categoria, de acordo com a idade'''

from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual-ano

if idade <= 9:
    print('A sua categoria é MIRIM.')
elif idade <= 14:
    print('A sua categoria é INFANTIL.')
elif idade <= 19:
    print('A sua categoria é JÚNIOR')
elif idade <=25:
    print('A sua categoria é SÊNIOR')
else:
    print('A sua categoria é MASTER')
print('O(A) atleta tem {} anos'.format(idade))
