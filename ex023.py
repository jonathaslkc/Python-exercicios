num = int(input('Digite um numero entre 0 a 9999: '))
numstr = str(num)
nums = ' '.join(numstr)
nums2 = nums.split(' ')
numinv = nums2[::-1]
print('Unidade: {}'.format(numinv[0]))
print('Dezena: {}'.format(numinv[1]))
print('Centena: {}'.format(numinv[2]))
print('Milhar: {}'.format(numinv[3]))
