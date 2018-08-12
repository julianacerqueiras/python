#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

frase = int(input('Digite um numero entre 0 e 9999: '))
num = str(frase)

print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milha: {}'.format(num[0]))