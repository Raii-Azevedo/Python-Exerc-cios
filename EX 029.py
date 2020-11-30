print ('''EX 029. Escreva um programa que leia a velocidade de uma carro. Se ele ultrapassar 80 km/h, 
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada Km acima do limite.''')
carro = int (input ('Velocidade do carro KM: '))
if carro > 80:
    multa = (carro - 80) * 7
    print (f'Um carro a {carro}KM/h paga multa de R${multa:.2f}')