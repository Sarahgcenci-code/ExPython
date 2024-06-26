salario = float(input('Qual o seu salário?'))
if salario <= 1.250:
    print('Seu salário aumentou para: {:.2f}'.format(salario * (15/100)+salario))
else:
    print('Seu salário aumentou para: {:.2f}'.format(salario * (10/100)+salario))