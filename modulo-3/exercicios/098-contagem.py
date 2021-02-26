from os import system
from time import sleep
# import time

def contador(i, f, p):
    l(f'contador de {i} até {f} de {abs(p)} em {abs(p)}')
    for n in range(i, f +p , p):
        print(f'\033[32m{n}    \033[m', end="", flush=True)
        sleep(0.5)
    print('\033[31mFim!\033[m')


def l(msg):

    print('-' * (len(msg) + 20))
    print(f'{msg.upper():^{len(msg) + 20}}')
    print('-' * (len(msg) + 20))


contador(1, 10, 1)

contador(10, 0, -2)


i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

if p == 0:# SE O NÚMERO FOR 0 VAI VIRAR 1
    p = 1
if i > f:
    if p > 0:
        p = p - (p * 2)
contador(i, f, p)