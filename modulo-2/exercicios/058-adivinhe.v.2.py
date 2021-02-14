from random import randint
# FAZER UM JOGO QUE PEÇA UM NÚMERO E MOSTRE SE O USUÁRIO ACERTOU OU NÃO
# FAZER ISSO ATÉ O USUÁRIO ACERTA

# FAZENDO O COMPUTADOR PENSAR EM UM NÚMERO
num_computador = randint(0,10)

# CRIANDO UM LOOP QURE SERÁ PARADO QUANDO O USUÁRIO ACERTA 
acerto = False
totvezes = 0
while not acerto:
    num_usuario = int(input('Tente acerta o número que eu pensei: '))
    totvezes += 1
    if num_computador == num_usuario:
        acerto = True
    else:
        if num_computador > num_usuario:
            print('Mais..\033[31mVOCÊ ERROU! TENTE NOVAMENTE!\033[m')
        elif num_computador < num_usuario:
            print('Menos..\033[31mVOCÊ ERROU! TENTE NOVAMENTE!\033[m')
print(f'\033[32mVOCÊ GANHOU!!! COM {totvezes} TENATATIVAS!\033[m')