print ('EX 003. Crie um programa que leia dois números e mostre a soma entre eles')
# FORMA 1 - SIMPLES:
x = int (input('Digite um número: '))
y = int (input('Digite um número: '))
s = x + y
print (f'{x} + {y} = {s}')

# FORMA 2 - USANDO FUNCIONALIDADES DO PYCHARM!
l = []
for c in range (1,3):
    l.append(int(input (f'Digite o {c}º número: ')))
    print (f'A soma é igual a {sum(l)}')
