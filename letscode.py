# Buscando arquivo e dando print de conteúdo de arquivo txt
"""arq = open('../../desktop/dom_casmurro_cap_1.txt', 'r', encoding='UTF-8')
texto = arq.read()
print(texto)
arq.close()"""
# Buscando arquivo e dando print linha por linha de arquivo txt
import csv

"""arq = open('../../desktop/dom_casmurro_cap_1.txt', 'r', encoding='UTF-8')
lin = arq.readline()
while lin != '':
    print(lin, end='')
    lin = arq.readline()
arq.close()"""
# Buscando arquivo e dando print linha por linha com FOR de arquivo txt
"""arq = open('../../desktop/dom_casmurro_cap_1.txt', 'r', encoding='UTF-8')
for lin in arq:
    print(lin, end='')
arq.close()"""
# Buscando arquivo e abrindo arquivo com WITH que abre e fecha automaticamente após o uso
"""with open('../../desktop/dom_casmurro_cap_1.txt', 'r', encoding='UTF-8') as arq:
    texto = arq.read()
    print(texto)"""
##########################################################################################
# Criacao de arquivo W (ATENCAO que se o nome do arquivo for de um arquivo já existente, ele sobrescreve-o!!!!!
"""with open('../../desktop/caution2.txt', 'w', encoding='UTF-8') as arq:
    arq.write('Hello World!\npython')
    # OU arq.write('Hello World!\n')
    # + ESSA arq.write('python')"""

"""# Criando arquivo csv
import csv

with open('../../desktop/warning.csv', 'w') as arq:
    escritor = csv.writer(arq, delimiter=';', lineterminator='\n')
    lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    escritor.writerows(lista)"""

# Abrindo arquivo csv criado
"""with open('../../desktop/warning.csv', 'r') as arq:
    leitor = csv.reader(arq, delimiter=';', lineterminator='\n')
    print('O conteudo do arquivo é:')
    print(leitor)
    for linha in leitor:
        print(linha)"""

# Abrindo arquivo csv e aplicando filtro (no caso, imprimindo somente aquelas com valores maiores que 1 na col 2)
"""with open('../../desktop/brasil_covid.csv', 'r', encoding='UTF-8') as arq:
    leitor = csv.reader(arq)
    header = next(leitor)
    for linha in leitor:
        if float(linha[2]) > 1:
            print(linha)"""

# Criando arquivo csv com cabecalho
"""with open('../../desktop/warning2.csv', 'w', encoding='utf-8', newline='') as arq:
    escritor = csv.writer(arq)
    escritor.writerow(['NOME', 'SOBRENOME', 'EMAIL', 'GENERO'])
    escritor.writerow(['Jonathas', 'Carvalho', 'jonathaslkc@Hotmai.com', 'Masculino'])"""

# Abrindo arquivo criado
"""with open('../../desktop/warning2.csv', 'r', encoding='utf-8') as arq:
    texto = csv.reader(arq)
    for linha in texto:
        print(linha)"""

# Criando programa para criar arquivo csv DADOS, alimentar, e abrir
"""cabecalho = ['NOME', 'SOBRENOME']
dados = []
opt = input('O que  deseja fazer?\n1 - Cadastrar\n0 - Sair\n --> ')
while opt != '0':
    nome = input('Digite seu nome: ')
    sobrenome = input('Digite seu sobrenome: ')
    dados.append([nome, sobrenome])
    opt = input('O que  deseja fazer?\n1 - Cadastrar\n0 - Sair\n --> ')

with open('../../desktop/dados.csv', 'w', encoding='utf-8', newline='') as arq:
    escritor = csv.writer(arq)
    escritor.writerow(cabecalho)
    escritor.writerows(dados)

with open('../../desktop/dados.csv', 'r', encoding='utf-8') as arq:
    texto = csv.reader(arq)
    for linha in texto:
        print(linha)"""

"""import requests as r

url = 'https://api.covid19api.com/dayone/country/brazil'
resp = r.get(url)
resp.status_code
raw_data = resp.json()
raw_data[0]
final_data = []
for obs in raw_data:
    final_data.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date']])
final_data.insert(0, ['Confirmados', 'Óbitos', 'Recuperados', 'Ativos', 'Data'])
final_data"""


def distinct(seq):
    return list(dict.fromkeys(seq))


print('O  meu  :', end='')
print(distinct([4, 1, 3, 2, 3, 4]))
print('Esperado: [4, 1, 3, 2]')
# [1995681, 1995681, 1995681] should equal [1995681, 4975043]
