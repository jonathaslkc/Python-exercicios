print('=' * 25)
print('{:^25}'.format('TERMOS DE UMA PA'))
print('=' * 25)
ptermo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
termo = ptermo + (10 - 1) * razao
for c in range(ptermo, termo + 1, razao):
    print(c, end=' -> ')
print('ACABOU')
