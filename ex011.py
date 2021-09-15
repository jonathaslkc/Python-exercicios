lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
tinta = 2
area = lar*alt
calc = (area/tinta)#*10
print('Sua parede tem a dimensao de {}x{} e sua área é de {}m².'.format(lar, alt, area))
#1l de tinta pinta 2m²
print('Para pintar essa parede, voce precisará de {}l de tinta.'.format(calc))