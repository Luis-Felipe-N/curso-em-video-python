from random import randint
from time import sleep

# FAZER UM PROGAMA QUE SIMULE UM GERADDOR DE PALPITES DA TELESENA
# ONDE O USUÁRIO ESCOLHE QUANTOS PALPITES E OS PALPITES NÃO SE REPITA 


print('-=' * 15)
print('{:^30}'.format('JOGO DA MEGA-SENA'))
print('-=' * 15)


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


print('-=' * 15)
for enumeracao, jogos in enumerate(palpites):
    jogos.sort()
    print(f'Jogo {enumeracao +1} : {jogos}')
    sleep(1)