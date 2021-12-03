def voto(ano):
	from datetime import datetime as date
	idade = date.now().year - ano
	if (17 >= idade >= 16) or (idade >= 65):
		return f'Com {idade} anos: VOTO OPCIONAL.'
	elif 64 >= idade >= 18:
		return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
	else:
		return f'Com {idade} anos: NAO VOTA.'


print('-=' * 20)
ano_nasc = int(input('Em que ano voce nasceu? '))
print(voto(ano_nasc))
