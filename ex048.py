cont = 0
calc = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        calc += c
        cont += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, calc))