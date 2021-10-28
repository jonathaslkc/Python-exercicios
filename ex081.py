nums = []
while True:
    nums.append(int(input('Digite um número: ')))
    opc = str(input('Deseja continuar? S/N ')).strip().upper()
    if opc == 'N':
        break
print('-=' * 25)
print(f'Voce digitou {len(nums)} elementos')
print(f'Os valores em ordem decrescente sao: {sorted(nums, reverse=True)}')
print('O valor 5 foi digitado!' if 5 in nums else 'Nao encontramos o valor 5!')
