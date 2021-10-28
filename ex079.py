nums = []
var = 0
opc = ''
while True:
    var = int(input('Digite um número: '))
    if var not in nums:
        nums.append(var)
    else:
        print('Valor já existente na lista! Numero nao registrado!')
    opc = str(input('Deseja continuar? S/N: ')).strip().upper()
    if opc == 'N':
        break
print(f'Numeros digitados: {sorted(nums)}')
