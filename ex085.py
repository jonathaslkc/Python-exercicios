tudo = []
geral = list()
par = list()
impar = list()
for c in range(0, 7):
    geral.append(int(input('Digite um número: ')))
    if geral[c] % 2 == 0:
        par.append(geral[c])
    else:
        impar.append(geral[c])
tudo.insert(0, geral[:])
tudo.insert(1, par[:])
tudo.insert(2, impar[:])
    #impar.clear()
    #par.clear()
#    geral.clear()
    #print(tudo)
print('-=' * 25)
print(f'Todos os valores digitados: {sorted(tudo[0])}')
print(f'Valores Pares digitados: {sorted(tudo[1])}')
print(f'Valores Ímpares digitados: {sorted(tudo[2])}')
