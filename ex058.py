from random import randint

print('Sou seu pc... Acabei de pensar em um número de 0 a 10')
print('Será que vc consegue advinhar qual foi?')
palpitepc = randint(0, 10)
cont = 1
palpite = int(input('Qual seu palpite? '))
while palpite != palpitepc:
    if palpite < palpitepc:
        print('Mais... tente novamente.')
        cont += 1
    if palpite > palpitepc:
        print('Menos... tente novamente')
        cont += 1
    palpite = int(input('Qual teu novo palpite? '))
print('BOA... Vc venceu! O número escolhido era {}. E vc acertou na {}ª tentativa!'.format(palpitepc, cont))
