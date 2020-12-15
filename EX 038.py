print ('''EX 038 – Escreva um programa que leia dois números inteiros e os compare mostrando na tela a seguinte mensagem:
O primeiro valor é maior.
O segundo valor é maior.
Não existe valor maior, os dois são iguais.''')
x = int (input ('Digite um número: '))
y = int (input ('Digite outro número: '))
if x > y:
    print ('O 1° valor é maior')
if x < y:
    print ('O 2° valor é maior')
if x == y:
    print ('Não existe valor maior, os dois são iguais')