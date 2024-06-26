nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2
if media <= 5:
    print('REPROVADO')
    print('A média de {} e {} resulta em: {}'.format(nota1,nota2,media))
elif media >=5 and media <7:
    print('RECUPERAÇÃO')
    print('A média de {} e {} resulta em: {}'.format(nota1,nota2,media))
elif media > 7:
    print('APROVADO')
    print('A média de {} e {} resulta em: {}'.format(nota1,nota2,media))
