primeiro=int(input('Primeiro termo: '))
razao= int(input('Razão: '))
for c in range(primeiro,10,razao):
    print('{} '.format(c), end=' ')