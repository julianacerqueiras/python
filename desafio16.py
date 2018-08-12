#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math

num = float(input('Digite um numero:'))

inteiro = math.floor(num)

print('O número {} tem parte inteira: {}'.format(num, inteiro))