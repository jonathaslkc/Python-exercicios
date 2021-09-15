nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
nome = nome.strip()

#find = nome.find(' ')
#pnome = nome[:find]

pnome = nome.split(' ')
nomecom = ''.join(pnome)
print('Seu nome em maiúsculo é: {}'.format(nome.upper()))
print('Seu nome em minúsculo é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} caracteres'.format(len(nomecom)))
print('Seu primeiro nome é {} e ele tem {} letras'.format(pnome[0], len(pnome[0])))
