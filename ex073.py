times = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Flamengo', 'Bragantino', 'Corinthians', 'Internacional',
         'Fluminense', 'Athletico-PR', 'Cuiabá', 'Ceará', 'Atlético-GO', 'São Paulo', 'Juventude', 'América-MG',
         'Santos', 'Bahia', 'Grêmio', 'Sport', 'Chapecoense')

print('-=' * 25)
print('Lista de Times do Brasileirao: ', times)
print('-=' * 25)
print('Os 5 primeiros sao:', times[0:5])
print('-=' * 25)
print('Os 4 últimos sao: ', times[-4:])
print('-=' * 25)
print('Times em Ordem Alfabética: ', sorted(times))
print('-=' * 25)
print(f'O Flamengo está na {times.index("Flamengo") + 1}ª posicao')
