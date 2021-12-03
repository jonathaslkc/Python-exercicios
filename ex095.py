jgd = dict()
gol = list()
cadastro = list()
listar = partidas = 0
opc = ''
while True:
    jgd['nome'] = str(input('Nome do jogador: ')).title().strip()
    partidas = int(input('Quantas partidas ele jogou: '))
    for g in range(0, partidas):
        gol.append(int(input(f' -Quanto(s) gol(s) na partida {g}: ')))
    jgd['gols'] = gol.copy()
    jgd['total'] = sum(gol)
    gol.clear()
    cadastro.append(jgd.copy())
    while True:
        opc = str(input('Deseja cadastrar mais jogados S/N? ')).upper().strip()
        if opc == 'S' or opc == 'N':
            break
        else:
            print('ERRO! Digite uma opcao válida!')
    if opc == 'N':
        break
print('-=' * 20)
print(f'{"COD":<5}{"NOME":<10}{"GOLS":<20}{"TOTAL":<5}')
print('-' * 40)
for i, n in enumerate(cadastro):
    print(f'{i:<5}{n["nome"]:<15}{str(n["gols"]):<15}{n["total"]:<5}')
print('-=' * 20)
while True:
    listar = int(input('Mostrar dados de qual jogador (999 p/ parar)? '))
    if listar == 999:
        break
    elif listar >= 0 and listar <= len(cadastro):
        print(f'    => LEVANTAMENTO DO JOGADOR {cadastro[listar]["nome"]}: ')
        for i, v in enumerate(cadastro[listar]['gols']):
            print(f'        - No jogo {i + 1} fez {v} gols.')
    else:
        print('OPCAO INVÁLIDA! CÓDIGO INEXISTENTE NO CADASTRO!')
    print('-' * 40)
print('\n<<< PROGRAMA ENCERRADO! >>>')
print('<< VOLTE SEMPRE! >>')