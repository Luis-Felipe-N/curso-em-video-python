# FAZER UM PROGAMA QUE LEIA 7 VALORES NÚM, CADASTRAR EM UM ÚNICA LISTA SEPARADAS POR NÚMS PAR E ÍMPARES, NO FINAL MOSTRA OS VALORES PARES E ÍMPARES EM ORDEM CRESCENTE.

valores = [[], []]

for v in range(1, 8):
    valor = int(input(f'Digite o {v}º valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)

valores[0].sort()
valores[1].sort()
print('-' * 33)
print(f'Os valores da lista são \033[34m{valores}\033[m')
print('-' * 33)
print(f'Os valores pares da lista são \033[32m{valores[0]}\033[m')
print('-' * 33)
print(f'Os valores ímpares da lista são \033[35m{valores[1]}\033[m')