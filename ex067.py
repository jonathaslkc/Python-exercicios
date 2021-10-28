print('{:-^25}'.format(' TABUADA V3.0 '))
while True:
    num = int(input('Digite um número para formar a tabuada: '))
    print('=-' * 25)
    if num < 0:
        break
    cont = 1
    while cont < 11:
        print(f'{num} x {cont:2} = {num * cont}')
        cont += 1
    print('=-' * 25)

print('TABUADA ENCERRADA!')