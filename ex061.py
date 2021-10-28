print('GERADOR DE PA')
print('=' * 20)
primtermo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
cont = 10
termcalc = primtermo
print('PROGRESSAO: ', end='')
while not cont == 0:
    print('{}'.format(termcalc), end=' -> ')
    termcalc += razao
    cont -= 1
print('FIM')
