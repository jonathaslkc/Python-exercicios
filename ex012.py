preco = float(input('Digite o preco do produto em R$ '))
desc = 5
vlfinal = preco-((desc/100)*preco)
print('O produto que custava R$ {:.2f}, na promocao com desconto de 5%, vale R$ {:.2f}'.format(preco, vlfinal))
