import datetime
anonasc = int(input('Qual o ano de seu nascimento? '))
dataatual = datetime.date.today()
idadelim = 18
saldo = dataatual.year - anonasc
if saldo < idadelim:
    print('Quem nasceu em {} tem {} anos.'.format(anonasc, saldo))
    print('Falta ainda {} anos para voce ser alistável ao Servico Militar.'.format(idadelim - saldo))
    print('Seu alistamento será em {}'.format(anonasc + idadelim))
elif saldo == idadelim:
    print('\033[1;32;40mGuerreiro! Este é seu ano para poder alistar-se ao Servico Militar!\033[m')
else:
    print('\033[1;31mPeríodo de alistamento ultrapassado em mais de {} anos!\033[m'.format(saldo - idadelim))
    print('\033[1;31mSeu alistamento foi em {}\033[m'.format(anonasc + idadelim))
