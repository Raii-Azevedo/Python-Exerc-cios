print ('''EX 044 – Elabore um programa que calcule um valor a ser pago pelo produto, considerando seu preço normal e condição de pagamento:
A vista dinheiro/cheque: 10% de desconto.
A vista no cartão: 5% de desconto.
Em até 2x no cartão: preço normal.
3x ou mais no cartão: 20% de juros.''')
produto = float (input('Valor do produto: '))
pag = int (input('''Método de Pagamento
[1] - A vista dinheiro/cheque
[2] - A vista cartão
[3] - Até 2x cartão
[4] - 3x ou mais cartão
Qual método deseja: '''))
if pag ==1:
    novo = produto - (produto * 10)/100
    print (f'Com 10% de desconto o produto passa a custar R${novo:.2f}')
elif pag ==2:
    novo = produto - (produto * 5)/100
    print (f'Com 5% de desconto o produto passa a custar R${novo:.2f}')
elif pag ==3:
    novo = produto / 2
    print (f'Dividir de 2x não tem desconto, o produto custará 2x R${novo:.2f}')
elif pag ==4:
    novo = produto + (produto * 20)/100
    print (f'Dividir de 3x ou mais acarreta em juros de 20%, o produto custará R${novo:.2f}')


