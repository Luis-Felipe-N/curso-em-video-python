# Fazer um conversor de binário, hexadecimal e octal

num = int(input('Digite um número inteiro: '))
conversao = int(input('Para qual base de conversão:\n[1] - BINÁRIO\n[2] - HEXADECIMAL\n[3] - OCTAL\nQual opção:'))


if conversao == 1:
    #converter para binário
    convertido = bin(num)
    print('o número convertido para binário fica {}'.format(convertido[2:]))
elif conversao == 2:
    #converter para hexadecimal
    convertido = hex(num)
    print('O número conivertido para hexadecimal é {}'.format(convertido[2:]))
elif conversao == 3:
    #converter para octal
    convertido = oct(num)
    print('O númerio convertido para octal é {}'.format(convertido[2:]))
else:
    print(f'\033[31m{conversao} NÃO É UMA OPÇÃO VÁLIDA\033[m')