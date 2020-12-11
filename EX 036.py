print ('''EX 036 – Escreva um programa para aprovar um empréstimo bancário para uma casa. O programa vai perguntar 
o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo
que ela não pode exceder 30% do salário ou então o empréstimo será negado.''')
print ('----- MEU BANCO -----')
emprestimo = float (input ('Valor do Empréstimo: '))
salario = float (input ('Digite seu sálário R$: '))
parcela = int (input ("Nº de Parcelas: "))
valor = emprestimo / parcela
if valor > (salario * 30)/100:
    print (f'Empréstimo negado. O valor da a parcela de R$ {valor:.2f} excede 30% do seu salário.')
else:
    print (f'Empréstimo concedido. Pagamento de {parcela} parcelas no valor de R$ {valor:.2f} ')

