num = int(input('Digite um número qualquer: '))
if num % 2 == 1:
    print('O número\033[31m {}\033[0;0m é\033[31m IMPAR!\033[0;0m'.format(num))
else:
    print('O número\033[31m {}\033[0;0m é\033[31m PAR!\033[0;0m'.format(num))
