num = int(input('Digite um número para calcular o fatorial: '))
print('Calculando {}! = '.format(num), end='')
cntrl = num
result = num
calc = num - 1
while not cntrl == 1:
    result *= calc
    print('{} x '.format(cntrl), end='')
    cntrl -= 1
    calc -= 1
print('{} = {}'.format(cntrl, result))
