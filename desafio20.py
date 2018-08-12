#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

aluno01 = str(input("Nome do aluno 01:"))
aluno02 = str(input("Nome do aluno 02:"))
aluno03 = str(input("Nome do aluno 03:"))
aluno04 = str(input("Nome do aluno 04:"))

lista = [aluno01, aluno02, aluno03, aluno04]
shuffle(lista)

print("Aluno(a) escolhido(a) para apagar o quadro foi: {}")
print(lista)