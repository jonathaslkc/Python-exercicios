dist = float(input('Qual a distancia da sua viagem? '))
print('Voce está prestes a comecar uma viagem de {:.1f} km.'.format(dist))
custoc = 0.5
custol = 0.45
if dist <= 200:
    preco = dist * custoc
else:
    preco = dist * custol
print('E o preco da sua passagem será de R$ {:.2f}'.format(preco))
