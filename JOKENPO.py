from random import randint
print ('\033[32mEX 045 – Crie um programa que faça o computador jogar Jokenpô com você.\033[m')
print('--*-'*20)
c = ''
print('Vamos jogar JOKENPÔ!')
while c in "S":
    itens = ('Pedra', 'Papel', 'Tesoura')
    jogo = int(input('''Digite o número desejado...
    \033[33m[0]- Pedra
    [1]- Papel
    [2]- Tesoura\033[m
    Digite o número: '''))
    pc = randint(0, 3)
    from time import sleep

    print('\033[32m=-\033[m' * 20)
    print('\033[31mJO'), sleep(1)
    print('\033[33mKEN'), sleep(1)
    print('\033[35mPO!!!'), sleep(1)
    print('\033[32m=-\033[m' * 20)

    if pc == 0:  # PEDRA
        if jogo == 0:
            print('Eu escolhi {}'.format(itens[pc])),
            print('Você escolheu {}'.format(itens[jogo])),
            print('\033[31mÉ um Empate\033[m')

    if pc == 0:
        if jogo == 1:
            print('Eu escolhi {}'.format(itens[pc])),
            print('Você escolheu {}'.format(itens[jogo])),
            print('\033[31mParabéns, você GANHOU\033[m')

    if pc == 0:
        if jogo == 2:
            print('Eu escolhi {}'.format(itens[pc])),
            print('Você escolheu {}'.format(itens[jogo])),
            print('\033[31mEu GANHEI!!!\033[m')

    if pc == 1:  # PAPEL
        if jogo == 0:
            print('Eu escolhi {}'.format(itens[pc])),
            print('Você escolheu {}'.format(itens[jogo])),
            print('\033[31mÉu GANHEI!!\033[m')

    if pc == 1:
        if jogo == 1:
            print('Eu escolhi {}'.format(itens[pc])), \
            print('Você escolheu {}'.format(itens[jogo])), \
            print('\033[31mÉ um Empate\033[m')

    if pc == 1:
        if jogo == 2:
            print('Eu escolhi {}'.format(itens[pc])),
            print('Você escolheu {}'.format(itens[jogo])),
            print('\033[31mVocê GANHOU!!!\033[m')

    if pc == 2:  # TESOURA
        if jogo == 0:
            print('Eu escolhi {}'.format(itens[pc])),
            print('Você escolheu {}'.format(itens[jogo])),
            print('\033[31mVocê GANHOU!!!\033[m')

    if pc == 2:
        if jogo == 1:
            print('Eu escolhi {}'.format(itens[pc])),
            print('Você escolheu {}'.format(itens[jogo])),
            print('\033[31mEu VENCI!!\033[m')

    if pc == 2:
        if jogo == 2:
            print('Eu escolhi {}'.format(itens[pc])), \
            print('Você escolheu {}'.format(itens[jogo])), \
            print('\033[31mÉ um Empate\033[m')
    c = str (input ('Quer jogar de novo? [S/N]: ')).strip().upper()
    print('\033[32m=-\033[m' * 20)
    if c == 'N':
        break
print ('\033[33mObrigado por jogar comigo!\033[m')