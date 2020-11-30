print ('''EX 028. Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e 
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu.''')
from random import randint
com = randint(1,5)
x = int (input ('Tente adivinhar o número que escolhi de 1 a 5: '))
if com == x:
    print (f'Acertou, escolhi o número {com}')
else:
    print (f'Errou, escolhi o número {com}')