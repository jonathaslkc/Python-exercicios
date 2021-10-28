cont = 1
conth = contm = mais18 = 0
while True:
    idade = input(f'Idade da {cont}ª pessoa: ')

    while True:
        if not idade.isdigit():
            idade = input(f'Número inválido! Digite novamente a idade da {cont}º pessoa: ')
        else:
            idade = int(idade)
            break

    sexo = str(input(f'Sexo da {cont}ª pessoa [M/F]: ')).strip().upper()

    while sexo not in 'MmFf':
        sexo = str(input(f'Dados de sexo inválido! Digite M pra masculino ou F para feminino: ')).strip().upper()

    if idade >= 18:
        mais18 += 1

    if sexo == 'M':
        conth += 1

    if sexo == 'F' and idade < 20:
        contm += 1

    print('-=' * 30)
    pergunta = str(input('Deseja cadastrar mais? [S/N]: ')).strip().upper()

    while pergunta not in 'SsNn':
        pergunta = str(input('Opcao inválida! Informe S para sim ou N para nao: ')).strip().upper()

    if pergunta == 'N':
        print('-' * 20)
        print('Sistema de cadastro finalizado!')
        print('-' * 20)
        break

    cont += 1

print('-=' * 30)
print('DADOS ESTATÍSTICOS:\n')
print(f'Foram cadastrados {cont} pessoas.')
print(f'{mais18} sao maiores que 18 anos.')
print(f'{conth} homens cadastrados.')
print(f'{contm} mulheres tem menos de 20 anos')
