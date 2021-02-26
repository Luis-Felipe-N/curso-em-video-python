def area(c, l):
    area = c * l
    print(f'A área é {area:.2f} m²')



def l():
    print('-' * 30)

l()
print(f'{"CALCULADOR DE AREA":^30}')
area(c=float(input('\nComprimento: m²')), l=float(input('Largura: m²')))