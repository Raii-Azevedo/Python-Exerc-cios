print ('''EX 022. Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as 
letras maiúsculas e minúsculas. Quantas letras ao todo(sem considerar espaços) Quantas letras tem o primeiro nome.''')
nome = input ('Nome Completo: ').strip()
print ('Seu nome tem {} letras'.format (len(nome.replace(' ',""))))
print ('O 1º nome tem {} letras'.format (len(str(nome.split()[0]))))
print (f'Nome em maiúsculo = {nome.upper()}')
print (f'Nome em minúsculo = {nome.lower()}')
