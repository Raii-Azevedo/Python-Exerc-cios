print ('''EX 031. Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
cobrando R$ 0,50 por km para viagens de até 200km e R$ 0,45 para viagens mais longas.''')
D = int (input ('Qual a distância em KM da viagem: '))
if D <= 200:
    Valor = D * 0.50
if D > 200:
    Valor = D * 0.45
print (f'O Preço da viagem para uma viagem de {D} é de R${Valor:.2f}')