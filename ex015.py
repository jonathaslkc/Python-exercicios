d = int(input('Digite a quantidade de dias em que foi alugado: '))
km = float(input('Digite a quilometragem percorrida - Km '))
dv = 60
kmv = 0.15
dp = d*dv
kmp = km * kmv
vf = kmp+dp
print('O carro que percorreu {} km em {} dias, possui débito no valor de {:.2f}'.format(km, d, vf))
