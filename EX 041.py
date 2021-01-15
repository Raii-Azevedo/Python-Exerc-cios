print ('''EX 041 – A Confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta 
e mostre sua categoria de acordo com a idade:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 20 anos: SÊNIOR
Acima: MASTER.''')
import datetime
from datetime import date
nome = str (input ('Nome: '))
ANO = int (input('Ano de nascimento: '))
PRAZO = date.today().year
IDADE = PRAZO - ANO

# IMPRIMIR A DATA DE HOJE E IDADE DO INDIVÍDUO
HOJE = date.today()
print (f'Hoje é {HOJE.strftime("%A %d. %B %Y")}')
print (f'{nome}, você nasceu em {ANO}. Portanto tem {IDADE} anos')

# MÓDULO ALISTAR
if IDADE <= 9:
    print (f'{nome}, sua categoria é MIRIM')
elif IDADE > 9 and IDADE <= 14:
    print(f'{nome}, sua categoria é INFANTIL')
elif IDADE > 14 and IDADE <= 19:
    print(f'{nome}, sua categoria é JÚNIOR')
elif IDADE > 19 and IDADE <= 20:
    print(f'{nome}, sua categoria é ADULTO')
else:
    print(f'{nome}, sua categoria é MASTER')