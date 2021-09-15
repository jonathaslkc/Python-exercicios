print('=====#=====#' * 5)
print('ANALISADOR DE TRIANGULOS')
print('=====#=====#' * 5)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if ((n1 + n2) < n3) or ((n1 + n3) < n2) or ((n3 + n2) < n1):
    print('Nao foi possível formar um triangulo com os segmentos {}, {} e {}'.format(n1, n2, n3))
else:
    print('Os segmentos acima podem formar um triangulo!')
print('- FIM -')
