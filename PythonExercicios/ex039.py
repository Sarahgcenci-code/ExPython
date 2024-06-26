from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual-nasc

print('Quem nasceu em {} tem {} anos em 2024.'.format(nasc,idade,atual))
if idade == 18:
    print('Você precisa se alistar imediatamente.')
elif idade < 18:
    print('Ainda faltam {} anos para o seu alistamento.'.format(18 - idade))
    print('Seu alistamento irá acontecer no ano de: {}'.format(atual + (18 - idade)))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
    print('Seu alistamento foi no ano de {}'.format(2024 - (idade - 18)))