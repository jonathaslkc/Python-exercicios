print('-=' * 20)
print('{:-^40}'.format(' CAIXA - BANCO JFC '))
print('-=' * 20)
print('')
n = 'a'
print (n[0] in 'asd')
valorsacado = int(input('Digite o valor a ser sacado (sem centavos) R$ '))

real = 50
cedulas = 0
resto = valorsacado

while True:
    if resto >= real:
        resto -= real
        cedulas += 1
    else:
        if cedulas > 0:
            print(f'foram {cedulas}x cedulas de R$ {real},00')
        if real == 50:
            real = 20
        elif real == 20:
            real = 10
        elif real == 10:
            real = 1

        cedulas = 0

        if resto == 0:
            break

print('-=' * 20)
print('SAQUE REALIZADO! TENHA UM BOM DIA!')
print('-=' * 20)


'''print('-=' * 20)
print('{:-^40}'.format(' CAIXA - BANCO JFC '))
print('-=' * 20)
print('')
segue = False
real1 = 1
real10 = 10
real20 = 20
real50 = 50
resto = calc20 = calc10 = calc1 = 0
valorsacado = int(input('Digite o valor a ser sacado (sem centavos) R$ '))
calc50 = valorsacado // real50
if calc50 * real50 == valorsacado:
    segue = True
else:
    resto = valorsacado - calc50 * real50
    calc20 = resto // real20
    if calc20 * real20 == resto:
        segue = True
    else:
        resto -= calc20 * real20
        calc10 = resto // real10
        if calc10 * real10 == resto:
            segue = True
        else:
            resto -= calc10 * real10
            calc1 = resto // real1
            if calc1 * real1 == resto:
                segue = True
if segue:
    print('-=' * 20)
    print('SAQUE EFETUADO COM SUCESSO!')
    print(f''Foram: 
    {calc50: ^3}x notas de R$ 50,00
    {calc20: ^3}x notas de R$ 20,00
    {calc10: ^3}x notas de R$ 10,00
    {int(calc1): ^3}x notas de R$  1,00
    ------------------------
    TOTAL =       R$ {(calc1 * real1) + (calc10 * real10) + (calc20 * real20) + (calc50 * real50):.2f}
    '')
else:
    print('ERRO! OPERACAO CANCELADA!')'''