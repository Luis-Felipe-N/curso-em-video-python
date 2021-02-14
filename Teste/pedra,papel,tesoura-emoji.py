from time import sleep
import emoji
from random import randint
linha = '-='
'''
Vou replicar o jogo pedra papel tesoura, mas com emoji
PARA PEDRA O CÓDIGO É : (emoji.emojize('Pedra :raised_fist:'))
PARA PAPEL O CÓDIGO É : (emoji.emojize('Papel :raised_hand:))
PARA TESOURA O CÓDIGO É : (emoji.emojize('Tesoura :victory_hand:))
'''

# DANDO AS OPÇÕES PARA O JOGADOR

print('{:=^40}'.format('\033[35m VAMOS JOGAR \033[m'))
print(emoji.emojize('''
ESCOLHA UMA DAS OPÇÕES ABAIXO :backhand_index_pointing_down:'''))
print((emoji.emojize('[ 0 ] - :raised_fist:')))
print((emoji.emojize('[ 1 ] - :raised_hand:')))
print((emoji.emojize('[ 2 ] - :victory_hand:')))
usuario = int(input('Qual sua opção: '))

# CRIANDO UMA LISTA COM OS ITENS DDO JOGO
itens = [(emoji.emojize(':raised_fist:')), (emoji.emojize(':raised_hand:')), (emoji.emojize(':victory_hand:'))]

# JO KEN PÔ 'ANIMADO'
print(itens[0])
sleep(1)
print(itens[1])
sleep(1)
print(itens[2])

# FAZENDO O COMPUTADOR JOGAR UM
computador = randint(0,2)
print('-=' * 10)
print('O COMPUTADOR JOGOU {}'.format(itens[computador]))

# VENDO QUEM GANHOU
if usuario == 0:#JOGADOR JOGOU PEDRA
    print('VOCÊ ESCOLHEU {} '.format(itens[usuario]))
    print('-=' * 10)
    if computador == 0:
        print('\033[34mEMPATE!\033[m')
    elif computador == 1:
        print('\033[31mVOCÊ PERDEU!\033[m')
    elif computador == 2:
        print('\033[32mVOCÊ GANHOU!\033[m')
elif usuario == 1:# JOGADOR JOGOU PAPEL
    print('VOCÊ ESCOLHEU {} '.format(itens[usuario]))
    print('-=' * 10)
    if computador == 0:
        print('\033[32mVOCÊ GANHOU!\033[m')
    elif computador == 1:
        print('\033[34mEMPATE!\033[m')
    elif computador == 2:
        print('\033[31mVOCÊ PERDEU!\033[m')
elif usuario == 2:# JOGADOR JOGOU TESOURA
    print('VOCÊ ESCOLHEU {} '.format(itens[usuario]))
    print('-=' * 10)
    if computador == 0:
        print('\033[31mVOCÊ PERDEU!\033[m')
    elif computador == 1:
        print('\033[32mVOCÊ GANHOU!\033[m')
    elif computador == 2:
        print('\033[34mEMPATE!\033[m')
else:
    print('\033[31mVOCÊ ESCOLHEU UMA OPÇÃO INVÁLIDA!\033[m')
    print('-=' * 17)
