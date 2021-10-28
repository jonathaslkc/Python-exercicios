num = int(input('Digite um número qualquer: '))
cor = {
    'red':' \033[1;31m',
    'green': '\033[1;32m',
    'yellow': '\033[1;33m',
    'clear': '\033[m'
}
bconv = int(input('Digite o número para converter em: {}[1] - Binário{}; {}[2] - Octal {}ou{} [3] Hexadecimal{}: '
                  .format(cor['red'], cor['clear'], cor['green'], cor['clear'], cor['yellow'], cor['clear'])))
if bconv == 1:
    print('{}-- Binário: {} --{}'.format(cor['red'], bin(num)[2:], cor['clear']))
elif bconv == 2:
    print('{}-- Octal: {} --{}'.format(cor['green'], oct(num)[2:], cor['clear']))
else:
    print('{}-- Hexadecimal: {} --{}'.format(cor['yellow'], hex(num)[2:], cor['clear']))
