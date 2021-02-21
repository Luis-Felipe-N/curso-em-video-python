# FAZER UM SIMULA DE MATRIZ QUE SOLICITE VALOR PARA 3 LINHAS E 3 COLUNAS
# MOSTRE TAMBÉM
# A SOMA DOS VALORES PARES
# A SOMA DOS VALORES DA TERCEIRA COLUNA
# O MAIOR NÚMERO DA SEGUNDA LINHA

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = soma_coluna = 0 

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para {[l]},{[c]}: '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            soma_coluna += matriz[l][c]
 
print('-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            print(f'\033[32m[{matriz[l][c]:^5}]\033[m', end="")
        else:
            print(f'\033[31m[{matriz[l][c]:^5}]\033[m', end="")
    print()

print('-' * 30)
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna {soma_coluna}')
