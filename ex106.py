from time import sleep


def txt_titulo(msg, cor='\033[1;36m'):
    print(f'{cor}-=' * len(msg))
    print(f'{msg:^{len(msg) * 2}}')
    print('-=' * len(msg))
    print('\033[m')


def pesquisa():
    laco = True
    while laco:
        info = input('Funcao ou Biblioteca > ')
        if info.strip().upper() != 'FIM':
            txt_titulo('Acessando o manual do comando "time"', '\033[1;32m')
            for i in range(3):
                sleep(1)
                print('.', end='')
            print()
            print(f'\033[1;33m{help(info)}\033[m')
        else:
            txt_titulo('ATÉ LOGO!', '\033[1;31m')
            laco = False


txt_titulo('SISTEMA DE AJUDA PyHELP')
pesquisa()
