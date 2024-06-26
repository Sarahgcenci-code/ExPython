from random import randint
computador = randint(0,10)
print('Seu computador pensou em um número entre 0 e 10.')
print('Adivinhe o número!')
acertou = False
palpites = 0
while not acertou:
    jogador=int(input('Número escolhido:'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('MAIS!')
        elif jogador > computador:
            print('MENOS!')
print('Acertou!')
print('Total de tentativas: {}'.format(palpites))