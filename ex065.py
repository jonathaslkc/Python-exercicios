maior = menor = media = soma = cont = 0
opc = 'S'
while not opc == 'N':
    cont += 1
    num = int(input('Digite o {}º número: '.format(cont)))
    opc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while not opc in 'NnSs':
        print('OPCAO INVÁLIDA! Digite novamente...')
        opc = str(input('Deseja continuar? [S/N]'))
    soma += num
    if num > maior:
        maior = num
    if cont == 1:
        menor = num
    else:
        if num < menor:
            menor = num
media = soma / cont
print('Voce digitou {} números.'.format(cont))
print('A média deu {}. E o maior foi {} e o menor {}'.format(media, maior, menor))
