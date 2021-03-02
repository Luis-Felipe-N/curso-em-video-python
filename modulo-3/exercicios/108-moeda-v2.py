from ex108 import moeda


num = float(input('Digite um número: '))
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'O aumento de 10% de {moeda.moeda(num)} é {moeda.moeda(moeda.aumentar(num, 10))}')
print(f'A redução de 13% de {moeda.moeda(num)} é {moeda.moeda(moeda.diminur(num, 13))}')