# FAZER UM PROGAMA QUE MOSTRE O ITEM E O PREÇO QUE ESTÃO DENTRO DE UMA ÚNICA TUPLA, NA MESMA LINHA COMO UMA NOTA FISCAL
lista_precos = 'Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.00 ,'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90

print('-' * 39)
print('{:^39}'.format('NOTA FISCAL'))
print('-' * 39)
for pos, item in enumerate(lista_precos):
    if pos % 2 == 0:# COMO OS ITENS ESTÃO NUMA POSIÇÃO PAR, DÁ PARA SEPARAR OS ITENS DOS PREÇOS
        print(item, end='')
        print('.' * (30 - len(item)), end='R$')
    else:
        print('{:>7}'.format(f'{item}'))