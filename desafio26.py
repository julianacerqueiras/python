#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e
# em que posição ela aparece a última vez

frase = str(input('Digite uma frase:')).upper().strip()

print('A frase contem {} letra(s) A!'.format(frase.count('A')))

print('Primeira posicição {}'.format(frase.find('A')+1))
print('Ultima posicição {}'.format(frase.rfind('A')+1))