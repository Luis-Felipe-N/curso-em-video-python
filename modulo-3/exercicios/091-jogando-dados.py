from random import randint
from time import sleep


# FAZER UM PROGAMA QUE SORTEI 4 NÚMERO, IGUAL UM DADOS E COLOCAR EM ORDEM


numeros_jogados = dict()

print('Vamos começar o jogo..')
print('-' * 30)

for x in range(1,5):
    numero_dado = randint(0,6) # GERANDO UM NÚMERO ALEATORIO

    print(f'O jogador{x} jogou {numero_dado}')
    sleep(1)

print('-' * 32)

for 