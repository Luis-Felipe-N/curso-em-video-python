# FAZER UM PROGAMA QUE MOSTRA UMA DETERMINADA SEQUENCIA DE FIBONACCI
# SEQUENCIA DE FIBOBACCI É UM NÚMERO SOMADO COM SEU ANTECESSOR
# SENDO O 1 SE REPETINDO E DEPOIS 2 + 1 = 3 3 + 2 = 5 5 + 3 = 8...

print('{:=^80}'.format(' \033[31m SEQUÊNCIA DE FIBONACCI\033[m '))
cont = 0
f1 = 0
f2 = 1
quant = int(input('Quantos termos: '))
cont = 0
while cont != quant:
    cont += 1
    if cont == 1:
        fn = 0
    elif cont <= 2:
        fn = 1
    else:
        fn = f1 + f2
        f1 = f2
        f2 = fn
    if cont != quant:
        print(fn , '-> ', end='')
    else:
        print(fn)