# FAZER UM PROGAMA QUE LEIA QUATRO VALORES E GUARDE EM UMA TUPLA E MOSTRE
# QUANTAS VEZES CADA QUE O 9 APARECEU
# EM QUE POSIÇÃO O 3 APARECE
# QUANTOS VALORES PARES FORAM MODIFICADO 

# !MODIFIQUEI A SINTAXE COM BASE NA RESOLUÇÃO!
# SIM, PODEMOS FAZER UMA TUPLA COM VARIOS INPUT
n = (int(input("Digite um número: ")), 
    int(input("Digite um número: ")),
    int(input("Digite um número: ")), 
    int(input("Digite um número: ")))

cont_par = 0


print(f'Você digitou os números: {n}')
print(f'O 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O 3 está na posição {n.index(3) + 1}ª posição')
else:
    print('Você não digite nenhum 3')
for x in n:
    if x % 2 == 0:
           cont_par += 1
print(f'Valores pares digitados foram {cont_par}')