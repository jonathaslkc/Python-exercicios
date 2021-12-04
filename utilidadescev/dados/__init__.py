# import locale


def leiadinheiro(msg):
    # locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    # locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
    laco = True
    valor = input(msg)
    while laco:
        if ',' in valor:
            valor = valor.replace(',', '.')
        """if valor.strip() == '':
            print(f'\033[1;31m"{valor.strip()}" nao é um valor válido!\033[m')
            valor = input(msg)
        else:
            try:
                valor = float(valor)
                laco = False
            except:
                print(f'\033[1;31m"{valor.strip()}" nao é um valor válido!\033[m')
                valor = input(msg)"""
        if valor.isalpha() or valor.strip() == '':
            print(f'\033[1;31m"{valor.strip()}" nao é um valor válido!\033[m')
            valor = input(msg)
        else:
            valor = float(valor)
            laco = False
    # if f:
    # valor = locale.currency(valor, symbol=True, grouping=True, international=False)
    return valor


def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO!\nDigite um número inteiro válido! \033[0m')
            continue
        except KeyboardInterrupt:
            print('\033[1;33mEntrada de dados interrompida pelo usuário.\033[0m')
            return 0
        else:
            return valor


def leiafloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO!\nPor favor, digite um número inteiro válido! \033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;33mUsuário interrompeu execucao do sistema.\033[m')
        else:
            return valor
