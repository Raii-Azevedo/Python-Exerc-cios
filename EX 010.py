print (''''EX 010. Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares 
ela pode comprar Considere US$ 1,00 = R$ 3,27''')
R = float (input ('Digite um valor em R$ para converter em U$: '))
D = R / 3.27
print (f'R$ {R:.2f} equivalem a U$ {D:.2f}')
# A FORMATAÇÃO {:.2F} É PARA LIMITAR O NÚMERO DE CASAS DECIMAIS APÓS A VÍRGULA.