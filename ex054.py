import datetime

ano = ''
for c in range(1, 8):
    ano += str(input('Digite o ano da {}ª pessoa: '.format(c)))
    ano += ' '
ano1 = ano.split()
ano2 = ''.join(ano1)
len = len(ano2)
contmen = 0
contmai = 0
dataatual = datetime.date.today()
for c in range(0, len, 4):
    if int(dataatual.year) - int(ano2[c:c + 4]) < 18:
        contmen += 1
    else:
        contmai += 1
print('Somam-se na faixa de MAIORIDADE {} pessoa(s)'.format(contmai))
print('Somam-se ABAIXO da faixa de MAIORIDADE {} pessoa(s)'.format(contmen))
