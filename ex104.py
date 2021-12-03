def leiaint(msg):
    laco = True
    while laco:
        valor = input(msg)
        if valor.isnumeric():
            valor = int(valor)
            return valor
            # laco = False
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido! \033[0m')


n = leiaint('Digite um numero: ')
print(f'Voce acabou de digitar o número {n}')
