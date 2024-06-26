from random import randint
v = 0
while True:
    player = int(input('Diga um valor: '))
    pc = randint(0,10)
    tot = player + pc
    tipo=' '
    while tipo not in 'PI':
        tipo=str(input('Par ou Ímpar? [p/i]')).strip().upper()[0]
    print(f'Você jogou {player} e o computador jogou {pc}')
    if tipo == 'P':
        if tot %2 == 0:
            print('Você venceu')
            v += 1
        else:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if tot %2 == 1:
            print('Você perdeu')
            break
    print('Vamos jogar de novo?')
print(f'Você venceu {v} vezes')