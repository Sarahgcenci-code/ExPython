velocidade = float(input('Qual é a velocidade do seu carro?'))
multa=(velocidade-80)*7
if velocidade<80:
    print('Você está dirigindo bem, continue assim...')
else:
    print('Você foi multado! Excedeu o limite permitido que é de 80km/h.')
    print('Você deve pagar a multa de: R${:.2f}'.format(multa))