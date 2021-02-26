import os


def LimpaTela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def existeCPF(jogadores, c):
    for nome, cpf in jogadores:
        if cpf == c:
            return True

    return False


def visualizarJogadores(jogadores):
    if len(jogadores) ==0:
        print('Nenhum jogador cadastrado')
    else:
        print('Jogadores já cadastrados:\n')
        for nome, cpf in jogadores:
            print(f'{nome} (cpf: {cpf})')

    print()


def InserirJogador(jogadores):
    visualizarJogadores(jogadores)
    nome = input('Digite o nome do jogador: ')
    cpf = input('Digite o CPF: ')


    if existeCPF(jogadores, cpf):
        print('Erro, CPF já cadastrado no sistema')
    else:
        print('Jogador cadastrado no sistema')

    jogadores.append((nome, cpf))


def lerCPFs(jogadores):
    n = int(input('Digite a quantidade de participantes: '))
    cpfs = []

    while len(cpfs) < n:
        visualizarJogadores(jogadores)
        c = input('Digite um CPF: ')

        while c in cpfs or not existeCPF(jogadores, c):
            print('CPF inválido!')
            c = input('Digite outro CPF: ')

            cpfs.append(c)

        return cpfs


def lerNumeros():
    n = int(input('Quantos números no cartão? '))
    while n < 6 or n > 15:
        print('Erro. Digite um número entre 6 e 15')
        n = int(input('Quantos números no cartão? '))

    numeros = []
    while len(numeros) < n:
        x = int(input('Digite um número entre 1 e 60: '))
        while x < 1 or x > 60 or x in numeros:
            print('Erro. Número inválido.')
            x = int(input('Tente novamente: '))

        numeros.append(x)

    return numeros


def inserirAposta(jogadores, apostas):
    cpfs = lerCPFs(jogadores)
    print(cpfs)
    numeros = lerNumeros()

    apostas.append((cpfs, numeros))


def nomeJogador(jogadores, cpfs):
    for n, c in jogadores:
        if c == cpf:
            return n


def visualizarApostas(jogadores, apostas):
    i = 0
    while i < len(apostas):
        cpfs, numeros = apostas[i]

        print(f'APOSTA {i+1}')
        print(f'Números: ', end=' ')
        for n in numeros:
            print(n, end=' ')
        print()

        print('Jogadores: ')
        for cpf in cpfs:
            print(f'{nomeJogador(jogadores, cpf)}')
        i += 1


def lerNumerosSorteados():
    l = []

    while len(l) < 6:
        x = int(input('Digite um dos números sorteados: '))

        if x < 1 or x > 60 or x in l:
            print('Erro. Número inválido')
        else:
            l.append(x)

    return l


def contida(l1, l2):
    for x in l1:
        if x not in l2:
            return False

    return True


def verificarApostasVencedoras(apostas, numeros):

    l = []

    for i in range (len(apostas)):
        _, nums = apostas[i]

        if contida(numeros, nums):
            l.append(i)

    return l


def listarVencedores(jogadores, apostas, vencedoras, premioPorCartao):
    LimpaTela()
    print('Vencedores:')

    for i in vencedoras:
        cpfs, _ = apostas[i]

        print(f'CARTÃO {i+1}')

        for cpf in cpfs:
            print(f'Nome: {nomeJogador(jogadores, cpf)} - R$ {premioPorCartao/len(cpfs):.2f}')


def inserirSorteio(jogadores, apostas):
    numeros = lerNumerosSorteados()
    vencedoras = verificarApostasVencedoras(apostas, numeros)

    premio = int(input('Digite o valor total do Prêmio: '))
    premioPorCartao = premio / len(vencedoras)

    if len(vencedoras)  > 0:
        premioPorCartao = premio / len(vencedoras)
        listarVencedoras(jogadores, apostas, vencedoras,
                          premioPorCartao)
    else:
        print('Não houve vencedor')


def main(argv=None):
    print('Seja bem vindo ao Bolão')

    menu='''
    Escolha uma opção:
    [1] - Cadastrar Jogador
    [2] - Visualizar Jogadores
    [3] - Cadastrar Aposta
    [4] - Visualizar apostas
    [5] - Inserir sorteio e Listar Vencedores
    [6] - Sair
    Opção: '''

    jogadores = []
    apostas = []

    opcao = input(menu)

    while opcao != '6':
        LimpaTela()
        if opcao == '1':
            print('Cadastrar Jogador')
            InserirJogador(jogadores)
        elif opcao == '2':
            visualizarJogadores(jogadores)
        elif opcao == '3':
            inserirAposta(jogadores, apostas)
        elif opcao == '4':
            visualizarApostas(jogadores, apostas)
        elif opcao == '5':
            inserirSorteio(jogadores, apostas)
        elif opcao != '6':
            print('Opção Inválida, tente novamente!')

        opcao = input(menu)

    print('Adeus')


if __name__ == '__main__':
    main()

