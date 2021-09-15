frase = str(input('Escreva uma frase: ')).strip().upper()
print('A letra -a- aparece {} vezes'.format(frase.count('A')))
print('A primeira letra -a- aparece na posicao {}'.format(frase.find('A') + 1))
print('A ultima letra -a- aparece na posicao {}'.format(frase.rfind('A') + 1))

