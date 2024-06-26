n1 = int(input('Primeiro Segmento: '))
n2 = int(input('Segundo Segmento: '))
n3 = int(input('Terceiro Segmento: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos podem formar um triângulo ',end='')
    if n1 == n2 == n3:
        print('EQUILÁTERO')
    elif n1 != n2 != n3 != n1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('não forma triângulo')