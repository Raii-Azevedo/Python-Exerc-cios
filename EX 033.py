print ('EX 033. Faça um programa que leia três números e mostre qual é o maior e qual é o menor.')
# USANDO RECURSOS DO PYCHARM
n = []
for c in range (3):
    n.append (int (input('Digite um número: ')))
print (f'O maior número digitado foi {max(n)} e o menor foi {min(n)}')

