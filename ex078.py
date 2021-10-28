listnum = []
indme = indma = ''
for i in range(0, 5):
    listnum.append(int(input(f'Digite o {i}ª número: ')))
menor = min(listnum)
maior = max(listnum)
for i, n in enumerate(listnum):
    if menor == n:
        indme += str(i) + '.. '
    if maior == n:
        indma += str(i) + '.. '
print(f'Voce digitou os valores {listnum}')
print(f'O maior valor digitado foi {maior} que está presente no(s) índice(s) {indma}')
print(f'O menor valor digitado foi {menor} que está presente no(s) índice(s) {indme}')
