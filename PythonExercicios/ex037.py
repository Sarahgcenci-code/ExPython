n = int(input('Digite um número: '))
print('''Escolha uma das bases para conversão: 
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para binário é igual a {}'.format(n,bin(n)))
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(n,oct(n)))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(n,hex(n)))
else:
    print('Opção inválida.')