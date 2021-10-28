print('{:=^30}'.format(' GERADOR DE PA '))
primtermo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
calcprimt = primtermo
cont = 10
conttermos = 0
mais = 1
while not mais == 0:
    print('PROGRESSAO: ', end='')
    for c in range(1, cont + 1):
        print('{}'.format(calcprimt), end=' -> ')
        calcprimt += razao
        conttermos += 1
    print('FIM')
    mais = int(input('Quantos termos voce quer mostrar mais? '))
    cont = mais
print('''
Voce saiu.
Progressao finalizada com {} termos mostrados.
'''.format(conttermos))
