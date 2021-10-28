lista = []
listap = []
listai = []
opc = ''
while True:
    lista.append(int(input('Digite um número: ')))
    opc = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if opc == 'N':
        break
for c in lista:
    if c % 2 == 0:
        listap.append(c)
    else:
        listai.append(c)
print('-=' * 25)
print(f'Os números digitados foram: {lista}')
print(f'Os números pares foram: {listap}')
print(f'Os números ímpares foram: {listai}')
