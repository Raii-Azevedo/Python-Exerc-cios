print ('EX 006. Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada')
# UTILIZANDO MÉTODO MATEMÁTICO:
x = int (input ('Digite um número: '))
print (f'O dobre do {x} é {x*2}')
print (f'O triplo de {x} é {x*3}')
print (f'A raiz quadrada de {x} = {x**(1/2)}')

# UTILIZANDO FUNCIONALIDADES DO PYCHARM!
print ('')
import math
x = int (input ('Digite um número: '))
print (f''' O dobro de {x} é {x*2}
O triplo de {x} é {x*3}
A raiz quadrada de {x} é {math.sqrt(x)}''')


