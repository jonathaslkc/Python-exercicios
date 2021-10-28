formulario = list()
notas = list()
resp = 'S'
opc = 0
print('-=' * 20)
print(f'{"SISTEMA DE CADASTRO DE NOTAS":^40}')
print('-=' * 20)
while True:
    nome = str(input('Nome: '))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    media = (notas[0] + notas[1]) / 2
    formulario.append([nome, [notas[0], notas[1]], media])
    resp = str(input('Deseja continuar? (S/N) '))
    if resp in 'Nn':
        break
    notas.clear()
print('-=' * 15)
print(f'{"No.":<4}{"NOME":<15}{"MÉDIA":<4}')
print('-' * 30)
for c, inf in enumerate(formulario):
    print(f'{c:<4}', end='')  # NUMERO
    print(f'{inf[0]:<15}', end='')  # NOME
    print(f'{inf[2]:<4}')  # MEDIA
print('-' * 30)
while True:
    opc = int(input('Mostrar notas de qual aluno (999 para sair)? '))
    if opc == 999:
        break
    else:
        print(f'Aluno: {formulario[opc][0]}  - Notas: {formulario[opc][1]}')
        print('')
print('FIM...')
print('VOLTE SEMPRE')

'''nome = list()
notas = list()
dados = list()
cadastro = list()
media = 0.0
opc = 'S'
print('-=' * 20)
print(f'{"SISTEMA DE CADASTRO DE NOTAS":^40}')
print('-=' * 20)
while True:
    if opc == 'S':
        nome.append(str(input('Nome: ').upper().strip()))
        notas.append(float(input('Nota 1: ')))
        notas.append(float(input('Nota 2: ')))
        dados.append(nome[:])
        dados.append(notas[:])
        cadastro.append(dados[:])
        nome.clear()
        dados.clear()
        notas.clear()
        opc = str(input('Deseja continuar? S/N: ')).upper().strip()
    else:
        break
print('-=' * 15)
print(f'{"No.":<4}{"NOME":<15}{"MÉDIA":<4}')
print('-' * 30)
for c, inf in enumerate(cadastro):
    print(f'{c:<4}', end='') #NUMERO
    for cc, inf2 in enumerate(inf):
        if cc % 2 == 0:
            print(f'{inf2[cc]:<15}', end='') #NOME
        else:
            for ccc, inf3 in enumerate(inf2):
                media += inf3
            print(f'{media / 2:<4.2f}') #NOTA
            media = 0
print('-' * 30)
while True:
    opc = int(input('Mostrar notas de qual aluno (999 para sair)? '))
    if opc == 999:
        break
    else:
        print(f'Aluno:{cadastro[opc][0]}  - Notas: {cadastro[opc][1]}')
        print('')
print('FIM...')
print('VOLTE SEMPRE')'''
