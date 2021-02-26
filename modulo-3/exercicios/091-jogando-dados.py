from random import randint
from time import sleep
from operator import itemgetter

# FAZER UM PROGAMA QUE SORTEI 4 NÚMERO, IGUAL UM DADOS E COLOCAR EM ORDEM

numeros_jogados = {}
ranking = {}

print('Vamos começar o jogo..')
print('-' * 30)

for x in range(1,5):
    numero_dado = randint(0,6) # GERANDO UM NÚMERO ALEATORIO
    print(f'O jogador{x} jogou {numero_dado}')
    sleep(1)
    numeros_jogados[f'jogador{x}'] = numero_dado
print('-' * 32)
print(f'{"GANHADOR":-^32}')
ranking = sorted(numeros_jogados.items(), key=itemgetter(1), reverse=True)
for e, rank in enumerate(ranking):
    print(f'{e +1}ª-{rank[0]} JOGOU {rank[1]}')
