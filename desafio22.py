#Crie um programa que leia o nome completo de uma pessoa e mostre
#O nome com todas as letras maiúsculas e minúsculas
#Quantas letras ao todo sem considerar espaços
#Quantas letras tem o primeiro nome

nome = str(input('Digite o seu nome completo:'))

print('Letras Maiusculas: {}'.format(nome.upper()))
print('Letras Minusculas: {}'.format(nome.lower()))
print('Quantidade de Letras: {}'.format(len(nome) - nome.count(' ')))
print('Quantidade de Letras Primeiro nome: {}'.format(nome.find(' ')))

