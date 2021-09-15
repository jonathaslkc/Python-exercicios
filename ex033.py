n1 = int(input('\033[1mPrimeiro\033[m numero: '))
n2 = int(input('\033[1mSegundo\033[m numero: '))
n3 = int(input('\033[1mTerceiro\033[m numero: '))
maior = n1
menor = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior  = n3
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O \033[1mmaior\033[m valor foi \033[4;30;42m{}\033[m'.format(maior))
print('O \033[1mmenor\033[m valor foi \033[4;30;42m{}\033[m'.format(menor))

''' SEGUNDA FORMA MAIS CLARA, PÓREM COM MAIS LINHAS
if n1 > n2 > n3:
    print('O maior valor foi {}'.format(n1))
    print('O menor valor foi {}'.format(n3))
if n1 > n3 > n2:
    print('O maior valor foi {}'.format(n1))
    print('O menor valor foi {}'.format(n2))
if n2 > n1 > n3:
    print('O maior valor foi {}'.format(n2))
    print('O menor valor foi {}'.format(n3))
if n2 > n3 > n1:
    print('O maior valor foi {}'.format(n2))
    print('O menor valor foi {}'.format(n1))
if n3 > n1 > n2:
    print('O maior valor foi {}'.format(n3))
    print('O menor valor foi {}'.format(n2))
if n3 > n2 > n1:
    print('O maior valor foi {}'.format(n3))
    print('O menor valor foi {}'.format(n1))'''
print('- FIM -')
