#faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua area e a quantidade de tinta necessaria para pinta-lá. Sabendo que cada litro de
#tinta punta uma area de 2m²

largura = float(input('Informe a largura da parede:'))
altura = float(input('Informe a altura da parede:'))

metragem = largura * altura

qtd_tinta = metragem / 2

print('Metro quadrado = {}\nQuantidade de Tinta = {}'.format(metragem, qtd_tinta))
