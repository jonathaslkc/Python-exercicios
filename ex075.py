cont = 0
var = (int(input(f'Digite um número: ')), int(input('Digite mais um número: ')),
       int(input('Digite outro número: ')), int(input('Digite o último número: ')))
for c in var:
    if c % 2 == 0:
        cont += 1
print(f'O valor 9 apareceu {var.count(9)} vezes')
if 3 in var:
    print(f'O valor 3 apareceu na {var.index(3) + 1}ª posicao')
else:
    print('O valor 3 nao foi digitado')
print(f'Os valores pares digitados foram {cont}')
