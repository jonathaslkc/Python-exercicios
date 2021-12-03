def escreva(titulo):
    tamanho = len(titulo)
    print('~' * (tamanho + int(tamanho/2)))
    print(f'{titulo.upper():^{tamanho + int(tamanho/2)}}')
    print('~' * (tamanho + int(tamanho/2)))



escreva('Jonathas Farias de Carvalho')
