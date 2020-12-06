print ('''EX 035. Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se 
elas podem ou não formar um triângulo.''')
A = int (input ('Reta 1 : '))
B = int (input ('Reta 3 : '))
C = int (input ('Reta 2 : '))
if A + B == C or A + C == B or B + C == A:
    print ('Pode formar um triângulo!')
else:
    print ('Não pode formar um triângulo')
