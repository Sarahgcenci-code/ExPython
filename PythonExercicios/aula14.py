'''for c in range (1,10):
    print(c)
print('fim')'''

'''c = 1 contador
while c < 10: Enquanto o contador for menor que 10
    print(c)
    c = c + 1 Ele entende que precisa somar c com +1
print('fim')'''

'''n = 1
while n != 0:
    condição de parada
    n = int(input('Digite um número: '))
print('fim')'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')'''

''' par = impar = 0 ( as variaveis par e impar recebem zero'''
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print('Você digitou {} números pares e {} números ímpares.'.format(par, impar))