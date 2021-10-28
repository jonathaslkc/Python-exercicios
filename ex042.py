print('=====#=====#' * 5)
print('ANALISADOR DE TRIANGULOS')
print('=====#=====#' * 5)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    if n1 == n2 == n3:
        tp = 'EQUILÁTERO'
    elif n1 != n2 != n3 != n1:
        tp = 'ESCALENO'
    else:
        tp = 'ISOSCELES'
    print('Os segmentos acima podem formar um triangulo!')
    print('Seu triangulo é do tipo {}!'.format(tp))
else:
    print('Nao foi possível formar um triangulo com os segmentos {}, {} e {}'.format(n1, n2, n3))

print('- FIM -')
