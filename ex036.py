vlrcasa = float(input('Valor da casa R$ '))
sal = float(input('Seu salário R$ '))
fin = int(input('Quantos anos de financiamento? '))
cores = {
        'red': '\033[1;31m',
        'green': '\033[1;32m',
        'clear': '\033[0m'
        }
prestacao = vlrcasa / (fin * 12)
limpgtsal = sal * 30 / 100
if prestacao <= limpgtsal:
    print('{}FINANCIAMENTO APROVADO!{} Para seu salário de R$ {:.2f}, as parcelas mensais para o financiamento será '
          'de {}R$ {:.2f}{}'.format(cores['green'], cores['clear'], sal, cores['green'], prestacao, cores['clear']))
else:
    print('{}FINANCIAMENTO NEGADO!{} Para pagar uma casa de R$ {:.2f} em {} anos, a prestacao deverá ser de '
          '{}R$ {:.2f}{}'.format(cores['red'], cores['clear'], vlrcasa, fin, cores['red'], prestacao, cores['clear']))


