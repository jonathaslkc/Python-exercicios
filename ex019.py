import random

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
a = [n1, n2, n3, n4]
sort = random.choice(a)
print('O aluno escolhido foi: {}'.format(sort))
