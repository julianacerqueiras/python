#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite o seu nome completo:')).strip()
n = nome.split()

print('Primeiro nome {}:'.format(n[0]))
print('Ultimo nome {}:'.format(n[len(n)-1]))
