from random import randint
from time import sleep

var = 0
jogos = []
temp = list()
print('-=' * 20)
print('{:^40}'.format('JOGO DA MEGA SENA'))
print('-=' * 20)
qtdjg = int(input('Quantos jogos deseja que eu sorteie? '))
for c in range(0, qtdjg):
    for c1 in range(0, 6):
        if c == 0 and c1 == 0:
            temp.append(randint(1, 60))
        while True:
            var = randint(1, 60)
            if var not in temp:
                temp.append(var)
                break
    jogos.append(temp[:])
    temp.clear()
print('-=' * 4, f' SORTEANDO {qtdjg:^3}JOGOS ', '-=' * 5)
for c in range(0, qtdjg):
    print(f'Jogo {c + 1:^2}: ', end=' ')
    print(f'{sorted(jogos[c])}')
    sleep(0.7)
print('-=' * 7, f'BOA SORTE!', '-=' * 7)
