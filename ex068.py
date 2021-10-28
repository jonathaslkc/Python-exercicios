from random import randint
from time import sleep
result = ''
opc = cont = 0
pc = randint(0, 5)
print('{:-^30}'.format(' GAME PAR OU ÍMPAR '))
print('Vamos jogar par ou ímpar?')
print('=-' * 15)

while True:
    opc = input('Digite o número entre 0 a 5: ')
    while True:
        if not opc.isdigit():
            opc = input('Digite um número INTEIRO entre 0 a 5: ')
        else:
            opc = int(opc)
            break
    while opc > 5 or opc < 0:
        opc = int(input('Opcao inválida! Digite novamente um número entre 0 a 5: '))
    pi = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    while not pi in 'PpIi':
        pi = str(input('Opcao inválida! Digite novamente Par ou Ímpar [P/I]')).strip().upper()[0]
    if ((opc + pc) % 2) == 0:
        result = 'PAR'
    else:
        result = 'IMPAR'

    print(f'Voce jogou {opc}, eu joguei {pc}. Total deu {opc + pc} ( {result} )')
    if result[0] == pi:
        print('Voce ganhou!')
        cont += 1
    else:
        print('Voce perdeu!')
        print('-=' * 15)
        sleep(1)
        break
    print('-=' * 15)
print(f'''GAME OVER!!!
Voce venceu {cont} vezes!
''')
