# FAZER UM PROGAMA QUE LEIA VÁRIAS PALAVRAS DE UMA TUPLAS E MOSTRE AS SUAS VOGAIS

palavras = 'aprender', 'sabedorida', 'faculdade', 'estudar', 'amor', 'python', 'django', 'javascript'
for palavra in palavras:# SEPARAR AS PALAVRAS
    vogais = ''
    for letra in palavra:# SEPARAR AS LETRAS
        if letra in 'aeiou':# SE NA LETRA TIVER VOGAL, COLOQUE ESSA VOGAL NA VARÍAVAL VOGAIS
            vogais += letra + ' '
    print(f'NA PALAVRA {palavra.upper()} temos {vogais}')