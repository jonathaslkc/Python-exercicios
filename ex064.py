num = soma = cont = 0
num = int(input('Digite o 1º número [999 p/ parar]: '))
while not num == 999:
    cont += 1
    soma += num
    num = int(input('Digite o {}º número [999 p/ parar]: '.format(cont + 1)))
print('\nRESULTADO:')
print('Foram digitados {} números e a soma deu {}'.format(cont, soma))
