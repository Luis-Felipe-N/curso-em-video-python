# FAZER UM PROGAMA QUE LEIA QUATRO VALORES E GUARDE EM UMA TUPLA

t = '',
cont9 = cont_par = p3 = 0
for x in range(1, 5):
    n = int(input("Digite um número: ")),
    t += n
print(f'Você digitou os valores {t[1:]}')
for pos, x in enumerate(t):
    if x == 9:
        cont9 += 1
    if x == 3:
        p3 +=  1
    if pos >= 1:
        if x % 2 == 0:
            cont_par += 1
        
print(f'O 9 apareceu {cont9} vezes')
if p3 > 0:
    print(f'O 3 está na posição {t.index(3)}ª posição')
else:
    print('Você não digite nenhum 3')
print(f'Valores pares digitados foram {cont_par}')