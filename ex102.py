def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: é o número a ser calculado o fatorial
    :param show: opcao para mostrar calculo do fatorial, como padrao False para mostrar somente resultado
    :return: retorno do resultado
    """
    result = 1
    if show:
        print(f'Calculando Fatorial {num}! - ', end='')
        for x in range(num, 0, -1):
            if x != 1:
                print(f'{x}', end=' x ')
            else:
                print(f'{x}', end=' = ')
            result *= x
        return f'{result}'
    else:
        for x in range(num, 0, -1):
            result *= x
        return f'resultado = {result}'


print(fatorial(10, True))
help(fatorial)
