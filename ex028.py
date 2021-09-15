import random
from time import sleep
print('\033[35m Vou pensar em um número entre 0 e 5... Tente advinhar! \033[0;0m')
print('\033[33m =-------= \033[0;0m' * 10)
ran = random.randint(0, 5)
num = int(input('Em que número pensei? '))
print('\033[34m PROCESSANDO... \033[0;0m')
sleep(3)
if num == ran:
    print('\033[32m PARABÉNS!! Voce conseguiu me vencer! \033[0;0m')
else:
    print('\033[31m GANHEI!! Pensei no número {} e voce em {} \033[0;0m'.format(ran, num))
print('--- FIM --')
