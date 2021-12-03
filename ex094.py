cadastro = list()
dados = dict()
opc = ''
media = 0
while True:
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
        if dados['sexo'] == 'M' or dados['sexo'] == 'F':
            break
        else:
            print('ERRO! Favor, digite somente M para Masculino ou F para Feminino!')
    dados['idade'] = int(input('Idade: '))
    cadastro.append(dados.copy())
    media += dados['idade']
    while True:
        opc = str(input('Cadastrar mais um [S/N]? ')).strip().upper()
        if opc == 'S' or opc == 'N':
            break
        else:
            print('ERRO! Favor, digite somente S para Sim, ou N para Nao!')
    if opc == 'N':
        break
media = media/len(cadastro)
print('-=' * 20)
print(f'A) Ao todo temos {len(cadastro)} pessoas cadastradas.')
print(f'B) A média de idade é {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram:', end=' ')
for n in cadastro:
    if n['sexo'] == 'F':
        print(f'({n["nome"]}) ', end='')
print()
print(f'D) A lista das pessoas que estao acima da média:')
for n, i in enumerate(cadastro):
    if i['idade'] >= media:
        print(f'    => Nome: {i["nome"]}; Sexo: {i["sexo"]}; idade: {i["idade"]}')
print('\n<< ENCERRADO >>')
