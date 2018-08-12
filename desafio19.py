#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

aluno01 = str(input("Nome do aluno 01:"))
aluno02 = str(input("Nome do aluno 02:"))
aluno03 = str(input("Nome do aluno 03:"))
aluno04 = str(input("Nome do aluno 04:"))

lista = [aluno01, aluno02, aluno03, aluno04]
sortudo = choice(lista)

print("Aluno(a) escolhido(a) para apagar o quadro foi: {}".format(sortudo))