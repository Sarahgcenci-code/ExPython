from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input('Em que ano a pessoa nasceu? '.format(pess)))
    idade=atual - nasc
    if idade>=19:
        totmaior +=1
    else:
        totmenor+=1
print('Tem {} pessoas maiores de idade e {} pessoas menores de idade'.format(totmaior, totmenor))