from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint (0,2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
player = int(input('Qual a sua jogada?'))
print('O computador jogou {}'.format(itens[pc]))
print('O jogador jogou {}'.format(itens[player]))
if pc == 0:
    if player == 0:
        print('empate')
    elif player == 1:
        print('jogador vence')
    elif player == 2:
        print('jogador perde')
    else:
        print('jogada inválida.')
elif pc == 1:
    if player == 0:
        print('pc vence')
    elif player == 1:
        print('empate')
    elif player == 2:
        print('jogador vence')
    else:
        print('jogada inválida.')
elif pc == 2:
    if player == 0:
        print('jogador vence')
    elif player == 1:
        print('pc vence')
    elif player == 2:
        print('empate')
    else:
        print('jogada inválida.')
