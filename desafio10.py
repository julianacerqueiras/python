#faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Doláres ela pode comprar. considere u$$1,00 = R$3,27

carteira = float(input('Saldo da carteira? R$'))

dolar = 3.27

conversao = carteira / dolar

print('Valor convertido em dolar U$${}'.format(conversao))