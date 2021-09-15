nomec = str(input('Digite seu nome completo: ')).strip()
nometrunc = nomec.split()
print('Seu primeiro é: {}'.format(nometrunc[0]))
print('Seu ultimo nome é: {}'.format(nometrunc[len(nometrunc) - 1]))
