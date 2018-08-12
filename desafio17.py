#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math

co = float(input('Valor do cateto oposto:'))
ca = float(input('Valor do cateto adjacente:'))
h = math.hypot(co, ca)
print('A hipotenusa do triângulo é = {}'.format(h))

