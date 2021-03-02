from ex107 import moeda

num = float(input('Digite um número: R$'))
print(f'A metade de R${num} é R${moeda.metade(num)}')
print(f'O dobro de R${num} é R${moeda.dobro(num)}')
print(f'O aumento de 10% de R${num} é R${moeda.aumentar(num, 10)}')
print(f'A redução de 13% de R${num} é R${moeda.diminur(num, 13)}')
