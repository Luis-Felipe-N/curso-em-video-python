# CONTADOR COM FOR
'''for x in range(1, 10): # O x É UMA ESTRUTURA DE CONTROLE E O RANGE DETERMINA QUANTAS VEZES O PROGAMA SERÁ EXECULTADO
    print(x) # O x VAI TROCAR CADA VEZ QUE O PROGAMA EXECULTAR, SE O RANGE COMEÇA COM 1 O x VALE 1, DEPOIS 2...
print('FIM!')'''

from time import sleep
i = int(input('inicio: '))# O i É ONDE O PROGAMA IRÁ COMEÇAR
f = int(input('Fim: ')) # O f É ONDE O PROGAMA VAI TERMINAR
p = int(input('Passo: ')) # QUANTOS PASSOS O PROGAMA VAI PULAR
for c in range(i,f+1,p):
    sleep(1)
    print(c)  


# CONTADOR COM WHILE
'''x = 1
while x < 10: ENQUANTO O x SER MENOR QUE DEZ, O PROGAMA SERÁ EXECULTADO NOVAMENTE
    print(x)
    x += 1 # CADA VEZ QUE O PROGAMA EXECULTAR ELE VAI ADICIONAR + 1 PARA x
'''