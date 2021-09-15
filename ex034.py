sal = float(input('Qual o valor do salário R$ '))
const = 1250.00
cores = {
    'negrito': '\033[1m',
    'sublinhado': '\033[4m',
    'verde': '\033[32m',
    'vermelho': '\033[31m',
    'fverm': '\033[41m',
    'fverd': '\033[42m',
    'limpa': '\033[0m'}

if sal > const:
    salr = (sal * 10 / 100) + sal
else:
    salr = (sal * 15 / 100) + sal
print('{1}SALÁRIO CORRIGIDO{0}! {2}Antigo{0} {3}R$ {5:.2f}{0}, {2}Reajustado{0} {4}R$ {6:.2f}{0}'.format(cores['limpa'], cores['negrito'], cores['sublinhado'], cores['vermelho'], cores['verde'], sal, salr))
