resp = 'S'
soma = quant = média = maior = menor = 0

while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N]')).upper().strip()
media = soma/quant
print('Você digitou {} números.'.format(quant))
print('A média é: {:.2f}'.format(media))
print('O maior número: {}, o menor número: {}'.format(maior, menor))
print('A soma dos números foi de: {}'.format(soma))


