matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for c2 in range(0, 3):
        matriz[c][c2] = int(input(f'Digite um número [{c, c2}]: '))
print('Matriz: ')
for c3 in range(0, 3):
    for c4 in range(0, 3):
        print(f' [{matriz[c3][c4]:^5}]', end='')
    print()
