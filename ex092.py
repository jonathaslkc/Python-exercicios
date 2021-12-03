import datetime

dados = dict()
dados['NOME'] = str(input('Nome: '))
dados['IDADE'] = int(input('Ano de Nascimento: '))
dados['IDADE'] = datetime.datetime.now().year - dados['IDADE']
dados['CTPS'] = int(input('CTPS (0 = Nao tem): '))
if dados['CTPS'] != 0:
    dados['APOSENTADORIA'] = int(input('Ano de Contratacao: '))
    dados['APOSENTADORIA'] = (('Quando completar ' + str(35 - (datetime.datetime.now().year - dados['APOSENTADORIA']) + dados['IDADE']) + ' anos')
                              if (datetime.datetime.now().year - dados['APOSENTADORIA']) < 35 else 'Aposentado!')
    dados['SALARIO'] = float(input('Salário R$: '))
    print('-=' * 20)
    for k, v in dados.items():
        print(f'    - {k}: {v}')
else:
    print('-=' * 20)
    for k, v in dados.items():
        print(f'    - {k}: {v}')
