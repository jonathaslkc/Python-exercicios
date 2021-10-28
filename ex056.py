cor = {
    'a': '\033[1;33m',
    'l': '\033[m'
}
media = 0
idademaisv = 0
contmulher = 0
nomemaisv = ''
for c in range(1, 5):
    print('DADOS DA {}ª PESSOA'.format(c))
    nome = str(input('Nome: ')).upper().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo ({}M{} p/ masc. ou {}F{} p/ fem.): '.format(cor['a'], cor['l'], cor['a'], cor['l']))).upper()
    media += idade
    if sexo == 'M':
        if idade > idademaisv:
            nomemaisv = nome
            idademaisv = idade
    if sexo == 'F':
        if idade < 20:
            contmulher += 1
media = media / 4
print('\nA média de idade do grupo é de {:.2f} anos'.format(media))
print('O homem mais velho tem {} anos e seu nome é {}'.format(idademaisv, nomemaisv))
print('No grupo tem {} mulheres abaixo de 20 anos'.format(contmulher))
