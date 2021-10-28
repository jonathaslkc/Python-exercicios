n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
ma = 7.0
mr = 4.9
print('Com as suas notas {:.2f} e {:.2f}, obteve a média {:.2f}.'.format(n1, n2, m))
if m >= ma:
    print('O aluno está Aprovado!')
elif m >= mr:
    print('O aluno está de Recuperacao!')
else:
    print('O aluno está Reprovado!')
