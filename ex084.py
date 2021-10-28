dados = []
pessoas = list()
opc = ''
mai = men = 0
while True:
    dados.append(str(input('Nome: ')).strip().upper())
    dados.append(float(input('Peso Kg ')))
    if dados[1] > mai:
        mai = dados[1]
    if not pessoas:
        men = dados[1]
    if dados[1] < men:
        men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    opc = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if opc == 'N':
        break
print('-=' * 25)
print(f'Foram detectados {len(pessoas)} cadastros!')
for d in pessoas:
    if mai == d[1]:
        dados.append(d[0])
print(f'As pessoas mais pesadas, com {mai} Kg, sao: {dados}')
dados.clear()
for d in pessoas:
    if men == d[1]:
        dados.append(d[0])
print(f'As pessoas mais leves, com {men} Kg, sao: {dados}')
dados.clear()
