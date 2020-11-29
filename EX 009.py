print ('EX 009. Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada')
x = int (input ('Digite um número para ver sua tabuada: '))
for c in range (11):
    print (f'{x} x {c} = {x*c}')
