print('--- SEQUENCIA DE FIBONACCI ---')
n = int(input('Digite um numero: '))
primeiro = 0
segundo = 1
calc = 0
cont = 0
print('FIBONACCI: {} - {}'.format(primeiro, segundo), end=' - ')
while not cont == n - 2:
    calc = primeiro + segundo
    primeiro = segundo
    segundo = calc
    print('{}'.format(calc), end='')
    print(' - ' if cont < (n - 3) else '', end='')
    cont += 1

