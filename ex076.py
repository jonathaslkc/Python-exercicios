item = ('Lapis', 1.75, 'Borracha', 2.0, 'Caderno', 15.9, 'Estojo', 25.0, 'Transferidor', 4.2,
        'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
print('-=' * 20)
print('{:^40}'.format(' LISTAGEM DE PRECOS '))
print('-=' * 20)
for i in range(0, len(item), 2):
        print(f'{item[i] :.<20}{" R$ ":.>13}{item[i + 1]:>7.2f}')
print('-=' * 20)
