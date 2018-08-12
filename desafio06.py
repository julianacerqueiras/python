#crie um algoritimo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Informe um número:'))

d = num * 2
t = num * 3
r = num ** (1/2)

print(' Dobro = {}, Triplo = {}, Raiz = {:.3f}'.format(d, t, r))