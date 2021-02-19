from random import randint
from time import sleep

# FAZER UM PROGAMA QUE SIMULE UM GERADDOR DE PALPITES DA TELESENA
# ONDE O USUÁRIO ESCOLHE QUANTOS PALPITES E OS PALPITES NÃO SE REPITA 

palpites = []
jogo = []

quant = int(input('Quantas jogos você quer que eu sorteie: '))

for v in range(0, quant):
    while len(jogo) != 6:
        num = randint(0, 60)
        if v == 0:
            jogo.append(num)
        elif num not in jogo:
            jogo.append(num)
    palpites.append(jogo[:])
    jogo.clear()
for e, j in enumerate(palpites):
    print(f'Jogo {e +1} : {j}')
    sleep(1)