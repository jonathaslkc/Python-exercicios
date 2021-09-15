import math

o = float(input('Comprimento do cateto oposto: '))
a = float(input('Comprimento do cateto adjacente: '))
#h = math.sqrt(((math.pow(o, 2))+(math.pow(a, 2))))
h = math.hypot(o, a)
#h = (o**2 + a**2)**(1/2)
print('A hipotenusa dos catetos é: {:.2f}'.format(h))
