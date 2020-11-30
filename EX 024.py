print ('EX 024. Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome ‘SANTO’')
cidade = str (input ('Digite o nome de uma cidade: ')).upper().split()
if "SANTO" in cidade[0]:
    print (f'A cidade {cidade} começa com Santo')
else:
    print ('Não começa com Santo')
