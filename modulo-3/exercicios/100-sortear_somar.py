from random import randint
from time import sleep

lista = []

def somarPar():
    soma = 0

    for e, l in enumerate(lista):
        if l % 2 == 0:
            soma += l

    print(f'Somando os números pares de {lista}, temos {soma}')


def sortear():
    print('Sorteando 5 valores: ', end="")

    for n in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n} ', end="", flush="True")
        sleep(0.5)

    print('PRONTO!')
    somarPar()


sortear()

