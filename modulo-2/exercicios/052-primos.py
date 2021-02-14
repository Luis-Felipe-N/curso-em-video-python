# FAZER UM PROGAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE SE ELE É OU NÃO UM NÚMERO PRIMO
num = int(input('DIGITE UM NÚMERO INTEIRO: '))
primos = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end='')
        primos += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
if primos == 2:
    print(f'\n\033[m{num} É UM NÚMERO INTEIRO!')
else:
    print(f'\n\033[m{num} NÃO É UM NÚMERO PRIMO!')