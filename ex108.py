from uteis.numeros import moeda

valor = float(input('Digite o Preco R$: '))
metade_moeda = moeda.metade(valor)
dobro_moeda = moeda.dobro(valor)
aumento_moeda = moeda.aumentar(valor, porc=10)
print(f'A metade de {moeda.format_moeda(valor)} é {metade_moeda}')
print(f'A dobro de {moeda.format_moeda(valor)} é {dobro_moeda}')
print(f'Aumentando 10%, temos {aumento_moeda}')
