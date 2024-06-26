n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção: int = 0
while opção != 5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR QUE
    [4] NOVOS NÚMEROS
    [5] SAIR''')
    opção = int(input('Qual é a sua opção?'))
    if opção == 1:
        n3 = n1 + n2
        print('{} + {} = {}'.format(n1,n2,n3))
    elif opção == 2:
     n4 = n1 * n2
     print('{} x {} = {}'.format(n1,n2,n4))
    elif opção == 3:
        if n1 > n2:
            print('Entre {} e {}, {} é maior'.format(n1,n2,n1))
        else:
            print('Entre {} e {}, {} é maior'.format(n1,n2,n2))
    elif opção == 4:
        n1 = int(input('Primeiro novo número: '))
        n2 = int(input('Segundo novo número: '))
else:
    print('Opção inválida.')
print('Fim do programa.')