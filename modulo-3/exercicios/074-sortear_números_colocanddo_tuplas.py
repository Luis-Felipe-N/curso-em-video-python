from random import randint
# FAZER UM PROGAMA QUE SORTEI 5 NÚMERO E COLOQUE EM UMA TUPLA
# DEPOIS MOSTRE O MAIOR O MENOR E OS NÚMEROS SOTEADOS
t = ('',)
for n in range(0,5):
    ns = randint(0,10),
    t += ns
print(f'Os números sorteados foi {t[1:]}')
print(f'O maior número é o {max(t[1:])}\nO menor número é o {min(t[1:])}')