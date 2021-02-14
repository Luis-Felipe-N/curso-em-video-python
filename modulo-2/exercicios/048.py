# FAZER UM PROGAMA QUE SOME TODOS OS NÚMEROS IMPARES MULTIPLOS DE 3
# E QUE SE ENCONTRAM ENTRE 1 E 500
s = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        cont += 1
        s += c
print('A SOMA DOS {} NÚMEROS SOMADOS É {}'.format(cont, s))