from random import randint
from time import sleep
pc = randint(0,5)
print('Pensei no número.')
player = int(input('Em que número eu pensei? '))
print('prosessando...')
sleep(2)
if player == pc:
    print('numero correto')
else:
    print('Vc errou')