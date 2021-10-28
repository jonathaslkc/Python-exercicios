maisbarato = prodbarato = total = prod1000 = 0
prodnome = ''

print('{:=^50}'.format('SISTEMA DE VENDAS COM ESTATATÍSTICAS'))
while True:
    nome = str(input('Nome do produto: ')).strip().upper()
    preco = float(input('Preco R$ '))
    total += preco

    if preco > 1000.00:
        prod1000 += 1

    if maisbarato == 0 or preco < maisbarato:
        maisbarato = preco
        prodbarato = nome

    pergunta = str(input('Deseja continuar? [S/N] ')).strip().upper()

    while pergunta not in 'SsNs':
        pergunta = str(input('Opcao inválida! Digite S para sim ou N pra nao: '))

    print('-=' * 25)

    if pergunta == 'N':
        print('-=' * 25)
        print('SISTEMA DE VENDAS ENCERRADO')
        print('-=' * 25)
        break
        
print(f'\nTOTAL GASTO: {total:.2f}')
print(f'Tivemos um total de {prod1000} produtos acima de R$ 1000,00.')
print(f'O produto {prodbarato: ^20} foi o mais barato, e custou R$ {maisbarato:.2f}.')
