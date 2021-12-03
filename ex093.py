jgd = dict()
gol = list()
partidas = 0
jgd['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Quantas partidas ele jogou: '))
for g in range(0, partidas):
    gol.append(int(input(f'Quanto(s) gol(s) na partida {g}: ')))
jgd['gols'] = gol.copy()
jgd['total'] = sum(gol)
print('-=' * 20)
print(jgd)
print('-=' * 20)
for k, v in jgd.items():
    print(f'{k}: {v}')
print('-=' * 20)
print(f'O Jogador {jgd["nome"].upper()} jogou {partidas} partidas.')
for n in range(0, partidas):
    print(f'     => Na partida {n}, fez {jgd["gols"][n]} ')
print(f'Foi um total de {jgd["total"]} gol(s)')
