from time import sleep


def contagem(numIni, numFim, numInterv):
    print('~' * 30)
    print(f'Contagem de {numIni} até {numFim} de {numInterv} em {numInterv}')
    if numInterv < 0:
        numInterv *= (-1)
    if numInterv == 0:
        numInterv = 1
    if numIni > numFim:
        numFim -= numInterv
        numInterv *= (-1)
    for n in range(numIni, numFim + 1, numInterv):
        sleep(0.3)
        print(n, end=' ')
    sleep(0.3)
    print('FIM!')
    sleep(0.5)


contagem(1, 10, 1)
contagem(10, 0, 2)
print('~' * 30)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
intervalo = int(input('Intervalo: '))
contagem(inicio, fim, intervalo)
