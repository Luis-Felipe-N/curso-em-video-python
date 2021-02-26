def escreva(frase):
    print('~' * (len(frase) + 10))
    print(f'{frase:^{len(frase) + 10}}')
    print('~' * (len(frase) + 10))


escreva('Olá, mundo!')
continuar = ''
while continuar != 'n':
    continuar = str(input('Deseja escrever uma frase [S/N]: ')).strip().lower()[0]
    if continuar == 's':
        escreva(str(input('Qual frase: ')).upper().strip())