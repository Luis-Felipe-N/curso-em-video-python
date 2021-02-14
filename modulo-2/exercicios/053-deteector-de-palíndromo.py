# FAZER UM PROGAMA QUE LEIA UMA FRASE E MOSTRE SE ELA É OU NÃO PALÍNDRIMO
# PALÍNDROMO SÃO PALAVRAS QUE SE LÉ DA MESMA FORMA DE TRÁS PARA FRENTE E FRETE PARA TRÁS

# PEDINDO A FRASE
# COM O METODO UPPER() VAMOS DEIXAR TODAS MAIUSCULA
# COM REPLACE() VAMOS TIRAR OS ESPAÇOS
frase = str(input('DIGITE UMA FRASE SEM (acentos): ')).upper()

# TIRANDO OS ESPAÇOS
frase_sem_espaco = (frase.replace(' ', ''))

# INVERTENDO A FRASE || [a:b:c] || COMO O a E O b É ZERO, VAI LER A FRASE INTEIRA
# E COMO O c É -1, VAI LER DE TRÁS PARA FRENTE
invertida = frase_sem_espaco[::-1]

print('O inverso de {} é {}.'.format(frase_sem_espaco, invertida))
# VENDO SE É UM PALÍNDROMO
if frase_sem_espaco == invertida:
    print('\033[32mA PALAVRA\033[35m "{}" \033[32mÉ UM PALÍINDROMO!\033[m'.format(frase))
else:
    print('\033[36m{} \033[31mNÃO É PALINDROMO\033[m'.format(frase))