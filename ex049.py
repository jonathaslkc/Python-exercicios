num = int(input('Qual número deseja ver a tabuada? '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))
