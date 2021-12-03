from random import randint
from time import sleep


def sorteia():
    numeros = list()
    print('Sorteando 5 valores da lista: ', end='')
    for n in range(5):
        sleep(0.8)
        numeros.append(randint(1, 10))
        print(numeros[n], end=' ')
    sleep(0.8)
    print(' << PRONTO! >>')
    somapar(numeros)


def somapar(num):
    totalp = 0
    sleep(1)
    for v in num:
        if v % 2 == 0:
            totalp += v
    print(f'Somando os valores pares, temos {totalp}')


sorteia()
