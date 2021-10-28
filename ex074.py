from random import randint
rand = ((randint(0, 9)), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print(f'Os números aleatorios foram {rand}')
print(f'O maior número da sequencia é o {max(rand)}')
print(f'O menor número da sequencia é o {min(rand)}')
