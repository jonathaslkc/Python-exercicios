l = list()
expr = str(input('Digite a expressao: '))
for c in expr:
    if c == '(':
        l.append('(')
    elif c == ')':
        if '(' in l:
            l.remove('(')
if l:
    print('Expressao errada!')
else:
    print('Expressao correta!')


'''lista = list()
seg = False
lista.append(str(input('Digite a expressao: ')))
if lista[0].count('(') == 1 and lista[0].count(')') == 1:
    seg = True
else:
    if lista[0].count('(') > 1:
        if lista[0].count('(') % 2 == 0 and lista[0].count(')') % 2 == 0:
            seg = True
    else:
        seg = False
if seg:
    print(f'Expressao: {lista}')
else:
    print('Expressao incorreta!')'''
