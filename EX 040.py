print('''EX 040 – Crie um programa que leia duas notas de um aluno e calcule sua média, 
mostrando uma mensagem no final, de acordo com a média atingida:
Média abaixo de 5,0 (REPROVADO)
Média entre 5,0 e 6,9 (RECUPERAÇÃO)
Média 7,0> (APROVADO)''')
n1 = float (input ('1ª nota: '))
n2 = float (input ('2ª nota: '))
media = (n1 + n2)/2
print (f'Média =  {media}')
if media < 5:
    print (f'Situação: REPROVADO')
elif media >=5 and media <= 6.9:
    print(f'Situação: RECUPERAÇÃO')
else:
    print ('Situação: APROVADO')
