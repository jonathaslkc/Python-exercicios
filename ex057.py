sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Opcao inválida! Favor digite novamente o sexo [M/F]: ')).upper().strip()[0]
print('O sexo {} foi escolhido com sucesso!'.format(sexo))
