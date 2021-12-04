import urllib.request

# import requests

"""url = 'http://www.google1.com.br'
try:
    print(f'Consegui acessar o site < {url} > com sucesso!' if requests.get(url).status_code == 200 else '')
except Exception as erro:
    print(f'\033[1;41mNao conseguimos acessar o site Pudim... \033[m\n<< {erro} >>')"""

try:
    site = urllib.request.urlopen('http://www.pu2dim.com.br')
except urllib.error.URLError as erro:
    print(f'\033[1;41mNao conseguimos acessar o site Pudim... <{erro}> \033[m')
else:
    print(f'\033[1;42mConsegui acessar o site Pudim com sucesso!\033[m')
