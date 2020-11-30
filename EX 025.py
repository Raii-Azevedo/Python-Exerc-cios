print ('EX 025. Crie um programa que leia o nome de uma pessoa e diga se ela tem ‘SILVA’ no nome.')
nome = str (input ('Nome completo: ')).upper().split()
if "SILVA" in nome:
    print ('Tem SILVA no nome')
else:
    print ('Não tem SILVA')