num = int(input('Digite um número: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;32m', end=' ')
        cont += 1
    else:
        print('\033[1;31m', end=' ')
    print(c, end=' ')
print('\033[mFIM')
print('O número {} foi dividido {} vezes'.format(num, cont))
if cont == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele NAO É PRIMO')
