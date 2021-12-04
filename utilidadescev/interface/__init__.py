from time import sleep

urlarquivo = '../../desktop/dados_pessoas.csv'


def print_formatado(txt, tipo='c'):
    tam = 40
    print('-' * tam)
    if tipo == 'c':
        print(f'{txt:^{tam}}')
    elif tipo == 'e':
        print(f'{txt:<{tam}}')
    elif tipo == 'd':
        print(f'{txt:>{tam}}')


def menu():
    print_formatado('MENU PRINCIPAL')
    print_formatado('\033[1;34m1 - Ver pessoas cadastradas\n2 - Cadastrar nova pessoa\n3 - Sair do sistema\033[m', 'e')
    opcao = trata_opcao(3)
    if opcao == 1:
        ver_pessoas()
    elif opcao == 2:
        cadastrar_pessoas()
    elif opcao == 3:
        print()
        print('Saindo do Programa...')
        sleep(2)


def ver_pessoas():
    import csv
    print('\n')
    try:
        with open(urlarquivo, 'r', encoding='utf-8') as arq:
            texto = csv.reader(arq)
            print_formatado('LISTA DE CADASTROS')
            print('-' * 40)
            for h, v in enumerate(texto):
                for i, x in enumerate(v):
                    if i % 2 == 0:
                        print(f'{x[:28]:<30}', end='')
                    else:
                        if h == 0:
                            print(f'{x:<10}')
                        else:
                            print(f'{x:<4}', end='')
                            print(f'{"anos":<6}')
            print('-' * 40)
    except Exception as erro:
        print(f'Arquivo Inexistente! < {erro} >')
    print('\n')
    menu()


def arquivo_existe():
    try:
        teste = open(urlarquivo, 'r')
        teste.close()
    except FileNotFoundError:
        return False
    else:
        return True


def cadastrar_pessoas():
    import csv
    print('\n' * 2)
    cabecalho = ['NOME', 'IDADE']
    nome = input('Digite seu nome: ')
    idade = input('Digite sua idade: ')
    idade = trata_inteiro(idade)
    dados = [nome, idade]
    sleep(0.3)
    print('\033[1;42m|||||||\033[m', end='')
    sleep(0.3)
    print('\033[1;42m||||||||||\033[m', end='')
    sleep(0.2)
    try:
        if arquivo_existe():
            sleep(0.2)
            print('\033[1;42m|||||\033[m', end='')
            with open(urlarquivo, 'a+', encoding='utf-8', newline='') as arq:
                escritor = csv.writer(arq)
                escritor.writerows([dados])
                print('\033[1;42m||||||||||\033[m')
                sleep(0.2)
                print('\033[1;32mNOVA INCLUSAO FEITA COM SUCESSO!\033[m')
        else:
            sleep(0.2)
            print('\033[1;42m|||||\033[m', end='')
            with open(urlarquivo, 'w', encoding='utf-8', newline='') as arq:
                escritor = csv.writer(arq)
                escritor.writerows([cabecalho])
                escritor.writerows([dados])
                print('\033[1;42m||||||||||\033[m')
                sleep(0.2)
                print('\033[1;32mCADASTRO FEITO COM SUCESSO!\033[m')
    except Exception as erro:
        print_formatado(f'\033[1;31mERRO NA OPERACAO! <{erro}>\033[m', 'e')
    else:
        sleep(0.3)
        print('Retornando ao Menu Principal...')
        sleep(0.3)
    print()
    menu()


def trata_opcao(qtd):
    laco = True
    while laco:
        opc = input('\033[1;3;33mSua opcao: \033[m').strip()
        if opc.isnumeric():
            opc = int(opc)
            if qtd >= opc > 0:
                return opc
            else:
                print('\033[1;31mA opcao escolhida nao existe!\033[m')
        else:
            print('\033[1;31mDigite uma opcao válida!\033[m')


def trata_inteiro(num):
    laco = True
    while laco:
        if num.isnumeric():
            num = int(num)
            return num
        else:
            num = input('\033[1;3;31mDigite um número inteiro válido: \033[m').strip()
