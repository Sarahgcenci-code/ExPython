frase= str(input('Digite sua frase: ')).upper().strip()
print('A frase aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')))
