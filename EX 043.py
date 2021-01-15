print('''EX 043 – Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule o seu IMC e mostre seus status, de acordo com a tabela abaixo:
Abaixo de 18,5 > Abaixo do peso.
Entre 18,5 e 25 > Peso ideal.
25 até 30 > Sobrepeso.
30 a 40 > Obesidade.
Acima de 40 > Obesidade mórbida.''')
nome = str (input ('Nome: '))
altura = float (input ('Altura: '))
peso = float (input ('Peso: '))
IMC = peso/ altura**2
if IMC < 18.5:
    print (f'{nome}, seu IMC é {IMC:.2f}. Você está abaixo do peso.')
elif IMC >= 18.5 and IMC <= 25:
    print (f'{nome}, seu IMC é {IMC:.2f}. Você está no peso ideal.')
elif IMC > 25 and IMC <= 30:
    print (f'{nome}, seu IMC é {IMC:.2f}. Você está com sobrepeso.')
elif IMC > 30 and IMC <= 40:
    print (f'{nome}, seu IMC é {IMC:.2f}. Você está com obesidade.')
elif IMC > 40:
    print (f'{nome}, seu IMC é {IMC:.2f}. Você está com obesidade mórbida')

