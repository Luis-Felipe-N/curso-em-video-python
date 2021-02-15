# FAZER UM PROGAMA QUE LEIA QUATRO VALORES E GUARDE EM UMA TUPLA E MOSTRE
# QUANTAS VEZES CADA QUE O 9 APARECEU
# EM QUE POSIÇÃO O 3 APARECE
# QUANTOS VALORES PARES FORAM MODIFICADO 

# !MODIFIQUEI A SINTAXE COM BASE NA RESOLUÇÃO!
# SIM, PODEMOS FAZER UMA TUPLA COM VARIOS INPUT
n = (int(input("Digite um número: ")), 
    int(input("Digite um número: ")), int(input("Digite um número: ")), 
    int(input("Digite um número: ")))

cont9 = cont_par = p3 = 0

for pos, x in enumerate(n):
    if x == 9:
        cont9 += 1
    if x == 3:
        p3 +=  1
    if pos >= 1:
        if x % 2 == 0:
            cont_par += 1


print(f'Você digitou os números: {n}')
print(f'O 9 apareceu {cont9} vezes')
if p3 > 0:
    print(f'O 3 está na posição {n.index(3)}ª posição')
else:
    print('Você não digite nenhum 3')
print(f'Valores pares digitados foram {cont_par}')