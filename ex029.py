vel = int(input('Qual a velocidade do carro? '))
velm = 80
vmult = 7.00
if vel > velm:
    multa = (vel - velm) * vmult
    print('\033[31m MULTADO! Voce excedeu o limite permitido que é de 80km/h! \033[0;0')
    print('\033[31m Voce deve pagar uma multa de \033[33m R$ {:.2f} \033[0;0m'.format(multa))
print('Tenha um bom dia! Dirija com seguranca.')