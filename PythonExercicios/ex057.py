s = str(input('Digite o sexo: ')).upper()[0].strip()
while s not in 'MmFf':
    s = str(input('Dados inválidos, informe novamente: ')).strip().upper()[0]
print('Sexo {} registrado.'.format(s))