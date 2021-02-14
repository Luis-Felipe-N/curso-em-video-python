from random import randint# IMPORTANDO FUNÇÃO DO MÓDULO RANDOM == ALEÁTORIo
venceu = 0# CONTADOR VAI MOSTRAR QUANTAS VEZES O USUÁRIO GANHOU
print('-' * 30)
print('VAMOS JOGAR IMPAR OU PAR!')
while True:# CRIANDO LOOP INFINITO
    print('-' * 30)
    num_usuario = int(input('Escolha um número: '))
    num_computador = randint(0,10)# SORTEANDO UM NÚMERO
    if num_usuario <= 10:
        escolha_usuario = str(input('Vai dar [P/I]')).strip().upper()[0]
        if (num_computador + num_usuario) % 2 == 0:# VENDO SE A SOMA ENTRE O NÚMERO DO USUÁRIO E DO COMPUTADOR É PAR OU ÍMPAR
            resultado = 'PAR'
            tipo = 'P'
        else:
            resultado = 'IMPAR'
            tipo = 'I'
        print('-' * 30)
        print(f'\033[34mO COMPUTADOR ESCOLHEU {num_computador} E VOCÊ ESCCOLHEU {num_usuario} O TOTAL É {num_computador + num_usuario}. DEU {resultado}\033[m')
        print('-' * 30)
        if escolha_usuario != tipo:# SE O USUÁRIO PERDER O JOGO VAI PARAR
            break
        else:# SE NÃO PERDER VAI PEDI PARA JOGAR NOVAMENTE
            print('\033[32mVOCÊ VENCEU!\033[m')
            print('VAMOS MAIS UMA VEZ..')
            venceu += 1
    else:
        print(f'\033[31mPOR FAVOR! JOGUE UM NÚMERO ENTRE 0 E 10, POR ACASO VOCÊ TEM {num_usuario} DEDOS?\033[m')
print(f'\033[31mGAME OVER!\033[m \033[32mVOCÊ VENCEU {venceu} VEZES.\033[m')