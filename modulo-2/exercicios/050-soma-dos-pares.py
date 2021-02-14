# FAZER UM PROGAMA QUE LEIA 6 INPUT E MOSTRE A SOMA SÓ DOS NÚMEROS PARES

s = 0
cont = 0
for c in range(0, 6): # IRÁ EXECUTA 6X VEZES
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0: # SE O n FOR PAR, ACRESCETE NO s
        s += n
        cont += 1
print('VOCÊ INFORMOU {} NÚMEROS PARES E A SOMA DESSES FALORES É {}'.format(cont, s))
