peso = 0.0
maior = 0.0
menor = 0.0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa Kg '.format(c)))
    if peso > maior:
        maior = peso
    if menor == 0.0:
        menor = peso
    if peso < menor:
        menor = peso
print('O MAIOR peso lido foi {:.2f} Kg e o MENOR {:.2f} Kg'.format(maior, menor))
