from math import sin, cos, tan, radians

ang = float(input('Digite o angulo que voce deseja: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O Seno     do angulo {} é igual a {:.2f}'.format(ang, sen))
print('O Coseno   do angulo {} é igual a {:.2f}'.format(ang, cos))
print('A tangente do angulo {} é igual a {:.2f}'.format(ang, tan))
