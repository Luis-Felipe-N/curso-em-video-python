from random import shuffle
# pegar 4 nomes em qualquer ordem e embaralhar



# 1-pegar os 4 nomes com o input e guarda em uma variavel 
n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceio nome: ')
n4 = input('Quarto nome: ')

# 2-criar uma lista com esse nomes
lista = [n1, n2, n3, n4]

# 3-embaralhar a lista
shuffle(lista)

# 4-mostrar o resultado
print(f'A ordem de apresentação do trabalho é {lista}.')