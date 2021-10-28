palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar',
            'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
cor = {'ver': '\033[1;32m', 'cls': '\033[m'}
'''for i in range(0, len(palavras)):
    print(f'Na palavra {cor["ver"]}{(palavras[i])}{cor["cls"]} temos a(s) vogal(is) ', end='')
    for c in range(0, len(palavras[i])):
        if palavras[i][c] in 'AaEeIiOoUu':
            print(palavras[i][c], end=' ')
    print('')'''
for i in palavras:
    print(f'Na palavra {cor["ver"]}{i.upper()}{cor["cls"]} temos a(s) vogal(is) ', end='')
    for c in range(0, len(i)):
        if i[c].lower() in 'aeiou':
            print(i[c], end=' ')
    print('')
