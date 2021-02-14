# FAZER UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E UMA RAZÃO DE UMA PROGRESSÃO ARITMÉTICA
# MOSTRAR OS 10 PRIMEIROS TERMOS DA PROGRESSÃO ARITMÉTICA

pa = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
n = 0

while n != 10:
    n += 1
    if n != 10:
        print(pa , '-> ', end='')
    else:
        print(pa)
    pa += razao