a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
#verificar quem é menor:
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

print('O menor valor digitado é: {}'.format(menor))

#verificar quem é maior:

maior = a
if a > b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor digitado é: {}'.format(maior))
