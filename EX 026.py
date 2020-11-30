print ('''EX 026. Faça um programa que leia uma frase pelo teclado e mostre: 
Quantas vezes aparece a letra ‘A’ Em que posição ela aparece a primeira vez Em que posição ela aparece a última vez''')
n = str(input('Digite uma frase: ')).strip().lower()
print ('A frase {} tem {} letras "a"'. format (n, (n.count('a'))))
print ('A primeira letra "a" é encontrada na posição {}'.format(n.find('a')))
print ('A ultima letra "a" é encontrada na posição {}'.format(n.rfind('a')))