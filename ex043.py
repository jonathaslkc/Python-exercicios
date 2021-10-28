from math import pow
peso = float(input('Digite o peso (ex.: 99.9) - Kg '))
altura = float(input('Digite a altura (ex.: 1.78) - Metros '))
print('========-------' * 3)
imc = (peso / pow(altura, 2))
if imc < 18.5:
    niv = 'Abaixo do Peso'
    msg = 'ATENCAO!'
elif imc >= 18.5 and imc < 25:
    niv = 'Peso Ideal'
    msg = 'PARABÉNS!'
elif imc >= 25 and imc < 30:
    niv = 'Sobrepeso'
    msg = 'CUIDADO!'
elif imc >=30 and imc < 40:
    niv = 'Obesidade'
    msg = 'ATENCAO!'
else:
    niv = 'Obesidade Mórbida'
    msg = 'ATENCAO, MUITO CUIDADO!'
print('IMC é de {:.2f} kg/m³'.format(imc))
print('{} - Está na seguinte faixa: {}!!'.format(msg, niv))
