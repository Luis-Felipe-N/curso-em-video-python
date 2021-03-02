from ex109 import moeda


num = float(input('Digite um número: '))
print(f'A metade de {moeda.meoda(num)} é {moeda.metade(num, False)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num)}')
print(f'O aumento de 10% de {num} é {moeda.aumentar(num, 10)}')
print(f'A redução de 13% de {num} é {moeda.diminur(num, 13)}')