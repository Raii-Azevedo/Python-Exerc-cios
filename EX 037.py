print ('''EX 037 – (Converter bases) Escreva um programa que leia um número inteiro qualquer e peça para o usuário 
escolher qual será a base de conversão. 1- binário 2- octal 3- hexadecimal.''')
n = int (input ('Digite um número: '))
x = int (input (f'''--- CONVERSOR ---
[1] Binário
[2] Octal
[3] Hexadecimal
Digite o número referente para realizar a conversão de {n}: '''))
if x == 1:
    print (f'{n} Binário = {bin(n)[2:]}')
if x == 2:
    print (f'{n} Octal = {oct(n)[2:]}')
if x == 3:
    print(f'{n} Hexadecimal = {hex(n)[2:]}')
else:
    if x != 1 and x != 2 and x != 3:
        print ('Opção não reconhecida')


