from random import choice
n1 = input('Primeiro aluno(a): ')
n2 = input('Segundo aluno(a): ')
n3 = input('Terceiro aluno(a): ')
n4 = input('Quarto aluno(a): ')
lista = [n1,n2,n3,n4]
escolhido = choice(lista)
print('O aluno(a) escolhido foi: {}'.format(escolhido))