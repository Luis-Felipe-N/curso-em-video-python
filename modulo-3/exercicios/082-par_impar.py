# FAZER UM PROGAMA QUE LEIA VÁRIOS NÚMEROS E COLOCAR EEM UMA LISTA
# DEPOIS DISSO CREI DUAS LISTA EXTRAS QUE VÃO TER VALORES PARES E ÍMPARE
# NO FINAL MOSTRE AS 3 LISTAS

pares = list()
impares = list()
valores = list()

while True:
    valores.append(int(input('Digite um números: ')))
    continuar = str(input('Desaja ccontinuar [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Desaja ccontinuar [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Você digitou os seguintes números: {valores}')
print(f'Você digitou os seguintes números pares: {pares}')
print(f'Você digitou os seguintes números impares: {impares}')