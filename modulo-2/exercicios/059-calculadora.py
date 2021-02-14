from time import sleep
# FAZER UM PROGAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU DE OPÇÕES NA TELA
'''
[ 1 ] - SOMAR
[ 2 ] - MULTIPLICAR
[ 3 ] - MAIOR 
[ 4 ] - NOVOS NÚMEROS
[ 5 ] - SAIR DO PROGAMA
'''

n = 1
n1 = float(input('Digite o primero número: '))
n2 = float(input('Digite o segundo número: '))

while n == 1:
    print('''
    ESCOLHA UMA OPÇÃO
    [ 1 ] - SOMAR
    [ 2 ] - MULTIPLICAR
    [ 3 ] - MAIOR
    [ 4 ] - NOVOS NÚMEROS
    [ 5 ] - SAIR DO PROGAMA''')
    op = int(input('SUA OPÇÃO: '))
    if op == 1:
        print(f'A soma dos valores entre {n1} + {n2} é {n1 + n2}')
    elif op == 2:
        print(f'A multiplicação entre {n1} * {n2} é {n1 * n2}.')
    elif op == 3:
        print(f'O maior número entre {n1} e {n2} é {max(n1, n2)}')
    elif op == 4:
        n1 = float(input('Digite um novo número: '))
        n2 = float(input('Digite outro número:'))
    elif op == 5:
        n = 0
        sleep(1)
        print('Finalizando..')
    else:
        print('{} não é uma opção válida!'.format(op))
    sleep(1)
print('ACABOU')