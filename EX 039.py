print ('''EX 039 – Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
Se ele ainda vai se alistar.
Se é hora de se alistar.
Se já passou da hora de se alistar. 
O programa deve informar quanto tempo falta/passou para o prazo de alistamento.''')
import datetime
from datetime import date
print ('---- ALISTAMENTO MILITAR ---- ')
nome = input ('Digite seu nome: ')
ANO = int (input ('Data de nascimento: '))
PRAZO = date.today().year
IDADE = PRAZO - ANO

# IMPRIMIR A DATA DE HOJE E IDADE DO INDIVÍDUO
HOJE = date.today()
print (f'Hoje é {HOJE.strftime("%A %d. %B %Y")}')
print (f'{nome}, você nasceu em {ANO}. Portanto tem {IDADE} anos')

# MÓDULO ALISTAR
if IDADE == 18:
    print (f'Deve se alistar imediatamente.')
elif IDADE < 18:
    SALDO = 18 - IDADE
    print (f'Você ainda não tem 18 anos. Faltam {SALDO} ano(s) para seu alistamento.')
else:
    SALDO = IDADE - 18
    print (f'Você já tem mais de 18 anos. Já deveria ter se alistado, seu alistamento foi há {SALDO} ano(s)')





