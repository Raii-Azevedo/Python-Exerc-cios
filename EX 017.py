print ('''EX 017. Faça um programa que leia o comprimento do cateto oposto e do 
cateto adjacente de um triângulo, calcule o mostre o comprimento da hipotenusa.''')
# UTILIZANDO FÓRMULA MATEMÁTICA
CO = int (input ('Cateto Oposto: '))
CA = int (input ('Cateto Adjacente: '))
HI = (CO**2 + CA**2)**(1/2)
print (f'Hipotenusa = {HI:.2f}')

print ('')
# UTILIZANDO FUNCIONALIDADES DO PYCHARM
import math
CO = int (input ('Cateto Oposto: '))
CA = int (input ('Cateto Adjacente: '))
HI = math.sqrt((pow(CO,2)+ pow(CA,2)))
print (f'Hipotenusa = {HI:.2f}')

# MÉTODO ALTERNATIVO
print('')
CO = int (input ('Cateto Oposto: '))
CA = int (input ('Cateto Adjacente: '))
HI = math.hypot(CO,CA)
print (f'Hipotenusa = {HI:.2f}')

