import datetime
ano = int(input('Que ano deseja analisar? [Coloque 0 para analisar o ano atual]: '))
if ano == 0:
    date = datetime.date.today()
    ano = date.year
print('O ano {} é bissexto!'.format(ano) if ((ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0)) else 'O ano {} é normal.'.format(ano))
