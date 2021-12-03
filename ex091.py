from random import randint
from time import sleep
from operator import itemgetter # PARA ORDENAR VALUES DO DICIONARIO E INCLUIR EM OUTRO DICIONARIO/LISTA

ranking = list()
jg = {
    'jogador 1': randint(1, 6),
    'jogador 2': randint(1, 6),
    'jogador 3': randint(1, 6),
    'jogador 4': randint(1, 6)
}
print('VALORES SORTEADOS:')
for k, i in jg.items():
    sleep(0.5)
    print(f'{k} tirou {i} no dado.')
print('-=' * 20)
print(f'{"== RANKING DOS JOGADORES ==":=^40}')
ranking = sorted(jg.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate(ranking):
    sleep(0.8)
    print(f'      {k + 1}º Lugar: {v[0]}, com {v[1]}')

''' MINHA SOLUCAO ################
import random, time
cad = dict()
jgdor = list()
cont = 0
print('Valores sorteados:')
time.sleep(1)
for v in range(0, 4):
    cad['id'] = v + 1
    cad['dado'] = random.randint(1, 6)
    print(f'Jogador {cad["id"]} tirou {cad["dado"]} no dado.')
    if v == 0 or cad['dado'] < jgdor[-1]['dado']:
        jgdor.append(cad.copy())
    else:
        cont = 0
        while cont < len(jgdor):
            if cad['dado'] >= jgdor[cont]['dado']:
                jgdor.insert(cont, cad.copy())
                break
            cont += 1
    time.sleep(0.5)
print('-=' * 20)
print(f'{"== RANKING DOS JOGADORES ==":=^40}')
for k, i in enumerate(jgdor):
    time.sleep(0.8)
    print(f'    {k+1}º Lugar: Jogador {i["id"]}, com {i["dado"]}')'''
