from random import randint
from time import sleep
# Fazer o jogo de pedra papel tesoura
itens = ['PEDRA', 'PAPEL', 'TESOURA']

# Pedir para o usuário jogar
barra = '=' * 34
print(f'''
\033[31m{barra}\033[m
\033[32mVAMOS JOGAR PEDRA, PAPEL, TESOURA.\033[m
\033[31m{barra}\033[m
\033[36mESCOLHA UM NÚMERO
[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA\033[m''')
usuario = int((input('VAI JOGAR QUAL?: ')))

# JO KEN PO
print('JO')
sleep(1)
print('KEN')
sleep(2)
print('PÔ!!')

# Em que o computador "pensou"
computador = randint(0,2)
print(f'O COMPUTADOR JOGOU {itens[computador]}.\nVOCÊ JOGOU {itens[usuario]}.')

# Vendo quem ganhou
if computador == 0:
    if usuario == 0:
        print('\033[33mEMPATE!\033[m')
    elif usuario == 1:
        print('\033[32mVOCÊ GANHOU!\033[m')
    elif usuario == 2:
        print('\033[31mVOCÊ PERDEU!\033[m')
    else:
        print('\033[31mJogada inválida!\033[m')
elif computador == 1:
    if usuario == 0:
        print('\033[31mVOCÊ PERDEU!\033[m')
                                                
    elif usuario == 1:
        print('\033[33mEMPATE\033[m')
    elif usuario == 2:
        print('\033[32mVOCÊ GANHOU!\033[m')
    else:
        print('\033[31mJogada inválida!\033[m')
elif computador == 2:
    if usuario == 0:
        print('\033[32mVOCÊ GANHOU!\033[m')
    elif usuario == 1:
        print('\033[31mVOCÊ PERDEU!\033[m')
    elif usuario == 2:
        print('\033[33mEMPATE\033[m')
    else:
        print('\033[31mJogada inválida!\033[m')