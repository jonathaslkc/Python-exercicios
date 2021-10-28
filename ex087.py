matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
m2l = nt = np = 0
print(f'{"Teste"}')
for c1 in range(0, 3):
    for c2 in range(0, 3):
        matriz[c1][c2] = int(input(f'Digite quanto a célula {c1, c2} receberá: '))
for c1 in range(0, 3):
    for c2 in range(0, 3):
        print(f'[{matriz[c1][c2]:^5}]', end=' ')
        if c1 == 1 and c2 == 0:
            m2l = matriz[c1][c2]
        elif c1 == 1:
            if matriz[c1][c2] > m2l:
                m2l = matriz[c1][c2]
        if matriz[c1][c2] % 2 == 0:
            np += matriz[c1][c2]
        if c2 == 2:
            nt += matriz[c1][c2]
    print()
print('-=' * 20)
print(f'A soma dos números pares é {np}')
print(f'A soma dos números da terceira coluna é {nt}')
print(f'O maior valor da segunda linha é {m2l}')
