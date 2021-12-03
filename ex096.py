def msgTit(txt):
    print('-=' * 15)
    print(f'{txt:^30}')
    print('-=' * 15)


def area(l, c):
    areat = l * c
    print(f'A área de um terreno de {l:.2f}m x {c:.2f}m é de {areat:.2f}m²')


msgTit('CONTROLE DE TERRENOS')
larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
area(larg, comp)
