#programa que leia o nome de uma pessoa e mostre:
#nome com todas maiusculas
#nome com todas minusculas
#quantas letras tem no nome sem considerar espaços
#quantas letras tem o primeiro nome

nome = str(input('Qual o seu nome?')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome)-nome.count(' '))
dividido = nome.split()
print(dividido[0])
print(len(dividido[0]))