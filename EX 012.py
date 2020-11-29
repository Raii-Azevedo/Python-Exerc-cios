print ('EX 012. Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto')
produto =  float (input ('Digite o valor do produto: '))
desconto = produto - (produto * 5)/100
print (f'Um produto de R${produto:.2f} com 5% de desconto passa a custar R${desconto:.2f}')