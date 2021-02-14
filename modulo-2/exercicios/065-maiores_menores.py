# FAZER UM PROGAMA QUE LEIA VÁRIOS NÚMEROS 
# MOSTRA A MÉDIA ENTRE TODOS OS NÚMEROS E MOSTRAR O MAIOR E O MENOR NÚMERO

fim = False
cont = 0
numeros = []
while not fim:
    cont += 1
    num = int(input('Digite um número: '))
    numeros.append(num)
    continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if continuar in 'N':
        fim = True
    elif continuar not in 'S':
        print('\033[31mOPÇÃO INVÁLIDA!\033[m')
soma = sum(numeros)
print('A média dos {} números é {:.1f}.'.format(cont, soma / cont))
print('O maior número foi {} e o menor número foi {}.'.format(max(numeros), min(numeros)))