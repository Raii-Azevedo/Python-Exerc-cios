print ('''EX 042 – Refaça o EX 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado.
Equilátero: Todos os lados iguais.
Isósceles: Dois lados iguais.
Escaleno: Todos os lados diferentes.''')
A = int (input ('Reta 1 : '))
B = int (input ('Reta 3 : '))
C = int (input ('Reta 2 : '))
if A + B == C or A + C == B or B + C == A:
    print ('Pode formar um triângulo!')
# TIPOS DE TRIÂNGULO
if A == B and B == C:
    print ('Triângulo Equilátero')
if A != B and B != C and C!= A:
    print ('Triângulo Escaleno')
if A == B or B == C or C == A:
    print ('Triângulo Isósceles')
