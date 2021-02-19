matriz = [[], [], []]

cont = 0
for m in range(0,9):
    if m < 3:
        vm = int(input(f'Digite um valor para [0, {cont}]: '))
        matriz[0].append(vm)
        cont += 1
    elif m < 6:
        vm = int(input(f'Digite um valor para [1, {cont - 3}]: '))
        matriz[1].append(vm)
        cont += 1
    elif m < 9:
        vm = int(input(f'Digite um valor para [2, {cont - 6}]: '))
        matriz[2].append(vm)
        cont += 1
print(f'[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]\n[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]\n[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]')