from random import randint


lista = []
def somarPar():
    soma = 0
    for e, l in enumerate(lista):
        if l % 2 == 0:
            if e == 0:
                n = l
            else:
                n += l
        soma = n
    print(f'Somando os números pares de {lista}, temos {soma}')

def sortear():
    print('Sorteando 5 valores: ', end="")
    for n in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n} ', end="")
    print('PRONTO!')
    somarPar()



sortear()

