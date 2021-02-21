# matriz = [[], [], []]
# cont = 0
# for m in range(0,9):
#     if m < 3:
#         vm = int(input(f'Digite um valor para [0, {cont}]: '))
#         matriz[0].append(vm)
#         cont += 1
#     elif m < 6:
#         vm = int(input(f'Digite um valor para [1, {cont - 3}]: '))
#         matriz[1].append(vm)
#         cont += 1
#     elif m < 9:
#         vm = int(input(f'Digite um valor para [2, {cont - 6}]: '))
#         matriz[2].append(vm)
#         cont += 1
# print(f'[{matriz[0][0]}] [ {matriz[0][1]} ] [ {matriz[0][2]} ]\n[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]\n[ {matriz[2][0]} ] [ {matriz[2][1]} ] [{matriz[2][2]}:^5]')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para {[l]}, {[c]}: '))

# UM LAÇO PARA MOTRAR OS RESULTADOS

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end="")
    print() # QUEBRAR A LINHA