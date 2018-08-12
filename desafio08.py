#escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

valor = int(input('Informe o tamanho em metros:'))

cm = valor * 100
mm = valor * 1000

print('Centimetro = {}cm \nMilimetro = {}mm'.format(cm, mm))

