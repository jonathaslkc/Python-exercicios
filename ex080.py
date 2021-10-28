num = []
cont = 0
for c in range(0, 5):
    var = int(input('Digite um número: '))
    if c == 0 or var > num[-1]:
        num.append(var)
    else:
        cont = 0
        while cont < len(num):
            if var <= num[cont]:
                num.insert(cont, var)
                break
            cont += 1
print('-=' * 25)
print(F'A listagem ordenada é a seguinte: {num}')

'''num = []
cont = var = 0
num.append(int(input(f'Digite um número: ')))
for c in range(1, 5):
    var = int(input(f'Digite outro número: '))
    if c == 1:
        if var > num[0]:
            num.append(var)
        else:
            num.insert(0, var)
    else:
        for n in range(0, len(num)):
            if var > num[n]:
                cont = n + 1
            else:
                cont = n
                break
        num.insert(cont, var)
print(f'Segue lista ordenada: {num}')'''
