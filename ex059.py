from time import sleep
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
opc = 0
while not opc == 5:
    print('=' * 25)
    print(
        '[ 1 ] Somar\n'
        '[ 2 ] Multiplicar\n'
        '[ 3 ] Maior\n'
        '[ 4 ] Novos Números\n'
        '[ 5 ] Sair do Programa\n')
    opc = int(input('Qual sua opcao? '))
    if opc == 1:
        result = v1 + v2
        print('O resultado de {} + {} = {}'.format(v1, v2, result))
    elif opc == 2:
        result = v1 * v2
        print('O resultado de {} x {} = {}'.format(v1, v2, result))
    elif opc == 3:
        if v1 == v2:
            print('O valor {} e {} sao iguais!'.format(v1, v2))
        elif v1 > v2:
            print('O valor {} é maior que {}'.format(v1, v2))
        else:
            print('O valor {} é maior que {}'.format(v2, v1))
    elif opc == 4:
        v1 = int(input('Digite o 1ª valor: '))
        v2 = int(input('Digite o 2º valor: '))
    else:
        print('Opcao inválida! Tente novamente!')
    sleep(1)
print('Voce saiu.')
