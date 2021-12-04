def aumentar(num, f=False, porc=0):
    num += num * porc / 100
    return num if not f else format_moeda(num)


def diminuir(num, f=False, porc=0):
    num -= num * porc / 100
    return num if not f else format_moeda(num)


def dobro(num, f=False):
    num *= 2
    return num if not f else format_moeda(num)


def metade(num, f=False):
    num /= 2
    return num if not f else format_moeda(num)


def format_moeda(num, f=True, p='R$'):
    if f:
        num = f'{p} {num:.2f}'
        num = num.replace('.', ',')
    return num


def resumo(num, aum=0, red=0):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preco Analsado:":<20}{format_moeda(num):<10}')
    print(f'{"Dobro do Preco:":<20}{dobro(num, f=True):<10}')
    print(f'{"Metade do Preco:":<20}{metade(num, f=True):<10}')
    print(f'{aum:<3}{"% de Aumento:":<17}{aumentar(num, f=True, porc=aum):<10}')
    print(f'{red:<3}{"% de Reducao:":<17}{diminuir(num, f=True, porc=red):<10}')
    print('-' * 30)
