from random import choice, randint
from time import sleep

itens = ['PEDRA', 'PAPEL', 'TESOURA']
print('''SUAS OPCOES: \n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA''')
opc = int(input('Qual sua jogada? '))
#pcopc = choice(['PEDRA', 'PAPEL', 'TESOURA'])
pcopc = randint(0, 2)
sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')  
sleep(0.5)
print('***#' * 8)
print('''Computador jogou {}
Jogador jogou {}'''.format(itens[pcopc], itens[opc]))
print('***#' * 8)
if opc == pcopc:
    print('OCORREU UM EMPATE!')
elif opc == 0 and pcopc == 2:
    print('JOGADOR VENCEU!')
elif opc == 1 and pcopc == 0:
    print('JOGADOR VENCEU!')
elif opc == 2 and pcopc == 1:
    print('JOGADOR VENCEU!')
else:
    print('COMPUTADOR VENCEU!!')