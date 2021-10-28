print('{:=^40}'.format(' LOJAS BOND '))
descdin = 10
descdeb = 5
juros = 20
compras = float(input('\nValor das compras R$ '))
print('''\nFORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista débito
[ 3 ] 2x no cartao
[ 4 ] 3x ou mais no cartao (limitado a 12x)''')
opcpag = int(input('Qual a opcao desejada? '))
if opcpag == 1:
    vlrpag = compras - (compras * descdin / 100)
    print('\nSua compra de R$ {:.2f} vai custar R$ {:.2f} no final (desconto de {}%).'.format(compras, vlrpag, descdin))
elif opcpag == 2:
    vlrpag = compras - (compras * descdeb / 100)
    print('\nSua compra de R$ {:.2f} vai custar R$ {:.2f} no final (desconto de {}%).'.format(compras, vlrpag, descdeb))
elif opcpag == 3:
    parc = compras / 2
    parctot = parc * 2
    print('\nSua compra de R$ {:.2f} foi divida em 2x com parcelas de R$ {:.2f}'.format(compras, parc, parctot))
    print('Total à pagar R$ {:.2f}.'.format(parctot))
elif opcpag == 4:
    parcpag = int(input('Deseja dividir em quantas parcelas? (a partir de 3x) '))
    if parcpag >= 3 and parcpag <= 12:
        vlrpag = compras + (compras * juros / 100)
        parc = vlrpag / parcpag
        print('\nSua compra de R$ {:.2f} dividida em {}x no cartao terao parcelas de R$ {:.2f}'.format(compras, parcpag, parc))
        print('Total à pagar R$ {:.2f}'.format(vlrpag))
    else:
        print('OPCAO DE PARCELAS INVÁLIDA! FAVOR, REPROCESSAR VENDA!')
else:
    print('OPCAO INVÁLIDA! FAVOR TENTE NOVAMENTE!')
print('\n \nOBRIGADO PELA PREFERENCIA!')
