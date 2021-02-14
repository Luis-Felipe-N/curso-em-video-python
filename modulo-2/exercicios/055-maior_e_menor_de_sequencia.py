# FAZER UM PROGAMA QUE LEIA O PESO DE PESSOAS E MOSTRE O MAIOR E MENOR PESO

lista_peso = []
for x in range(1, 6):
    peso = float(input(f'Digite o peso da {x}ª pessoa: '))
    lista_peso.append(peso)
print('O menor peso lido foi {}.'.format(min(lista_peso)))
print('O maior peso lido foi {}.'.format(max(lista_peso)))