#faça um algoritimo que leia o preço de um produto e mostra seu novo preço, com 5% de desconto

preco = float(input('Informe o valor do produto:'))

desconto = preco - (preco * 5 / 100)


print('Valor sem desconto {:.2f}\nValor com desconto {:.2f}'.format(preco, desconto))