ficha = dict()
ficha['nome'] = str(input('Nome: '))
ficha['media'] = float(input(f'Média do {ficha["nome"]}: '))
if ficha['media'] >= 7:
    ficha['status'] = 'APROVADO'
elif (ficha['media'] < 7) and (ficha['media'] >= 5):
    ficha['status'] = 'RECUPERACAO'
else:
    ficha['status'] = 'REPROVADO'
print('-=' * 20)
for k, v in ficha.items():
    print(f' - {k} é igual a {v}')
