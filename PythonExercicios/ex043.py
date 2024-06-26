'''Desenvolva uma lógica que leia
o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status'''

peso = float(input('Peso: '))
altura = float(input('Altura: '))
imc= peso / (altura**2)

if imc < 18.5:
    print('Abaixo do peso ideal.')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal.')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida.')
print('IMC: {:.1f}'.format(imc))
print('Fim do programa.')