print ('''EX 011. Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área 
e a quantidade de tintas necessárias para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m2''')
L = float (input ('Informe a Largura da parede: '))
H = float (input ('Informe a Altuura da parede: '))
A = L * H
T = (1 * A) / 2
print (f'''A parede possui dimensões {L} x {H}
E uma área de {A} m²
São necessários {T}L para pintar uma parede de {A}m²''')

