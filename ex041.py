import datetime

anonasc = int(input('Ano de nascimento: '))

dataatual = datetime.date.today()
difano = dataatual.year - anonasc
print('Voce tem {} anos de idade, sua CATEGORIA é:'.format(difano))
if difano <= 9:
    categoria = 'MIRIM'
elif difano > 9 and difano <= 14:
    categoria = 'INFANTIL'
elif difano > 14 and difano <= 19:
    categoria = 'JUNIOR'
elif difano > 19 and difano <= 25:
    categoria = 'SENIOR'
else:
    categoria = 'MASTER'
print('\033[1;32;40m' + categoria + '\033[m')
