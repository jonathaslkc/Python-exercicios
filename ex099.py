from random import randint
from time import sleep


def maior2(lista):
    print('-=' * 15)
    sleep(0.6)
    print('Analisando os valores passados...')
    sleep(1)
    apresentalista(lista)
    if lista:
        nummaior = max(lista)
    else:
        nummaior = 0
    sleep(0.5)
    print(f'Foram informados {len(lista)} valores ao todo.')
    print(f'O maior valor foi {nummaior}.')
    lista.clear()


def apresentalista(lista):
    for n in lista:
        sleep(0.5)
        print(n, end=' ')


def preencherlista(qtd):
    lista = list()
    for n in range(qtd):
        lista.append(randint(0, 9))
    maior2(lista)


def maior(* num):
    maiorv = 0
    print('-=' * 20)
    print('Analisando os valores passados...')
    for n in num:
        sleep(0.5)
        print(n, end=' ')
        if maiorv == 0:
            maiorv = n
        else:
            if maiorv < n:
                maiorv = n
    sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo.')
    sleep(0.5)
    print(f'O maior valor foi {maiorv}')
    '''print(f'O maior valor foi {max(num) if num else 0}')'''


'''qtd = int(input('Quantos números deseja para avaliar? '))
preencherlista(qtd)

preencherlista(6)
preencherlista(3)
preencherlista(2)
preencherlista(0)'''
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(6)
maior()
