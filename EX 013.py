print ('EX 013. Faça um algoritmo que leia o salário de uma funcionário e mostre seu novo salário, com 15% de aumento')
salario =  float (input ('Digite seu salário: '))
aumento = salario + (salario * 15)/100
print (f'Um Salário de R${salario:.2f} com 15% de aumento passa a ser R${aumento:.2f}')