from uteis.numeros import moeda

valor = float(input('Digite o Preco R$: '))
print(f'A metade de {moeda.format_moeda(valor)} é {moeda.metade(valor, f=True)}')
print(f'O dobro de {moeda.format_moeda(valor)} é {moeda.dobro(valor, f=True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(valor, f=True, porc=10)}')
print(f'Diminuindo 10%, temos {moeda.diminuir(valor, f=True, porc=10)}')
