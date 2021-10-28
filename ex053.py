frase = str(input('Digite a frase: ')).strip().upper()
frasevet = frase.split(' ')
fraseconc = ''.join(frasevet)
#fraseinv = fraseconc[::-1]
fraseinv = ''
for c in range(len(fraseconc) -1, -1, -1):
    fraseinv += fraseconc[c]
print('O inverso da frase {} é {}'.format(fraseconc, fraseinv))
if fraseinv == fraseconc:
    print('A frase é um palíndromo!')
else:
    print('A frase NAO é um palíndromo!')

