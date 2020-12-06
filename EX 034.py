print ('''EX 034. Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.''')
salario = float (input ('Digite seu salário R$: '))
if salario > 1250:
    novo = salario + (salario * 10)/100
    print (f'O Salário de R$ {salario:.2f} com 10% de aumento passa a ser R$ {novo:.2f}')
if salario <= 1250:
    novo = salario + (salario * 15) / 100
    print(f'O Salário de R$ {salario:.2f} com 15% de aumento passa a ser R$ {novo:.2f}')
